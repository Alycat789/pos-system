import json

all_the_stuff = []
big_thing = {}

big_thing["name"] = "The name value"
big_thing["number"] = 3.14159

big_thing["little_things"] = []

little_thing = {"title": "one", "value": 1}
big_thing["little_things"].append(little_thing)

little_thing = {"title": "two", "value": 2}
big_thing["little_things"].append(little_thing)

all_the_stuff.append(big_thing)
all_the_stuff.append(big_thing)

print(json.dumps(all_the_stuff, indent=4))

thing = all_the_stuff[1]
print(thing["name"])
print(thing["number"])
print(thing["little_things"][0])