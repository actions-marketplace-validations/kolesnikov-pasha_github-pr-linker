from github_parser.extract_pr_data import get_action, get_pr_data
from entities.entities import EventAction

cases = [
    ({"action": "opened"}, EventAction.OPENED),
    ({"action": "closed", "pull_request": {"merged": False}}, EventAction.CLOSED),
    ({"action": "ready_for_review"}, EventAction.READY_FOR_REVIEW),
    (get_pr_data("pr_linker/github_parser/tests/examples/example_github_event_1.json"), EventAction.OPENED),
    (get_pr_data("pr_linker/github_parser/tests/examples/example_github_event_2.json"), EventAction.MERGED)
]

for case in cases:
    actual_result = get_action(case[0])
    assert actual_result == case[1], f"Test case input = {case[0]}, expected output = {case[1]}, actual output = {actual_result}"