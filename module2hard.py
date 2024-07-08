def find_password(n):
    result = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result.append(str(i))
                result.append(str(j))
    return ''.join(result)


for n in range(3, 21):
    password = find_password(n)
    print(f"{n} - {password}")