from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QFormLayout, QHBoxLayout

class UnitSettings(QDialog):
    def __init__(self, unit_options, current_units):
        super().__init__()
        self.setWindowTitle("Configuración de Unidades")
        
        layout = QVBoxLayout()
        
        form_layout = QFormLayout()
        
        self.unit_system_label = QLabel("Sistema de Unidades:")
        form_layout.addRow(self.unit_system_label)
        
        self.unit_system_combobox = QComboBox()
        self.unit_system_combobox.addItems(unit_options.keys())
        self.unit_system_combobox.currentIndexChanged.connect(self.on_unit_system_changed)
        form_layout.addRow(self.unit_system_label, self.unit_system_combobox)
        
        self.length_label = QLabel("Longitud:")
        self.length_combobox = QComboBox()
        form_layout.addRow(self.length_label, self.length_combobox)
        
        self.force_label = QLabel("Fuerza:")
        self.force_combobox = QComboBox()
        form_layout.addRow(self.force_label, self.force_combobox)
        
        self.area_label = QLabel("Área:")
        self.area_combobox = QComboBox()
        form_layout.addRow(self.area_label, self.area_combobox)
        
        layout.addLayout(form_layout)
        
        self.button_layout = QHBoxLayout()
        self.apply_button = QPushButton("OK")
        self.apply_button.clicked.connect(self.apply_settings)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        self.button_layout.addWidget(self.apply_button)
        self.button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(self.button_layout)
        
        self.setLayout(layout)
        
        self.unit_options = unit_options
        self.current_units = current_units
        
        self.on_unit_system_changed(0)  # Initialize the first unit system
        
        self.unit_system_combobox.setCurrentText("SI")
        self.update_comboboxes(current_units)
    
    def on_unit_system_changed(self, index):
        selected_system = self.unit_system_combobox.currentText()
        units = self.unit_options[selected_system]
        
        self.length_combobox.clear()
        self.length_combobox.addItems(units['length'])
        
        self.force_combobox.clear()
        self.force_combobox.addItems(units['force'])
        
        self.area_combobox.clear()
        self.area_combobox.addItems(units['area'])
    
    def update_comboboxes(self, units):
        self.length_combobox.setCurrentText(units['length'])
        self.force_combobox.setCurrentText(units['force'])
        self.area_combobox.setCurrentText(units['area'])
    
    def apply_settings(self):
        self.current_units = {
            'length': self.length_combobox.currentText(),
            'force': self.force_combobox.currentText(),
            'area': self.area_combobox.currentText()
        }
        self.accept()
    
    def get_selected_units(self):
        return self.current_units
