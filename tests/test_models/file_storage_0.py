import unittest
import os
from datetime import datetime
import time

from models.engine.file_storage import FileStorage

from models.base_model import BaseModel



class testpath(unittest.TestCase):
    def test_path(self):
        d = FileStorage()

        self.assertFalse(os.path.exists(FileStorage._FileStorage__file_path))
if __name__ == '__main__':
    unittest.main()

