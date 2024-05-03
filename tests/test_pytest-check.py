import pytest


@pytest.fixture
def sample_fixture():
    return {"a": 1, "b": 2}


def test_sample_fail(sample_fixture):
    assert sample_fixture == 1


def test_sample_pass(sample_fixture):
    assert sample_fixture == {"a": 1, "b": 2}


def test_always_fails():
    assert False


@pytest.mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert (maybe_palindrome == "".join(reversed(maybe_palindrome))) == expected_result
