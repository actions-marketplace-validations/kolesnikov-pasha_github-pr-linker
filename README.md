<p align="center">
  <a href="https://github.com/kolesnikov-pasha/github-pr-linker/actions"><img alt="typescript-action status" src="https://github.com/kolesnikov-pasha/github-pr-linker/actions/workflows/pr_tests.yaml/badge.svg"></a>
</p>

# Update your Notion task with GitHub PR url

Create branch in format `*/{task_id}/{any-description}` and this action will automatically update your Notion task's property with the PR url and comment .

## Inputs

| input            | description                                           | required | default |
| ---------------- | ----------------------------------------------------- | -------- | ------- |
| `notion-token`   | Notion Secret API Key                                 | `true`   | `none`  |
| `database-id`    | ID of a database you want to use as a source of tasks | `true`   | `none`  |
| `task-id-param`  | Page parameter responsible for representing tasks IDs | `false`  | `ID`    |
| `task-id-prefix` | Common prefix of the task ID parameter values         | `false`  | `TASKS` |

## Configure

1. [Generate Notion secret](https://developers.notion.com/docs/getting-started#step-1-create-an-integration)
2. [Share your Notion Database (or Page) with the integration](https://developers.notion.com/docs/getting-started#step-2-share-a-database-with-your-integration)
3. Navigate to your Notion board, click on your task and add a new URL property. (Property name: `Github PR`)
4. Add github action like in [this example](.github/workflows/open_pr_notification.yaml)

## Usage

```yml
name: Add PR to Notion
on:
  pull_request:
    types: [opened]
jobs:
  notion:
    runs-on: ubuntu-latest
    steps:
      - name: Update notion page
        uses: kadaradam/notion-pr-link@latest
        with:
          notion_secret: secret_1234567890abcdef1234
          notion_prop: PR
```