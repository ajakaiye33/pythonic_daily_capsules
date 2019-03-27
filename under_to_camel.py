def under_to_camel(var):
    """
    Write a function to convert a variable
    name from under_score format to camelCase.
    """
    assem_str = ''
    # split the string by the underscore
    splited_str = var.split('_')

    # loop through the list and
    # apply title() to string
    for i in splited_str:
        assem_str += i.title()

    return assem_str[0].lower() + assem_str[1:]


print(under_to_camel('my_income_tax_from_2015'))
