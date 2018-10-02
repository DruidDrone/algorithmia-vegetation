################################################################################
# Sanitise/check input                                                         # 
# ============================================================================ #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
from Algorithmia.errors import AlgorithmException

def sanity(input):
    """Sanitise input."""
    if type(input) is not dict:
        raise AlgorithmException("Only JSON accepted", 'UnsupportedError')
