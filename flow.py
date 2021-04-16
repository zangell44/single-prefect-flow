from prefect import task, Flow
from prefect.storage import GitRepo

storage = GitRepo(file_path='flow.py', git_url='https://github.com/zangell44/single-prefect-flow.git')

@task
def say_hello(name):
        logger = prefect.context.get("logger")
        logger.info('Hi' + name)

with Flow('my-hello-flow') as flow:
        say_hello('Zach')

flow.storage = storage
