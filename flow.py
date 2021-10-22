from prefect import task, Parameter, Flow
from os import getenv
from typing import Tuple
from prefect.storage import Git

pg_db = Parameter("LOGARY_PG_DB", default=getenv("LOGARY_PG_DB", default="analytics"))
@task(nout=2)
def fetch_model(dsn_params) -> Tuple[str, str]:
    # m = _fetch_model(dsn_params)
    # return m.id, m
    return 'test', '123'


def build_dsn_params(dbname, application_name):
    return pg_db

with Flow(
    "missing_uuid",
    # state_handlers=[print_state_callback],
) as flow:
    # https://deepnote.com/project/Media-Mix-Model-5xns-00xTG6nRlUK1f9DfA/%2Ftest_preprocessing.ipynb

    #
    ########### CONFIG #######

    dsn_params = lambda name: build_dsn_params(
        # user=pg_user,
        # password=pg_password,
        # host=pg_host,
        # port=pg_port,
        dbname=pg_db,
        # sslmode=pg_sslmode,
        application_name=f"mmm/{name}",
    )
    model_id, model = fetch_model(dsn_params("fetch_model"))

flow.storage = Git(flow_path='flow.py', repo='zangell44/single-prefect-flow')

flow.register('test')
