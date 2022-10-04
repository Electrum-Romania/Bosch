from src.templates.threadwithstop import ThreadWithStop

class LaneRecognitionThread(ThreadWithStop):

    def __init__(self, outPs):
        super(LaneRecognitionThread, self).__init__()
        self.daemon = True

        self.outPs = outPs

    def run(self):
        print('a');