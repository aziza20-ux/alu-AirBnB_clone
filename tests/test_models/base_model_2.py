import unittest
import time
from models.base_model import BaseModel


class TestId(unittest.TestCase):

    def test_id(self):

        d = BaseModel()

        b = BaseModel()

        self.assertNotEqual(d, b)
