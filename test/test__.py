def f(string):
    print(string)
    if string<0 | string >= 100000000:
        return False

    numbers = ['零','一','二','三','四','五','六','七','八','九']
    small_part = ['十','百','千']
    big_part = ['万']
    string = str(string)
    string = list(string)
    last_str = list('')

    while (string[-1] != None):
        last_str.append(numbers[int(string[-1])])

    last_str[:] = last_str[::-1]

    for i in range(len(string)):
        count = 0

        if count ==4:
            last_str[-4]
    return last_str

if __name__ == '__main__':
    string = int(input())
    last_str = f(str)
    print(last_str)