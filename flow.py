import prefect
from prefect import task, Flow
from prefect.storage import Git
from pathlib import Path
import inspect

storage = Git(flow_path='flow.py', repo='zangell44/single-prefect-flow')

# get the path to my txt file
# this is tricky because my flow file
# is being cloned into a temporary directory when loaded
# from storage
# file_path = Path(__file__).resolve().parent
try:
        file_path = inspect.getfile(lambda: None)
except:
        breakpoint()

# load the file
with open(file_path + '/test.txt', 'r') as my_file:
        name = my_file.read()


@task
def say_hello(name):
        logger = prefect.context.get("logger")
        logger.info('Hi' + name)

with Flow('my-hello-flow') as flow:
        say_hello(name)

flow.storage = storage
