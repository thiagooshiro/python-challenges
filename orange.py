def uniformChecking(oranges: list, blacks: list):
    oranges.sort()
    blacks.sort()
    index = 0
    for student in blacks:
        print('black:', student)
        print(oranges[index])
        if student > oranges[index]:
            return False
        else:
            index += 1
    return True

blackUniform = [150, 179, 149, 152, 154]
orangeUniform = [162, 181, 151, 160, 150]

print(uniformChecking(orangeUniform, blackUniform))