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
        self.valdim = 4
        self.valtext = '4'
        
        self.dimensions.valueChanged.connect(self.valuechange)
        self.GridSize.textChanged.connect(self.textchange)
        self.comboBox.activated[str].connect(self.selectionchange)        

        self.Load.clicked.connect(self.click)

    def click(self):

        fd = open(self.name, 'rb')
        
        if '8' in self.valtext:
            dt = np.float64
        elif '4' in self.valtext:
            dt = np.float32

        dat = np.fromfile(file=fd, dtype=dt, sep="")

        magic = self.valdim
        ndim = self.valgrid
        
        if magic == 4:
            shape = (ndim, ndim, ndim, magic)
        elif magic == 3:
            shape = (ndim, ndim, ndim)
        else:
            print('Not yet supported...')
        dat = dat.reshape(shape, order='F') 
        fd.close()
        if magic == 4:
            dat = dat[:, :, :, 0]
        self.X = dat[:, :, :]
        del dat
        
        self.accept()
            
    def selectionchange(self, text):
        self.valtext = text

    def textchange(self):
        try:
            self.valgrid = int(self.GridSize.text())
        except ValueError:
            pass
            
    def valuechange(self):
        self.valdim = int(self.dimensions.value())
