def norway_pandemic():
    velkommen = False
    while velkommen == False:
        region = input("Hvor er du bosatt? ")
        print(region[0])
        if region[0] == "v":
            break
        fullvaksinert = input("Er du fullvaksinert? ")
        if fullvaksinert == "ja":
            break
        nyligen_sjuk = input("Har du gjennomgått koronasykdom de siste seks månedene? ")
        if nyligen_sjuk == "ja":
            break
        print("Velkommen til Norge, men du må teste deg och sitte i karentene.")
        exit()
    print("Velkommen til Norge!")
    exit()

norway_pandemic()
