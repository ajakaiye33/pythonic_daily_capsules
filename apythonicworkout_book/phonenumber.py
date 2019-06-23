#
# def create_phone_number(n):
#     """
#     trandsfor to phone number format
#     """
#     nf = ''
#     for i in n:
#         nf += str(i)
#     return f"({nf[0:3]}) {nf[3:6]}-{nf[6:]}"
#
#
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#


####

# def scramble(s1, s2):
#
#
# # scramble('rkqodlw', 'world') ==> True
# # scramble('cedewaraaossoqqyt', 'codewars') ==> True
# # scramble('katas', 'steak') ==> False
#
# print(scramble('rkqodlw', 'world'))
# print(scramble('cedewaraaossoqqyt', 'codewars'))
# print(scramble('katas', 'steak'))

def pig_it(stringy):
    """Move the first letter of each word to the end of it, then add "ay" to the end
    of the word. Leave punctuation marks untouched.Examples
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !"""
    dey = []
    ass = stringy.split()
    for j in ass:
        if len(j) > 1:
            dey.append(j[1:] + j[0] + "ay")
    return " ".join(dey)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
