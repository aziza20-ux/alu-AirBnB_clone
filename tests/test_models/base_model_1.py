import unittest
import time
from models.base_model import BaseModel

class TestTodict(unittest.TestCase):

    def test_todict(self):
        d = BaseModel()

        dic = d.to_dict()

        self.assertIn('__class__', dic)
        self.assertEqual(dic['__class__'], 'BaseModel')

        self.assertIsInstance(dic, dict)
