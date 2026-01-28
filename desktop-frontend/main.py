import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
import requests
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/api"

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        layout = QVBoxLayout()

        self.label = QLabel("Upload CSV")
        layout.addWidget(self.label)

        btn = QPushButton("Upload")
        btn.clicked.connect(self.upload_csv)
        layout.addWidget(btn)

        self.setLayout(layout)

    def upload_csv(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select CSV")
        if file:
            with open(file, "rb") as f:
                res = requests.post(f"{API_URL}/upload/", files={"file": f})
                summary = res.json()["summary"]
                self.label.setText(str(summary))
                plt.bar(summary["type_distribution"].keys(), summary["type_distribution"].values())
                plt.show()

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
