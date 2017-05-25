import sys
from teia.teia import TeiaApp
import qdarkstyle

def main():
    app = TeiaApp(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    #PyQt main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
