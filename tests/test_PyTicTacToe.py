import unittest
from PyQt5.QtWidgets import QApplication
from PyTicTacToe.PyTicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.game = TicTacToe()

    def test_initial_state(self):
        self.assertEqual(self.game.current_player, "X")
        for button in self.game.buttons.values():
            self.assertEqual(button.text(), "")

    def test_player_move(self):
        self.game.on_button_click(0, 0)
        self.assertEqual(self.game.buttons[(0, 0)].text(), "X")
        self.assertEqual(self.game.current_player, "O")

    def test_winner(self):
        self.game.buttons[(0, 0)].setText("X")
        self.game.buttons[(0, 1)].setText("X")
        self.game.buttons[(0, 2)].setText("X")
        self.assertTrue(self.game.check_winner())

    def test_draw(self):
        x_moves = [(0, 0), (0, 2), (2, 0), (2, 1), (1, 2)]
        o_moves = [(0, 1), (1, 0), (1, 1), (2, 2)]
        for i, move in enumerate(x_moves):
            self.game.buttons[move].setText("X")

        for i, move in enumerate(o_moves):
            self.game.buttons[move].setText("O")
        self.assertFalse(self.game.check_winner())
        self.assertTrue(
            all(button.text() != "" for button in self.game.buttons.values())
        )

    def tearDown(self):
        self.game.close()

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()
