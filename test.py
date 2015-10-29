from LRUCache import LRUCache

test = LRUCache(3)
test.put("1", "one")
test.put("2", "two")
test.put("3", "three")
test.put("4", "four")
test.put("5", "five")
test.put("6", "six")
test.purge("6")
test.purge("4")
test.put("1", "one")
test.put("2", "two")
print(test.purge("1"))
print(test.get("5"))
print(test.get("2"))
print(test.get("1"))
print(test.get("6"))
print(test.get("3"))
print(test.get("2"))
print(test.get("4"))
for k in test.data.keys():
    print(k, '-->', test.data[k])

print(test.stats())
