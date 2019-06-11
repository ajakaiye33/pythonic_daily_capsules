import operator
people = [{"first": "Reuven", "last": "Lerner", "email": "reuven@Lerner.co.il"},
          {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
          {"first": "Vladimir", "last": "Putin", "email": "president@kremavax.ru"}]

for person in sorted(people, key=operator.itemgetter('last', 'first')):
    print(f"{person['last']},{person['first']}:{person['email']}")
    # for k, v in sorted(i.items()):
    # print(f"{k}:{v}")
