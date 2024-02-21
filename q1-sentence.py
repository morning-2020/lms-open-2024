def sentence(n, count):
    if n == 1 or n > 100:
        return count
    else:
        if n % 2 == 0:
            return sentence(n//2, count + 1)
        else:
            return sentence(3*n + 1, count + 1)

max_sentence = [0, 0]
years = 0
for i in range(1, 101):
    years = sentence(i, 0)
    if years > max_sentence[1]:
        max_sentence = [i, years]

print(max_sentence) #list of [starting_globe, sentence_length]
