class Avto():
    def __init__(self, model, znamka):
        self.model = model
        self.znamka = znamka

    def povejZnamko(self):
        return self.znamka

    def povejModel(self):
        return self.model

def ustvariAvtomobil():
    avto1 = Avto("UNO", "fiat")
    avto2 = Avto("GOLF","vw")
    avto3 = Avto ("FELICIA", "skoda")
    avto4 = Avto ("PUNTO", "fiat")
    seznamAvtomobilov = [avto1, avto2, avto3, avto4]
    return seznamAvtomobilov


def main():
    seznam = ustvariAvtomobil()
    print("UGANI ZNAMKO AVTOMOBILA")
    tocke = 0
    for avto in seznam:
        print "Katere avtomobilske znamke je ta model: " + avto.povejModel()
        vnos = raw_input("Vnesi znamko: ")
        if vnos.lower() == avto.povejZnamko():
            print "Bravo"
            tocke += 1
            print "Trenutno stevilo tock: " + str(tocke)
        else:
            print "Vec srece prihodnjic"
            print "Stevilo dosezenih tock: " + str(tocke)
            break


if __name__ == '__main__':
    main()