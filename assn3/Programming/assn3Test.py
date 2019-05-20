from pegBoard import *

if __name__ == '__main__':
    # This week we are testing the back track approach

    initialState = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    states = [initialState]
    # path = back_track(states)
    path = backtrack_heuristic(states)
    # print(path)
