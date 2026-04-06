import pytest


def test_uppercase():
    assert "python".upper() == "PYTHON"


def test_reversed():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]


@pytest.fixture
def example_fixture():
    return 42


def test_with_fixture(example_fixture):
    assert example_fixture == 42


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonso",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        }
    ]


def format_data_for_display(people):
    return [f"{p['given_name']} {p['family_name']}: {p['title']}"
            for p in people]


def format_data_for_excel(people):
    return [f"{p['given_name']}, {p['family_name']}, {p['title']}"
            for p in people]


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonso Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager"
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == [
        "Alfonso, Ruiz, Senior Software Engineer",
        "Sayid, Khan, Project Manager"
    ]


def is_palindrome(word):
    return word == word[::-1]


@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "bob",
    "Never odd or even",
    "Do geese see God?"
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", False),
    ("bob", True),
    ("Never odd or even", False),
    ("Do geese see God?", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
