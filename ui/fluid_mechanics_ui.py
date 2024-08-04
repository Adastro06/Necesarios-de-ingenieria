from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class FluidMechanicsUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label = QLabel("Seleccione el tipo de cálculo en Mecánica de Fluidos")
        layout.addWidget(label)
        
        self.combobox = QComboBox()
        options = ["Calcular Número de Reynolds", "Calcular Fuerza de Arrastre"]
        options.sort()  # Ordenar alfabéticamente
        self.combobox.addItems(options)
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        layout.addWidget(self.combobox)
        
        self.setLayout(layout)
    
    def on_combobox_changed(self, index):
        if self.combobox.currentText() == "Calcular Número de Reynolds":
            self.calculate_reynolds_number()
        elif self.combobox.currentText() == "Calcular Fuerza de Arrastre":
            self.calculate_drag_force()
    
    def calculate_reynolds_number(self):
        # Implementar lógica de cálculo del número de Reynolds
        pass
    
    def calculate_drag_force(self):
        # Implementar lógica de cálculo de fuerza de arrastre
        pass
