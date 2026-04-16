# AGENTS.md

## Interactions with Users

- Always activate `/caveman full` skill at the beginning of a session (if the skills is available).

## Implementing the Use of Environment Variables

- If you are creating a shell file, Docker file, or something similar and this file requires an environment variable, do not add a default value for this variable to the file. Instead, add an error message that hints towards the missing environment variable.
