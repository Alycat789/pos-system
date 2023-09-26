import json
import os

def read_json_file(filepath):
    with open(filepath) as f:
        return json.load(f)

def write_json_file(filepath, payload):
    with open(filepath, "w") as f:
        json.dump(payload, f, indent=4)

def main():
    root = os.path.dirname(__file__)
    filepath = os.path.join(root, "sample.json")

    thing_from_file = read_json_file(filepath)

    # thing_from_file["thing"] = "new and different data"

    # write_json_file(filepath, thing_from_file)

    my_things = read_json_file(filepath)
    my_things.append({"name": "Whozit", "price": 3.29})
    my_things.append({"name": "Dunno", "price": 19.25})

    write_json_file(filepath, my_things)

if __name__ == "__main__":
    main()
