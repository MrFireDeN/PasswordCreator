# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys, math, random, string

from PyQt6 import QtCore, QtGui, QtWidgets
from form import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def setup_connections(self):
        self.doubleSpinBoxP.textChanged.connect(self.spinbox_changed)
        self.doubleSpinBoxV.textChanged.connect(self.spinbox_changed)
        self.doubleSpinBoxT.textChanged.connect(self.spinbox_changed)

        self.checkLatCap.stateChanged.connect(self.on_checkbox_state_changed)
        self.checkLatUpper.stateChanged.connect(self.on_checkbox_state_changed)
        self.checkRusCap.stateChanged.connect(self.on_checkbox_state_changed)
        self.checkRusUpper.stateChanged.connect(self.on_checkbox_state_changed)
        self.checkSimbols.stateChanged.connect(self.on_checkbox_state_changed)
        self.checkDigits.stateChanged.connect(self.on_checkbox_state_changed)

        self.btnGenerate.clicked.connect(self.on_btn_clicked)

    def spinbox_changed(self):
        # Переменные из DoubleSpinBox
        self.__P = self.doubleSpinBoxP.value()
        self.__V = self.doubleSpinBoxV.value()
        self.__T = self.doubleSpinBoxT.value()

        if self.__P <= 0:
            self.__P = 1
        if self.__V <= 0:
            self.__V = 1
        if self.__T <= 0:
            self.__T = 1

        # Считаем нижную границу пароля S*
        self.__S = math.ceil(math.fabs((V * T) / P))
        print(self.__S)
        self.labelNumS.setText(str(self.__S))

        # Функция для счета длины пароля L
        self.__calculateL()

    def on_checkbox_state_changed(self):
        # Переменные из CheckBox
        self.__latCap = self.checkLatCap.value()
        self.__latUpper = self.checkLatUpper.value()
        self.__rusCap = self.checkRusCap.value()
        self.__rusUpper = self.checkRusUpper.value()
        self.__simbols = self.checkSimbols.value()
        self.__digits = self.checkDigits.value()

        # Считаем мощность алфавита A
        self.__A = latCap * 26 + latUpper * 26 + rusCap * 33 + rusUpper * 33 + symbols * 33 + digits * 10
        print(self.__A)

        # Вывод пароля в текстовое поле
        self.labelNumA.setText(str(self.__A))

        # Функция для счета длины пароля L
        self.__calculateL()

    def __calculateL(self):
        # Если поля пустые
        if not(self.__S and self.__A):
            return

        # Считаем длину пароля L
        self.__L = math.log(self.__S, self.__A)

        # Выводим
        self.labelNumL.setText(str(self.__L))

    def on_btn_clicked(self):
        # Генерация пароля
        password = ""

        # Пул символов, из которых будет сгенерирован пароль
        pool = ""
        if self.__latCap:
            pool += string.ascii_uppercase
        if self.__latUpper:
            pool += string.ascii_lowercase
        if self.__rusCap:
            pool += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        if self.__rusUpper:
            pool += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        if self.__simbols:
            pool += "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
        if self.__digits:
            pool += string.digits

        if (pool):
            # Генерация пароля случайным образом из пула символов
            for _ in range(int(self.__L)):
                password += random.choice(pool)

            # Установка сгенерированного пароля в текстовое поле
            self.linePassword.setText(password)
        else:
            self.linePassword.setText("!!!Алфавит пустой!!!")

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    ui.spinbox_changed()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()