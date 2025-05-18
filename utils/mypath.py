import os

class Path(object):
    @staticmethod
    def pathology_root_dir():
      
        root_dir = "/home/SDMSegmentation/"
        return os.path.join(root_dir, "PathologyDataset") 
        
        