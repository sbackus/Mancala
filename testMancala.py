#-------------------------------------------------------------------------------
# Name:        mancalaT
# Purpose:
#
# Author:      SBackus
#
# Created:     18/12/2012
# Copyright:   (c) SBackus 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from mancala import *
import unittest

class TestCup(unittest.TestCase):

    def test_that_a_new_cup_has_four_stones(self):
        cup = Cup()
        self.assertEquals(cup.getStoneCount(),4)

    def test_that_a_new_cup_can_be_created_with_3_stones(self):
        cup = Cup(3)
        self.assertEquals(cup.getStoneCount(),3)

    def test_getters_and_setters_for_nextCup(self):
        cup1 = Cup()
        cup2 = Cup(3)
        cup1.setNext(cup2)
        self.assertEquals(cup1.getNext(),cup2)

    def test_that_stone_count_goes_up_after_adding_stones(self):
        cup = Cup()
        count = cup.getStoneCount()
        cup.addStone()
        count +=1
        self.assertEquals(cup.getStoneCount(), count)

    def test_that_when_a_cup_with_1_stone_is_selected_the_stone_is_moved_to_the_next_cup(self):
        cup1 = Cup(1)
        cup2 = Cup()
        cup1.setNext(cup2)
        cup1.select()
        self.assertEquals(cup1.getStoneCount(),0)
        self.assertEquals(cup2.getStoneCount(),5)

    def test_that_when_a_cup_with_3_stones_is_selecte_they_are_distributed_correctly(self):
        cup0 = Cup(3)
        cup1 = Cup(1)
        cup2 = Cup(2)
        cup3 = Cup(3)
        cup0.setNext(cup1)
        cup1.setNext(cup2)
        cup2.setNext(cup3)
        cup0.select()
        self.assertEquals(cup1.getStoneCount(),2)
        self.assertEquals(cup2.getStoneCount(),3)
        self.assertEquals(cup3.getStoneCount(),4)


if __name__ == '__main__':
    unittest.main(exit=False)

