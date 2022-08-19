from VarTodos import VarTodos
from VarClinicas import VarClinicas
from ImportDB import importarbase
from AreaProg import AreaProg
from DiasIRAB import DiasIRAB
from direcciones import direcciones
from DxRespiMVS import DxRespiMVS
from EdadFDR import EdadFDR
from NoHipox import NoHipox
from RedCapFiliales import Filiales
from TestVSR import VSR

def inicial():
    VarTodos()
    VarClinicas()
    Filiales()

def reportes():
    importarbase()
    AreaProg()
    DiasIRAB()
    #direcciones()
    DxRespiMVS()
    EdadFDR()
    NoHipox()
    VSR()




