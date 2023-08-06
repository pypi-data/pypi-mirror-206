import getpass
import grp
import logging
import os
import time as ttime

from ophyd.sim import NullStatus
from ophyd.status import SubscriptionStatus

from . import eiger
from .flyer import MXFlyer

logger = logging.getLogger(__name__)


class MXRasterFlyer(MXFlyer):
    def __init__(self, vector, zebra, detector) -> None:
        self.name = "MXRasterFlyer"
        super().__init__(vector, zebra, detector)

    def kickoff(self):
        # ttime.sleep(0.2)  # TODO see if vector starts ok without this sleep
        self.vector.go.put(1)
        return NullStatus()

    def update_parameters(self, *args, **kwargs):
        logger.debug("starting updating parameters")
        self.configure_vector(**kwargs)
        row_index = kwargs.get("row_index", 0)
        if row_index == 0:
            logger.debug("row 0: fully configuring zebra")
            self.configure_zebra(**kwargs)
        else:
            numImages = kwargs["num_images"]
            logger.debug(f"row {row_index}: only setting pulse max")
            self.zebra.pc.pulse.max.put(numImages)
        logger.debug("finished updating parameters")

    def configure_detector(self, **kwargs):
        file_prefix = kwargs["file_prefix"]
        data_directory_name = kwargs["data_directory_name"]
        self.detector.file.external_name.put(file_prefix)
        self.detector.file.write_path_template = data_directory_name

    def configure_zebra(self, **kwargs):
        angle_start = kwargs["angle_start"]
        exposurePeriodPerImage = kwargs["exposure_period_per_image"]
        detector_dead_time = kwargs["detector_dead_time"]
        scanWidth = kwargs["scan_width"]
        imgWidth = kwargs["img_width"]
        numImages = kwargs["num_images"]
        self.zebra_daq_prep()
        self.zebra.pc.encoder.put(3)  # encoder 0=x, 1=y,2=z,3=omega
        ttime.sleep(0.5)  # used since LSDC 1 - reason unknown
        self.zebra.pc.direction.put(0)  # direction 0 = positive
        self.zebra.pc.gate.sel.put(0)
        self.zebra.pc.pulse.sel.put(1)
        self.zebra.pc.pulse.start.put(0)

        PW = (exposurePeriodPerImage - 2 * detector_dead_time) * 1000
        PS = (exposurePeriodPerImage) * 1000
        GW = scanWidth - (1.0 - (PW / PS)) * (imgWidth / 2.0)
        self.setup_zebra_vector_scan(
            angle_start=angle_start,
            gate_width=GW,
            scan_width=scanWidth + 0.001,  # JA not sure why, but done in old LSDC
            pulse_width=PW,
            pulse_step=PS,
            exposure_period_per_image=exposurePeriodPerImage,
            num_images=numImages,
            is_still=imgWidth == 0,
        )

    # expected zebra setup:
    #     time in ms
    #     Posn direction: positive
    #     gate trig source - Position
    #     pulse trig source - Time
    def setup_zebra_vector_scan(
        self,
        angle_start,
        gate_width,
        scan_width,
        pulse_width,
        pulse_step,
        exposure_period_per_image,
        num_images,
        is_still=False,
    ):
        self.zebra.pc.gate.start.put(angle_start, wait=True)
        if is_still is False:
            logger.debug(f"before: gate width: {gate_width} gate step: {scan_width}")
            self.zebra.pc.gate.width.put(gate_width, wait=True)
            self.zebra.pc.gate.step.put(scan_width, wait=True)
        self.zebra.pc.gate.num_gates.put(1, wait=True)
        self.zebra.pc.pulse.start.put(0, wait=True)
        logger.debug(f"before: pulse width: {pulse_width}")
        self.zebra.pc.pulse.width.put(pulse_width, wait=True)
        self.zebra.pc.pulse.step.put(pulse_step, wait=True)
        logger.debug(f"before: pulse delay: {exposure_period_per_image / 2 * 1000}")
        self.zebra.pc.pulse.delay.put(exposure_period_per_image / 2 * 1000, wait=True)
        logger.debug(
            f"after: gate width: {self.zebra.pc.gate.width.get()} gate step: {self.zebra.pc.gate.step.get()}"
            f"after: pulse width: {self.zebra.pc.pulse.width.get()} pulse delay: {self.zebra.pc.pulse.delay.get()}"
        )
        self.zebra.pc.pulse.max.put(num_images, wait=True)
        self.vector.hold.put(0)  # necessary to prevent problems upon
        # exposure time change

    def detector_arm(self, **kwargs):
        start = kwargs["angle_start"]
        width = kwargs["img_width"]
        total_num_images = kwargs["total_num_images"]
        exposure_per_image = kwargs["exposure_period_per_image"]
        file_prefix = kwargs["file_prefix"]
        data_directory_name = kwargs["data_directory_name"]
        file_number_start = kwargs["file_number_start"]
        x_beam = kwargs["x_beam"]
        y_beam = kwargs["y_beam"]
        wavelength = kwargs["wavelength"]
        det_distance_m = kwargs["det_distance_m"]
        num_images_per_file = kwargs["num_images_per_file"]

        self.detector.cam.save_files.put(1)
        self.detector.cam.file_owner.put(getpass.getuser())
        self.detector.cam.file_owner_grp.put(grp.getgrgid(os.getgid())[0])
        self.detector.cam.file_perms.put(420)
        file_prefix_minus_directory = str(file_prefix)
        file_prefix_minus_directory = file_prefix_minus_directory.split("/")[-1]

        self.detector.cam.acquire_time.put(exposure_per_image)
        self.detector.cam.acquire_period.put(exposure_per_image)
        # Setting trigger mode before num_triggers due to change in Eiger REST API change
        self.detector.cam.trigger_mode.put(eiger.EXTERNAL_ENABLE)
        self.detector.cam.num_triggers.put(total_num_images)
        self.detector.cam.file_path.put(data_directory_name)
        self.detector.cam.fw_name_pattern.put(f"{file_prefix_minus_directory}_$id")

        self.detector.cam.sequence_id.put(file_number_start)

        # originally from detector_set_fileheader
        self.detector.cam.beam_center_x.put(x_beam)
        self.detector.cam.beam_center_y.put(y_beam)
        self.detector.cam.omega_incr.put(width)
        self.detector.cam.omega_start.put(start)
        self.detector.cam.wavelength.put(wavelength)
        self.detector.cam.det_distance.put(det_distance_m)

        self.detector.file.file_write_images_per_file.put(num_images_per_file)

        def armed_callback(value, old_value, **kwargs):
            if old_value == 0 and value == 1:
                return True
            return False

        status = SubscriptionStatus(self.detector.cam.armed, armed_callback, run=False)

        self.detector.cam.acquire.put(1)

        return status

    def describe_collect(self):
        return {"stream_name": {}}

    def collect(self):
        logger.debug("raster_flyer.collect(): going to unstage now")
        yield {"data": {}, "timestamps": {}, "time": 0, "seq_num": 0}

    def unstage(self):
        pass

    def collect_asset_docs(self):  # not to be done here
        for _ in ():
            yield _
