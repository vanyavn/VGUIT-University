import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
class CodingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кодировщик")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("""
    QWidget {
        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                     stop: 0 #880CC2, stop: 1 #F0F4F8);
        border-radius: 10px;
        font-family: System, sans-serif;  /* Устанавливаем шрифт для всего приложения */
    }
    QLabel {
        font-size: 20px;
        color: #2C3E50;
        font-weight: bold;
    }
    QLineEdit {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #4A0031;
        background-color: #880CC2;
    }
    QPushButton {
        background-color: #4A0031;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px;
        transition: background-color 0.3s;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
""")

        self.title_label = QLabel("Кодировщик", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font: System; padding: 10px;")
        self.mode_label = QLabel("Текущий режим: Не выбран", self)
        self.mode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mode_label.setStyleSheet("font: System; font-size: 18px; padding: 10px; color: #34495E;")
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.mode_label)
        self.button_even_ones = QPushButton("Четное число единиц")
        self.button_double = QPushButton("Удвоение элементов")
        self.button_inverse = QPushButton("Инверсный код")
        self.button_even_ones.clicked.connect(self.show_even_ones)
        self.button_double.clicked.connect(self.show_double)
        self.button_inverse.clicked.connect(self.show_inverse)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_even_ones)
        button_layout.addWidget(self.button_double)
        button_layout.addWidget(self.button_inverse)
        main_layout.addLayout(button_layout)
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Введите строку")
        main_layout.addWidget(self.input_line)
        self.encode_button = QPushButton("Закодировать")
        self.encode_button.clicked.connect(self.encode)
        self.decode_button = QPushButton("Декодировать")
        self.decode_button.clicked.connect(self.decode)
        main_layout.addWidget(self.encode_button)
        main_layout.addWidget(self.decode_button)
        self.setLayout(main_layout)
        self.current_mode = None
        self.encoded_result = None  # Переменная для хранения закодированного результата
    def show_even_ones(self):
        self.current_mode = "even_ones"
        self.input_line.setPlaceholderText("Введите строку (0 и 1)")
        self.mode_label.setText("Текущий режим: Четное число единиц")
    def show_double(self):
        self.current_mode = "double"
        self.input_line.setPlaceholderText("Введите строку")
        self.mode_label.setText("Текущий режим: Удвоение элементов")
    def show_inverse(self):
        self.current_mode = "inverse"
        self.input_line.setPlaceholderText("Введите строку (0 и 1)")
        self.mode_label.setText("Текущий режим: Инверсный код")
    def encode(self):
        text = self.input_line.text().strip()
        if not text:
            self.show_result("Введите строку")
            return
        if self.current_mode == "even_ones": self.encoded_result = self.encode_even_ones(text)
        elif self.current_mode == "double": self.encoded_result = self.encode_double(text)
        elif self.current_mode == "inverse": self.encoded_result = self.encode_inverse(text)
        else: self.encoded_result = "Выберите режим кодирования"
        self.show_result(self.encoded_result)
    def decode(self):
        if self.encoded_result is None:
            self.show_result("Сначала закодируйте данные")
            return
        if self.current_mode == "even_ones": result = self.decode_even_ones(self.encoded_result)
        elif self.current_mode == "double": result = self.decode_double(self.encoded_result)
        elif self.current_mode == "inverse": result = self.decode_inverse(self.encoded_result)
        else: result = "Выберите режим декодирования"
        self.show_result(result)
    def show_result(self, result):
        result_window = QMessageBox(self)
        result_window.setWindowTitle("Результат")
        result_window.setText(f"Результат: {result}")
        copy_button = result_window.addButton("Скопировать результат", QMessageBox.ButtonRole.ActionRole)
        result_window.setStandardButtons(QMessageBox.StandardButton.Ok)
        result_window.exec()
        if result_window.clickedButton() == copy_button: self.input_line.setText(result)
    def is_valid_input(self, text):
        return all(char in '01' for char in text)
    def encode_even_ones(self, text):
        if not self.is_valid_input(text):
            return "Введите только 0 и 1"
        count_ones = text.count('1')
        control_bit = '0' if count_ones % 2 == 0 else '1'
        return text + control_bit
    def decode_even_ones(self, text):
        if not self.is_valid_input(text):
            return "Введите только 0 и 1"
        data = text[:-1]
        control_bit = text[-1]
        count_ones = data.count('1')
        expected_bit = '0' if count_ones % 2 == 0 else '1'
        result = "Корректно" if control_bit == expected_bit else "Ошибка в данных"
        return f"{result}\nДекодированный результат: {data}"
    def encode_double(self, text):
        return ''.join(['10' if char == '1' else '01' for char in text])
    def decode_double(self, text):
        if len(text) % 2 != 0:
            return "Ошибка: длина строки должна быть четной"
        result = []
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if pair == '01': result.append('0')
            elif pair == '10': result.append('1')
            else: return "Ошибка: некорректные данные"
        return ''.join(result)
    def encode_inverse(self, text):
        count_ones = text.count('1')
        if count_ones % 2 == 0:
            return text * 2  # Повторяем строку в том же виде
        else:
            inverted = ''.join(['1' if char == '0' else '0' for char in text])
            return text + inverted  # Исходная + инверсная
    def decode_inverse(self, text):
        if len(text) % 2 != 0:
            return "Ошибка: длина строки должна быть четной"
        half = len(text) // 2
        first_part = text[:half]
        second_part = text[half:]
        count_ones = first_part.count('1')
        if count_ones % 2 == 0:
            if first_part == second_part:
                return "Корректно\nДекодированный результат: " + first_part
            else:
                return f"Ошибка в данных: {first_part} != {second_part}"
        else:
            inverted_first_part = ''.join(['1' if char == '0' else '0' for char in first_part])
            if inverted_first_part == second_part:
                return "Корректно\nДекодированный результат: " + inverted_first_part
            else:
                return f"Ошибка в данных: {inverted_first_part} != {second_part}"
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CodingApp()
    window.show()
    sys.exit(app.exec())