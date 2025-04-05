class Train:
    def __init__(self,split=0.25):
        self.split = split
class Hyperparameter:
    def train_meter(self):
        print("training......")
        return "training"