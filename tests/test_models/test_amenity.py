#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_doc(self):
        """
        Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(console.__doc__)

        #  Class check
        self.assertIsNotNone(HBNBCommand.__doc__)

        # Methods check
        for method in dir(HBNBCommand):
            self.assertIsNotNone(method.__doc__)

    def test_pep8(self):
        """ Style pep8 """
        style = pep8.StyleGuide(quiet=True)
        f1 = 'amenity.py'
        # f2 = 'tests/test_console.py'
        # result = style.check_files([f1, f2])
        result = style.check_files([f1])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        # self.assertEqual(True,True)

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
