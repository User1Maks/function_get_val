from utils import dicts


def test_get_val():
    assert dicts.get_val(
        {"vcs": "mercurial", "program": "python", "university": "Skypro"},
        "vcs", "git") == "mercurial"

    assert dicts.get_val(
        {"vcs": "mercurial", "program": "python", "university": "Skypro"},
        "", "git") == "git"

    assert dicts.get_val({}, "", "git") == "git"
