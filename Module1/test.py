car_list = [
    {"brand": "Ford", "model": "mustang", "year": 2000, "price": 1000},
    {"brand": "Maruti", "model": "alto", "year": 2005, "price": 2000},
    {"brand": "volkswagen", "model": "polo", "year": 2010, "price": 3000},
    {"brand": "hyundai", "model": "verna", "year": 2015, "price": 4000},
    {"brand": "honda", "model": "city", "year": 2020, "price": 5000}
]

budget = int(input("Enter your budget: "))
found = False
i = 0
options = []
for car in car_list:
    i += 1
    if car["price"] <= budget:
        options.append(car)
        print(f"Option {i} for your budget:\n"
              f"Brand: {car['brand']}\n"
              f"Model: {car['model']}\n"
              f"Year: {car['year']}\n"
              f"Price: {car['price']}\n")
        found = True
if not found:
    print("No relevant cars found.")

select = int(input("Please select an option to buy: "))
selected_car = options[select - 1] if 0 < select <= len(options) else None

if selected_car:
    print(f"Selected Car:\n"
          f"Brand: {selected_car['brand']}\n"
          f"Model: {selected_car['model']}\n"
          f"Year: {selected_car['year']}\n"
          f"Price: {selected_car['price']}\n")
else:
    print("Invalid option selected.")
