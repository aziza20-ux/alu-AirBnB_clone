import unittest
import time
from models.base_model import BaseModel

class Str(unittest.TestCase):
    def test_str(self):
        s = BaseModel()

        st = str(s)

        self.assertIn("[BaseModel]", st)

        self.assertIn(s.id, st)


