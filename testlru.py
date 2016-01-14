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

    def test_iterable(self):
        all_data = {(x, y) for x, y in self.test_cache}
        actual_data = {("1", "one"), ("2", "two"), ("3", "three")}
        self.assertEqual(all_data, actual_data)

    def test_contains(self):
        self.assertTrue("3" in self.test_cache)

    def test_not_contains(self):
        self.assertFalse("4" in self.test_cache)

    def test_len_n(self):
        self.assertEqual(len(self.test_cache), 3)

if __name__ == '__main__':
    unittest.main()
