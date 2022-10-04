from src.templates.workerprocess            import WorkerProcess
from src.hardware.camera.CameraThread       import CameraThread
from src.utils.camerastreamer.LaneRecognitionThread import LaneRecognitionThread

class LaneRecognitionProcess(WorkerProcess):

    def __init__(self, inPs, outPs, daemon = True):
        super(LaneRecognitionProcess, self).__init__(inPs, outPs)

    def run(self):
        super(LaneRecognitionProcess, self).run()

    def _init_threads(self):
        laneTh = LaneRecognitionThread(self.inPs, self.outPs)
        self.threads.append(laneTh)
