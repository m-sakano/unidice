#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QRubberBand
from main_window import Ui_Form
from selectWidget import Ui_Form2
from PIL import Image, ImageGrab
import os, sys, time
import pyocr
import pyocr.builders
import ConfigParser

class MainWindow(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.select = [0,0,0,0]

        horzHeaders = ['プレイヤー','ダイス']
        self.tableWidget.setColumnCount(len(horzHeaders))
        self.tableWidget.setHorizontalHeaderLabels(horzHeaders)

        self.lineEdit.setText(config.get('default','area'))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.textChanged.connect(self.saveConfigArea)

        self.pushButton_3.clicked.connect(self.showSelectWidget)
        self.pushButton.clicked.connect(self.analyse)
        self.pushButton_2.clicked.connect(self.reset)

    def showSelectWidget(self):
        self.widget = SelectWidget()
        self.widget.show()

    def reset(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def analyse(self):
        # 選択範囲の面積がゼロの場合は何もしない
        area = self.lineEdit.text().encode('utf-8').split(',')
        if area[0]==area[2] or area[1]==area[3]:
            return

        data = []
        for i in range(0, self.tableWidget.rowCount()):
            name = self.tableWidget.item(i, 0).text()
            dice = self.tableWidget.item(i, 1).text()
            row = (name, int(dice))
            data.append(row)

        self.grab = self.grabWindow()
        self.picture2text(self.img)

        data = list(set(data + self.extractText(self.txt)))
        if self.radioButton.isChecked():
            data.sort(key=lambda rec: rec[1], reverse=True)
        elif self.radioButton_2.isChecked():
            data.sort(key=lambda rec: rec[1], reverse=False)

        self.tableWidget.setRowCount(len(data))

        row = 0
        for record in data:
            name = QtWidgets.QTableWidgetItem()
            dice = QtWidgets.QTableWidgetItem()
            name.setText(record[0])
            dice.setText(str(record[1]))
            self.tableWidget.setItem(row, 0, name)
            self.tableWidget.setItem(row, 1, dice)
            row += 1

    def saveConfigArea(self):
        value = self.lineEdit.text().encode('utf-8')
        config.set('default', 'area', value)
        with open('config.cfg','wb') as configfile:
            config.write(configfile)

    def grabWindow(self):
        area = self.lineEdit.text().encode('utf-8').split(',')
        self.img = ImageGrab.grab((int(area[0]),int(area[1]),int(area[2]),int(area[3])))
        width = int(area[2]) - int(area[0])
        height = int(area[3]) - int(area[1])
        zoom = 1    #拡大すると精度がよくなるかもしれない？
        self.img.resize((width*zoom, height*zoom),resample=Image.LANCZOS)

    def picture2text(self, picture):
        tools = pyocr.get_available_tools()
        tool = tools[0]
        self.txt = tool.image_to_string(
            picture,
            lang="jpn",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )

    def extractText(self, text):
        data = []
        for line in text.split("\n"):
            if line[1:2] == '1':
                line = line[0:1] + u'イ' + line [2:]
            if line[3:4] == 'T':
                line = line[0:3] + u'！' + line[4:]
            #if line[3:4] == '7':
            line = line[0:3] + u'！' + line[4:]
            if u'ダイス' in line:
                line = line.replace('!', u'！')
                line = line.replace(u'！3', u'は')
                line = line.replace(u'！S', u'は')
                line = line.replace(u'、', '')
                name = line[line.find(u'ダイス')+3:line.find(u'・')]
                name = name.replace(u'！', '')
                name = name[0:name.find(u'は')]
                name = name.replace(u'、', '')
                name = name.replace(' ', '')
                name = name.replace('.', '')
                name = name.replace('4', 'A')
                name = name.replace('5', 'S')
                name = name.replace('8', 'B')
                name = name.replace('7', 'T')
                name = name.replace('0', 'O')
                if len(name) > 2:
                    name = name[0:2]
                if len(name) == 2:
                    name = name[0]+'.'+name[1]+'.'
                dice = line[line.find(u'・')+1:line.find(u'を出')]
                dice = dice.replace(u'！','1')
                dice = dice.replace(u'イ', '4')
                dice = dice.replace('O', '0')
                dice = dice.replace('D', '0')
                dice = dice.replace('S', '5')
                dice = dice.replace('T', '7')
                dice = dice.replace('B', '8')
                if len(dice) > 3:
                    dice = dice[0:3]
                if dice.isdigit():
                    record = (name, int(dice))
                    data.append(record)
        return data

class SelectWidget(QWidget, Ui_Form2):

    select = [0,0,0,0]

    def __init__(self, parent=None):
        super(SelectWidget, self).__init__(parent)
        self.setWindowOpacity(0.5)
        self.setupUi(self)
        desktop = QtWidgets.QDesktopWidget()
        self.resize(desktop.availableGeometry().width(), desktop.availableGeometry().height())
        self.rubberband = QRubberBand(
            QRubberBand.Rectangle, self)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.select[0] = event.screenPos().x()
        self.select[1] = event.screenPos().y()
        self.origin = event.pos()
        self.rubberband.setGeometry(
            QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubberband.show()
        QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())
        QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.select[2] = event.screenPos().x()
        self.select[3] = event.screenPos().y()
        if self.rubberband.isVisible():
            self.rubberband.hide()
            rect = self.rubberband.geometry()

        # ポインタ座標を左上→右下に揃える
        if self.select[0] > self.select[2]:
            tmp = self.select[0]
            self.select[0] = self.select[2]
            self.select[2] = tmp
        if self.select[1] > self.select[3]:
            tmp = self.select[1]
            self.select[1] = self.select[3]
            self.select[3] = tmp
        # 選択した面積がゼロの場合は何もしないで関数を終わる
        if self.select[0]==self.select[2] or self.select[1]==self.select[3]:
            QWidget.mouseReleaseEvent(self, event)
            self.close()
            return
        # ポインタ座標をメインウインドウに設定する
        area = ''
        for point in self.select:
            area = area + str(int(point)) + ','
        main_window.lineEdit.setText(area[0:-1])
        self.close()
        QWidget.mouseReleaseEvent(self, event)

if __name__ == '__main__':
    if os.name == 'nt':
        os.environ['PATH']=os.environ['PATH']+';'+os.getcwd()
    config = ConfigParser.RawConfigParser()
    config.read('config.cfg')
    app = QApplication(sys.argv)
    main_window = MainWindow()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("windowicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    main_window.show()
    sys.exit(app.exec_())
