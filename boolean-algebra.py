OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == 'conjunction':
        if x==1 and y==1: return 1
        else: return 0
    elif operation == 'disjunction':
        if x==0 and y==0: return 0
        else: return 1
    elif operation == 'implication':
        if x==1: return y
        else: return 1
    elif operation == 'exclusive':
        return (x+y)%2
    else:
        if x==y: return 1
        else: return 0
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
