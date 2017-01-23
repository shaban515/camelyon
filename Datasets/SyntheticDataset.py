import numpy as np

class SyntheticDataset:
    def __init__(self):
        self.rows = 64
        self.cols = 64
        self.depth = 1;
        self.noOfSamples = 1000;
        self.noOfClasses = 4
        self.classLimits = [0, 4, 40, 64]
        self.counter = 0
        self.dataset = np.zeros((self.noOfSamples,self.depth,self.rows,self.rows), dtype=np.int8)

    def addSquare(self,classId,noOfSample):
        pass


def main():
    ds1 = SyntheticDataset()
    aa = np
    print(ds1.dataset.shape)


if  __name__ =='__main__':main()
