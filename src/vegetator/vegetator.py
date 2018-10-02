################################################################################
# Image Vegetator                                                              # 
# ============================================================================ #
#                                                                              #
# Wraps functionality of the                                                   #
# https://methods.officialstatistics.org/algorithms/nocturne/segment service.  #
#                                                                              #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
import Algorithmia

class Vegetator():

    def __init__(self):
        self.client = Algorithmia.client()

    def pre_processing(self, src):
        """hook method."""
        pass

    def post_processing(self, src):
        """hook method."""
        return -1

    def process(self, src):
        """Process the input street-level images.

        Parameters
        ----------
        src: str
            The location of the input images.

        Returns
        -------
        list
            A list of predicted percentage vegetation for each image.
        """
        src_dir = self.pre_processing(src)
        return [self.post_processing(img_loc) for img_loc in src_dir.files()]
