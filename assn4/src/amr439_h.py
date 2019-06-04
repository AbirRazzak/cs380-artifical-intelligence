from Pentago_base import win
H_CORNER_POINTS = 2
H_CORNERS_ADJACENT = 10
H_CORNER_THREE_IN_A_ROW = 100
H_WIN = 1000000


def amr439_h(player, board):
    if player == '.':
        return 0

    # Base heuristic value
    h = 0

    # Check win conditions
    # Assign the opponent's piece
    opponent = 'b'
    if player == 'b':
        opponent = 'w'

    if win(player, board):
        h = h + H_WIN
    if win(opponent, board):
        h = h - H_WIN
    if win(player, board) and win(opponent, board):
        # If the resulting action is a tie, then award half win points
        # Better to tie than to potentially lose is the logic in this decision
        h = h + (H_WIN / 2)

    # Award points based of triples strategy
    h = h + amr439_triples(player, board)

    return h


# 3-in-a-Row
# heuristic that checks for 3 in a row in any row/column that does not include the center of the quadrants
def amr439_triples(player, board):
    h = 0

    # Prioritize getting 3 in a row in a single quadrant, excluding the center piece
    # "Corner" pieces are worth more, because they offer 2 different ways of getting 3 in a row

    # Starting spot for each quadrant
    x = [3, 0, 3, 0]
    y = [3, 3, 0, 0]

    for i in range(4):
        starting_x = x.pop()
        starting_y = y.pop()

        # Corner 1 (Top Left)
        c1 = board[starting_y][starting_x] == player
        # Corner 2 (Top Right)
        c2 = board[starting_y][starting_x + 2] == player
        # Corner 3 (Bottom Left)
        c3 = board[starting_y + 2][starting_x] == player
        # Corner 4 (Bottom Right)
        c4 = board[starting_y + 2][starting_x + 2] == player

        # Award corner points
        if c1:
            h = h + H_CORNER_POINTS
        if c2:
            h = h + H_CORNER_POINTS
        if c3:
            h = h + H_CORNER_POINTS
        if c4:
            h = h + H_CORNER_POINTS

        # If both adjacent corners are occupied by the player
        if c1 and c2:
            in_between = board[starting_y][starting_x + 1]

            # if the space in between in empty award them additional points
            if in_between is '.':
                h = h + H_CORNERS_ADJACENT

            # if the space in between is occupied by the player, 3 in a row is achieved
            elif in_between is player:
                h = h + H_CORNER_THREE_IN_A_ROW

            # if the space in between in occupied by the other player, remove points
            else:
                h = h - (H_CORNER_POINTS / 2)

        # If both adjacent corners are occupied by the player
        if c1 and c3:
            in_between = board[starting_y + 1][starting_x]

            # if the space in between in empty award them additional points
            if in_between is '.':
                h = h + H_CORNERS_ADJACENT

            # if the space in between is occupied by the player, 3 in a row is achieved
            elif in_between is player:
                h = h + H_CORNER_THREE_IN_A_ROW

            # if the space in between in occupied by the other player, remove points
            else:
                h = h - (H_CORNER_POINTS / 2)

        # If both adjacent corners are occupied by the player
        if c4 and c2:
            in_between = board[starting_y + 1][starting_x + 2]

            # if the space in between in empty award them additional points
            if in_between is '.':
                h = h + H_CORNERS_ADJACENT

            # if the space in between is occupied by the player, 3 in a row is achieved
            elif in_between is player:
                h = h + H_CORNER_THREE_IN_A_ROW

            # if the space in between in occupied by the other player, remove points
            else:
                h = h - (H_CORNER_POINTS / 2)

        # If both adjacent corners are occupied by the player
        if c4 and c3:
            in_between = board[starting_y + 2][starting_x + 1]

            # if the space in between in empty award them additional points
            if in_between is '.':
                h = h + H_CORNERS_ADJACENT

            # if the space in between is occupied by the player, 3 in a row is achieved
            elif in_between is player:
                h = h + H_CORNER_THREE_IN_A_ROW

            # if the space in between in occupied by the other player, remove points
            else:
                h = h - (H_CORNER_POINTS / 2)

    return h