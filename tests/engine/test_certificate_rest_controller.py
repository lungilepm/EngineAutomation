from helpers.engine.CertificateRestController import CertificateRestController
from utilities.genericUtilities import *

obj_auth = CertificateRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

