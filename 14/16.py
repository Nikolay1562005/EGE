for i in range(40, 0, -1):
    if bin(i)[2:][-4:] == '1011':
        print(i)
        break