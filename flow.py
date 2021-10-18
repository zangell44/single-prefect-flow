import prefect
from prefect import task, Flow, Parameter
from prefect.storage import Git

#storage = Git(flow_path='flow.py', repo='zangell44/single-prefect-flow', git_token_secret_name="SUPAH_SECRET_GH_TOKEN") # commit='4854091758c9ca28766a60abeae88e66be0e9b63')
storage = Git(flow_path='flow.py', repo='zangell44/single-prefect-flow')

#name = 'foo'

@task
def say_hello(name):
	logger = prefect.context.get("logger")
	logger.info('Hi' + name)
	
with Flow('my-hello-flow') as flow:
	name = Parameter(name="name", default='Zach')
	say_hello(name)

flow.storage = storage
flow.register('test')
#flow.run()
