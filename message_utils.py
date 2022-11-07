__PR_ACTION_TO_EMOJI__ = {
    "opened": "✋",
    "edited": "✍️", 
    "closed": "❌", 
    "reopened": "🔙", 
    "synchronize": "🔁", 
    "converted_to_draft": "📝", 
    "ready_for_review": "💁‍♂️", 
    "review_requested": "🔎"
}


def map_action2emoji(action):
    return __PR_ACTION_TO_EMOJI__[action]