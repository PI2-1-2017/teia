from PyQt5 import QtWidgets

from teia.imageuploader import ImageUploader
# Widgets
from teia.searchwidget import SearchWidget
# Ui
from teia.ui.ui_teia_mainwindow import Ui_TeiaMainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_TeiaMainWindow):

    def __init__(self):
        super().__init__()
        self.searching = False
        self.target = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Teia')
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        # Widgets
        self.searchFrame = SearchWidget(self.searchFrame)

        # Buttons
        self.imageButton.clicked.connect(self.upload_image)
        self.startButton.clicked.connect(self.stream)
        # Show window
        self.show()

    def upload_image(self):
        image = ImageUploader().inputFile()
        self.searchFrame.setTarget(image)

    def stream(self):
        self.searching = not self.searching
        if self.searching:
            self.startButton.setText('Parar Busca')
        else:
            self.startButton.setText('Iniciar Busca')
        self.searchFrame.stream()
