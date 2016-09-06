from glue.config import data_factory
from glue.core import Data
from glue.config import importer

from qt_widget import QtFortranDialog
import numpy as np



def is_dat(filename, **kwargs):
    return filename.endswith('.dat')

#def showNdimDialog(self, ):
#    text, ok = QtGui.QInputDialog.getInt(self, 'Input Ndim', 'Enter Ndim:')
#    if ok:
#        return text

@data_factory('Import Fortran Unformatted File')
def fort_import(name):
    wi = QtFortranDialog(name)
    wi.exec_()
    return Data(cube=wi.X)
    

