from .lab import Lab 
from .deep import Deep

from Algorithmia.errors import AlgorithmException

def instance(vegetation_method):
    if vegetation_method == 'lab':
        return Lab()
    if vegetation_method == 'deep':
        return Deep()
    raise AlgorithmException("Expected 'lab' or 'deep'", 'UnsupportedError')
