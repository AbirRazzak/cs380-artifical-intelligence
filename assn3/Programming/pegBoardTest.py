from pegBoard import *
import unittest

class PegBoardTests(unittest.TestCase):
    def test_goal(self):
        try:
            board = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.assertTrue(goal(board))

            board = [[1, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
            self.assertFalse(goal(board))

        except Exception:
            self.fail('test_goal() failed. Unknown exception occurred.')

    def test_precondition(self):
        try:
            # test if values are correct
            board = [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            rule = [
                [0, 0],  # jumper
                [0, 1],  # goner
                [0, 2]  # newpos
            ]
            self.assertTrue(precondition(rule, board))
            # jumper missing
            board = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.assertFalse(precondition(rule, board))
            # goner missing
            board = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.assertFalse(precondition(rule, board))
            # newpos already has a peg
            board = [[1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.assertFalse(precondition(rule, board))

            # test if jumper and goner are the same peg
            board = [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 0]
            ]
            rule = [
                [1, 1],
                [1, 1],
                [1, 3]
            ]
            self.assertFalse(precondition(rule, board))

            # test if pegs are not adjacent
            rule = [
                [1, 1],
                [3, 2],
                [1, 3]
            ]
            self.assertFalse(precondition(rule, board))

            # test if newpos is incorrect
            rule = [
                [1, 1],
                [1, 2],
                [1, 0]
            ]
            self.assertFalse(precondition(rule, board))

        except Exception:
            self.fail('test_precondition() failed. Unknown exception occurred.')

    def test_apply_rule(self):
        try:
            board = [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            rule = [
                [0, 0],  # jumper
                [0, 1],  # goner
                [0, 2]  # newpos
            ]
            new_board = apply_rule(rule, board)

            target_board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.assertEqual(new_board, target_board)

        except Exception:
            self.fail('() failed. Unknown exception occurred.')

    def test_applicable_rules(self):
        try:
            state = [[1, 0, 1, 1], [0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1]]
            target = [[[0, 3], [0, 2], [0, 1]], [[0, 3], [1, 2], [2, 1]], [[2, 3], [1, 2], [0, 1]], [[2, 3], [2, 2], [2, 1]], [[3, 0], [2, 0], [1, 0]], [[3, 1], [2, 2], [1, 3]], [[3, 3], [2, 2], [1, 1]], [[3, 3], [2, 3], [1, 3]]]
            self.assertEqual(applicable_rules(state), target)

        except Exception:
            self.fail('test_applicable_rules() failed. Unknown exception occurred')

    def test_flail_wildly(self):
        try:
            for x in range(100):
                initial_state = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
                result = flail_wildly(initial_state)
                self.assertNotEqual(result, 2)  # run flail wildly 100 times and make sure no exceptions occur
        except Exception:
            self.fail('test_flail_wildly() failed. Unknown exception occurred.')

        # TEMPLATE:
        # try:
        #
        # except Exception:
        #     self.fail('() failed. Unknown exception occurred.')


if __name__ == '__main__':
    unittest.main()
