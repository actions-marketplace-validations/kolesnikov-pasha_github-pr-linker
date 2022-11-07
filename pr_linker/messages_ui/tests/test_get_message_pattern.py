from messages_ui.message_utils import get_message
from entities.entities import EventAction, Text

cases = [
    (
        (EventAction.OPENED, "Test PR", "test_pr.com", "kolesnikov-pasha", "github.com/kolesnikov-pasha"), 
        [Text("👋 Opened pull request \""), Text("Test PR", href="test_pr.com"), Text("\" by "), Text("kolesnikov-pasha", href="github.com/kolesnikov-pasha")]
    ),
    (
        (EventAction.READY_FOR_REVIEW, "Added ABOBA to resources", "aboba.com", "kolesnikov-pasha", "github.com/kolesnikov-pasha"),
        [Text("👀 Pull request \""), Text("Added ABOBA to resources", href="aboba.com"), Text("\" by "), Text("kolesnikov-pasha", href="github.com/kolesnikov-pasha"), Text(" is ready for review")]
    )
]
for case in cases:
    actual_output = get_message(*case[0])
    assert actual_output == case[1], f"Test case input = {case[0]}, expected output = [{', '.join(list(map(str, case[1])))}], actual output = [{', '.join(list(map(str, actual_output)))}]"