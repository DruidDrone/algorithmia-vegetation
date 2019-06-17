################################################################################
# Image Vegetator                                                              # 
# ============================================================================ #
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
            A dictionary containing filenames and associated percentage vegetation scores.
        """
        files = src if type(src) is list else self.pre_processing(src).files()
        return {img_loc[img_loc.rfind("/")+1:]:self.post_processing(img_loc) for img_loc in files}
