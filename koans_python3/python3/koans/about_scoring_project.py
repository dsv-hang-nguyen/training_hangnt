#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import math
import functools
import collections

SET = 3

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(rolls):
       if not rolls:
           return 0
       counts = collections.Counter(rolls)
       scoring_counts = _get_rolls_to_scoring_counts(counts)
       return _calc_set_points(scoring_counts) + _calc_nonset_points(scoring_counts)
def _get_rolls_to_scoring_counts(rolls_to_counts):
       '''Return a dict of rolls to scoring counts.

       ScoringCounts is a namedtuple: ScoringCounts(sets, nonsets)
       containing the set count and nonset count as values for each roll key.

       '''

       rolls_to_scoring_counts = {}
       ScoringCounts = collections.namedtuple('ScoringCounts', 'sets nonsets')

       for roll in rolls_to_counts:
           cur_roll_count = rolls_to_counts[roll]

           if _roll_has_a_set(cur_roll_count):
               set_count = math.floor(cur_roll_count / SET)
               nonset_count = cur_roll_count % SET
           else:
               set_count = 0
               nonset_count = cur_roll_count

           rolls_to_scoring_counts[roll] = ScoringCounts(set_count, nonset_count)
       return rolls_to_scoring_counts


def _roll_has_a_set(roll_count):
       return roll_count >= SET


def _calc_set_points(rolls_to_scoring_counts):
       def _accumulate_set_points(accum, roll):
           SET_ROLL_TO_POINTS = {
               1: 1000,
               2: 2 * 100,
               3: 3 * 100,
               4: 4 * 100,
               5: 5 * 100,
               6: 6 * 100
           }
           return accum + SET_ROLL_TO_POINTS[roll] * rolls_to_scoring_counts[roll].sets

       return functools.reduce(_accumulate_set_points, rolls_to_scoring_counts, 0)


def _calc_nonset_points(rolls_to_scoring_counts):
       def _accumlate_nonset_points(accum, roll):
           ROLL_TO_POINTS = {
               1: 100,
               2: 0,
               3: 0,
               4: 0,
               5: 50,
               6: 0
           }
           return accum + ROLL_TO_POINTS[roll] * rolls_to_scoring_counts[roll].nonsets

       return functools.reduce(_accumlate_nonset_points, rolls_to_scoring_counts, 0)

class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1,5,5,1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2,3,4,6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1,1,1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2,2,2]))
        self.assertEqual(300, score([3,3,3]))
        self.assertEqual(400, score([4,4,4]))
        self.assertEqual(500, score([5,5,5]))
        self.assertEqual(600, score([6,6,6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2,5,2,2,3]))
        self.assertEqual(550, score([5,5,5,5]))
        self.assertEqual(1150, score([1,1,1,5,1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1,2,2,2]))
        self.assertEqual(350, score([1,5,2,2,2]))