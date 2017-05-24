import sys
from teia.teia import TeiaApp

def main():
    app = TeiaApp(sys.argv)

    #PyQt main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
