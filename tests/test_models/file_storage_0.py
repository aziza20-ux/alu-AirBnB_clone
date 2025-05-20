import unittest
import os
from datetime import datetime
import time

from models import storage

from models.base_model import BaseModel


class testpath(unittest.TestCase):
    def setUp(self):
        s = BaseModel()

    def test_path(self):
        s = BaseModel()
        s.save()

        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_object(self):
        s = BaseModel()
        s.save()

        key = f"BaseModel.{s.id}"
        objects = storage.all()
        self.assertIn(key, objects)

    def test_all_empty(self):

        result = storage.all()
        self.assertNotEqual(len(result), 0)

    def test_all(self):
        obj = BaseModel()

        storage.new(obj)

        objects = storage.all()

        self.assertIn(obj, objects.values())

    def tearDown(self):
        storage._FileStorage__objects.clear()
        storage.save()


if __name__ == '__main__':

    unittest.main()
