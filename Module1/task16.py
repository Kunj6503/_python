set = {"peach","cherry","banana"}
print(set)

set.add("chiku")
print("updated set : ",set)

set.remove("chiku")
print("updated set : ",set)

for x in set:
    print(x)

set["cherry"]="cheeku"
print(set)