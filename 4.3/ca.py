def reverse(text):
    list = []
    x = len(text) - 1
    while x >= 0:
        list.append(text[x])
        x -= 1
    text_joined = "".join(list)
    print(text_joined)
    return text_joined

reverse("abc")