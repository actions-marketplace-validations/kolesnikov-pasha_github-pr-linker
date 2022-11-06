import json

def get_pr_data(text=None):
    print(text)
    if text is not None:
        return json.loads(text)
    else:
        with open("example_github_event.json", "r") as f:
            data = "".join(f.readlines())
            return json.loads(data)


def get_action(pr_data):
    return pr_data["action"]


def get_author_url(pr_data):
    return pr_data["sender"]["url"]


def get_author_login(pr_data):
    return pr_data["sender"]["login"]


def get_pr_url(pr_data):
    return pr_data["pull_request"]["html_url"]


def get_pr_name(pr_data):
    return pr_data["pull_request"]["title"]


def get_source_branch(pr_data):
    return pr_data["pull_request"]["head"]["ref"]