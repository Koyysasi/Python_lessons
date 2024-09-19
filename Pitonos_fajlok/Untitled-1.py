def main():
    parametermMentesFuggveny()
    parameteresFuggveny(6)
    parameteresEljaras(2, 2)
    parameterMentesEljaras()

def parametermMentesFuggveny():
    return("meghivtad a fuggvenyt, de nem adtal neki parametert\nmire szamitottal?")

def parameteresFuggveny(a):
    return(a + 2)

def parameterMentesEljaras():
    if 1 == 1:
        print("igen, 1 egyenlo 1-el")
    else:
        print("Wat")

def parameteresEljaras(a, b):
    print(a*b)


if(__name__ == '__main__'):
    main()