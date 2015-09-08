def checkio(number):
    count = 0
    for i in list(bin(number)):
        if i == '1': count += 1
    return count
    
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
