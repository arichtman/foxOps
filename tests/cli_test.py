#!/usr/bin/env python
"""Tests for `foxops` package."""
import pytest
from click.testing import CliRunner
from foxops import cli


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_no_arguments(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0


def test_debug_argument(runner: CliRunner) -> None:
    """Debug flag enables debug logging"""
    result = runner.invoke(cli.cli, ["--debug", "group"])
    assert result.exit_code == 0
    assert "DEBUG:foxops" in result.output
