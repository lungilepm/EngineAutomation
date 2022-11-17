from helpers.engine.CfgPackageRestController import CfgPackageRestController
from utilities.genericUtilities import *

obj_auth = CfgPackageRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

