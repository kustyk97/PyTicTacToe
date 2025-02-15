# Tic Tac Toe Game with GUI using PyQt

import sys
from PyQt5.QtWidgets import QApplication
from PyTicTacToe.PyTicTacToe import TicTacToe


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
