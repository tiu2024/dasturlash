o1 = input("1-o'yinchi: ")
o2 = input("2-o'yinchi: ")

if o1 == o2:
    print("Durang")
elif o1 == "tosh" and o2 == "qaychi":
    print("1-o'yinchi yutdi")
elif o1 == "qaychi" and o2 == "qog'oz":
    print("1-o'yinchi yutdi")
elif o1 == "qog'oz" and o2 == "tosh":
    print("1-o'yinchi yutdi")
else:
    print("2-o'yinchi yutdi")
