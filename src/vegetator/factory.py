################################################################################
# Algo factory.                                                                # 
# ============================================================================ #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
from .lab import Lab 
from .deep import Deep

from Algorithmia.errors import AlgorithmException

def instance(vegetation_method):
    """Get a Vegetator.

    Parameters
    ----------
    vegetation_method: str
        The vegetation method to use. Either:
        - lab: Lab based segmentation.
        - deep: Deep image segmentaton.

    Returns
    -------
    Vegetator
    """
    if vegetation_method == 'lab':
        return Lab()
    if vegetation_method == 'deep':
        return Deep()
    raise AlgorithmException("Expected 'lab' or 'deep'", 'UnsupportedError')
