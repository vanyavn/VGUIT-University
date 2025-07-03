import sys
import math
import heapq
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QMessageBox, QHBoxLayout
)
from PyQt6.QtCore import Qt

class HuffmanNode:
    def __init__(self, weight, symbol=None):
        self.weight = weight
        self.symbol = symbol
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.weight < other.weight

def build_huffman_tree(frequencies):
    priority_queue = [HuffmanNode(weight, symbol) for symbol, weight in frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        low1 = heapq.heappop(priority_queue)
        low2 = heapq.heappop(priority_queue)
        merged = HuffmanNode(low1.weight + low2.weight)
        merged.left = low1
        merged.right = low2
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]

def generate_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    if node is not None:
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        else:
            generate_codes(node.left, prefix + '0', codebook)
            generate_codes(node.right, prefix + '1', codebook)
    return codebook

def calculate_entropy(frequencies):
    return -sum(p * math.log2(p) for p in frequencies.values() if p > 0)

def calculate_average_length(codes, frequencies):
    return sum(frequencies[symbol] * len(code) for symbol, code in codes.items())

class HuffmanApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Huffman Coding')
        self.setGeometry(100, 100, 700, 570)

        # Set layout and background color
        layout = QHBoxLayout()  # Using QHBoxLayout to arrange widgets horizontally
        
        # Left part of the screen for frequencies and calculation results
        self.left_layout = QVBoxLayout()
        self.frequencies = {
            'x1': 0.21,
            'x2': 0.18,
            'x3': 0.15,
            'x4': 0.12,
            'x5': 0.10,
            'x6': 0.07,
            'x7': 0.07,
            'x8': 0.07,
            'x9': 0.03
        }
        
        # Label for displaying initial frequencies
        self.result_label = QLabel(self)
        string_dict = str(self.frequencies)
        self.result_label.setText('Исходные данные:\n\n\n ' + string_dict)
        self.left_layout.addWidget(self.result_label)
        
        # Button for calculating Huffman codes
        self.calculate_button = QPushButton('Сжать и рассчитать избыточность', self)
        self.calculate_button.clicked.connect(self.calculate_huffman)
        self.left_layout.addWidget(self.calculate_button)
        
        # Set the background color for the QWidget to light lilac
        self.setStyleSheet("background-color: #D8B5D8; font-family: System;")  # Light lilac background and System font
        
        # Right part of the screen for the detailed results
        self.right_layout = QVBoxLayout()
        self.right_layout.setContentsMargins(15, 0, 0, 0)  # Set 15px left margin for results
        
        # Labels to display results on the left and right
        self.left_result_label = QLabel(self)
        self.right_result_label = QLabel(self)
        
        self.right_layout.addWidget(self.right_result_label)
        
        # Add layouts to the main layout
        layout.addLayout(self.left_layout)
        layout.addLayout(self.right_layout)
        self.setLayout(layout)

    def calculate_huffman(self):
        try:
            # Clear previous results in the labels
            self.left_result_label.setText("")
            self.right_result_label.setText("")
            
            # Build the Huffman tree and calculate the results
            root = build_huffman_tree(self.frequencies)
            codes = generate_codes(root)
            entropy = calculate_entropy(self.frequencies)
            average_length = calculate_average_length(codes, self.frequencies)
            redundancy_ratio = (average_length - entropy) / average_length if average_length else 0

            # Left part - Huffman codes
            left_result = "Коды Хаффмена:\n"
            for i in range(1, 10):
                symbol = f'x{i}'
                code = codes.get(symbol, 'Неизвестен')
                left_result += f"{symbol}: {code}\n"
            
            left_result += f"\nЭнтропия H: {entropy:.4f} бит\n"
            left_result += f"Средняя длина кода L: {average_length:.4f} бит\n"
            left_result += f"Коэффициент избыточности R: {redundancy_ratio:.4f} (или {redundancy_ratio * 100:.2f}%)\n"
            
            # Set the left result label
            self.left_result_label.setText(left_result)
            self.left_layout.addWidget(self.left_result_label)

            # Right part - Detailed calculations
            calculation_details = "Подробные расчеты:\n"
            calculation_details += "Энтропия H рассчитывается по формуле:\n"
            calculation_details += "H = -∑(p * log2(p))\n"
            for symbol, freq in self.frequencies.items():
                if freq > 0:
                    calculation_details += f"H({symbol}) = -({freq:.2f} * log2({freq:.2f})) = {freq * math.log2(freq):.4f}\n"
            calculation_details += f"Общая энтропия H = {entropy:.4f} бит\n\n"
            calculation_details += "Средняя длина кода L рассчитывается по формуле:\n"
            calculation_details += "L = ∑(p * L(x))\n"
            for symbol in codes:
                calculation_details += f"L({symbol}) = {self.frequencies[symbol]:.2f} * len({codes[symbol]}) = " \
                                       f"{self.frequencies[symbol]:.2f} * {len(codes[symbol])} = " \
                                       f"{self.frequencies[symbol] * len(codes[symbol]):.4f}\n"
            calculation_details += f"Общая средняя длина кода L = {average_length:.4f} бит\n\n"
            calculation_details += "Коэффициент избыточности R рассчитывается по формуле:\n"
            calculation_details += "R = (L - H) / L\n"
            calculation_details += f"R = ({average_length:.4f} - {entropy:.4f}) / {average_length:.4f} = {redundancy_ratio:.4f}\n"
            
            # Set the right result label
            self.right_result_label.setText(calculation_details)
            self.right_layout.addWidget(self.right_result_label)

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")  # Вывод ошибки в консоль
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HuffmanApp()
    window.show()
    sys.exit(app.exec())
