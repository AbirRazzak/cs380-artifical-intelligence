from pegBoard import *

if __name__ == '__main__':
    # This week we are testing the flail wildly approach

    # Uncomment this out if you want to have some fun counting :)
    # win = False
    # counter = 0
    # while not win:
    #     initialState = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    #     f = flail_wildly(initialState)
    #     if f == 0:
    #         win = True
    #     if f == 1:
    #         counter = counter + 1
    #     if f == 2:
    #         exit()
    #
    # print('Only took {} times to solve!'.format(counter))

    initialState = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    flail_wildly(initialState)
