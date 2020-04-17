from colorama import init, Fore
from os import system, listdir
from itertools import product
from platform import platform
from time import sleep
import sys


wordlist_generator = """
 _    _               _ _     _     _     _____                           _             
| |  | |             | | |   (_)   | |   |  __ \                         | |            
| |  | | ___  _ __ __| | |    _ ___| |_  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |/\| |/ _ \| '__/ _` | |   | / __| __| | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
\  /\  / (_) | | | (_| | |___| \__ \ |_  | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
 \/  \/ \___/|_|  \__,_\_____/_|___/\__|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   

"""


def clear(): system("cls") if platform().startswith("Windows") else system("clear")


def progress_bar(total, completed, bar_symbol="█" , space_symbol="-", lenght=50):
    progress = int(lenght * (completed * 100 / total) / 100)
    if total < completed:
        return
    sys.stdout.write(f"\rProgress Bar: %{int(completed * 100 / total)} |{bar_symbol*progress}{space_symbol*(lenght - progress)}| {total}/{completed}")


def save_file(txt, word):
    with open(txt if txt.endswith(".txt") else f"{txt}.txt", "a") as file:
        file.write(word)
        sys.stdout.flush()


def total_word(stirng, min, max):
    num = 0
    for i in range(min, max+1):
        num += len(stirng)**i
    return num


def generator(string, file, min, max):
    string = "".join(sorted(set(string)))
    number = 0
    for _ in range(min, max+1):
        for word in product(string, repeat=_):
            number += 1
            word_ = "".join(word)
            save_file(file, f"{word_}\n")
            progress_bar(total_word(string, min, max), number)
            sleep(0.1)


def main():
    clear()
    init(True)
    print(f"{Fore.LIGHTBLUE_EX}{wordlist_generator}")
    print(f"{Fore.LIGHTBLUE_EX}\t\tPython WordList Generator\n")
    stirng = input(f"{Fore.LIGHTBLUE_EX}İşleme alınacak karakterleri giriniz: ")
    if not stirng:
        print("Geçersiz karakterler.")
        exit()

    while 1:
        min = input(f"{Fore.LIGHTBLUE_EX}En az uzunluk sayısı: ")
        if min.isdigit():
            break
        else:
            print("Bir sayı değeri girmelisiniz.")
    if not min:
        print("Geçersiz uzunluk.")
        exit()

    while 1:
        max = input(f"{Fore.LIGHTBLUE_EX}En fazla uzunluk sayısı: ")
        if min.isdigit():
            break
        else:
            print("Bir sayı değeri girmelisiniz.")
    if not max:
        print("Geçersiz uzunluk.")

    if min >= max:
        print("Geçersiz uzunluklar.")
        sys.exit()

    while 1:
        file = input(f"{Fore.LIGHTBLUE_EX}Kaydedilecek .txt dosyası: ")
        if file in listdir("./") or f"{file}.txt" in listdir("./"):
            print("Başka bir .txt dosyası ismi giriniz. Bu isimde zaten bir txt dosyası mevcut.")
        else:
            break
    if not file:
        print("Geçersiz dosya adı.")
        exit()

    generator(stirng, file, int(min), int(max))



if __name__ == '__main__':
    main()
