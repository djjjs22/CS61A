# """The Game of Hog."""
#
# from dice import six_sided, make_test_dice
# from ucb import main, trace, interact
#
# GOAL = 100  # The goal of Hog is to score 100 points.
#
# ######################
# # Phase 1: Simulator #
# ######################
#
#
# def roll_dice(num_rolls, dice=six_sided):
#     """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
#     the outcomes unless any of the outcomes is 1. In that case, return 1.
#
#     num_rolls:  The number of dice rolls that will be made.
#     dice:       A function that simulates a single dice roll outcome.
#     """
#     # These assert statements ensure that num_rolls is a positive integer.
#     assert type(num_rolls) == int, 'num_rolls must be an integer.'
#     assert num_rolls > 0, 'Must roll at least once.'
#     # BEGIN PROBLEM 1
#     "*** YOUR CODE HERE ***"
#     # END PROBLEM 1
#     total = 0
#     flag = 0
#     for i in range(1,num_rolls+1):
#         tmp_roll = dice()
#         total += tmp_roll
#         if tmp_roll == 1:
#             flag = 1
#     if flag:
#         return 1
#     else:
#         return total
#
#
# def boar_brawl(player_score, opponent_score):
#     """Return the points scored by rolling 0 dice according to Boar Brawl.
#
#     player_score:     The total score of the current player.
#     opponent_score:   The total score of the other player.
#
#     """
#     # BEGIN PROBLEM 2
#     "*** YOUR CODE HERE ***"
#     n = player_score % 10
#     m = opponent_score // 10
#     if m > n:
#         return 3 * abs(m -n)
#     elif m == n:
#         return 3 * abs(m - n)
#     else:
#         return 3 * abs(m - n)
#     # END PROBLEM 2
#
#
# def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
#     """Return the points scored on a turn rolling NUM_ROLLS dice when the
#     player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.
#
#     num_rolls:       The number of dice rolls that will be made.
#     player_score:    The total score of the current player.
#     opponent_score:  The total score of the other player.
#     dice:            A function that simulates a single dice roll outcome.
#     """
#     # Leave these assert statements here; they help check for errors.
#     assert type(num_rolls) == int, 'num_rolls must be an integer.'
#     assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
#     assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
#     # BEGIN PROBLEM 3
#     "*** YOUR CODE HERE ***"
#     # END PROBLEM 3
#     if num_rolls == 0:
#         score =  boar_brawl(opponent_score, player_score)
#     else:
#         score =  roll_dice(num_rolls, dice)
#     return score
#
#
# def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
#     """Return the total score of a player who starts their turn with
#     PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
#     """
#     score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
#     return score
#
# def is_prime(n):
#     """Return whether N is prime."""
#     if n == 1:
#         return False
#     k = 2
#     while k < n:
#         if n % k == 0:
#             return False
#         k += 1
#     return True
#
# def num_factors(n):
#     """Return the number of factors of N, including 1 and N itself."""
#     # BEGIN PROBLEM 4
#     "*** YOUR CODE HERE ***"
#     fac = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             fac += 1
#             i += 1
#         else:
#             i += 1
#     return fac
#     # if fac == 3 or fac == 4:
#     #     return n
#     # else:
#     #     return 'not Sus Fuss'
#     # END PROBLEM 4
#
# def sus_points(score):
#     """Return the new score of a player taking into account the Sus Fuss rule."""
#     # BEGIN PROBLEM 4
#     "*** YOUR CODE HERE ***"
#     if num_factors(score) == 3 or num_factors(score) == 4:
#         i = score
#         while not is_prime(i):
#             i += 1
#         return i
#     else:
#         final_score = score
#         return final_score
#         # return 'not Sus Fuss'
#
#     # for i in range(score,n):
#     #     if is_prime(i):
#     # END PROBLEM 4
#
# def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
#     """Return the total score of a player who starts their turn with
#     PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
#     """
#     # BEGIN PROBLEM 4
#     "*** YOUR CODE HERE ***"
#     # END PROBLEM 4
#     if num_rolls == 0:
#         boar_brawl(opponent_score, player_score)
#     else:
#         p1 = player_score
#         p2 = opponent_score
#         sus_points(p1)
#         sus_points(p2)
# print(simple_update(2, 5, 7, make_test_dice(2, 4)))