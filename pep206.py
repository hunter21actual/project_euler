for i in range(101010101, 138902663, 2):
    s = str(i**2)
    if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9':
        print(i)
        break
