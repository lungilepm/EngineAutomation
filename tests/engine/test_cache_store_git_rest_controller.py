from helpers.engine.CacheStoreGitRestController import CacheStoreGitRestController
from utilities.genericUtilities import *

obj_auth = CacheStoreGitRestController()
agencies = INT_HOST[os.environ.get('ENV', 'use_agencies')] 

