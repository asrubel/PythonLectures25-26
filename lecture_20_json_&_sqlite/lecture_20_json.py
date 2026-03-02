import json

movies_dict = {
    "movies": [
        {
            "title": "Inception",
            "director": "Christopher Nolan",
            "year": 2010
        },
        {
            "title": "The Lord of the Rings: The Fellowship of the Ring",
            "director": "Peter Jackson",
            "year": 2001
        },
        {
            "title": "Parasite",
            "director": "Bong Joon Ho",
            "year": 2019
        }
    ]
}

with open('movies.json', 'w') as outfile:
    json.dump(movies_dict, outfile, indent=4)

json_str = json.dumps(movies_dict, indent=4)
print(json_str)

with open('movies.json', 'r') as infile:
    movies_dict = json.load(infile)
    print(movies_dict)

print(type(json.loads(json_str)))
