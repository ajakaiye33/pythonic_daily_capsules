
a = 10
b = 3
c = 7


def test_score(b):
    a = 11
    return a + b + c


c = + c + test_score(5)
print(c)

customer = {
    "UT": [{
        "name": "Mary",
        "age": 28
    }, {
        "name": "John",
        "age": 31
    }],
    "NY": [{
        "name": "Linda",
        "age": 71
    }]
}


def num_of_cust_per_state(dic):
    """
    Receives a dictionary containing states(keys) and customers for those states:
    (list of dictionaries)
    return a final dictionary containing the count of customers per states
    """
    empty = {}
    for state, cust in dic.items():
        empty[state] = len(cust)
    return empty


print(num_of_cust_per_state(customer))
