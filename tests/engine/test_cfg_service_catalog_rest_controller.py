from helpers.engine.CfgServiceCatalogRestController import CfgServiceCatalogRestController
from utilities.genericUtilities import *

obj_auth = CfgServiceCatalogRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

