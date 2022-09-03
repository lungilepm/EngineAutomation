import os

from atlassian import Confluence

from configs.hosts_config import CONFLUENCE_HOST

jira_username = CONFLUENCE_HOST[os.environ.get('ENV', 'username')]
jira_api_token = CONFLUENCE_HOST[os.environ.get('ENV', 'Key')]
url = CONFLUENCE_HOST[os.environ.get('ENV', 'confluenceUrl')]
confluence = Confluence(
    url=url,
    username=jira_username,
    password=jira_api_token,
    cloud=True)
