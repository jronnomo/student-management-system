import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # define widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()
        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()
        self.output_label = QLabel("")
        calculate_button = QPushButton('Calculate')
        self.dropdown = QComboBox()
        self.dropdown.addItems(['Metric (km)', 'Imperial (mi)'])

        calculate_button.clicked.connect(self.calculate_average_speed)

        # Add widget to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.dropdown, 0, 2)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)

        self.units = self.dropdown.currentText()
        self.setLayout(grid)

    def calculate_average_speed(self):
        average_speed = float(self.distance_line_edit.text()) / float(self.time_line_edit.text())
        if self.dropdown.currentText() == 'Metric (km)':
            self.output_label.setText(f"Average speed: {average_speed} km/h")
        else:
            self.output_label.setText(f"Average speed: {average_speed} mi/h")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
