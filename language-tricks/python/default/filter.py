# Just like JS filter
names = ["anthony", "penny", "angel", "billy"]

# filters out names that start with 'a'
a_names = list(filter(lambda name: name[0] == "a", names))


people = [
    {"name": "james", "age": 50},
    {"name": "bob", "age": 2},
    {"name": "jason", "age": 10},
    {"name": "cat", "age": 6},
    {"name": "dog", "age": 99},
]

## extracting name with list comprehension
old = [name["name"] for name in filter(lambda person: person["age"] > 10, people)]

## extract combining filter and map
old_name = list(
    map(
        lambda x: f"{x['name']} is old",
        filter(lambda person: person["age"] > 10, people),
    )
)

## WAY better way of doing the same thing
best_name = [f"{person['name']} is old" for person in people if person["age"] > 10]
