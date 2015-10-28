from LRUCache import LRUCache

test = LRUCache(3)
test.put("1", "one")
test.put("2", "two")
test.put("3", "three")
test.put("4", "four")
test.put("5", "five")
test.put("6", "six")
test.delete("6")
test.delete("4")
test.put("1", "one")
test.put("2", "two")
print(test.get("5"))
for k in test.data.keys():
    print(k, '-->', test.data[k])
