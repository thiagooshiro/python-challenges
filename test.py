

def arraySum(target, array):
    answer = []
    index = 0
    for num in array:
        for element in array:
            if element != array[index] and element != num:
                if num + element == 10:
                    if num not in answer and element not in answer:
                        answer.append(num)
                        answer.append(element)


    return answer


array = [6, 5, 4, -5, 8, 15, 1, 9, 2]

resp = arraySum(10, array)
print(resp)