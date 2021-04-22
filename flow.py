import prefect
from prefect import task, Flow
from prefect.storage import Git

storage = Git(flow_path='flow.py', repo='zangell44/single-prefect-flow',  git_token_secret_name="SUPAH_SECRET_GH_TOKEN")

@task
def say_hello(name):
        logger = prefect.context.get("logger")
        logger.info('Hi' + name)

with Flow('my-hello-flow') as flow:
        say_hello('Zach2')

flow.storage = storage
