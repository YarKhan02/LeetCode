def reverse(s):
    return " ".join(word[::-1] for word in s.split(" "))

print(reverse('hello yar'))