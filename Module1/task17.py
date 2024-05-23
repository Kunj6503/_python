dict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(dict)

x = dict.keys()
y = dict.values()
print(x,"\n",y)

dict["type"] = "sedan"
print(dict)

dict["year"] = "2024"
print(dict)

dict.update({"year":2050})
print(dict)

del dict ["brand"]
print(dict)

for x in dict:
    print(dict)
for y in dict.keys():
    print(y)

print(dict.get("model"))

for x in dict.values():
    print(x)

if x == "Mustang":
    print(dict["Mustang"])