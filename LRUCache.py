class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = {}

        self.first = self.last = None
        self.hit = self.miss = 0

    def put(self, key, value):
        if key in self.data:
            self.__touch(key)
            self.data[key]["value"] = value
            return self.data[key]

        if self.size == self.capacity:
            self.purge(self.last)

        if self.first is not None:
            self.__update(self.first, "newer", key)

        self.size += 1
        self.data[key] = {"value": value, "newer": None, "older": self.first}

        self.first = key
        if self.last is None:
            self.last = key

        return self.data[key]

    def get(self, key):
        if key in self.data:
            self.hit += 1
            self.__touch(key)
            return self.data[key]["value"]
        else:
            self.miss += 1
            return False

    def purge(self, key):
        if key not in self.data:
            return False

        deleted = self.data[key]

        if self.size == 1:
            self.clear()
            return True

        if self.last == key:
            self.__update(deleted["newer"], "older", None)
            self.last = deleted["newer"]
        elif self.first == key:
            self.__update(deleted["older"], "newer", None)
            self.first = deleted["older"]
        else:
            self.__update(deleted["newer"], "older", deleted["older"])
            self.__update(deleted["older"], "older", deleted["newer"])

        self.size -= 1
        del self.data[key]
        return True

    def stats(self):
        percentage = self.hit / (self.hit + self.miss)
        return {"hit": self.hit, "miss": self.miss, "percentage": percentage}

    def clear(self):
        self.size = 0
        self.data = {}
        self.first = self.last = None

    def __update(self, key, label, value):
        if key in self.data:
            temp = self.data[key]
            temp[label] = value
            self.data[key] = temp

    def __touch(self, key):
        if key not in self.data:
            return False

        if self.first == key:
            return True

        item = self.data[key]
        self.__update(self.first, "newer", key)

        if self.last == key:
            self.__update(item["newer"], "older", None)
            self.last = item["newer"]
        else:
            self.__update(item["newer"], "older", item["older"])
            self.__update(item["older"], "newer", item["newer"])

        self.data[key] = {"value": self.data[key]["value"], "newer": None, "older": self.first}
        self.first = key
        return True
