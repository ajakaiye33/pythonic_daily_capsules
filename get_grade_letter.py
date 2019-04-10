
def get_grade_letter(score):
    """
    Receives a score and you should return:
    "A" if the score is 90 or above
    "B" if the score is 80 to 89
    "C" if the score is 70 to 79
    "D" if the score is 60 to 69
    "F" if the score is less than 60
    """
    if score >= 90:
        grade = "A"
    elif score >= 80 <= 89:
        grade = "B"
    elif score >= 70 <= 79:
        grade = "C"
    elif score >= 60 <= 69:
        grade = "D"
    elif score < 60:
        grade = "F"

    return grade


print(get_grade_letter(90))
print(get_grade_letter(80))
print(get_grade_letter(75))
print(get_grade_letter(67))
print(get_grade_letter(42))
