import os
from contextlib import contextmanager
from typing import Any, Dict, Optional

from dagster_cloud_cli import gql


@contextmanager
def client_from_env(deployment: Optional[str] = None):
    url = os.environ["DAGSTER_CLOUD_URL"]
    if deployment:
        url = url + "/" + deployment
    with gql.graphql_client_from_url(url, os.environ["DAGSTER_CLOUD_API_TOKEN"]) as client:
        yield client


def get_registry_info() -> Dict[str, Any]:
    with client_from_env() as client:
        return gql.get_ecr_info(client)
