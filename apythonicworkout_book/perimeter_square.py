
def perimeter(n):
    # your code
    se = 0
    for i in range(n+1):
        se += i
    return se * 4


print(perimeter(5))
