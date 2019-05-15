
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

    }, {
        "name": "Lisa",
        "age": 25
    }]
}


def eldes_customer(dic):
    midway = {}
    inner_chamber = {}
    for i, j in customer.items():
        for u in j:
            midway[i] = u
    return midway


print(eldes_customer(customer))
