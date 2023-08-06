# sprinkler (s7r)
Sprinkler is a easy to use job runner. It runs individual tasks inside of docker containers on a single host machine.
Currently sprinkler supports both python and nodejs (yarn and npm) runtimes.

Sprinkler works best when integrated with a git repository.

# Prerequisites
 - Python3 >= 3.6
 - redis
 - docker


# Quickstart
After installing the prerequisites you can install sprinkler via pip.
```bash
pip3 install s7r
```

The sprinkler tool is now available on the command line via the `sprinkler` keyword.
```bash
sprinkler version
```

There are three sprinkler services that all perform different functions.
 - task-manager
 - webserver
 - scheduler
When setting up sprinkler in a production environment, we recommend using
systemd to orchestrate these services.

In order to enable all sprinkler functionality, run all three of these services.
To enable secrets encryption and secure sessions make sure that the `SPRINKLER_SECRET`
environment variable is set. If this variable changes, then sprinkler will be unable to
decrypt secrets, and all sessions will be invalidated.

When run, sprinkler will create a `.sprinkler` directory in your home directory.
Inside of this, the sqlite database which stores run history, config values, secrets,
and api keys is held, as well as sub-directories for local logs, and the sprinkler generated ssh key.

After starting the services, the rest of the setup is easiest to complete through the UI
although it can all be completed from the CLI as well.

You must point sprinkler to the targets directory by setting the `TARGETS_DIRECTORY` config.

To set up sprinkler with a remote git repo in the sprinkler directory,
then use the `sprinkler git init ~/.sprinkler/ git@github.com:<...>` command.
This will clone the given remote into a subdirectory within the `.sprinkler` directory.
This will automatically set the `TARGETS_DIRECTORY` to the root directory inside of the repo that you cloned.

With all of the services running, and the `TARGETS_DIRECTORY` set, you can utilize the UI or CLI to configure sprinkler and trigger tasks.

# Sprinkler-Utils
Sprinkler provides a utils package for use within sprinkler tasks. The package provides the following functions:

## get_request_body
This function will return the request body if one exists. This enables content to be passed
into the task when it is triggered by a webhook. If the task is triggered by a schedule
then this will return None.

## get_secret
This function will return the value of a secret. If the secret doesn't exist, then a default value can be provided.

## send_response
This function can be used to send a response to a request. This function should only be invoked once per task.
The response will be sent upon completion of the entire task. Additionally the task must be setup as a `call-and-response`
type task for the response to be sent. Otherwise sprinkler will reply with a `task started`
message immediately upon receiving a trigger. This type of task can be used as a simple webserver,
however it is important to realize that this will not be as performant as other webservers as each request
is handled within a separate docker container.


# sprinkler_config.yaml
Each target is required to have a `sprinkler_config.yaml` file. This file defines the runtime for the target,
as well as the tasks within the target.
## Schema
```yaml
runtime: python | node-npm | node-yarn # The runtime.
version: string # The version of the runtime to use.
os: Optional[string] # The os for the image to use.
# The runtime, version, and os will be combined together to pick the base image to utilize.
# {runtime}{version}-{os} EX: python3.11-slim-buster
failure_task: Optional
    target: string # The target containing the task to trigger when a task within this target fails.
    task: string # The task to trigger when a task within this target fails.


tasks:
    - task: string # The name of the task.
      entrypoint: string # The file to execute when running this task
      schedule: Optional[string[chron expression]] # A schedule to run this task on.
      timeout: Optional[int] # The number of seconds to let this task run before killing it. If it is not set, then the task will run indefinitely.
      failure_task:
        target: string # The target containing the task to trigger when a task within this target fails.
        task: string # The task to trigger when a task within this target fails.
    type: call-and-response | fire-and-forget # The default task type is `fire-and-forget`.

```
