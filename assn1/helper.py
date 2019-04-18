from typing import List


def rvalue_at(rule: List[List[int]], state: List[List[int]], v: int):
    """
    obtains the value in the state of the specified rule param
    :param rule: current rule being run
    :param state: current state of the board
    :param v: 0 = jumper, 1 = goner, 2 = newpos
    :rtype: int
    :return: returns the value at the rule location
    """
    row = rule[v][0]
    column = rule[v][1]
    return state[row][column]


def set_value_at(pos: List[int], state: List[List[int]], value: int):
    """
    sets the value at the specified position of the board
    :param pos: position ([row][column]) to get value at
    :param state: current state of the board
    :param value: what to set the value at the position to
    :rtype: List[List[int]]
    :return: a copy of the board with the modified value at the position
    """
    row = pos[0]
    column = pos[1]
    state_copy = state.copy()
    state_copy[row][column] = value
    return state_copy
