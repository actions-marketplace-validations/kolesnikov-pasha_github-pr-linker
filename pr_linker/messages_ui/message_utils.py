from entities import entities


__PR_NAME__ = "<PR_NAME>"
__PR_AUTHOR__ = "<PR_AUTHOR>"

__PR_ACTION_TO_PATTERN__ = {
    entities.EventAction.OPENED: ["👋 Opened pull request \"", __PR_NAME__,  "\" by ", __PR_AUTHOR__],
    entities.EventAction.EDITED: ["✍️ Edited pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__], 
    entities.EventAction.CLOSED: ["❌ Closed pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__], 
    entities.EventAction.REOPENED: ["🔙 Reopened pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__], 
    entities.EventAction.SYNCRONIZE: ["🔥 Updated pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__], 
    entities.EventAction.CONVERTED_TO_DRAFT: ["📝 Converted pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__, " to draft"], 
    entities.EventAction.READY_FOR_REVIEW: ["👀 Pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__, " is ready for review"], 
    entities.EventAction.REVIEW_REQUESTED: ["🔎 Review requested for pull request \"", __PR_NAME__, "\" by ", __PR_AUTHOR__]
}


def get_message(action, pr_name, pr_url, author_name, author_url):
    pattern = __PR_ACTION_TO_PATTERN__[action]
    message = []
    for pattern_part in pattern:
        if pattern_part == __PR_NAME__:
            message.append(entities.Text(pr_name, href=pr_url))
        elif pattern_part == __PR_AUTHOR__:
            message.append(entities.Text(author_name, href=author_url))
        else:
            message.append(entities.Text(pattern_part))

    return message