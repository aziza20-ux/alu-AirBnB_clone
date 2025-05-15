import unittest
import time
from models.base_model import BaseModel

class Created(unittest.TestCase):

    def test_created(self):
        d = BaseModel()

        time.sleep(0.01)

        c = BaseModel()

        self.assertNotEqual(d.created_at, c.created_at)
