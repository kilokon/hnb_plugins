# import os
import re

# test_Name_v01.hipnc

DELIMITER = "_"


class ConnotGetVersionError(Exception):
    pass


class FileName:
    def __init__(self):
        self.__file_info = None

    @property
    def file_info(self):
        return self.__file_info

    @file_info.setter
    def file_info(self, f_name):
        if len(f_name.split(DELIMITER)) == 2:
            m = re.match(r"(?P<title>\w+)_(?P<file_version>\w+)", f_name)
            if m is not None:
                self.__file_info = {
                    "title": m.group("title"),
                    "file_version": m.group("file_version"),
                }
        elif len(f_name.split(DELIMITER)) == 3:
            m = re.match(
                r"(?P<topic>\w+)_(?P<title>\w+)_(?P<file_version>\w+)", f_name
            )
            if m is not None:
                self.__file_info = {
                    "topic": m.group("topic"),
                    "title": m.group("title"),
                    "file_version": m.group("file_version"),
                }
        elif len(f_name.split(DELIMITER)) == 4:
            m = re.match(
                r"(?P<project>\w+)_(?P<topic>\w+)_(?P<title>\w+)_(?P<file_version>\w+)",
                f_name,
            )
            if m is not None:
                self.__file_info = {
                    "project": m.group("project"),
                    "topic": m.group("topic"),
                    "title": m.group("title"),
                    "file_version": m.group("file_version"),
                }
        else:
            self.__file_info = None

    def get_current_version(self) -> int:
        if self.file_info is not None:
            v = self.file_info.get("file_version")
            if v is not None:
                m = re.search(r"[\d.]+", v)
                if m is not None:
                    return int(m[0])
        raise ConnotGetVersionError


def file_name_validate(name):
    if DELIMITER not in name or not re.match(r"^[a-zA-Z]", name):
        return 0
    return 1


# TESTS
def test_hipFileA():
    filename = "test_Name_v01.hipnc"
    assert file_name_validate(filename) == 1


def test_noDelimiterInHipName():
    filename = "testNamev01.hipnc"
    assert file_name_validate(filename) == 0


def test_specialCharacterInHipName():
    filename = "_Name_v01.hipnc"
    assert file_name_validate(filename) == 0


def test_name():
    filename = "test_Name_v01.hipnc"
    f_n = FileName()
    f_n.file_info = filename
    assert f_n == {"topic": "test"}


# if __name__ == "__main__":
#     filename = "test_Name_v01.hipnc"
#     f_n = FileName()
#     f_n.file_info = filename
#     print(f_n.get_current_version())
