import prefect
from prefect import task, Flow

@task
def say_hello(name):
	logger = prefect.context.get("logger")
	logger.info('Hi' + name)
	
with Flow('my-hello-flow') as flow:
	say_hello('Zach')
