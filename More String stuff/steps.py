def steps(num):
    output = ''
    count = 0
    for i in range(1, num + 1):
        count += 1
        output += str(i) * 3 + '\n' + '\t' * count

    return output


print(steps(3))
print(steps(6))
