d={}
print(d)
d["employee no"]='123'
print(d)
d["employee name"]="ragu"
print(d)
print(d["employee no"])
print(d.get("employee name"))
for key in d:
    print(key)
for value in d.values():
    print(value)
for key , value in d.items():
    print(key, value)
d.pop("employee no")
print(d)
d.popitem()
print(d)


