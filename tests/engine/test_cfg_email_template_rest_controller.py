from helpers.engine.CfgEmailTemplateRestController import CfgEmailTemplateRestController
from utilities.genericUtilities import *

obj_auth = CfgEmailTemplateRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

