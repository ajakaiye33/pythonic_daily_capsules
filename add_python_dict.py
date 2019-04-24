def add_python_to_dict(di):
    """
    Receives a dictionary  as input, adds a new key-value pair saying,
    'fav_language:python' to it, and returns it!
    """
    di["fav_langugae"] = "python"
    return di


print(add_python_to_dict({"fish": "turner", "career": "data analyst"}))
