from alphaz.models.tests import AlphaTest, test
from alphaz.libs import py_lib, api_lib
from alphaz import dataclass, AlphaDataclass

import copy
from typing import Dict, List
import unittest

from core import core

LOG = core.get_logger("tests")


class TestClass:
    def __init__(self, a: str, b: int, c: float):
        self.a = a
        self.b = b
        self.c = c


@dataclass
class TestDataclass(AlphaDataclass):
    a: str
    b: int
    c: float


@dataclass
class TestParentDataclass(AlphaDataclass):
    childs_dt: list[TestDataclass]
    childs: List[TestClass]


class SubType(AlphaTest):
    def __init__(self):
        self.l: list[str] = []

        self.c1, self.c2 = TestClass("e", 2, 0.1), TestClass("c", 3, 0.8)
        self.dt1, self.dt2 = TestDataclass("e", 2, 0.3), TestDataclass("r", 4, 1.2)
        self.pdt1, self.pdt2 = TestParentDataclass(
            [self.dt1, self.dt2], [self.c1, self.c2]
        ), TestParentDataclass([self.dt2, self.dt1], [self.c2])

    @test()
    def sub_type_types(self):
        elements = [
            [list[str], list],
            [list[int], list],
            [List[int], list],
            [list[int] | list[str], list],
            [List[int] | list[str], list],
            [list[int] | None, list],
            [TestDataclass, TestDataclass],
            [TestDataclass | None, TestDataclass],
            [List[TestDataclass], list],
            [list[TestDataclass], list],
            [TestDataclass, AlphaDataclass],
            [[], list],
            [[1, 2, 3], list],
            [[1, 2, ""], list],
            [self.l, list],
            [[self.c1, self.c2], list],
            [[self.dt1, self.dt2], list],
            [[self.pdt1, self.pdt2], list],
            [[self.pdt1.childs_dt, self.pdt2.childs_dt], list],
            [[self.pdt1.childs, self.pdt2.childs], list],
            [self.pdt1.childs_dt, list],
            [self.pdt1.childs, list],
        ]
        for t1, t2 in elements:
            if not self.assert_is_true(
                py_lib.is_subtype(t1, t2, debug=True), no_log=True
            ):
                print("            TEST: ", t1, t2)

    @test()
    def get_sub_type(self):
        elements = [
            [list[str], list],
            [list[int], list],
            [List[int], list],
            [list[int] | list[str], list],
            [List[int] | list[str], list],
            [List[int] | list[str] | None, list],
            [None |  List[int] | list[str], list],
            [list[int] | None, list],
            [TestDataclass, TestDataclass],
            [TestDataclass | None, TestDataclass],
            [List[TestDataclass], list],
            [list[TestDataclass], list],
            [TestDataclass, AlphaDataclass],
            [[], list],
            [[1, 2, 3], list],
            [[1, 2, ""], list],
            [self.l, list],
            [[self.c1, self.c2], list],
            [[self.dt1, self.dt2], list],
            [[self.pdt1, self.pdt2], list],
            [[self.pdt1.childs_dt, self.pdt2.childs_dt], list],
            [[self.pdt1.childs, self.pdt2.childs], list],
            [self.pdt1.childs_dt, list],
            [self.pdt1.childs, list],
        ]

        for t1, t2 in elements:
            if not self.assert_is_true(
                py_lib.is_subtype(py_lib.get_first_non_none_type(t1), t2, debug=True),
                no_log=True,
            ):
                print("            TEST: ", t1, t2)

    @test()
    def auto_map_from_dict(self):
        json_str_dt = {"a": "e", "b": "2", "c": "0.3"}
        json_str_pdt = {"childs_dt": [json_str_dt], "childs": []}

        dt = TestDataclass.map_from_dict(json_str_dt)
        pdt = TestParentDataclass.map_from_dict(json_str_pdt)

        pdt1 = copy.copy(self.pdt1)
        pdt1.childs_dt = [self.dt1]
        pdt1.childs = []
        self.assert_equal(self.dt1, dt)
        self.assert_equal(pdt1, pdt)


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
