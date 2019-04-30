import unittest
from testing_unittests import eat, nap

class TestingTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I am eating broccoli, coz my body needs healthy foods"
        )

    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I am eating pizza, coz YOLO!"
        )
    
    def test_nap_short(self):
        self.assertEqual(
            nap(1),
            "Power nap is great"
        )

    def test_nap_long(self):
        self.assertEqual(
            nap(3),
            "Damnit I overslept"
        )

if __name__ == "__main__":
    unittest.main()