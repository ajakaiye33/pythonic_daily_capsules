from statistics import mean


def analyze_age_dict(lst):
    """
    Receives a list of dictionaries, pulls the value associated with key  "age"
    from each dictioanry, and return a new dictionary with two keys:
    *"average": The average age of the inpu dict
    *"dictionary_count": The number of lelement processed
    """
    counter = 0
    divi = []
    say = {}
    for di in lst:
        for v in di.values():
            if di["age"] == v:
                counter += 1
                divi.append(v)
                say["ave_age"] = mean(divi)
                say["dict_counter"] = counter
    return say


print(analyze_age_dict([{"names": "Bob", "age": 22}, {"name": "Jane", "age": 26}]))
print(analyze_age_dict([{"names": "Hermione", "age": 22}]))
print(analyze_age_dict([{"names": "Bob", "age": 22}, {
      "name": "Jane", "age": 26, "name": "Alice", "last_name": "Jones"}]))
