from github_parser.extract_pr_data import get_action
from entities.entities import EventAction

cases = [
    ({"action": "opened"}, EventAction.OPENED),
    ({"action": "closed"}, EventAction.CLOSED),
    ({"action": "ready_for_review"}, EventAction.READY_FOR_REVIEW)
]

for case in cases:
    actual_result = get_action(case[0])
    assert actual_result == case[1], f"Test case input = {case[0]}, expected output = {case[1]}, actual output = {actual_result}"