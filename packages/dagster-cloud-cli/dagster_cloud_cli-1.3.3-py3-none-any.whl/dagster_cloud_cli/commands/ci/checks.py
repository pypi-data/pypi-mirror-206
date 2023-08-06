import os
import pathlib
from dataclasses import dataclass, field
from enum import Enum
from typing import List

import pydantic

from dagster_cloud_cli import gql

from ... import ui
from ...core import pydantic_yaml


def get_validation_errors(validation_error: pydantic.ValidationError) -> List[str]:
    errors = []
    for error in validation_error.errors():
        if "type" in error:
            location = ".".join([str(part) for part in error["loc"] if part != "__root__"])
            if error["type"] == "value_error.missing":
                errors.append(f"expected '{location}': missing required field")
            elif error["type"] == "value_error.extra":
                errors.append(f"unexpected '{location}': unknown field")
            else:
                errors.append(f"{error['type']} at '{location}': {error['msg']}")
    return errors


@dataclass
class CheckResult:
    errors: List[str] = field(default_factory=list)
    messages: List[str] = field(default_factory=list)


def check_dagster_cloud_yaml(yaml_path: pathlib.Path) -> CheckResult:
    result = CheckResult()

    if not yaml_path.exists():
        result.errors.append(f"No such file {yaml_path}")
        return result

    yaml_text = yaml_path.read_text()
    if not yaml_text.strip():
        result.errors.append(f"Unexpected blank file {yaml_path}")
        return result

    try:
        parsed = pydantic_yaml.load_dagster_cloud_yaml(yaml_path.read_text())
    except pydantic.ValidationError as err:
        for error in get_validation_errors(err):
            result.errors.append(error)
        return result

    for location in parsed.locations:
        if location.build and location.build.directory:
            build_path = yaml_path.parent / location.build.directory
            if not build_path.is_dir():
                result.errors.append(
                    f"Build directory {build_path} not found for location"
                    f" {location.location_name} at {build_path.absolute()}"
                )
    return result


class Check(Enum):
    error = "error"
    warn = "warn"
    skip = "skip"


class Verdict(Enum):
    failed = "failed"
    warning = "warning"
    skipped = "skipped"
    passed = "passed"


def handle_result(
    result: CheckResult,
    check: Check,
    prefix_message: str,
    success_message: str,
    failure_message: str,
) -> Verdict:
    def full_msg(msg):
        return prefix_message + msg

    def passed(msg):
        ui.print("✅" + full_msg(msg))

    def warning(msg):
        ui.print("🟡" + ui.yellow(full_msg(msg)))

    def failed(msg):
        ui.print("🚫" + ui.red(full_msg(msg)))

    def print_indented(msgs):
        lines = "\n".join(msgs).splitlines(keepends=False)
        for line in lines:
            ui.print("  | " + line)

    if check == Check.skip:
        return Verdict.skipped

    if result.errors:
        if check == Check.error:
            failed(failure_message)
            print_indented(result.messages)
            print_indented(result.errors)
            ui.print("\n")
            return Verdict.failed
        elif check == Check.warn:
            warning(failure_message)
            print_indented(result.messages)
            print_indented(result.errors)
            ui.print("\n")
            return Verdict.warning
    else:
        passed(success_message)
        print_indented(result.messages)
        ui.print("\n")
        return Verdict.passed


def check_connect_dagster_cloud() -> CheckResult:
    if "DAGSTER_CLOUD_URL" not in os.environ:
        return CheckResult(["DAGSTER_CLOUD_URL not set"])
    if "DAGSTER_CLOUD_API_TOKEN" not in os.environ:
        return CheckResult(["DAGSTER_CLOUD_API_TOKEN not set"])
    result = CheckResult()
    result.messages.append(
        f"Connecting to {os.environ['DAGSTER_CLOUD_URL']} using DAGSTER_CLOUD_API_TOKEN"
    )
    with gql.graphql_client_from_url(
        os.environ["DAGSTER_CLOUD_URL"], os.environ["DAGSTER_CLOUD_API_TOKEN"]
    ) as client:
        try:
            gql.get_organization_settings(client)
            result.messages.append("Connection successful")
        except Exception as err:
            result.errors.append(f"Failed to connect to {os.environ['DAGSTER_CLOUD_URL']}: {err}")

    return result
