# Sample Git Hooks

These hooks can be customised to suit ones needs. 
They are provided as examples and starting point only.

## Commit Message Hook
The commit message hook is a simple script that checks the commit message for a specific pattern.

It should be saved as `<repo_root>/.git/hooks/commit-msg` and should be 
an executable file (`chmod 755 commit-msg`).

### Files:

* [`commit-msg.py`](commit-msg.py): Sample commit message hook in Python.
* [`commit-msg.rb`](commit-msg.rb): Sample commit message hook in Ruby.

These sample hooks verify that a commit message follows the following structure:

* First line of the message is a Subject line (50 characters max)
* Second line is blank
* Third and subsequent lines form a Body (72 characters max per line)

This hook does not enforce the language of a commit message, however, 
it is recommended to follow best practices.

See various resources for commit message guidelines and conventions at the end of this document.

## Post Checkout Hook
The post checkout hook is a simple script that runs after a checkout operation (branch or files from index).

It should be saved as `<repo_root>/.git/hooks/post-checkout` and should be 
an executable file (`chmod 755 post-checkout`).

### Files:

* [`post-checkout`](post-checkout): Sample post checkout hook as Bash script.

This hook check whether the type of checkout is a branch checkout and only runs
if there is a change in HEAD ref.
It can be customised using environment variables defined in `<repo_root>/.env.git-hooks.local` file.

This script takes a docker compose file and rebuilds and restarts the specified containers.

## Post Merge Hook
The post merge hook is a simple script that runs after a merge operation. This hook does not modify the outcome of a merge.

It should be saved as `<repo_root>/.git/hooks/post-merge` and should be
an executable file (`chmod 755 post-merge`).

### Files:
* [`post-merge`](post-merge): Sample post merge hook as Bash script.

This hook behaves similar to the post checkout hook, but it runs after a merge operation.

## References
* [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
* [Git Commit Message Guidelines](https://cbea.ms/git-commit/)
* [Keep Your Commits "Atomic"](https://www.freshconsulting.com/insights/blog/atomic-commits/)
* [Semantic Versioning](https://semver.org/)
