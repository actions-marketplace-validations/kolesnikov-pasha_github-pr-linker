import json
from notion_api import notion_utils

IDS = [
    "d1f5b7bb-c59a-463a-a709-66ffc3dbcb0e",
    "707aabe5-de8f-4d36-b0fc-b2d43e8112a3",
    "0084f0fa-9fd7-44e3-8eeb-d09808ea927d",
    "b99ad1a7-add4-472c-86dc-d168600aabc5",
    "6f4e6773-ed7b-40c1-9ec6-2ecba346be01",
    "9eaf9024-b6f5-433d-9422-bf2106158add",
    "8352b383-ef1d-4227-a253-55d2352be531",
    "a2d4c464-a8d7-4acf-bffe-a5d86d9cd247",
    "f2d2b32a-9fc4-41c6-83f4-56e2f999a8cf",
    "8938db9c-e901-42f4-81d4-bf1380a2b745",
    "ec16fb29-39ae-4829-95d8-a64b2956719a",
    "fb79b2fb-6d6b-432a-ba04-63af23af88f7"
]
TASKS_IDS = [
    "TASKS-12",
    "TASKS-11",
    "TASKS-10",
    "TASKS-9",
    "TASKS-8",
    "TASKS-7",
    "TASKS-5",
    "TASKS-6",
    "TASKS-4",
    "TASKS-3",
    "TASKS-2",
    "TASKS-1"
]

with open("pr_linker/notion_api/tests/examples/database_example_1.json", "r") as f:
    database = json.load(f)
for i, page in enumerate(notion_utils.__iterate_through_database_pages__(database)):
    id = notion_utils.__get_page_id__(page)
    assert id == IDS[i], f"Failed, expected id = {IDS[i]}, found id = {id}"
    task_id = notion_utils.__get_task_id__(page)
    assert task_id == TASKS_IDS[i], f"Failed, expected task id = {IDS[i]}, found task id = {id}"

for task_id, page_id in zip(TASKS_IDS, IDS):
    page = notion_utils.find_page_by_id(database, task_id)
    assert notion_utils.__get_page_id__(page) == page_id, f"Failed finding correct page for task_id = {task_id}" 