from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class HydraulicsUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label = QLabel("Seleccione el tipo de cálculo en Hidráulica")
        layout.addWidget(label)
        
        self.combobox = QComboBox()
        options = ["Calcular Caudal", "Calcular Pérdida de Presión"]
        options.sort()  # Ordenar alfabéticamente
        self.combobox.addItems(options)
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        layout.addWidget(self.combobox)
        
        self.setLayout(layout)
    
    def on_combobox_changed(self, index):
        if self.combobox.currentText() == "Calcular Caudal":
            self.calculate_flow_rate()
        elif self.combobox.currentText() == "Calcular Pérdida de Presión":
            self.calculate_pressure_loss()
    
    def calculate_flow_rate(self):
        # Implementar lógica de cálculo de caudal
        pass
    
    def calculate_pressure_loss(self):
        # Implementar lógica de cálculo de pérdida de presión
        pass
