from src.templates.threadwithstop import ThreadWithStop

class LaneRecognitionThread(ThreadWithStop):

    def __init__(self, inPs, outPs):
        super(LaneRecognitionThread, self).__init__()
        self.daemon = True

        self.outPs = outPs
        self.inPs = inPs

    def run(self):
        while True:
            for inP in self.inPs:
                print(inP.recv())
