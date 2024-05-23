dict =[ {
"brand": "Ford",
"model": "mustang",
"year": 2000,
"price": 1000
},{
"brand": "Maruti",
"model": "alto",
"year": 2005,
"price": 2000
},{
"brand": "volkswagen",
"model": "polo",
"year": 2010,
"price": 3000
},{
"brand": "hyundai",
"model": "verna",
"year": 2015,
"price": 4000
},{
"brand": "honda",
"model": "city",
"year": 2020,
"price": 5000
} ]

user = input("enter the name of the car : ").strip().lower()

for dict in dict:
    if dict["model"]==user:
        print("Brand : ",dict["brand"],
              "\nModel : ",dict["model"],
              "\nYear : ",str(dict["year"]))
        break
else:
    print("car not found in the database")


budget = int(input("Enter you budget = "))

for dict in dict:
    if dict["price"]<=budget:
        print("Brand : ",dict["brand"],
              "\nModel : ",dict["model"],
              "\nYear : ",str(dict["year"]),
              "\nPrice : ",dict["price"])
        break
else:
    print("Gareeb ho aap")