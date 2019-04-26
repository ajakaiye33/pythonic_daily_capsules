def longest_key(di):
    """
    Receives a dictionary with only string keys and returns the longest keys in the dictionary
    """
    for k in di.keys():
        fi = []
        fi.append(k)
        return max(fi)


print(longest_key({"hello": "world", "abc": 123, }))
print(longest_key({}))
print(longest_key({"rmotr": "intro to python"}))
