################################################################################
# Algorithmia image vegetation algorithm                                       #
# ============================================================================ #
#                                                                              #
# This algorithm predicts the percentage vegetation present in street-level    #
# images. The implementation wraps the functionality of the                    #
# https://methods.officialstatistics.org/algorithms/nocturne/segment service.  #
#                                                                              #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
from .util import sanity 
from .vegetator import factory 

def apply(input):
    """Algorithmia entry point."""
    sanity(input)
    src_images = input['src']
    detection_method = input['method']
    veg_method = factory.instance(detection_method)
    percentages = veg_method.process(src_images)
