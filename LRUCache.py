class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self._data = {}

        self.first = self.last = None
        self.hit = self.miss = 0

    def put(self, key, value):
        if key in self._data:
            self._touch(key)
            self._data[key]["value"] = value
            return self._data[key]

        if self.size == self.capacity:
            self.purge(self.last)

        if self.first is not None:
            self._update(self.first, "newer", key)

        self.size += 1
        self._data[key] = {"value": value, "newer": None, "older": self.first}

        self.first = key
        if self.last is None:
            self.last = key

        return self._data[key]

    def get(self, key):
        if key in self._data:
            self.hit += 1
            self._touch(key)
            return self._data[key]["value"]
        else:
            self.miss += 1
            return None

    def purge(self, key):
        if key not in self._data:
            return False

        deleted = self._data[key]

        if self.size == 1:
            self.clear()
            return True

        if self.last == key:
            self._update(deleted["newer"], "older", None)
            self.last = deleted["newer"]
        elif self.first == key:
            self._update(deleted["older"], "newer", None)
            self.first = deleted["older"]
        else:
            self._update(deleted["newer"], "older", deleted["older"])
            self._update(deleted["older"], "older", deleted["newer"])

        self.size -= 1
        del self._data[key]
        return True

    def stats(self):
        percentage = self.hit * 1.0 / (self.hit + self.miss)
        return {"hit": self.hit, "miss": self.miss, "percentage": percentage}

    def clear(self):
        self.size = 0
        self._data = {}
        self.first = self.last = None

    def _update(self, key, label, value):
        if key in self._data:
            temp = self._data[key]
            temp[label] = value
            self._data[key] = temp

    def _touch(self, key):
        if key not in self._data:
            return False

        if self.first == key:
            return True

        item = self._data[key]
        self._update(self.first, "newer", key)

        if self.last == key:
            self._update(item["newer"], "older", None)
            self.last = item["newer"]
        else:
            self._update(item["newer"], "older", item["older"])
            self._update(item["older"], "newer", item["newer"])

        self._data[key] = {"value": self._data[key]["value"], "newer": None, "older": self.first}
        self.first = key
        return True

    def __iter__(self):
        for key, value in self._data.items():
            yield (key, value["value"])
        return

    def __contains__(self, item):
        return item in self._data

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return "LRUCache{}".format(str(list(self.__iter__())))

    def __eq__(self, rhs):
        if not isinstance(rhs, LRUCache):
            return NotImplemented
        return self._data == rhs._data
