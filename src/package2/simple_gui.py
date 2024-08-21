import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Simple GUI")
    window.setGeometry(100, 100, 300, 200)
    
    label = QLabel("Hello, PyQt6!", window)
    label.setGeometry(100, 80, 200, 30)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()