# Write your solution here
def fractionate(amount: int):
    from fractions import Fraction
    fractions = []
    for i in range(amount):
        fractions.append(Fraction(1,amount))
    return fractions

