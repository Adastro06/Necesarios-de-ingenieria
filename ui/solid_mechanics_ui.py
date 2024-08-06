from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QMessageBox, QLineEdit
from ui.unit_settings import UnitSettings

class SolidMechanicsUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label = QLabel("Seleccione el tipo de cálculo en Mecánica de Sólidos")
        layout.addWidget(label)
        
        self.combobox = QComboBox()
        options = ["Calcular Esfuerzo", "Calcular Deformación"]
        options.sort()  # Ordenar alfabéticamente
        self.combobox.addItems(options)
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        layout.addWidget(self.combobox)
        
        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("Ingrese el valor de la fuerza (N)")
        self.input1.focusOutEvent = self.add_unit_to_input1
        layout.addWidget(self.input1)
        
        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("Ingrese el valor del área (m^2)")
        self.input2.focusOutEvent = self.add_unit_to_input2
        layout.addWidget(self.input2)
        
        self.calculate_button = QPushButton("Calcular", self)
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)
        
        self.unit_settings_button = QPushButton("Configuración de Unidades", self)
        self.unit_settings_button.clicked.connect(self.open_unit_settings)
        layout.addWidget(self.unit_settings_button)
        
        self.result_label = QLabel("Resultado: ", self)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        
        # Unidades predeterminadas
        self.unit_settings = {
            'length': 'm',
            'force': 'N',
            'area': 'm^2'
        }
        
        self.current_stress = None
        self.current_stress_in_pascals = None
        self.force_value = None
        self.area_value = None
    
    def on_combobox_changed(self, index):
        self.update_input_placeholders()
    
    def update_input_placeholders(self):
        if self.combobox.currentText() == "Calcular Esfuerzo":
            self.input1.setPlaceholderText(f"Ingrese el valor de la fuerza ({self.unit_settings['force']})")
            self.input2.setPlaceholderText(f"Ingrese el valor del área ({self.unit_settings['area']})")
        elif self.combobox.currentText() == "Calcular Deformación":
            self.input1.setPlaceholderText(f"Ingrese el valor del cambio de longitud ({self.unit_settings['length']})")
            self.input2.setPlaceholderText(f"Ingrese el valor de la longitud original ({self.unit_settings['length']})")
    
    def add_unit_to_input1(self, event):
        if self.input1.text() and not self.input1.text().endswith(f" {self.unit_settings['force']}"):
            self.input1.setText(f"{self.input1.text()} {self.unit_settings['force']}")
        QLineEdit.focusOutEvent(self.input1, event)
    
    def add_unit_to_input2(self, event):
        if self.input2.text() and not self.input2.text().endswith(f" {self.unit_settings['area']}"):
            self.input2.setText(f"{self.input2.text()} {self.unit_settings['area']}")
        QLineEdit.focusOutEvent(self.input2, event)
    
    def calculate(self):
        try:
            self.force_value = float(self.input1.text().split()[0])
            self.area_value = float(self.input2.text().split()[0])
            
            if self.combobox.currentText() == "Calcular Esfuerzo":
                self.current_stress_in_pascals = self.calculate_stress_in_pascals(self.force_value, self.area_value)
                self.current_stress, unit = self.convert_stress_to_readable_unit(self.current_stress_in_pascals)
                self.result_label.setText(f"Resultado: {self.current_stress:.2f} {unit}")
            elif self.combobox.currentText() == "Calcular Deformación":
                result = self.calculate_strain(self.force_value, self.area_value)
                self.result_label.setText(f"Resultado: {result:.2f} (sin unidad)")
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, ingrese valores numéricos válidos.")
    
    def calculate_stress_in_pascals(self, force, area):
        # Convertir fuerza y área a unidades base (Newton y metros cuadrados)
        force_in_newtons = self.convert_to_newtons(force, self.unit_settings['force'])
        area_in_square_meters = self.convert_to_square_meters(area, self.unit_settings['area'])
        
        # Calcular el esfuerzo en Pascales
        stress_in_pascals = force_in_newtons / area_in_square_meters
        return stress_in_pascals
    
    def convert_to_newtons(self, force, unit):
        if unit == 'kN':
            return force * 1000
        elif unit == 'lbf':
            return force * 4.44822
        return force
    
    def convert_to_square_meters(self, area, unit):
        if unit == 'cm^2':
            return area / 10000
        elif unit == 'mm^2':
            return area / 1000000
        elif unit == 'in^2':
            return area * 0.00064516
        elif unit == 'ft^2':
            return area * 0.092903
        return area
    
    def convert_stress_to_readable_unit(self, stress_in_pascals):
        # Determinar la unidad legible
        if stress_in_pascals >= 1e6:
            return stress_in_pascals / 1e6, 'MPa'
        elif stress_in_pascals >= 1e3:
            return stress_in_pascals / 1e3, 'kPa'
        elif stress_in_pascals < 1:
            return stress_in_pascals * 1000, 'mPa'
        return stress_in_pascals, 'Pa'
    
    def get_stress_unit(self):
        if self.unit_settings['area'] in ['cm^2', 'mm^2']:
            return "MPa"
        elif self.unit_settings['area'] in ['in^2', 'ft^2']:
            return "psi"
        return "Pa"
    
    def calculate_strain(self, change_in_length, original_length):
        # Convertir longitudes a unidades base (metros)
        change_in_length = self.convert_to_meters(change_in_length, self.unit_settings['length'])
        original_length = self.convert_to_meters(original_length, self.unit_settings['length'])
        
        # Calcular la deformación
        strain = change_in_length / original_length
        
        return strain
    
    def convert_to_meters(self, length, unit):
        if unit == 'cm':
            return length / 100
        elif unit == 'mm':
            return length / 1000
        elif unit == 'in':
            return length * 0.0254
        elif unit == 'ft':
            return length * 0.3048
        return length
    
    def update_input_values(self):
        if self.force_value is not None:
            self.input1.setText(f"{self.convert_force_to_current_unit(self.force_value)} {self.unit_settings['force']}")
        if self.area_value is not None:
            self.input2.setText(f"{self.convert_area_to_current_unit(self.area_value)} {self.unit_settings['area']}")
    
    def convert_force_to_current_unit(self, force):
        if self.unit_settings['force'] == 'kN':
            return force / 1000
        elif self.unit_settings['force'] == 'lbf':
            return force / 4.44822
        return force
    
    def convert_area_to_current_unit(self, area):
        if self.unit_settings['area'] == 'cm^2':
            return area * 10000
        elif self.unit_settings['area'] == 'mm^2':
            return area * 1000000
        elif self.unit_settings['area'] == 'in^2':
            return area / 0.00064516
        elif self.unit_settings['area'] == 'ft^2':
            return area / 0.092903
        return area
    
    def open_unit_settings(self):
        unit_options = {
            'SI': {'length': ['m', 'cm', 'mm'], 'force': ['N', 'kN'], 'area': ['m^2', 'cm^2', 'mm^2']},
            'Imperial': {'length': ['ft', 'in'], 'force': ['lbf'], 'area': ['ft^2', 'in^2']}
        }
        unit_settings_dialog = UnitSettings(unit_options, self.unit_settings)
        if unit_settings_dialog.exec_():
            self.unit_settings = unit_settings_dialog.get_selected_units()
            self.update_input_placeholders()
            self.update_input_values()
            if self.current_stress_in_pascals is not None:
                self.current_stress, unit = self.convert_stress_to_readable_unit(self.current_stress_in_pascals)
                self.result_label.setText(f"Resultado: {self.current_stress:.2f} {unit}")
