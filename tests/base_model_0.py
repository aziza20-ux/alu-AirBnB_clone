import unittest
import time
from models.base_model import BaseModel

class TestingBaseModel(unittest.TestCase):

    def test_save(self):
        b = BaseModel()

        original_time = b.updated_at

        time.sleep(0.01)

        b.save()

        self.assertGreater(b.updated_at, original_time)
if __name__ == '__main__':
        unittest.main()
