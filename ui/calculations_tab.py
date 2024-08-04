from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QStackedWidget, QLabel

from ui.hydraulics_ui import HydraulicsUI
from ui.solid_mechanics_ui import SolidMechanicsUI
from ui.fluid_mechanics_ui import FluidMechanicsUI
from ui.electricity_ui import ElectricityUI

class CalculationsTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.stacked_widget = QStackedWidget()
        
        self.default_widget = QWidget()
        default_layout = QVBoxLayout()
        default_label = QLabel("Seleccione una materia para ver los cálculos disponibles.")
        default_layout.addWidget(default_label)
        self.default_widget.setLayout(default_layout)
        
        self.hydraulics_ui = HydraulicsUI()
        self.solid_mechanics_ui = SolidMechanicsUI()
        self.fluid_mechanics_ui = FluidMechanicsUI()
        self.electricity_ui = ElectricityUI()
        
        self.stacked_widget.addWidget(self.default_widget)
        self.stacked_widget.addWidget(self.hydraulics_ui)
        self.stacked_widget.addWidget(self.solid_mechanics_ui)
        self.stacked_widget.addWidget(self.fluid_mechanics_ui)
        self.stacked_widget.addWidget(self.electricity_ui)
        
        layout = QVBoxLayout()
        self.combobox = QComboBox()
        options = ["", "Electricidad", "Hidráulica", "Mecánica de Fluidos", "Mecánica de Sólidos"]
        options.sort()  # Ordenar alfabéticamente
        self.combobox.addItems(options)
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        
        layout.addWidget(self.combobox)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
    
    def on_combobox_changed(self, index):
        if self.combobox.currentText() == "Hidráulica":
            self.stacked_widget.setCurrentWidget(self.hydraulics_ui)
        elif self.combobox.currentText() == "Mecánica de Sólidos":
            self.stacked_widget.setCurrentWidget(self.solid_mechanics_ui)
        elif self.combobox.currentText() == "Mecánica de Fluidos":
            self.stacked_widget.setCurrentWidget(self.fluid_mechanics_ui)
        elif self.combobox.currentText() == "Electricidad":
            self.stacked_widget.setCurrentWidget(self.electricity_ui)
        else:
            self.stacked_widget.setCurrentWidget(self.default_widget)
