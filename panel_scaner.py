import requests
from colorama import Fore,init
import os

clear = os.system("cls" or "clear")
init()


banner_txt = """
                                                                                                                    
    //   ) )                                               // | |                                               
   //___/ /      ___         __        ___       //       //__| |     ___   /      _   __       ( )       __    
  / ____ /     //   ) )   //   ) )   //___) )   //       / ___  |   //   ) /     // ) )  ) )   / /     //   ) ) 
 //           //   / /   //   / /   //         //       //    | |  //   / /     // / /  / /   / /     //   / /  
//           ((___( (   //   / /   ((____     //       //     | | ((___/ /     // / /  / /   / /     //   / /   
"""

print(Fore.LIGHTYELLOW_EX+banner_txt)

def main_over():

    target = input(Fore.GREEN+"Enter URL [ site.com ] : ")

    test_list = input("If Costume List Ya Defult List (c,d) : ")

    if test_list == "c":
        file_1 = input("Enter Admin List [ list.txt ] : ")

        def panel():
            lists = open(file_1,"r").read().split()
            print("")
            print("-"*50)
            for l in lists:
                URL = "http://" + target + "/" + l
                r = requests.get(URL).status_code

                if r == 200:
                    print(Fore.BLUE+"[+] "+Fore.LIGHTRED_EX+"Horaaa This Panel [ '/{}' ]".format(l))
                    save = open("rander/log.txt",)
                    save.write("[+] "+"Horaaa This Panel [ '/{}' ]".format(l))
                else:
                    print(Fore.RED+"[+] "+Fore.WHITE+"Not this admin : /"+l)


        panel()
    
    if test_list == "d":
        def panel():
            lists = open("static/list.txt","r").read().split()
            print("")
            print("-"*50)
            for l in lists:
                URL = "http://" + target + "/" + l
                r = requests.get(URL).status_code

                if r == 200:
                    print(Fore.BLUE+"[+] "+Fore.LIGHTRED_EX+"Horaaa This Panel [ '/{}' ]".format(l))
                    save = open("rander/log.txt","a")
                    save.write("[+] "+"Horaaa This Panel [ '/{}' ]".format(l))
                else:
                    print(Fore.RED+"[+] "+Fore.WHITE+"Not this admin : /"+l)


        panel()


def dev():
    print(Fore.BLUE+"-"*50)
    print(Fore.GREEN+"""
        developer : Alireza Zare
        Github : http://github.com/code-irans
        program : python, php, c#
    """)


print(Fore.GREEN+"""
[1] Search To Url Admin Panel
[2] developer option
[3] Update App {}
{}
""".format(Fore.WHITE+"(locadet...)", Fore.GREEN+"[4] exit Code"))

k = input("Enter option App : ")

if k == "1":
    os.system("cls" or "clear")
    print(Fore.LIGHTYELLOW_EX+banner_txt)
    main_over()
if k == "2": 
    dev()
if k == "4":
    print(Fore.RED+"Exit Code [ Ctrl-c ]")
    exit()


# control - c || heandler

try:
    pass
except KeyboardInterrupt:
   print(Fore.RED+"Exit Crtl+ C )):")