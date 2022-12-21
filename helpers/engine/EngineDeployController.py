from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
import os
from configs.hosts_config import INT_HOST
import logging as logger


class EngineDeployController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_engine_rest_importexport_generatecompleteexportfiles_helper(self, exportPOE=None, exportAuth=None,
                                                                        excludeAgencyParents=None,
                                                                        includeAgencyChildren=None, exportMLCS=None,
                                                                        exportENGINE=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/zip'}

        # The parameters of get_engine_rest_importexport_generatecompleteexportfiles_helper
        parameters = {
            'exportPOE': exportPOE,
            'exportAuth': exportAuth,
            'excludeAgencyParents': excludeAgencyParents,
            'includeAgencyChildren': includeAgencyChildren,
            'exportMLCS': exportMLCS,
            'exportENGINE': exportENGINE,
            'agencyId': agencyId}

        # The request payload of get_engine_rest_importexport_generatecompleteexportfiles_helper
        payload = {
        }

        # Default values to be used
        if not exportPOE:
            parameters['exportPOE'] = INT_HOST[os.environ.get('ENV', 'exportPOE')]

        if not exportAuth:
            parameters['exportAuth'] = INT_HOST[os.environ.get('ENV', 'exportAuth')]

        if not excludeAgencyParents:
            parameters['excludeAgencyParents'] = INT_HOST[os.environ.get('ENV', 'excludeAgencyParents')]

        if not includeAgencyChildren:
            parameters['includeAgencyChildren'] = INT_HOST[os.environ.get('ENV', 'includeAgencyChildren')]

        if not exportMLCS:
            parameters['exportMLCS'] = INT_HOST[os.environ.get('ENV', 'exportMLCS')]

        if not exportENGINE:
            parameters['exportENGINE'] = INT_HOST[os.environ.get('ENV', 'exportENGINE')]

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ENGINE/rest/importExport/generateCompleteExportFiles', payload=payload,
                                             headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

