import numpy as np
??
class SMO(object):
    def __init__(self):
        self.dataMat=[]
        self.labelMat=[]


    def loadData(self,dir):
        fd = open(dir)
        for line in fd.readlines():
            line = line.strip()
            if line == '':
                continue
            lineList = line.split()
            self.dataMat.append(float(lineList[0]),float(lineList[1]))
            self.labelMat.append(float(lineList[2]))

    def viewDataSet(self):
        print 'dataMat:'
        print self.dataMat
        print 'labelMat:'
        print self.dataMatlabelMat

    def selectJrand(i,m):
        j = i
        while ( j == i ):
            j = int (random.uniform(0 , m))
        return j




            


