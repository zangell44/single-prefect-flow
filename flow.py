import prefect
from prefect import task, Flow, Parameter
from prefect.storage import Git

storage = Git(flow_path='flow.py', repo='zangell44/single-prefect-flow')

@task
def say_hello(name):
	logger = prefect.context.get("logger")
	logger.info('Hi' + name)
	
with Flow('my-hello-flow') as flow:
	name = Parameter(name, default='Zach')
	say_hello(name)

flow.storage = storage
flow.register('test')
#flow.run(
