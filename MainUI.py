import sys
import zipfile,math
NoOfProcessor = 4
from multiprocessing import Process, Manager
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QMainWindow
import pickle

AcceptedExtenderList = [".zip", ".7z", ".apk", ".rar", ".tar"]
TryingPassWordListList = []
with open("data/UPWL.pickle", "rb") as UPWL:
    TryingPassWordListList.append(pickle.load(UPWL))


class Cracker():
    def __init__(self, ZipLists):
        print("cracker made")
        self.ZipLists = ZipLists

    def DoorBreaching(self, ZipFile, PasswordDictSync):
        print("yamete cudasai")
        SelectedZipFile = zipfile.ZipFile(ZipFile)
        try:
            SelectedZipFile.extractall()
            PasswordDictSync[ZipFile] = ""
            print("DoorBreaching")
            return
        except:
            for ProcessingNo in range(0, len(TryingPassWordListList)):
                ExecutedDoorBreachingProcess = self.DoorBreachingProcess(SelectedZipFile,
                                                                         TryingPassWordListList[ProcessingNo])
                if ExecutedDoorBreachingProcess:
                    PasswordDictSync[ZipFile] = ExecutedDoorBreachingProcess
                    return
                else:
                    continue

    def DoorBreachingProcess(self, SelectedZipFile, TryingPassWordList):
        for PasswordGuess in TryingPassWordList:
            try:
                SelectedZipFile.extractall(password = PasswordGuess)
                print("DoorBreachingProcess")
                return PasswordGuess
            except:
                continue
        return False

    def Execute(self):
        print("Executed")
        counter = 0
        ProcessList = []
        with Manager() as manager:
            PasswordDictSync = manager.dict()
        while True:
            for cores in range(0, NoOfProcessor):
                if counter >= len(self.ZipLists()):
                    break
                if ProcessList[cores].is_alive():
                    print('Puta')
                    continue
                else:
                    print('Puta')
                    ProcessList[cores] = Process(target = self.DoorBreaching,
                                                 args = (self.ZipLists[counter], PasswordDictSync))
                    counter = counter + 1
                    ProcessList[cores].daemon()
                    ProcessList[cores].start()


link = []


class Signal(QObject):
    DragEventSignal = pyqtSignal(int)

    def SendData(self, option):
        return


class WidgetRCV(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.msg = Signal()
        print("pussy")

    def dragLeaveEvent(self, event):
        event.accept()
        print("leaved")
        self.msg.DragEventSignal.emit(2)

    def dragEnterEvent(self, event):
        YesToSendYes = False
        event.accept()
        if event.mimeData().hasUrls:
            for url in event.mimeData().urls():
                print(str(url.toLocalFile()))
                if url.isLocalFile() and str(url.toLocalFile()).endswith(tuple(AcceptedExtenderList)):
                    YesToSendYes = True

            if YesToSendYes:
                print("yes")
                self.msg.DragEventSignal.emit(1)
            else:
                print("no")
                self.msg.DragEventSignal.emit(0)

    def dropEvent(self, event):
        event.accept()
        print("pussy")
        if event.mimeData().hasUrls:
            ZipFileList=[]
            event.setDropAction(Qt.CopyAction)
            self.msg.DragEventSignal.emit(2)
            self.setStyleSheet("Border:2px dashed white;background-color: rgba(255, 255, 255, 0);")
            print(event.mimeData().urls())
            print("drop Event Happened")
            for url in event.mimeData().urls():
                print(str(url.toLocalFile()))
                if url.isLocalFile() and str(url.toLocalFile()).endswith(tuple(AcceptedExtenderList)):
                    ZipFileList.append(url.toLocalFile())
            if ZipFileList:
                Crack= Cracker(ZipFileList)
                Crack.Execute()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 611)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.023, y2:0, stop:0.159091 rgba(175, 60, 138, 255), stop:1 rgba(255, 98, 0, 255));")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setStyleSheet("")
        self.MainWidget.setObjectName("MainWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MainWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.SubWidget = WidgetRCV()
        self.SubWidget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.SubWidget.setStyleSheet("Border:2px dashed white;\n"
                                     "background-color: rgba(255, 255, 255, 0);")
        self.SubWidget.setObjectName("SubWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.SubWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(self.SubWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "Border:0px solid white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/fileicon2.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.label_2 = QtWidgets.QLabel(self.SubWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);background-color: rgba(255, 255, 255, 0);\n"
                                   "Border:0px solid white;\n"
                                   "font: 75 15pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.label_3 = QtWidgets.QLabel(self.SubWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgba(255, 255, 255, 0);\n"
                                   "Border:0px solid white;\n"
                                   "font: 75 15pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.SelectFileBtn = QtWidgets.QPushButton(self.SubWidget)
        self.SelectFileBtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "color: rgb(105, 145, 255);\n"
                                         "Border:0px ;\n"
                                         "font: 75 15pt \"Arial\";")
        self.SelectFileBtn.setObjectName("SelectFileBtn")
        self.horizontalLayout.addWidget(self.SelectFileBtn)
        self.label_4 = QtWidgets.QLabel(self.SubWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);background-color: rgba(255, 255, 255, 0);\n"
                                   "Border:0px solid white;\n"
                                   "font: 75 15pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.SubWidget, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.MainWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.SubWidget.setAcceptDrops(True)
        self.SubWidget.msg.DragEventSignal.connect(self.DragEventSignal_emitted)

    @pyqtSlot(int)
    def DragEventSignal_emitted(self, option):
        self.label.setPixmap(QtGui.QPixmap("data/fileicon{}.png".format(option)))
        self.SubWidget.setStyleSheet("Border:2px solid white;background-color: rgba({}, {}, {}, {});"
                                     .format((255*((option+1)%2)), (255*math.ceil(option/2)),
                                    (255*math.floor(option/2)),((50+80*(option%2))*(1-math.floor(option/2)))))
        self.label_2.setStyleSheet(
            "color: rgba(255, 255, 255, {});background-color: rgba(255, 255, 255, 0);Border:0px solid white;font: 75 15pt \"Arial\";".format(255*math.floor(option/2)))
        self.label_3.setStyleSheet(
            "color: rgba(255, 255, 255, {});background-color: rgba(255, 255, 255, 0);Border:0px solid white;font: 75 15pt \"Arial\";".format(255*math.floor(option/2)))
        self.label_4.setStyleSheet(
            "color: rgba(255, 255, 255, {});background-color: rgba(255, 255, 255, 0);Border:0px solid white;font: 75 15pt \"Arial\";".format(255*math.floor(option/2)))
        self.SelectFileBtn.setStyleSheet(
            "color: rgba(255, 255, 255, {});background-color: rgba({}, {}, 255, {});Border:0px ;font: 75 15pt \"Arial\";".format(255*math.floor(option/2),255-150*math.floor(option/2),255-110*math.floor(option/2),255*math.floor(option/2)))
        print("fuck off")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "drag & drop zip file"))
        self.label_3.setText(_translate("MainWindow", "or click"))
        self.SelectFileBtn.setText(_translate("MainWindow", "HERE"))
        self.label_4.setText(_translate("MainWindow", "to open file"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
