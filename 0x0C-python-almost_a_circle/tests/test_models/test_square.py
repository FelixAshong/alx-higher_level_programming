#!/usr/bin/python3
import unittest
import json
import io
import sys

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        y = Square(10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Square(10, 10, 10, 15)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)
        x = Square(56444, 500, 90000, 240000)
        self.assertEqual(x.size, 56444)
        self.assertEqual(x.x, 500)
        self.assertEqual(x.y, 90000)
        self.assertEqual(x.id, 240000)

    def test_attrs_type_validation(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("20", 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(4.3, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2: 1}, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("20")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(["hello world", "?"])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(20, "x", 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(20, -42.3, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(20, 10, "y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(20, 10, 5.2)
        self.assertRaises(TypeError, Square, float("NaN"))
        self.assertRaises(TypeError, Square, float("inf"))
        self.assertRaises(TypeError, Square, float("NaN"),
                          float("NaN"), float("NaN"))
        self.assertRaises(TypeError, Square, float("inf"),
                          float("inf"), float("inf"))
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, [10, 10],
                          [10, 10], [10, 10])
        self.assertRaises(TypeError, Square, "abebe",
                          "abebe", "abebe")
        self.assertRaises(TypeError, Square, 10,
                          [10, 10], {10, 10})

    def test_attrs_value_validation(self):
        Base._Base__nb_objects = 0
        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err, Square, -20)
        self.assertRaisesRegex(ValueError, w_err, Square, 0)
        self.assertRaisesRegex(ValueError, w_err, Square, -20000000)

        h_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, h_err, Square, -20)
        self.assertRaisesRegex(ValueError, h_err, Square, 0)
        self.assertRaisesRegex(ValueError, h_err, Square, -20000000)

        x_err = "x must be >= 0"
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -10)
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -100000)

        y_err = "y must be >= 0"
        self.assertRaisesRegex(ValueError, y_err, Square, 10, 10, -10)
        self.assertRaisesRegex(ValueError, y_err, Square, 1, 1, -100000)

    def test_area(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        self.assertEqual(x.area(), 100)
        x = Square(1234)
        self.assertEqual(x.area(), 1522756)
        x = Square(1)
        self.assertEqual(x.area(), 1)
        x = Square(43)
        self.assertEqual(x.area(), 1849)

    def test_display(self):
        Base._Base__nb_objects = 0

        captured_print = io.StringIO()
        sys.stdout = captured_print

        x = Square(2, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  ##\n  ##\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        x = Square(1, 1)
        x.display()
        self.assertEqual(captured_print.getvalue(), " #\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        x = Square(1, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  #\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        sys.stdout = sys.__stdout__

    def test_str(self):
        Base._Base__nb_objects = 0
        x = Square(1, 2, 2)
        self.assertEqual(x.__str__(), "[Square] (1) 2/2 - 1")

        x = Square(1, 1)
        self.assertEqual(x.__str__(), "[Square] (2) 1/0 - 1")

        x = Square(10000, 10000)
        self.assertEqual(x.__str__(), "[Square] (3) 10000/0 - 10000")

    def test_args_update(self):
        Base._Base__nb_objects = 0
        x = Square(1, 2, 2)

        x.update(1, 10, 10, 20)
        self.assertEqual(x.__str__(), "[Square] (1) 10/20 - 10")

        x.update(1, 10, 10, 20, 20)
        self.assertEqual(x.__str__(), "[Square] (1) 10/20 - 10")

        x.update(1, 10, 10, 20, 20, 40, 50, 60)
        self.assertEqual(x.__str__(), "[Square] (1) 10/20 - 10")

        x.update(10)
        self.assertEqual(x.id, 10)

        x.update(13, 10, 20, 20)
        self.assertEqual(x.__str__(), "[Square] (13) 20/20 - 10")

    def test_kwargs_update(self):
        Base._Base__nb_objects = 0
        x = Square(1, 1, 2, 2)

        x.update(id=1, size=10, x=20, y=20)
        self.assertEqual(x.__str__(), "[Square] (1) 20/20 - 10")

        x.update(id=1, size=10, x=20, y=20, chala=40)
        self.assertEqual(x.__str__(), "[Square] (1) 20/20 - 10")

        x.update(id=10)
        self.assertEqual(x.id, 10)

        x.update(id=15, x=10, y=20, size=20)
        self.assertEqual(x.id, 15)
        self.assertEqual(x.__str__(), "[Square] (15) 10/20 - 20")

        temp = {'x': 1, 'y': 9, 'id': 1, 'size': 2}
        x.update(**temp)
        self.assertEqual(x.id, 1)
        self.assertEqual(x.__str__(), "[Square] (1) 1/9 - 2")

        temp = {'x': 120, 'y': 98, 'id': 5, 'size': 200}
        x.update(**temp)
        self.assertEqual(x.id, 5)
        self.assertEqual(x.__str__(), "[Square] (5) 120/98 - 200")

    def test_args_kwargs_update(self):
        Base._Base__nb_objects = 0
        x = Square(1, 2, 2)

        x.update(20, id=1)
        self.assertEqual(x.id, 20)

        x.update(1, 30, width=10, size=10, x=20, y=20, chala=40)
        self.assertEqual(x.__str__(), "[Square] (1) 2/2 - 30")

        x.update(id=10)
        self.assertEqual(x.id, 10)

        x.update(id=15, x=10, y=20, size=20)
        self.assertEqual(x.id, 15)
        self.assertEqual(x.__str__(), "[Square] (15) 10/20 - 20")

        x.update(13, 10, 20, 20)
        self.assertEqual(x.id, 13)
        self.assertEqual(x.__str__(), "[Square] (13) 20/20 - 10")

        temp = {'x': 1, 'y': 9, 'id': 1, 'size': 2}
        temp2 = [10, 20, 40, 50]
        x.update(*temp2, **temp)
        self.assertEqual(x.id, 10)
        self.assertEqual(x.__str__(), "[Square] (10) 40/50 - 20")

        temp = {'x': 20, 'y': 8, 'id': 7, 'size': 21}
        temp2 = [6000, 240, 7653, 5970]
        x.update(*temp2, **temp)
        self.assertEqual(x.id, 6000)
        self.assertEqual(x.__str__(), "[Square] (6000) 7653/5970 - 240")

    def test_to_dict(self):
        Base._Base__nb_objects = 0
        x = Square(1, 2, 2)

        expected = {"id": 1, "size": 1, "x": 2, "y": 2}
        self.assertDictEqual(x.to_dictionary(), expected)

        x.update(10, 40)
        expected = {"id": 10, "size": 40, "x": 2, "y": 2}
        self.assertDictEqual(x.to_dictionary(), expected)

        x.update(x=40, y=30)
        expected = {"id": 10, "size": 40, "x": 40, "y": 30}
        self.assertDictEqual(x.to_dictionary(), expected)

        y = Square(2)
        expected = {"id": 2, "size": 2, "x": 0, "y": 0}
        self.assertDictEqual(y.to_dictionary(), expected)

    def test_create_rect(self):
        x = Rectangle(10, 10, 2, 3)
        contents = x.to_dictionary()
        y = Rectangle.create(**contents)
        self.assertEqual(x.to_dictionary(), y.to_dictionary())
        self.assertEqual(vars(x), vars(y))

        x = Rectangle(10, 2, 3)
        contents = x.to_dictionary()
        y = Rectangle.create(**contents)
        self.assertEqual(x.to_dictionary(), y.to_dictionary())
        self.assertEqual(vars(x), vars(y))

        x = Rectangle(1, 2)
        contents = x.to_dictionary()
        y = Rectangle.create(**contents)
        self.assertEqual(x.to_dictionary(), y.to_dictionary())
        self.assertEqual(vars(x), vars(y))

    def test_create_square(self):
        x = Square(10, 2, 3)
        contents = x.to_dictionary()
        y = Square.create(**contents)
        self.assertEqual(x.to_dictionary(), y.to_dictionary())

        x = Square(10, 3)
        contents = x.to_dictionary()
        y = Square.create(**contents)
        self.assertEqual(x.to_dictionary(), y.to_dictionary())

        x = Square(2)
        contents = x.to_dictionary()
        y = Square.create(**contents)
        self.assertEqual(x.to_dictionary(), y.to_dictionary())


if __name__ == "__main__":
    unittest.main()
