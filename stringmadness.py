def stringMadness(tgtstring):
    workingString = tgtstring.upper()
    answer = ''
    counter = 0
    letter = workingString[0]
    for element in workingString:

       if letter == element and counter < 9:
           counter += 1
       else:
            answer += str(counter) + letter
            letter = element
            counter = 1   
    return answer + str(counter) + letter
           



example = 'aAABBCCDDSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEE'

print (stringMadness(example))