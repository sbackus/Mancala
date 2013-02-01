#-------------------------------------------------------------------------------
# Name:        mancala
# Purpose:
#
# Author:      SBackus
#
# Created:     18/12/2012
# Copyright:   (c) SBackus 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cup:
    def __init__(self,stones=4):
        self.stones = stones
        self.nextCup = None

    def getStoneCount(self):
        return self.stones

    def setNext(self, cell):
        self.nextCup = cell

    def getNext(self):
        return self.nextCup

    def addStone(self):
        self.stones +=1

    def select(self):
        self.nextCup.sew(self.stones)
        self.stones = 0

    def sew(self,numberOfStones):
        if numberOfStones>0:
            self.stones +=1
        if numberOfStones-1>0:
            self.nextCup.sew(numberOfStones-1)

