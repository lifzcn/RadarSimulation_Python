import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget

from gui import Ui_Form
import numpy as np
import matplotlib.pyplot as plt


class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.StartSimulation.clicked.connect(self.calculate)
        self.ExitSystem.clicked.connect(self.exit)

    def calculate(self, parent=None):
        k = 1.38e-23
        c = 3.0e8
        t0 = 273.15 + 25
        pi = 3.14

        valuePeakPower = float(self.lineEdit_1.text()) * 1e3  # 峰值功率
        valueAntennaGain = pow(10, float(self.lineEdit_2.text()) / 10)  # 天线增益
        valueCarrierFrequency = float(self.lineEdit_3.text()) * 1e9  # 载波频率
        valueReceiverLength = float(self.lineEdit_4.text()) * 1e6  # 接收机带宽
        valueReceiverNoiseFactor = pow(10, float(self.lineEdit_5.text()) / 10)  # 接收机噪声系数
        valueSystemLoss = pow(10, float(self.lineEdit_6.text()) / 10)  # 系统损耗
        valueOutputMinSigNoiseRatio = pow(10, float(self.lineEdit_7.text()) / 10)  # 输出端最低信噪比
        valueBaseRCS = float(self.lineEdit_8.text())  # 基准RCS
        valueTargetRCS = float(self.lineEdit_9.text())  # 目标RCS
        valueTargetDistance = float(self.lineEdit_10.text()) * 1e3  # 目标距离
        valueRadarDistanceRange = float(self.lineEdit_11.text()) * 1e3  # 雷达距离量程

        valueWaveLength = c / valueCarrierFrequency

        valueRmaxMolecular = valuePeakPower * pow(valueAntennaGain, 2) * pow(valueWaveLength, 2) * valueTargetRCS
        valueRmaxDenominator = pow(4 * pi, 3) * k * t0 * valueReceiverLength * valueReceiverNoiseFactor * valueSystemLoss * valueOutputMinSigNoiseRatio
        valueRmax = round(pow(valueRmaxMolecular / valueRmaxDenominator, 0.25) / 1000, 3)

        self.lineEdit_12.setText(str(valueRmax))

        valueSNRMolecular = valuePeakPower * pow(valueAntennaGain, 2) * pow(valueWaveLength, 2) * valueTargetRCS
        valueSNRDenominator = pow(4 * pi, 3) * k * t0 * valueReceiverLength * valueReceiverNoiseFactor * valueSystemLoss * pow(valueTargetDistance, 4)
        valueSNR = round(valueSNRMolecular / valueSNRDenominator, 3)

        N1 = 2 * valueRadarDistanceRange / c
        step = 1 / valueReceiverLength
        listTag = np.arange(0, N1, step)
        length = len(listTag)
        N2 = 2 * valueTargetDistance / c
        intNum = round(N2 / step)
        listValue = [0] * length
        if intNum:
            listValue[intNum - 1] = pow(valueSNR, 1 / 2)
        for i in range(length):
            listTag[i] = listTag[i] * c / 2 / 1000
            listValue[i] = listValue[i] + np.random.randn(1)
        plt.plot(listTag, listValue)
        plt.xlabel("Distance(Km)")
        plt.grid()
        plt.savefig("result.jpg")

        self.WaveImgDisplay.setPixmap(QtGui.QPixmap("result.jpg"))

    def exit(self, parent=None):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
