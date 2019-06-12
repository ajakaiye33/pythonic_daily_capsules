# import operator
# people = [{"first": "Reuven", "last": "Lerner", "email": "reuven@Lerner.co.il"},
#           {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
#           {"first": "Vladimir", "last": "Putin", "email": "president@kremavax.ru"}]
#
# for person in sorted(people, key=operator.itemgetter('last', 'first')):
#     print(f"{person['last']},{person['first']}:{person['email']}")
#     # for k, v in sorted(i.items()):
#     # print(f"{k}:{v}")


hy = [-2, 3, -4, -5, - 8, 8, 9, 3, 2, 4]
jey = []
for i in hy:
    jey.append(abs(i))
print(sorted(jey))
stringy = []
vow = "aeiou"
stauy = ["john", "gana", "hanna", "janna"]
for i in stauy:
    if i in vow:
        print(i)
