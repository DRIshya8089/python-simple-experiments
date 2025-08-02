def decrypt():
    input = 'a2b2c5'
    n = 3
    word = ''
    i = 0
    num = ''
    if input[::].isalpha() :
      return '-1'
    while i < len(input):
        if input[i].isalpha():
            chara = input[i]
            i += 1
            
        elif input[i].isdigit():
            num += input[i]
            i += 1
            word += chara * int(num)
        else:
            i += 1

    if n <= len(word):
        return word[n - 1]
    else:
        return '-1'
    print(word)

print(decrypt()) 