import os


def test_example_overrides_existing_variables():
    assert os.environ["NAME"] == "Homer Simpson"


def test_example_does_not_override_existing_variables():
    assert os.environ["NAME"] == "Bart Simpson"
