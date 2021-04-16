import prefect
from prefect import task, Flow
from prefect.storage import GitRepo

storage = GitRepo(flow_path='flow.py', username='zangell44', repo_name='single-prefect-flow', branch_name='marvin')

@task
def say_hello(name):
        logger = prefect.context.get("logger")
        logger.info('Hi' + name)

with Flow('my-hello-flow') as flow:
        say_hello('Zach')

flow.storage = storage
