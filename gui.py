# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 700)
        Form.setMinimumSize(QtCore.QSize(1000, 700))
        Form.setMaximumSize(QtCore.QSize(1000, 700))
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(210, 20, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.RadarReceiverWave = QtWidgets.QLabel(Form)
        self.RadarReceiverWave.setGeometry(QtCore.QRect(580, 120, 151, 16))
        self.RadarReceiverWave.setObjectName("RadarReceiverWave")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 80, 281, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PeakPower = QtWidgets.QLabel(self.layoutWidget)
        self.PeakPower.setObjectName("PeakPower")
        self.gridLayout.addWidget(self.PeakPower, 0, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.AntennaGain = QtWidgets.QLabel(self.layoutWidget)
        self.AntennaGain.setObjectName("AntennaGain")
        self.gridLayout.addWidget(self.AntennaGain, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.CarrierFrequency = QtWidgets.QLabel(self.layoutWidget)
        self.CarrierFrequency.setObjectName("CarrierFrequency")
        self.gridLayout.addWidget(self.CarrierFrequency, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.ReceiverLength = QtWidgets.QLabel(self.layoutWidget)
        self.ReceiverLength.setObjectName("ReceiverLength")
        self.gridLayout.addWidget(self.ReceiverLength, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.ReceiverNoiseFactor = QtWidgets.QLabel(self.layoutWidget)
        self.ReceiverNoiseFactor.setObjectName("ReceiverNoiseFactor")
        self.gridLayout.addWidget(self.ReceiverNoiseFactor, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.SystemLoss = QtWidgets.QLabel(self.layoutWidget)
        self.SystemLoss.setObjectName("SystemLoss")
        self.gridLayout.addWidget(self.SystemLoss, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.OutputMinSigNoiseRatio = QtWidgets.QLabel(self.layoutWidget)
        self.OutputMinSigNoiseRatio.setObjectName("OutputMinSigNoiseRatio")
        self.gridLayout.addWidget(self.OutputMinSigNoiseRatio, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.BaseRCS = QtWidgets.QLabel(self.layoutWidget)
        self.BaseRCS.setObjectName("BaseRCS")
        self.gridLayout.addWidget(self.BaseRCS, 7, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.TargetRCS = QtWidgets.QLabel(self.layoutWidget)
        self.TargetRCS.setObjectName("TargetRCS")
        self.gridLayout.addWidget(self.TargetRCS, 8, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 1)
        self.TargetDistance = QtWidgets.QLabel(self.layoutWidget)
        self.TargetDistance.setObjectName("TargetDistance")
        self.gridLayout.addWidget(self.TargetDistance, 9, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 9, 1, 1, 1)
        self.RadarDistanceRange = QtWidgets.QLabel(self.layoutWidget)
        self.RadarDistanceRange.setObjectName("RadarDistanceRange")
        self.gridLayout.addWidget(self.RadarDistanceRange, 10, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 10, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(530, 80, 251, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RadarDistanceRange_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.RadarDistanceRange_2.setObjectName("RadarDistanceRange_2")
        self.gridLayout_2.addWidget(self.RadarDistanceRange_2, 0, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(530, 660, 241, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.StartSimulation = QtWidgets.QPushButton(self.layoutWidget2)
        self.StartSimulation.setObjectName("StartSimulation")
        self.gridLayout_3.addWidget(self.StartSimulation, 0, 0, 1, 1)
        self.ExitSystem = QtWidgets.QPushButton(self.layoutWidget2)
        self.ExitSystem.setObjectName("ExitSystem")
        self.gridLayout_3.addWidget(self.ExitSystem, 0, 1, 1, 1)
        self.WaveImgDisplay = QtWidgets.QLabel(Form)
        self.WaveImgDisplay.setGeometry(QtCore.QRect(330, 150, 645, 485))
        self.WaveImgDisplay.setText("")
        self.WaveImgDisplay.setObjectName("WaveImgDisplay")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RadarSystemSimulation"))
        self.Title.setText(_translate("Form", "早期雷达探测系统的模拟"))
        self.RadarReceiverWave.setText(_translate("Form", "雷达接收机显示器波形"))
        self.PeakPower.setText(_translate("Form", "峰值频率(KW)"))
        self.AntennaGain.setText(_translate("Form", "天线增益(dB)"))
        self.CarrierFrequency.setText(_translate("Form", "载波频率(GHz)"))
        self.ReceiverLength.setText(_translate("Form", "接收机带宽(MHz)"))
        self.ReceiverNoiseFactor.setText(_translate("Form", "接收机噪声系数(dB)"))
        self.SystemLoss.setText(_translate("Form", "系统损耗(dB)"))
        self.OutputMinSigNoiseRatio.setText(_translate("Form", "输出端最低信噪比(dB)"))
        self.BaseRCS.setText(_translate("Form", "基准RCS(m2)"))
        self.TargetRCS.setText(_translate("Form", "目标RCS(m2)"))
        self.TargetDistance.setText(_translate("Form", "目标距离(Km)"))
        self.RadarDistanceRange.setText(_translate("Form", "雷达距离量程(Km)"))
        self.RadarDistanceRange_2.setText(_translate("Form", "雷达作用距离(Km)"))
        self.StartSimulation.setText(_translate("Form", "开始仿真"))
        self.ExitSystem.setText(_translate("Form", "退出系统"))