from glue.config import data_factory, link_function
from glue.core import Data
from glue.config import auto_refresh

from qt_widget import QtFortranDialog

auto_refresh(True)


@data_factory('Import Fortran Unformatted File')
def fort_import(name):
    wi = QtFortranDialog(name)
    wi.exec_()
    return Data(x=wi.X)
