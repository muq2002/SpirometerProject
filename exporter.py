from PyQt5.QtWidgets import QFileDialog, QMessageBox
import csv
import numpy as np

class Exporter:
    def __init__(self, window):
        self.window = window

    def export_data(self):
        if not self.window.serial_connection.data:
            QMessageBox.warning(self.window, "No Data", "No data to export.")
            return
        
        filename, _ = QFileDialog.getSaveFileName(self.window, "Save Data", "", "CSV Files (*.csv)")
        if filename:
            with open(filename, "w", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Value"])
                csv_writer.writerow(np.transpose(np.array(self.window.serial_connection.data)))
            QMessageBox.information(self.window, "Export Complete", f"Data has been exported to {filename}.")
