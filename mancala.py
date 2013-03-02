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

    def __str__(self):
        return "("+str(self.stones)+")"


class Store(Cup):
    def __init__(self,stones=0, next=None):
        self.stones = stones
        self.nextCup = next

    def __str__(self):
        return "(  "+str(self.stones)+"  )"


class Board(object):
    def __init__(self):
        self.sides = [[],[]]
        self.sides[0] = self.initializeSide()
        self.sides[1] = self.initializeSide()
        self.getStore(0).setNext(self.getCup(1,0))
        self.getStore(1).setNext(self.getCup(0,0))

    def initializeSide(self, pitsPerSide=6):
        cups = []
        for i in range(0,pitsPerSide):
            cups.append(Pit())
        cups.append(Store())
        for i in range(0,pitsPerSide):
           cups[i].setNext(cups[i+1])
        return cups

    def getCup(self,sideNumber,index):
        return self.sides[sideNumber][index]

    def getSide(self,sideNumber):
        return self.sides[sideNumber]

    def getStore(self,sideNumber):
        return self.getSide(sideNumber)[-1]

    def __str__(self):
        board = "\n  "+ str(self.getStore(0))+"\n"
        for i in range(0,6):
            board += str(i) + "-"+str(self.sides[0][i]) +" "+ str(self.sides[1][i]) + "-"+ str(i)+"\n"
        return board +"  "+ str(self.getStore(1))+"\n"