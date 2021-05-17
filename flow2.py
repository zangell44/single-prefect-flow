import os
from prefect import Flow, Parameter, task
from prefect.run_configs import KubernetesRun
from prefect.storage import Git
@task(log_stdout=True)
def say_hello(name):
    print("Hello, {}!".format(name))
with Flow("Hello World") as flow:
    thename = Parameter("name")
    say_hello(thename)
storage = Git(
    repo="zangell44/single-prefect-flow",
    flow_path="flow2.py",
    #branch_name="my/branch-name",
    use_ssh=True,
)
#storage.add_flow(flow) # the Flow object
#storage.get_flow(flow.name) # try to load the flow from git storag
