from helpers.engine.CfgCertificateTypeRestController import CfgCertificateTypeRestController
from utilities.genericUtilities import *

obj_auth = CfgCertificateTypeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

