def double3(word):
    index = 0
    count = 0
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            count = count + 1
            if count == 3:
                return True
            index = index + 2
        else:
            count = 0
            index = index + 1
    return False

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if double3(word):
        print word
