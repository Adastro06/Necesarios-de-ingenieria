from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class ElectricityUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label = QLabel("Seleccione el tipo de cálculo en Electricidad")
        layout.addWidget(label)
        
        self.combobox = QComboBox()
        options = ["Calcular Corriente", "Calcular Resistencia"]
        options.sort()  # Ordenar alfabéticamente
        self.combobox.addItems(options)
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        layout.addWidget(self.combobox)
        
        self.setLayout(layout)
    
    def on_combobox_changed(self, index):
        if self.combobox.currentText() == "Calcular Resistencia":
            self.calculate_resistance()
        elif self.combobox.currentText() == "Calcular Corriente":
            self.calculate_current()
    
    def calculate_resistance(self):
        # Implementar lógica de cálculo de resistencia
        pass
    
    def calculate_current(self):
        # Implementar lógica de cálculo de corriente
        pass
