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

class Cup(object):
    def __init__(self,stones=4, next=None):
        self.stones = stones
        self.nextCup = next

    def getStoneCount(self):
        return self.stones

    def setNext(self, cup):
        self.nextCup = cup

    def getNext(self):
        return self.nextCup

    def addStone(self):
        self.stones +=1

class Pit(Cup):

    def select(self):
        self.nextCup.sew(self.stones)
        self.stones = 0

    def sew(self, numberOfStones):
        if numberOfStones>0:
            self.stones +=1
        if numberOfStones-1>0:
            self.nextCup.sew(numberOfStones-1)


class Store(Cup):
    pass

class Side(object):
    def __init__(self,pitsPerSide=6):
        self.cups = []
        for i in range(0,pitsPerSide):
            self.cups.append(Pit())
        self.cups.append(Store())
        for i in range(0,pitsPerSide):
            self.cups[i].setNext(self.cups[i+1])

    def getCup(self,index):
        return self.cups[index]

    def getStore(self):
        return self.cups[-1]

class Board(object):
    def __init__(self,pitsPerSide=6):
        self.sides = [Side(),Side()]
        self.sides[0].getStore().setNext(self.sides[1].getCup(0))
        self.sides[1].getStore().setNext(self.sides[0].getCup(0))

    def getCup(self,side,index):
        return self.getSide(side).getCup(index)

    def getSide(self,index):
        return self.sides[index]

    def __print__(self):
        #for cups in sides
        print self.sides