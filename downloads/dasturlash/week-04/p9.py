camel = input("camelCase nomi: ")

snake = ""
for h in camel:
    if h.isupper():
        snake += "_" + h.lower()
    else:
        snake += h

print(f"snake_case nomi: {snake}")
