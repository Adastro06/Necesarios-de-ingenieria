from PyQt5.QtWidgets import QMainWindow, QTabWidget
from ui.calculations_tab import CalculationsTab
from ui.unit_converter_ui import UnitConverterUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación de Ingeniería")
        
        self.tab_widget = QTabWidget()
        
        self.calculations_tab = CalculationsTab()
        self.unit_converter_tab = UnitConverterUI()
        
        self.tab_widget.addTab(self.calculations_tab, "Cálculos")
        self.tab_widget.addTab(self.unit_converter_tab, "Convertidor de Unidades")
        
        self.setCentralWidget(self.tab_widget)
