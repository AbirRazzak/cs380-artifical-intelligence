## B.

When calculating a heuristic, we should never count the empty tile, as doing so will overestimate the heuristic causing the heuristic to be non-admissible.

_h0(node): 0_

The shortest path will always be greater than zero unless the initial state is also the goal state. Either way, h0 never overpredicts the path, therefore it is admissible.

_h1(node): number of tiles out of place_

It will always take at least the number of tiles out of place (often times more) steps to get to the goal state. If h1 = 0 then the board is in the goal state. If the h1 = 1, then the shortest number of steps it could take to get into the goal state is, at best case, 1 (meaning the tile out of place is in the center and the empty space is occupying where that tile needs to go). Therefore, t1 is admissible.

_h2(node): sum of distances out of place_

This heuristic is admissible because a tile at minimum needs to travel the distance out of place to get to where it needs to be. Since tiles can only move 1 space at a time, there is no way to get more optimal than this. Use the example in h4 to prove that this is admissible. h2 = 16 and the optimal solution took 18.

_h3(node): 2*DT(node)_

h3 is non-admissible if DT(node) also includes the empty tile. In the question sheet it does not list whether DT(node) includes or excludes empty tiles, therefore the answer to this one is a bit ambiguous. Say, tile 8 and empty tile need to be swapped. Simply moving tile 8 to the left would solve the problem, instead of attempting to swap the 2 tiles. If DT excludes the empty tile, then this will be admissible.

_h4(node): h2(node) + 3*S(node)_

Words are hard, so here I will use proof by example:
Suppose you have a table of:

3 4 5

8 _ 6

2 1 7

h4 = 16 + 3 (6)

h4 = 16 + 18

h4 = 34

However a solution I came up with only requires 18 steps. First, move the 8 to the center. Then move all the outer numbers clockwise until they are in their correct position. Then move 8 back to the left and the goal state has been achieved.
