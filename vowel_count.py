
def vowel_count(phrasy):
    """
    vowelCount(str) that takes a str 
    parameter and returns
    the number of vowels
    the string contains
    """
    counter = 0
    vowel = "aeiou"
    for i in vowel:
        for s in phrasy.lower():
            if i == s:
                counter += 1
    return counter


print(vowel_count("Eat egg an day"))
