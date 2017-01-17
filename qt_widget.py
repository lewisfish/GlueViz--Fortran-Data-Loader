from glue.external.qt import QtGui
from glue.external.qt.QtCore import Qt
from glue.utils.qt.helpers import load_ui
import numpy as np
import os

UI_MAIN = os.path.join(os.path.dirname(__file__), 'dialog.ui')


class QtFortranDialog(QtGui.QDialog):

    def __init__(self, name):

        super(QtFortranDialog, self).__init__()

        self.ui = load_ui(UI_MAIN, self)
        self.name = name
        self.X = []
        self.Y = []
        self.Z = []
        self.valdim = 3
        self.valtext = '3'
        self.flag = False
        self.forthDim.hide()
        self.forthval = 0

        self.Formattedbut.toggled.connect(self.hidelayout)
        self.Unformattedbut.toggled.connect(self.showlayout)

        self.dimensions.valueChanged.connect(self.valuechange)
        self.GridSize.textChanged.connect(self.textchange)
        self.comboBox.activated[str].connect(self.selectionchange)

        self.Load.clicked.connect(self.click)

        self.forthDim.valueChanged.connect(self.forthdimChange)

    def click(self):

        if not self.flag:
            fd = open(self.name, 'rb')

            if '8' in self.valtext:
                dt = np.float64
            elif '4' in self.valtext:
                dt = np.float32

            dat = np.fromfile(file=fd, dtype=dt, sep="")

            magic = self.valdim
            try:
                ndim = self.valgrid
            except AttributeError:
                self.GridSize.setFocus()

            if magic == 4:
                shape = (ndim, ndim, ndim, magic)
            elif magic == 3:
                shape = (ndim, ndim, ndim)
            else:
                print('Not yet supported...')
            dat = dat.reshape(shape)
            fd.close()
            if magic == 4:
                dat = dat[:, :, :, self.forthval]
            self.X = dat[:, :, :]
            # self.Y = dat[0, :, 0]
            # self.Z = dat[0, 0, :]
            del dat
        else:
            self.X = np.loadtxt(self.name)

        self.accept()

    def selectionchange(self, text):
        self.valtext = text

    def textchange(self):
        try:
            self.valgrid = int(self.GridSize.text())
        except ValueError:
            pass
        except AttributeError:
            self.GridSize.setFocus()

    def valuechange(self):
        self.valdim = int(self.dimensions.value())

        if self.valdim == 4:
            self.forthDim.show()
        else:
            self.forthDim.hide()

    def forthdimChange(self):

        self.forthval = int(self.forthDim.value())

    def hidelayout(self):

            self.dimensions.hide()
            self.comboBox.hide()
            self.GridSize.hide()
            self.label.hide()
            self.label_2.hide()
            self.label_3.hide()

            self.flag = True

    def showlayout(self):
        if self.flag:
            self.dimensions.show()
            self.comboBox.show()
            self.GridSize.show()
            self.label.show()
            self.label_2.show()
            self.label_3.show()

            self.flag = False
