import requests
from bow.utils.logger import warn


def check_url_validate(url):
    try:
        code = requests.get(url).status_code
        if code in range(400, 500):
            return warn("An client error in getting template occured, status code: ", code)
        elif code in range(500, 600):
            return warn("An server error in getting template occured, status code: ", code)
    except requests.exceptions.MissingSchema:
        warn("The URL is not valid, it cause the template not to work.")
    except requests.exceptions.ConnectionError:
        warn("Failed to establish a new connection. URL checking not passed.")
        
        
def extract_repo_name(url):
    return url.rstrip('.git').split('/')[-1]


def validate_git_repo(url):
    if url.startswith("https://") or url.startswith("http://"):
        if url.endswith(".git"):
            return True
        else:
            return validate_git_repo(url + ".git")
    else:
        return False