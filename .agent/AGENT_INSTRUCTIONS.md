# Repository Agent Instructions

## Purpose

Work in this repository as a careful contributor. Preserve its existing organization and conventions, and make changes that are focused, reviewable, and supported by a clear rationale.

## Before making changes

1. Confirm that you are working in the repository. If it is not available locally, clone the configured repository before proceeding.
2. Check the current branch and working tree. Preserve any existing user changes; do not overwrite or discard them.
3. Fetch and integrate the latest changes from the relevant base branch. Use a fast-forward update when possible, and resolve any conflicts carefully before continuing.
4. Read `README.md` and inspect the repository structure to understand its purpose, setup, and conventions.
5. Create a topic branch with a concise, descriptive name related to the task. Do not make task changes directly on the base branch.

## Making changes

- Keep the existing directory structure and project conventions intact.
- Make only changes that are relevant to the requested task.
- If a structural or convention change would improve the result, explain its rationale in the handoff and, where appropriate, in the change itself.
- Follow the setup and dependency guidance in `README.md` and the project's configuration files.
- Avoid committing generated files, local environments, credentials, or unrelated user changes.
- Run appropriate checks for the changes and report their results. If a check cannot be run, state why.

## Review and delivery

1. Review the final diff for correctness, scope, and accidental changes.
2. Stage only the files related to the task and create a clear commit when delivery requires one.
3. Publish the topic branch to the configured remote when requested or otherwise authorized.
4. Open a pull request targeting `main`, with a concise summary, rationale, and relevant verification results.
5. Report the branch, commit, pull request link, and any remaining limitations to the user.
