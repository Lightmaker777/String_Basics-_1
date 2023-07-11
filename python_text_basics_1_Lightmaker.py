# Task 1

city = "\nLondon\n"

print(city)

# Task 2

city = "berlin"
population = "3645000\n"

print(city.capitalize() + " : " + population)

# Task 3

city = "London"
population = "9000000\n"

print("City: " + city, "(" + str(isinstance(city,str)) + ")")
print("Population: " + population)

# Task 4

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
if "capital" in text:
    index = text.index("capital")
    print("capital:", index)

# Task 5

text = """Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."""
print(text.split())

#Task 6

text = """\nBerlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."""
new_text = text.replace("capital", "capital of Germany")
    
print(new_text)
























