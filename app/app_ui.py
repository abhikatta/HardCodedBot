from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie, QIcon, QPixmap, QFont
import sys
import os
# from chadBot import chatbot
sys.path.append('../')
sys.path.append('./')


class App(QWidget):

    def __init__(self):
        super().__init__()
        # self.bot = chad_noob_bot()

        # gif style properties
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignmentFlag(5))

        # Start button for listening gif
        self.start_gif_button = QPushButton('Speak', self)
        self.start_gif_button.setFont(QFont('Montserrat', 10))
        self.start_gif_button.clicked.connect(self.play_gif)

        # print console output
        self.console_output_text = QLabel(self)
        self.console_output_text.setText(" ")
        # print Statement
        self.statement_text = QLabel(self)
        self.statement_text.setText("statement text")

        # Create a vertical layout and add the button and label to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.start_gif_button)
        layout.addWidget(self.gif_label)
        layout.addWidget(self.statement_text)
        layout.addWidget(self.console_output_text)
        self.window_settings()

    def window_settings(self):
        window_title = 'noobBot'
        self.setWindowTitle(window_title)
        self.setWindowIcon(
            QIcon(os.path.join('./assets/images/', 'noobBot_window_icon.png')))
        self.set_taskbar_icon(os.path.join(
            './assets/images/', 'noobBot_window_icon.png'))
        self.setMinimumSize(380, 360)
        self.setMaximumSize(380, 360)

    def set_taskbar_icon(self, icon_path):
        # Load the icon from file
        icon = QIcon(QPixmap(icon_path))

        # Set the icon for the taskbar
        try:
            if sys.platform == 'win32':
                import ctypes
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                    'myappid')
                self.setWindowIcon(icon)
        except:
            pass

    def play_gif(self):

        # Set the GIF animation to the label and start playing
        self.start_gif_button.setText("Listening")
        self.gif = QMovie(os.path.join('./assets/gifs/', 'giphy.gif'))
        self.gif.setSpeed(100)
        self.gif_label.setMovie(self.gif)
        self.gif.start()

        # button spam fix
        self.bot.greeting()
        self.console_output

    def stop_gif(self):
        self.start_gif_button.setText("Speak")
        self.gif_label.clear()
        self.console_output_text.clear()