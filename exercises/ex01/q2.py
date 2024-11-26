def price(drinks):
    prices = [("kaffe", 30), ("öl", 50), ("kola", 25)]
    [n, name] = drinks.split()
    for (s, price) in prices:
        if s == name:
            return price * int(n)
    return 0

def get_order():
    drink = input("Vad vill ni dricka?")
    total = 0
    while drink != "Det är bra så":
        p = price(drink)
        if p == 0:
            print("Finns tyvärr inte")
        total += p
        drink = input("Något mer?")
    print("Det blir", total, "kronor")
