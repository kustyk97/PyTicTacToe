from PyQt5.QtWidgets import QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox, QLabel
from PyQt5.QtGui import QFont

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)
        self.grid_layout = QGridLayout()
        self.buttons = {}
        self.reset_button = None
        self.current_player = "X"
        self.current_player_label = None
        self.init_ui()

    def init_ui(self):
        self.current_player_label = QLabel(f"Current Player: {self.current_player}")
        self.grid_layout.addWidget(self.current_player_label, 0, 0)
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda checked, r=row, c=col: self.on_button_click(r, c))
                button.setFont(QFont("Arial", 40))
                self.grid_layout.addWidget(button, row+1, col)
                self.buttons[(row, col)] = button
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_game)
        self.grid_layout.addWidget(self.reset_button, 0, 2)
        container = QWidget()
        container.setLayout(self.grid_layout)
        self.setCentralWidget(container)
    

    def on_button_click(self, row, col):
        button = self.buttons[(row, col)]
        if button.text() == "":
            button.setText(self.current_player)
            if self.current_player == "X":
                button.setStyleSheet("color: red")
            else:
                button.setStyleSheet("color: blue")
            if self.check_winner():
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Game Over")
                msg_box.setText(f"Player {self.current_player} wins!")
                close_button = msg_box.addButton("Close Game", QMessageBox.RejectRole)
                restart_button = msg_box.addButton("Restart Game", QMessageBox.AcceptRole)
                msg_box.setDefaultButton(restart_button)
                ret = msg_box.exec_()
                if msg_box.clickedButton() == close_button:
                    self.close()
                elif msg_box.clickedButton() == restart_button:
                    self.reset_game()
            elif all(button.text() != "" for button in self.buttons.values()):
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Game Over")
                msg_box.setText(f"It's draw :/")
                close_button = msg_box.addButton("Close Game", QMessageBox.RejectRole)
                restart_button = msg_box.addButton("Restart Game", QMessageBox.AcceptRole)
                msg_box.setDefaultButton(restart_button)
                ret = msg_box.exec_()
                if msg_box.clickedButton() == close_button:
                    self.close()
                elif msg_box.clickedButton() == restart_button:
                    self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.current_player_label.setText(f"Current Player: {self.current_player}")

    def check_winner(self):
        for row in range(3):
            if self.buttons[(row, 0)].text() == self.buttons[(row, 1)].text() == self.buttons[(row, 2)].text() != "":
                return True
        for col in range(3):
            if self.buttons[(0, col)].text() == self.buttons[(1, col)].text() == self.buttons[(2, col)].text() != "":
                return True
        if self.buttons[(0, 0)].text() == self.buttons[(1, 1)].text() == self.buttons[(2, 2)].text() != "":
            return True
        if self.buttons[(0, 2)].text() == self.buttons[(1, 1)].text() == self.buttons[(2, 0)].text() != "":
            return True
        return False

    def reset_game(self):
        for button in self.buttons.values():
            button.setText("")
        self.current_player = "X"