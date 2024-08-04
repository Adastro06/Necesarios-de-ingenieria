from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class SolidMechanicsUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label = QLabel("Seleccione el tipo de cálculo en Mecánica de Sólidos")
        layout.addWidget(label)
        
        self.combobox = QComboBox()
        options = ["Calcular Deformación", "Calcular Esfuerzo"]
        options.sort()  # Ordenar alfabéticamente
        self.combobox.addItems(options)
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        layout.addWidget(self.combobox)
        
        self.setLayout(layout)
    
    def on_combobox_changed(self, index):
        if self.combobox.currentText() == "Calcular Esfuerzo":
            self.calculate_stress()
        elif self.combobox.currentText() == "Calcular Deformación":
            self.calculate_strain()
    
    def calculate_stress(self):
        # Implementar lógica de cálculo de esfuerzo
        pass
    
    def calculate_strain(self):
        # Implementar lógica de cálculo de deformación
        pass
