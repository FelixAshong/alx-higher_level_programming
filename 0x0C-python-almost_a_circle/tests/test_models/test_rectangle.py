#!/usr/bin/python3
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectCls(unittest.TestCase):
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10)
        y = Rectangle(10, 10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10, 10, 10, 15)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)

    def test_attrs_type_validation(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("20", 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, "20")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(20, 20, "x", 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(20, 20, 10, "y")
        self.assertRaises(TypeError, Rectangle, float("NaN"), float("inf"))
        self.assertRaises(TypeError, Rectangle, float("inf"), float("NaN"))
        self.assertRaises(TypeError, Rectangle, float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
        self.assertRaises(TypeError, Rectangle, float("inf"), float("inf"),
                          float("inf"), float("inf"))
        self.assertRaises(TypeError, Rectangle, None, None)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, [10, 10], [10, 10],
                          [10, 10], [10, 10])
        self.assertRaises(TypeError, Rectangle, "abebe", "abebe",
                          "abebe", "abebe")
        self.assertRaises(TypeError, Rectangle, 10, (10, 10),
                          [10, 10], {10, 10})

    def test_attrs_value_validation(self):
        Base._Base__nb_objects = 0
        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err, Rectangle, -20, 20)
        self.assertRaisesRegex(ValueError, w_err, Rectangle, 0, 20)
        self.assertRaisesRegex(ValueError, w_err, Rectangle, -20000000, 20)

        h_err = "height must be > 0"
        self.assertRaisesRegex(ValueError, h_err, Rectangle, 20, -20)
        self.assertRaisesRegex(ValueError, h_err, Rectangle, 20, 0)
        self.assertRaisesRegex(ValueError, h_err, Rectangle, 20, -20000000)

        x_err = "x must be >= 0"
        self.assertRaisesRegex(ValueError, x_err, Rectangle, 10, 10, -10)
        self.assertRaisesRegex(ValueError, x_err, Rectangle, 10, 10, -100000)

        y_err = "y must be >= 0"
        self.assertRaisesRegex(ValueError, y_err, Rectangle, 10, 10, 10, -10)
        self.assertRaisesRegex(ValueError, y_err, Rectangle, 1, 1, 1, -100000)

    def test_area(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10)
        self.assertEqual(x.area(), 100)
        x = Rectangle(1, 1234)
        self.assertEqual(x.area(), 1234)
        x = Rectangle(1345, 1)
        self.assertEqual(x.area(), 1345)

    def test_display(self):
        Base._Base__nb_objects = 0

        captured_print = io.StringIO()
        sys.stdout = captured_print

        x = Rectangle(2, 2, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  ##\n  ##\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        x = Rectangle(1, 1)
        x.display()
        self.assertEqual(captured_print.getvalue(), "#\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        x = Rectangle(1, 1)
        x.display()
        self.assertEqual(captured_print.getvalue(), "#\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        x = Rectangle(1, 1, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  #\n")
        captured_print.seek(0)
        captured_print.truncate(0)

        sys.stdout = sys.__stdout__

    def test_str(self):
        Base._Base__nb_objects = 0
        x = Rectangle(1, 1, 2, 2)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 2/2 - 1/1")

        x = Rectangle(1, 1)
        self.assertEqual(x.__str__(), "[Rectangle] (2) 0/0 - 1/1")

        x = Rectangle(10000, 10000)
        self.assertEqual(x.__str__(), "[Rectangle] (3) 0/0 - 10000/10000")

    def test_args_update(self):
        Base._Base__nb_objects = 0
        x = Rectangle(1, 1, 2, 2)

        x.update(1, 10, 10, 20, 20)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 20/20 - 10/10")

        x.update(1, 10, 10, 20, 20, 40, 50, 60)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 20/20 - 10/10")

        x.update(10)
        self.assertEqual(x.id, 10)

        x.update(13, 10, 10, 20, 20)
        self.assertEqual(x.__str__(), "[Rectangle] (13) 20/20 - 10/10")

    def test_kwargs_update(self):
        Base._Base__nb_objects = 0
        x = Rectangle(1, 1, 2, 2)

        x.update(id=1, width=10, height=10, x=20, y=20)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 20/20 - 10/10")

        x.update(id=1, width=10, height=10, x=20, y=20, chala=40)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 20/20 - 10/10")

        x.update(id=10)
        self.assertEqual(x.id, 10)

        x.update(width=13, id=15, x=10, y=20, height=20)
        self.assertEqual(x.id, 15)
        self.assertEqual(x.__str__(), "[Rectangle] (15) 10/20 - 13/20")

        temp = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        x.update(**temp)
        self.assertEqual(x.id, 1)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 1/9 - 10/2")

    def test_args_kwargs_update(self):
        Base._Base__nb_objects = 0
        x = Rectangle(1, 1, 2, 2)

        x.update(20, id=1)
        self.assertEqual(x.id, 20)

        x.update(1, 30, 40, width=10, height=10, x=20, y=20, chala=40)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 2/2 - 30/40")

        x.update(id=10)
        self.assertEqual(x.id, 10)

        x.update(width=13, id=15, x=10, y=20, height=20)
        self.assertEqual(x.id, 15)
        self.assertEqual(x.__str__(), "[Rectangle] (15) 10/20 - 13/20")

        x.update(13, 10, 10, 20, 20)
        self.assertEqual(x.id, 13)
        self.assertEqual(x.__str__(), "[Rectangle] (13) 20/20 - 10/10")

        temp = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        temp2 = [10, 20, 30, 40, 50]
        x.update(*temp2, **temp)
        self.assertEqual(x.id, 10)
        self.assertEqual(x.__str__(), "[Rectangle] (10) 40/50 - 20/30")

    def test_to_dict(self):
        Base._Base__nb_objects = 0
        x = Rectangle(1, 1, 2, 2)

        expected = {"id": 1, "width": 1, "height": 1, "x": 2, "y": 2}
        self.assertDictEqual(x.to_dictionary(), expected)

        x.update(10, 20, 40)
        expected = {"id": 10, "width": 20, "height": 40, "x": 2, "y": 2}
        self.assertDictEqual(x.to_dictionary(), expected)

        x.update(x=40, y=30)
        expected = {"id": 10, "width": 20, "height": 40, "x": 40, "y": 30}
        self.assertDictEqual(x.to_dictionary(), expected)

        y = Rectangle(1, 2)
        expected = {"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}
        self.assertDictEqual(y.to_dictionary(), expected)

if __name__ == "__main__":
    unittest.main()
