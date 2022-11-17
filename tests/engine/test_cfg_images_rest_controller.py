from helpers.engine.CfgImagesRestController import CfgImagesRestController
from utilities.genericUtilities import *

obj_auth = CfgImagesRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

