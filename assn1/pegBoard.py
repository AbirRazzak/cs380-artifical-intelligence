from typing import List  # imported for linting and readability
from helper import *  # created a helper class to process data
from random import randint

def goal(board: List[List[int]]):
    """
    returns if the pegboard has reached the goal condition
    :type board: [[][]]
    """
    goal_board = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return board == goal_board


def precondition(rule: List[List[int]], state: List[List[int]]):
    """
    checks if values of jumper, goner, and newpos positions are 1, 1, and 0, respectively
    :param rule: the rule being applied, in [jumper, goner, newpos] format
    :param state: the current state of the board
    """
    if rvalue_at(rule, state, 0) == 0 or rvalue_at(rule, state, 1) == 0:
        # pegs don't exist at jumper and goner
        return False

    if rvalue_at(rule, state, 2) == 1:
        # new position location is already taken
        return False

    # check if jumper and goner are adjacent
    if rule[0] == rule[1]:
        # the jumper and goner are the same peg
        return False
    dist = [a - b for a, b in zip(rule[1], rule[0])]  # gets the distance between the jumper and goner
    if dist[0] > 1 or dist[1] > 1:
        # if the goner is more than 1 slot away from the jumper
        return False

    # check if newpos is in the correct position
    newdist = [a - b for a, b in zip(rule[2], rule[1])]  # get the distance between the goner and newpos
    if dist != newdist:
        # newpos is not in the correct location
        # newdist' distance should be in the same direction as dist
        return False

    return True


def apply_rule(rule: List[List[int]], state: List[List[int]]):
    """
    applies the given rule to the state
    :param rule: the rule being applied, in [jumper, goner, newpos] format
    :param state: current state of the board
    :return: a copy of the state with the applied rule (given the rule is proper)
    """
    if not precondition(rule, state):
        return state
    else:
        jumper = rule[0]
        goner = rule[1]
        newpos = rule[2]

        state_copy = set_value_at(jumper, state, 0)
        state_copy = set_value_at(goner, state_copy, 0)
        state_copy = set_value_at(newpos, state_copy, 1)

        return state_copy


# TODO: applicableRules
def applicable_rules(state: List[List[int]]):
    """
    iterates through the board and checks for all rules that can be applied by the precondition
    :param state: current state of the board
    :return: all possible rules that can be applied to the current board
    """
    # using flail wildly, so just check everything
    available_moves = [[[]]]
    num_rows = len(state)
    num_columns = len(state[0])
    for row1 in range(num_rows):
        for column1 in range(num_columns):
            for row2 in range(num_rows):
                for column2 in range(num_columns):
                    for row3 in range(num_rows):
                        for column3 in range(num_columns):
                            # basically checking every slot for every slot checked
                            # jumper checks all slots for goners
                            # and goners check all slots for newpos'
                            # could optimize later by only checking if a peg exists before nesting
                            # but that's what defensive programming is for ;)
                            curr_rule = [
                                [row1, column1],
                                [row2, column2],
                                [row3, column3]
                            ]
                            if precondition(curr_rule, state):
                                available_moves.append(curr_rule)

    available_moves.remove([[]])  # removes the empty rule from top of list
    return available_moves


def describe_state(state: List[List[int]]):
    """
    prints out the current state of the board (0 = empty, 1 = peg exists)
    :param state: current state of the board
    """
    for row in state:
        print(row)


def describe_rule(rule: List[List[int]]):
    """
    prints out what a rule means in English
    :param rule: rule that needs to be translated
    """
    print("The peg at {} jumps over the peg at {} and lands in {}".format(rule[0], rule[1], rule[2]))


def flail_wildly(board: List[List[int]]):
    try:
        state = board.copy()
        describe_state(state)
        rules = applicable_rules(state)
        while len(rules) != 0 and not goal(state):
            print('Available Rules: ')
            for rule in rules:
                print(rule)

            random_rule = rules[randint(0, len(rules) - 1)]
            describe_rule(random_rule)
            state = apply_rule(random_rule, state)

            print('\n\n')
            describe_state(state)
            rules = applicable_rules(state)

        if goal(state):
            print('Goal Condition obtained!')
            return 0
        if len(rules) == 0:
            print('Dead End hit. Unable to continue.')
            return 1

    except Exception:
        return 2
