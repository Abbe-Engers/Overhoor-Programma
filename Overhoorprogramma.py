import os
import random
import shutil

ProgrammaURL = "C:/Users/aenge/OneDrive/Bureaublad/python/Overhoor Programma"
goed = 0
fout = 0
cijfer = 1
keuze = ""
overhoor_woord = 1
lijst_path = ""
splitter = 1
lijst = []
overhoor_lijst_lijst = []
one_lijst = []
two_lijst = []
one_lijst_naam = ""
two_lijst_naam = ""
volgorde_lijst = ""
txts = ""

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
    global keuze
    keuze = input(": ")

def update_txts():
    txts = os.listdir("./lijsten")
    return txts

def volgorde_lijst_function():
    one_lijst_naam = one_lijst[0]
    two_lijst_naam = two_lijst[0]
    print(" ")
    print("1: " + one_lijst_naam + ". 2: " + two_lijst_naam)
    print("bijv: 1-2 of 2-1")
    global volgorde_lijst
    volgorde_lijst = input("Volgorde: ")
    return volgorde_lijst

def overhoor_lijst():
    global cijfer
    global keuze
    global goed
    global fout
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
                overhoor_lijst()
                return

            else:
                leeg_scherm()
                print("Fout antwoord!")
                fout += 1
                print("\n" * 10)
                overhoor_lijst()

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
                overhoor_lijst()
                return


            else:
                leeg_scherm()
                print("Fout antwoord!")
                fout += 1
                print("\n" * 10)
                overhoor_lijst()

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
    update_txts()
    lijst_naam = lijst_naam + ".txt"
    if (lijst_naam in update_txts()):
        print(" ")
        print("lijst gevonden: " + lijst_naam)
        global lijst_path
        lijst_path = "/lijsten/" + lijst_naam
        with open("." + lijst_path) as f:
            global lijst
            lijst = f.read().split()
            return lijst
    else:
        print("Kan de opgevraagde lijst helaas niet vinden, probeer opnieuw.")
        lijst_path = ""
        return
    return

def split_words():
    global two_lijst
    global one_lijst
    one_lijst.clear()
    two_lijst.clear()
    for word in lijst:
        global splitter
        if (splitter >= 2):
            two_lijst.append(word)
            splitter = 1
        else:
            one_lijst.append(word)
            splitter = 2

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

def add_words():
    os.startfile(ProgrammaURL + lijst_path)
    leeg_scherm()
    input("druk enter: ")
    with open("." + lijst_path) as f:
        global lijst
        lijst = f.read().split()
    split_words()
    return

def show_words():
    print(lijst)
    print(" ")
    print(two_lijst)
    print(" ")
    print(one_lijst)

def leeg_scherm():
    print("\n" * 100)

def lees_woordenlijst(BESTANDSNAAM):
    return

def main():
    menu_show()
    global keuze
    if (keuze == "s"):
        leeg_scherm()
        for i in range(len(one_lijst)):
            print(one_lijst[i] + (" "*(20-len(one_lijst[i]))) + "   :   " + two_lijst[i])
        print("\n")
        keuze = " "
        main()

    if (keuze == "k"):
        leeg_scherm()
        show_lijsten()
        print("\n" * 2)
        i = input("keuze: ")
        kies_lijst(i)
        split_words()
        print("\n" * 8)
        main()

    if (keuze == "e"):
        add_words()
        leeg_scherm()
        main()
        keuze = " "

    if (keuze == "d"):
        del_words()
        leeg_scherm()
        main()
        keuze = " "

    if (keuze == "m"):
        leeg_scherm()
        maak_lijst()
        main()
        keuze = " "

    if (keuze == "o"):
        global goed
        global fout
        leeg_scherm()
        goed = 0
        fout = 0
        split_words()
        volgorde_lijst_function()
        leeg_scherm()
        overhoor_lijst()
        keuze = " "
        main()

    del_prullenbak()

del_prullenbak()
leeg_scherm()
main()