import json

info_about_me = {
    "name": "Michele",
    "has_a_dog": False
}

with open("info.json", "w") as f:
    json.dump(info_about_me, f)



with open("info.json", "r") as f:
    info = json.load(f)

if info["has_a_dog"]:
    print("{} has a dog".format(info["name"]))
else:
    print("{} does not have a dog".format(info["name"]))