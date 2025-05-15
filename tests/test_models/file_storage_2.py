#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageAllMethod(unittest.TestCase):
    def setUp(self):
        """Create a new FileStorage instance and a BaseModel object."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def test_all_method(self):
        """Test that all() returns the correct dictionary with the object."""
        all_objs = self.storage.all()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], self.model)


if __name__ == "__main__":
    unittest.main()

