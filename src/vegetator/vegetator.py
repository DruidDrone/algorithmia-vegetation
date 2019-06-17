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
        
        def get_datafile(img_loc):
            idx = img_loc.rfind("/")
            data_dir = img_loc[:idx]
            file_str = img_loc[idx+1:]
            #return self.client.dir(data_dir)
            return self.client.dir(data_dir).file(file_str)

        files = self.pre_processing([get_datafile(f) for f in src]).files() if type(src) is list else self.pre_processing(src).files()
        file_name = lambda file_str: file_str[file_str.rfind("/")+1:]
        return {file_name(img_loc.getName()):self.post_processing(img_loc) for img_loc in files}
