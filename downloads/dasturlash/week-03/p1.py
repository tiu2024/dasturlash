def main():
    toliq_ism = input("F.I.O? ").title()

    print(f"Salom, {ism_ajratish(toliq_ism)}")

def ism_ajratish(ism):
    name1, name2 = ism.split()

    if name1.endswith("ov") or name1.endswith("ova"):
        return name2
    
    return name1

# def ism_ajratish(ism):
#     name1, name2 = ism.split()

#     if name1.endswith("ov") or name1.endswith("ova"):
#         ism = name2
#         familiya = name1
#     else:
#         ism = name1
#         familiya = name2
    
#     return ism

def familiya_ajratish(ism):
    name1, name2 = ism.split()

    if name1.endswith("ov") or name1.endswith("ova"):
        ism = name2
        familiya = name1
    else:
        ism = name1
        familiya = name2
    
    return familiya

main()