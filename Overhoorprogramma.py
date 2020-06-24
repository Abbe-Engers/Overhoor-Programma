import os
import random
import shutil

ProgrammaURL = "Uw programma URL hier!"

def menu_show():
    print("========================")
    print("| k: kies lijst        |")
    print("| s: show de woorden   |")
    print("| o: overhoor          |")
    print("| e: edit woorden      |")
    print("| d: delete lijsten    |")
    print("| m: maak lijst aan    |")
    print("========================")
    print(" ")

    return input(": ")

def update_txts():
    txts = os.listdir("./lijsten")
    return txts

def volgorde_lijst_function(one_lijst_, two_lijst_):
    one_lijst_naam = one_lijst_[0]
    two_lijst_naam = two_lijst_[0]
    print(" ")
    print("1: " + one_lijst_naam + ". 2: " + two_lijst_naam)
    print("Kies: 1-2 of 2-1")
    volgorde_lijst = input("Volgorde: ")
    leeg_scherm()
    return volgorde_lijst

def overhoor_lijst(volgorde_lijst_, one_lijst_, two_lijst_, goed_, fout_, overhoor_woord_, overhoor_lijst_lijst):
    volgorde_lijst = volgorde_lijst_
    overhoor_woord = overhoor_woord_
    overhoor_lijst_lijst = overhoor_lijst_lijst
    one_lijst = one_lijst_
    two_lijst = two_lijst_
    cijfer = 1
    keuze = ""
    goed = goed_
    fout = fout_
    if (volgorde_lijst == "2-1"):
        if (len(one_lijst) > 1):
            overhoor_key = random.randint(1, (len(one_lijst)-1))
            overhoor_woord = one_lijst[overhoor_key]
            zijn_antwoord = input(two_lijst[overhoor_key] + ": ")

            if (zijn_antwoord == overhoor_woord):
                overhoor_lijst_lijst.append(two_lijst[overhoor_key])
                one_lijst.remove(one_lijst[overhoor_key])
                two_lijst.remove(two_lijst[overhoor_key])
                leeg_scherm()
                goed += 1
                print(goed)
                overhoor_lijst(volgorde_lijst, one_lijst, two_lijst, goed, fout, overhoor_woord, overhoor_lijst_lijst)
                return

            else:
                leeg_scherm()
                print("Fout antwoord!")
                fout += 1
                print("\n" * 10)
                overhoor_lijst(volgorde_lijst, one_lijst, two_lijst, goed, fout, overhoor_woord, overhoor_lijst_lijst)

        else:
            if (goed == 0 or goed < 0):
                return
            cijfer = (((goed - fout) / goed) * 9) + 1
            if (cijfer < 1):
                cijfer = 1
            print("Gefeliciteerd!! je hebt een " + str(cijfer))
            print("\n" * 4)
            keuze = ""
            return

    if (volgorde_lijst == "1-2"):
        if (len(one_lijst) > 1):
            overhoor_key = random.randint(1, (len(one_lijst)-1))
            overhoor_woord = two_lijst[overhoor_key]
            zijn_antwoord = input(one_lijst[overhoor_key] + ": ")

            if (zijn_antwoord == overhoor_woord):
                woordje = one_lijst[overhoor_key]
                overhoor_lijst_lijst.append(woordje)
                one_lijst.remove(woordje)
                two_lijst.remove(two_lijst[overhoor_key])
                leeg_scherm()
                goed += 1
                overhoor_lijst(volgorde_lijst, one_lijst, two_lijst, goed, fout, overhoor_woord, overhoor_lijst_lijst)
                return


            else:
                leeg_scherm()
                print("Fout antwoord!")
                fout += 1
                print("\n" * 10)
                overhoor_lijst(volgorde_lijst, one_lijst, two_lijst, goed, fout, overhoor_woord, overhoor_lijst_lijst)

        else:
            if (goed == 0 or goed < 0):
                return
            cijfer = (((goed - fout) / goed) * 9) + 1
            if (cijfer < 1):
                cijfer = 1;
            print("Gefeliciteerd!! je hebt een " + str(cijfer))
            print("\n" * 4)
            keuze = ""
            return


def maak_lijst():
    aanmaak_naam = input("Naam van de lijst: ")
    open("./lijsten/" + aanmaak_naam + ".txt", "w+")
    leeg_scherm()
    print(aanmaak_naam + ".txt aangemaakt.")
    print("\n" * 9)

def show_lijsten():
    for i in update_txts():
        i = i[:-4]
        print(i)

def kies_lijst(lijst_naam):
    lijst_path = ""
    lijst_naam = lijst_naam + ".txt"
    if (lijst_naam in update_txts()):
        lijst_path = "/lijsten/" + lijst_naam
        with open("." + lijst_path) as f:
            lijst = f.read().split()
            return lijst, lijst_path
    else:
        print("Kan de opgevraagde lijst helaas niet vinden, probeer opnieuw.")
        lijst_path = ""
        return
    return

def split_words(lijst_):
    one_lijst = []
    two_lijst = []
    splitter = 1
    for word in lijst_:
        if (splitter >= 2):
            two_lijst.append(word)
            splitter = 1
        else:
            one_lijst.append(word)
            splitter = 2
    return one_lijst, two_lijst

def del_words():
    if (os.path.isdir(ProgrammaURL + "/lijsten/Prullenbak")):
        os.rmdir(ProgrammaURL + "/lijsten/Prullenbak")

    os.mkdir(ProgrammaURL + "/lijsten/Prullenbak")
    os.startfile(ProgrammaURL + "/lijsten")
    leeg_scherm()
    input("druk enter: ")
    del_prullenbak()


def del_prullenbak():
    if (os.path.isdir(ProgrammaURL + "/lijsten/Prullenbak")):
        shutil.rmtree(ProgrammaURL + "/lijsten/Prullenbak")

def add_words(lijst_naam):
    os.startfile(ProgrammaURL + kies_lijst(lijst_naam)[1])
    leeg_scherm()
    input("druk enter: ")
    return

def leeg_scherm():
    print("\n" * 100)

def lees_woordenlijst(BESTANDSNAAM):
    return

def main(i_):
    i = i_
    keuze = menu_show()

    if (keuze == "s"):
        leeg_scherm()
        for k in range(len(split_words(kies_lijst(i)[0])[0])):
            print(split_words(kies_lijst(i)[0])[0][k] + (" "*(20-len(split_words(kies_lijst(i)[0])[0][k]))) + "   :   " + split_words(kies_lijst(i)[0])[1][k])
        print("\n")
        main(i)

    if (keuze == "k"):
        leeg_scherm()
        show_lijsten()
        print("\n" * 2)
        i = input("keuze: ")
        split_words(kies_lijst(i)[0])
        print("\n" * 8)
        main(i)

    if (keuze == "e"):
        add_words(i)
        leeg_scherm()
        main(i)

    if (keuze == "d"):
        del_words()
        leeg_scherm()
        main(i)

    if (keuze == "m"):
        leeg_scherm()
        maak_lijst()
        main(i)

    if (keuze == "o"):
        leeg_scherm()
        overhoor_lijst(volgorde_lijst_function(split_words(kies_lijst(i)[0])[0], split_words(kies_lijst(i)[0])[1]), split_words(kies_lijst(i)[0])[0], split_words(kies_lijst(i)[0])[1], 0, 0, 1, [])
        main(i)

    del_prullenbak()

del_prullenbak()
leeg_scherm()
main("")
