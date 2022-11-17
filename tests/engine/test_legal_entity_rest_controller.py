from helpers.engine.LegalEntityRestController import LegalEntityRestController
from utilities.genericUtilities import *

obj_auth = LegalEntityRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

