from helpers.engine.CfgPdfTemplateRestController import CfgPdfTemplateRestController
from utilities.genericUtilities import *

obj_auth = CfgPdfTemplateRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

