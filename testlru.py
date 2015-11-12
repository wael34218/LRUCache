import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.test_cache = LRUCache(3)
        self.test_cache.put("1", "one")
        self.test_cache.put("2", "two")
        self.test_cache.put("3", "three")

    def test_cache_capacity_1(self):
        self.test_cache.put("4", "four")
        self.test_cache.put("5", "five")
        self.test_cache.put("6", "six")
        val = self.test_cache.get("4")
        self.assertEqual(val, 'four')

    def test_cache_capacity_2(self):
        self.test_cache.put("4", "four")
        self.test_cache.put("5", "five")
        self.test_cache.put("6", "six")
        val = self.test_cache.get("3")
        self.assertEqual(val, None)

    def test_cache_touch(self):
        val = self.test_cache.get("1")
        self.test_cache.put("4", "four")
        self.test_cache.put("5", "five")
        val = self.test_cache.get("1")
        self.assertEqual(val, "one")

    def test_cache_purge(self):
        self.test_cache.purge("1")
        val = self.test_cache.get("1")
        self.assertEqual(val, None)

    def test_cache_clear(self):
        self.test_cache.clear()
        val = self.test_cache.get("1")
        self.assertEqual(val, None)

    def test_cache_statistics(self):
        self.test_cache.get("1")
        self.test_cache.get("2")
        self.test_cache.get("3")
        self.test_cache.get("4")
        self.test_cache.get("5")
        self.test_cache.get("6")
        res = {"hit": 3, "miss": 3, "percentage": 0.5}
        self.assertEqual(self.test_cache.stats(), res)


if __name__ == '__main__':
    unittest.main()