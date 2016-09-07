from glue.config import data_factory
from glue.core import Data

from qt_widget import QtFortranDialog

@data_factory('Import Fortran Unformatted File')
def fort_import(name):
    wi = QtFortranDialog(name)
    wi.exec_()
    return Data(cube=wi.X)
    

