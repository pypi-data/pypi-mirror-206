# Copyright 2023 Q-CTRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The CLI tool to generate release note.
"""
import click
from git import (
    InvalidGitRepositoryError,
    Repo,
)

from qctrlreleasenoter.generate_release_notes import generate_note


@click.command(
    help="""
    Prints release notes for the commits between the latest tag and `branch`.

    Commits are expected to follow the Conventional Commits specification
    (https://www.conventionalcommits.org/en/v1.0.0/). That is, messages are
    typically expected to be of the form:

        \b
        <kind>: <title>

        \b
        <description>

    The valid types and the release type they lead to are defined in the
    contributing guidelines (https://code.q-ctrl.com/contributing).

    Messages for commits introducing breaking changes are expected to be of
    the form:

        \b
        <kind>!: <title>

        \b
        <description>

        \b
        BREAKING CHANGE: <explanation of the breaking change>
    """
)
@click.option(
    "--branch",
    default="master",
    help="Branch on which the release will be made (defaults to master).",
)
@click.option(
    "--ignore/--no-ignore",
    default=True,
    help="Whether to ignore commits from robot@q-ctrl.com (defaults to True).",
)
@click.option(
    "--github",
    is_flag=True,
    default=False,
    help="Open GitHub with the release notes prefilled.",
)
@click.option(
    "--phase",
    type=click.Choice(["stable", "alpha", "beta"]),
    default="stable",
    help="Select the phase for the release (defaults to stable).",
)
def main(branch, ignore, github, phase):
    """
    Main entry to generate the release note.
    """
    try:
        generate_note(branch, ignore, github, phase, repo=Repo("."))
    except InvalidGitRepositoryError as err:
        raise RuntimeError("The current directory is not a valid repository.") from err
