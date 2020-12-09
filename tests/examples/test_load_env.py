import os


def test_assert_env():
    assert os.getenv("NAME") == "Homer Simpson"
    assert os.getenv("EMAIL") == "chunkylover53@aol.com"
