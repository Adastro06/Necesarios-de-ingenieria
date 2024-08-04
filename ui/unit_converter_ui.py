from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class UnitConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label = QLabel("Convertidor de Unidades")
        layout.addWidget(label)
        
        self.input_value = QLineEdit(self)
        self.input_value.setPlaceholderText("Ingrese el valor a convertir")
        layout.addWidget(self.input_value)
        
        self.unit_from = QComboBox(self)
        self.unit_from.addItems(["metros", "kilogramos", "segundos"])
        layout.addWidget(self.unit_from)
        
        self.unit_to = QComboBox(self)
        self.unit_to.addItems(["centímetros", "gramos", "milisegundos"])
        layout.addWidget(self.unit_to)
        
        btn_convert = QPushButton("Convertir")
        btn_convert.clicked.connect(self.convert_units)
        layout.addWidget(btn_convert)
        
        self.result_label = QLabel("Resultado: ")
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def convert_units(self):
        try:
            value = float(self.input_value.text())
            unit_from = self.unit_from.currentText()
            unit_to = self.unit_to.currentText()
            result = self.perform_conversion(value, unit_from, unit_to)
            self.result_label.setText(f"Resultado: {result}")
        except ValueError:
            self.result_label.setText("Ingrese un valor numérico válido.")
    
    def perform_conversion(self, value, unit_from, unit_to):
        # Implementar la lógica de conversión de unidades
        # Este es un ejemplo básico, debe ser ampliado según las necesidades
        conversions = {
            ("metros", "centímetros"): value * 100,
            ("kilogramos", "gramos"): value * 1000,
            ("segundos", "milisegundos"): value * 1000
        }
        return conversions.get((unit_from, unit_to), "Conversión no disponible")
