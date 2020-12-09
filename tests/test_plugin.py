import os
from unittest import mock


def test_does_not_run_invalid_file(testdir):
    testdir.copy_example("test_load_env.py")

    result = testdir.runpytest("--env-file=./.invalidenv", "-v", "test_load_env.py")

    assert result.ret == 3


def test_loads_env_from_cli(testdir):
    testdir.copy_example(".env")
    testdir.copy_example("test_load_env.py")

    result = testdir.runpytest("--env-file=./.env", "-v", "test_load_env.py")

    result.stdout.fnmatch_lines(
        [
            "*::test_assert_env PASSED*",
        ]
    )

    assert result.ret == 0


@mock.patch.dict(os.environ, {"NAME": "Bart Simpson"}, clear=True)
def test_does_not_override_existing_variables(testdir):
    testdir.copy_example(".env")
    testdir.copy_example("test_overrides.py")

    result = testdir.runpytest(
        "--env-file=./.env",
        "-v",
        "test_overrides.py::test_example_does_not_override_existing_variables",
    )

    result.stdout.fnmatch_lines(
        [
            "*test_overrides.py::test_example_does_not_override_existing_variables PASSED*",
        ]
    )

    assert result.ret == 0


@mock.patch.dict(os.environ, {"NAME": "Bart Simpson"}, clear=True)
def test_overrides_existing_variables(testdir):
    testdir.copy_example(".env")
    testdir.copy_example("test_overrides.py")

    result = testdir.runpytest(
        "--env-file=./.env",
        "--override-system-env=True",
        "-v",
        "test_overrides.py::test_example_overrides_existing_variables",
    )

    result.stdout.fnmatch_lines(
        [
            "*test_overrides.py::test_example_overrides_existing_variables PASSED*",
        ]
    )

    assert result.ret == 0
