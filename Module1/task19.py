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

budget = int(input("Enter you budget = "))
found=False
i=0
options = []
for dict in dict:
    i+=1
    if dict["price"]<=budget:
        options.append(dict)
        print(f"Option {i} for your poor budget : \n""Brand : ",dict["brand"],
              "\nModel : ",dict["model"],
              "\nYear : ",str(dict["year"]),
              "\nPrice : ",dict["price"])
        
        found=True      
if not found:
    print("no relevant cars found")

    
select = int(input("please select any one option to buy : "))
try:
    if select<=i:
        car = options[select-1]
        print("Congratulations, you have selected ", car["model"])
    
except:
    print("enter a valid choice")