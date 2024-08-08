def hl():
    from colorama import Fore

    print(Fore.CYAN + '    you should choose a number ')
    print(Fore.CYAN + '    then choose a unit')
    print(Fore.CYAN + '    here go ....')
    # bk = int(input(Fore.BLUE+ " \n ["Fore.WHITE + '0'+ Fore.BLUE + "]" Fore.CYAN + "Back =>"))

    if bk == 0:
        converting()


def converting():
    import os, time, sys,socket
    from colorama import Fore
    from time import strftime
 

    os.system("cls")
    print(Fore.RED+"""\n
     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
    ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
    ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
    ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ version 2.0.1""",)
    print("")
    print("")
    try:
        from colorama import Fore
    except:
        print(Fore.RED + "┌─[卐]",Fore.WHITE + "you should install the package of colorama (pip3 install colorama) ")
    try:
        import requests
    except:
        print(Fore.RED + "┌─[卐]",Fore.WHITE + "you should install the package of requests (pip3 install requests) ")

    #length
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)

    print(Fore.YELLOW+f'┌─[@Home/..]', strftime('%D'))
    print('')
    print(Fore.GREEN+'   [*]', Fore.WHITE+'select an option for using ', Fore.GREEN+'[*]')
    print('')
    print( Fore.GREEN+"   [01]", Fore.WHITE+"LENGTH",Fore.GREEN+" [02]", Fore.WHITE+"DATA", Fore.GREEN+"  [03]",Fore.WHITE+"TIME\n",Fore.GREEN+"  [04]",Fore.WHITE+"AREA",Fore.GREEN+"   [05]",Fore.WHITE+"VOLUME",Fore.GREEN+"[06]",Fore.WHITE+"MASS\n",Fore.GREEN+"  [07]",Fore.WHITE+"SPEED",Fore.GREEN+"  [08]",Fore.WHITE+"TR",Fore.GREEN+"    [09]", Fore.WHITE+"EXIT",Fore.GREEN+"\n   [10]", Fore.WHITE+"Help")
    print("")

    namecover = input(Fore.GREEN+"┌─[")







    #exit
    if namecover == '10':
            hl()
    elif namecover == '9':
        os.system("cls")
        sys.exit()




    print("")




    print(Fore.GREEN + "[&]" ,Fore.RESET+" ENTER YOUR NUMBER :")
    print("")
    number = float(input(Fore.RED+"┌─[$]"))

    print("")

    print(Fore.YELLOW+"------------------------------------------")


    #numbers float
    while True:
        if namecover == '1':
            os.system("cls")
            print(Fore.RED+'┌─[@Home\LENGTH]')
            time.sleep(0.1)
            print(Fore.GREEN+'['+ Fore.WHITE+'1'+ Fore.GREEN + ']'+ Fore.RESET+"KILOMETER")
            time.sleep(0.1)
            print(Fore.GREEN+"[2]", Fore.RESET+"METER")
            time.sleep(0.1)
            print(Fore.GREEN+"[3]", Fore.RESET+"MILLIMETER")
            time.sleep(0.1)
            print(Fore.GREEN+"[4]", Fore.RESET+"CENTIMETER")
            time.sleep(0.1)
            print(Fore.GREEN+"[5]", Fore.RESET+"Foot")
            time.sleep(0.1)
            print(Fore.GREEN+"[6]", Fore.RESET+"MILE")
            print("")
            length = int(input("┌─[=]"))

            if length == 1:

                print(Fore.RED + '┌─[卐Home\LENGTH\KILOMETER]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KM TO METER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KM TO CM")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KM TO MILIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "KM TO MILE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "KM TO FOOT")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"Which : \n\n", Fore.GREEN+"[1]",Fore.YELLOW+"KM TO METER\n",Fore.GREEN+"[2]",Fore.YELLOW+"KM TO CM\n", Fore.GREEN+"[3]",Fore.YELLOW+"KM TO MILIMETER\n",Fore.GREEN+"[4]",Fore.YELLOW+"KM TO MILE\n",Fore.GREEN+"[5]",Fore.YELLOW+"KM TO FOOT ==>:")
                print("")

                kcov = int(input("┌─[=]"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"┌─[CONVERTING........")
                print("")
                time.sleep(1.5)
                if kcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*1000,"METERS")
                if kcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*100000,"CM")
                if kcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*1000000,"MM")
                if kcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*0.621371192,"MILE")
                if kcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*3280.8399,"FOOT")
            elif length == 2:

                print(Fore.RED + '┌─[@Home\LENGTH\METER]')
                time.sleep(0.1)
                pprint("")
                print(Fore.GREEN + "[1]", Fore.RESET + "METER TO KILOMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "METER TO MILIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "METER TO CM")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "METER TO MILE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "METER TO FOOT ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"METER TO KILOMETER\n",Fore.GREEN+"[2]",Fore.YELLOW+"METER TO MILIMETER\n",Fore.GREEN+"[3]",Fore.YELLOW+"METER TO CM\n",Fore.GREEN+"[4]",Fore.YELLOW+"METER TO MILE\n",Fore.GREEN+"[5]",Fore.YELLOW+"METER TO FOOT ==>:")
                mcov = int(input("┌─[=]"))
                print("")

                print(Fore.RED+"┌─[CONVERTING........")
                print("")
                print(Fore.CYAN+"------------------------------------------")

                time.sleep(1.5)

                if mcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/1000, "KILOMETER")
                if mcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000, "MM")
                if mcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100, "CM")
                if mcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.000621371192, "MILE")
                if mcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.2808399, "FOOT")
            elif length == 3:

                print(Fore.RED + '┌─[@Home\LENGTH\MILIMETER]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MILIMETER TO KILOMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MILIMETER TO METER")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MILIMETER TO CM")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MILIMETER TO MILE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MILIMETER TO Foot ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MILIMETER TO KILOMETER\n",Fore.GREEN+"[2]",Fore.YELLOW+"MILIMETER TO METER\n",Fore.GREEN+"[3]",Fore.YELLOW+"MILIMETER TO CM\n",Fore.GREEN+"[4]",Fore.YELLOW+"MILIMETER TO MILE\n",Fore.GREEN+"[5]",Fore.YELLOW+"MILIMETER TO Foot ==>:")
                mcov = int(input("┌─[=]"))
                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if mcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number/1000000, "KILOMETER")
                if mcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*0.1, "CM")
                if mcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*0.001, "M")
                if mcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*0.000000621371192, "MILE")
                if mcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*0.0032808399, "FOOT")

            elif length == 4:

                print(Fore.RED + '┌─[@Home\LENGTH\CENTIMETER]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "CENTIMETER TO KILOMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "CENTIMETER TO METER")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "CENTIMETER TO MM")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "CENTIMETER TO MILE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "CENTIMETER TO Foot ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"CENTIMETER TO KILOMETER\n",Fore.GREEN+"[2]",Fore.YELLOW+"CENTIMETER TO METER\n",Fore.GREEN+"[3]",Fore.YELLOW+"CENTIMETER TO MM\n",Fore.GREEN+"[4]",Fore.YELLOW+"CENTIMETER TO MILE \n",Fore.GREEN+"[5]",Fore.YELLOW+"CENTIMETER TO FOOT ==>:")
                # print("")

                mcov = int(input("┌─[=]"))

                print("")
                print(Fore.CYAN+"------------------------------------------")
                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if mcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/100000, "KILOMETER")
                if mcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.01, "M")
                if mcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10, "MM")
                if mcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.00000621371192, "MILE")
                if mcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.032808399, "FOOT")

            elif length == 5:

                print(Fore.RED + '┌─[@Home\LENGTH\FOOT]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "FOOT TO KILOMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "FOOT TO METER")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "FOOT TO MM")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "FOOT TO MILE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "FOOT TO CM ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]", Fore.YELLOW+"FOOT TO KILOMETER\n",Fore.GREEN+"[2]",Fore.YELLOW+"FOOT TO METER\n",Fore.GREEN+"[3]",Fore.YELLOW+"FOOT TO MM\n",Fore.GREEN+"[4]",Fore.YELLOW+"FOOT TO MILE \n",Fore.GREEN+"[5]",Fore.YELLOW+"FOOT TO CM ==>:")

                mcov = int(input("┌─[=]"))

                print("")

                print(Fore.CYAN+"------------------------------------------")
                print("")
                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if mcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/0.0003048,"KILOMETER")
                if mcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.3048,"M")
                if mcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*304.8,"MM")
                if mcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.000189393939,"MILE")
                if mcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*30.48,"CM")
            elif length == 6:

                print(Fore.RED + '┌─[@Home\LENGTH\MILE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MILE TO KILOMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MILE TO METER")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MILE TO MM")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MILE TO FOOT")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MILE TO CM ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MILE TO KILOMETER\n",Fore.GREEN+"[2]",Fore.YELLOW+"MILE TO METER\n",Fore.GREEN+"[3]",Fore.YELLOW+"MILE TO MM\n",Fore.GREEN+"[4]",Fore.YELLOW+"MILE TO FOOT \n",Fore.GREEN+"[5]",Fore.YELLOW+"MILE TO CM ==>:")
                # print("")

                mcov = int(input("┌─[=]"))

                print("")

                print(Fore.CYAN+"------------------------------------------")
                print("")
                print(Fore.RED+"┌─[CONVERTING........")


                print("")

                time.sleep(1.5)

                if mcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number/1.609344, "KILOMETER")
                if mcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*1609.344, "M")
                if mcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*1609344, "MM")
                if mcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*5280, "FOOT")
                if mcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE", number*160934.4, "CM")
        #date
        elif namecover == '2':
            os.system("cls")
            print(Fore.RED + '┌─[@Home\DATA]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.CYAN + "BYTE")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.CYAN + "KILOBYTE")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.CYAN + "MEGABYTE")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.CYAN + "GIGABYTE")
            time.sleep(0.1)
            print(Fore.GREEN + "[5]", Fore.CYAN + "TERABYTE ")
            time.sleep(0.1)
            print(Fore.GREEN + '[6]', Fore.CYAN + "PETABYTE")
            print('')
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"BYTE\n",Fore.GREEN+"[2]",Fore.CYAN+"KILOBYTE\n",Fore.GREEN+"[3]",Fore.CYAN+"MEGABYTE\n",Fore.GREEN+"[4]",Fore.CYAN+"GIGABYTE\n",Fore.GREEN+"[5]",Fore.CYAN+"TERABYTE\n",Fore.GREEN+"[6]",Fore.CYAN+"PETABYTE ==>:")
            # print("")
            Date = int(input("<=>"))

            if Date == 1:

                print(Fore.RED + '┌─[@Home\DATA\BYTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "BYTE TO KILOBYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "BYTE TO MEGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "BYTE TO GIGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "BYTE TO TERABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "BYTE TO PETABYTE ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"BYTE TO KILOBYTE\n",Fore.GREEN+"[2]",Fore.YELLOW+"BYTE TO MEGABYTE\n",Fore.GREEN+"[3]",Fore.YELLOW+"BYTE TO GIGABYTE\n",Fore.GREEN+"[4]",Fore.YELLOW+"BYTE TO TERABYTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"BYTE TO PETABYTE ==>:")
                # print("")
                Dcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if Dcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0009765625,"KB")
                if Dcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.53674316/10000000,"MB")
                if Dcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.31322575/10000000,"GB")
                if Dcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.09494702/10000000000000,"TB")
                if Dcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*8.8817842/100000000000000000,"PB")
            elif Date == 2:

                print(Fore.RED + '┌─[@Home\DATA\KILOBYTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KILOBYTE TO BYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KILOBYTE TO MEGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KILOBYTE TO GIGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "KILOBYTE TO TERABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "KILOBYTE TO PETABYTE ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"KILOBYTE TO BYTE\n",Fore.GREEN+"[2]",Fore.YELLOW+"KILOBYTE TO MEGABYTE\n",Fore.GREEN+"[3]",Fore.YELLOW+"KILOBYTE TO GIGABYTE\n",Fore.GREEN+"[4]",Fore.YELLOW+"KILOBYTE TO TERABYTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"KILOBYTE TO PETABYTE ==>:")
                # print("")
                Dcov= int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")
                print("")

                time.sleep(1.5)

                if Dcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1024,"B")
                if Dcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0009765625,"MB")
                if Dcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.5367431/10000000,"GB")
                if Dcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.31322575/10000000000,"TB")
                if Dcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.09494702/10000000000000,"PB")
            elif Date == 3:

                print(Fore.RED + '┌─[@Home\DATA\MEGABYTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MEGABYTE TO BYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MEGABYTE TO KILOBYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MEGABYTE TO GIGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MEGABYTE TO TERABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MEGABYTE TO PETABYTE ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MEGABYTE TO BYTE\n",Fore.GREEN+"[2]",Fore.YELLOW+"MEGABYTE TO KILOBYTE\n",Fore.GREEN+"[3]",Fore.YELLOW+"MEGABYTE TO GIGABYTE\n",Fore.GREEN+"[4]",Fore.YELLOW+"MEGABYTE TO TERABYTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"MEGABYTE TO PETABYTE ==>:")
                # print("")
                Dcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if Dcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1048576,"B")
                if Dcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1024,"KB")
                if Dcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0009765625,"GB")
                if Dcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.53674316/10000000,"TB")
                if Dcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.3122575/10000000000,"PB")
            elif Date == 4:

                print(Fore.RED + '┌─[@Home\DATA\GIGABYTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "GIGABYTE TO BYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "GIGABYTE TO KILOBYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "GIGABYTE TO MEGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "GIGABYTE TO TERABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "GIGABYTE TO PETABYTE ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"GIGABYTE TO BYTE\n",Fore.GREEN+"[2]",Fore.YELLOW+"GIGABYTE TO KILOBYTE\n",Fore.GREEN+"[3]",Fore.YELLOW+"GIGABYTE TO MEGABYTE\n",Fore.GREEN+"[4]",Fore.YELLOW+"GIGABYTE TO TERABYTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"GIGABYTE TO PETABYTE ==>:")
                # print("")

                Dcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if Dcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.07374182*1000000000,"B")
                if Dcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1048576,"KB")
                if Dcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1024,"MB")
                if Dcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0009765625,"TB")
                if Dcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.53674316/10000000,"PB")
            elif Date == 5:

                print(Fore.RED + '┌─[@Home\DATA\TERABYTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "TERABYTE TO BYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "TERABYTE TO KILOBYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "TERABYTE TO MEGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "TERABYTE TO GIGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "TERABYTE TO PETABYTE ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"TERABYTE TO BYTE\n",Fore.GREEN+"[2]",Fore.YELLOW+"TERABYTE TO KILOBYTE\n",Fore.GREEN+"[3]",Fore.YELLOW+"TERABYTE TO MEGABYTE\n",Fore.GREEN+"[4]",Fore.YELLOW+"TERABYTE TO GIGABYTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"TERABYTE TO PETABYTE ==>:")
                # print("")

                Dcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if Dcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.09951163*1000000000000,"B")
                if Dcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.07374182*1000000000,"KB")
                if Dcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1048576,"MB")
                if Dcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1024,"GB")
                if Dcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0009765625,"PB")
            elif Date == 6:

                print(Fore.RED + '┌─[@Home\DATA\PETABYTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "PETABYTE TO BYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "PETABYTE TO KILOBYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "PETABYTE TO MEGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "PETABYTE TO GIGABYTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "PETABYTE TO TERABYTE ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"PETABYTE TO BYTE\n",Fore.GREEN+"[2]",Fore.YELLOW+"PETABYTE TO KILOBYTE\n",Fore.GREEN+"[3]",Fore.YELLOW+"PETABYTE TO MEGABYTE\n",Fore.GREEN+"[4]",Fore.YELLOW+"PETABYTE TO GIGABYTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"PETABYTE TO TERABYTE ==>:")
                # print("")

                Dcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if Dcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.12589991*1000000000000000,"B")
                if Dcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.09951163*1000000000000,"KB")
                if Dcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1048576,"MB")
                if Dcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1048576,"GB")
                if Dcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1024,"TB")
        #time
        elif namecover == '3':
            os.system("cls")
            print(Fore.RED + '┌─[@Home\TIME]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.RESET + "YEAR")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.RESET + "WEEK")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.RESET + "DAY")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.RESET + "HOUR")
            time.sleep(0.1)
            print(Fore.GREEN + "[5]", Fore.RESET + "MINUTE")
            time.sleep(0.1)
            print(Fore.GREEN + "[6]", Fore.RESET + "SECOND")
            time.sleep(0.1)
            print(Fore.GREEN + "[7]", Fore.RESET + "MILISECOOND")
            print("")
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"YEAR\n",Fore.GREEN+"[2]",Fore.CYAN+"WEEK\n",Fore.GREEN+"[3]",Fore.CYAN+"DAY\n",Fore.GREEN+"[4]",Fore.CYAN+"HOUR\n",Fore.GREEN+"[5]",Fore.CYAN+"MINUTE\n",Fore.GREEN+"[6]",Fore.CYAN+"SECOND\n",Fore.GREEN+"[7]",Fore.CYAN+"MILISECOOND ==>")
            # print("")
            timr = int(input("<=>"))
            if timr == 1:

                print(Fore.RED + '┌─[@Home\TIME\YEAR]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "YEAR TO WEEK")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "YEAR TO DAY")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "YEAR TO HOUR")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "YEAR TO MINUTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "YEAR TO SECOND ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "YEAR TO MILISECOOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+" WICH : \n\n", Fore.GREEN+"[1]",Fore.YELLOW+"YEAR TO WEEK\n", Fore.GREEN+"[2]",Fore.YELLOW+"YEAR TO DAY\n",Fore.GREEN+"[3]",Fore.YELLOW+"YEAR TO HOUR\n",Fore.GREEN+"[4]",Fore.YELLOW+"YEAR TO MINUTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"YEAR TO SECOND\n",Fore.GREEN+"[6]",Fore.YELLOW+"YEAR TO MILISECOOND ==>")
                # print("")

                tcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"┌─[CONVERTING........")

                print("")

                time.sleep(1.5)

                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*52.1428571,"WK")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*365,"d")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*8760,"H")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*525600,"MIN")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*31536000,"S")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.1536*10000000000,"MS")
            elif timr == 2:

                print(Fore.RED + '┌─[@Home\TIME\WEEK]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "WEEK TO YEAR")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "WEEK TO DAY")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "WEEK TO HOUR")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "WEEK TO MINUTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "WEEK TO SECOND ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "WEEK TO MILISECOOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"WEEK TO YEAR\n",Fore.GREEN+"[2]",Fore.YELLOW+"WEEK TO DAY\n",Fore.GREEN+"[3]",Fore.YELLOW+"WEEK TO HOUR\n",Fore.GREEN+"[4]",Fore.YELLOW+"WEEK TO MINUTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"WEEK TO SECOND\n",Fore.GREEN+"[6]",Fore.YELLOW+"WEEK TO MILISECOOND ==>")
                # print("")
                tcov= int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"[*]CONVERTING........")

                print("")

                time.sleep(1.5)


                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0191780822,"Y")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*7,"d")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*168,"H")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10080,"MIN")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*604800,"S")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*604800000,"MS")
            elif timr == 3:

                print(Fore.RED + '┌─[@Home\TIME\DAY]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "DAY TO YEAR")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "DAY TO WEEK")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "DAY TO HOUR")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "DAY TO MINUTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "DAY TO SECOND ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "DAY TO MILISECOOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"DAY TO YEAR\n",Fore.GREEN+"[2]",Fore.YELLOW+"DAY TO WEEK\n",Fore.GREEN+"[3]",Fore.YELLOW+"DAY TO HOUR\n",Fore.GREEN+"[4]",Fore.YELLOW+"DAY TO MINUTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"DAY TO SECOND\n",Fore.GREEN+"[6]",Fore.YELLOW+"DAY TO MILISECOOND ==>")
                # print("")
                tcov= int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"[*]CONVERTING........")

                print("")

                time.sleep(1.5)


                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.00273972603,"Y")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.142857143,"WK")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*24,"H")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1440,"MIN")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*86400,"S")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*86400000,"MS")
            elif timr == 4:

                print(Fore.RED + '┌─[@Home\TIME\HOUR]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "HOUR TO YEAR")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "HOUR TO WEEK")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "HOUR TO DAY")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "HOUR TO MINUTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "HOUR TO SECOND ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "HOUR TO MILISECOOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"HOUR TO YEAR\n",Fore.GREEN+"[2]",Fore.YELLOW+"HOUR TO WEEK\n",Fore.GREEN+"[3]",Fore.YELLOW+"HOUR TO DAY\n",Fore.GREEN+"[4]",Fore.YELLOW+"HOUR TO MINUTE\n",Fore.GREEN+"[5]",Fore.YELLOW+"HOUR TO SECOND\n",Fore.GREEN+"[6]",Fore.YELLOW+"HOUR TO MILISECOOND ==>")
                # print("")

                tcov = int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"[*]CONVERTING........")

                print("")

                time.sleep(1.5)


                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.000114155251,"Y")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.00595238095,"WK")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0416666667,"d")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*60,"MIN")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3600,"S")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3600000,"MS")
            elif timr == 5:

                print(Fore.RED + '┌─[@Home\TIME\MINUTE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MINUTE TO YEAR")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MINUTE TO WEEK")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MINUTE TO HOUR")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MINUTE TO DAY")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MINUTE TO SECOND ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "MINUTE TO MILISECOOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MINUTE TO YEAR\n",Fore.GREEN+"[2]",Fore.YELLOW+"MINUTE TO WEEK\n",Fore.GREEN+"[3]",Fore.YELLOW+"MINUTE TO DAY\n",Fore.GREEN+"[4]",Fore.YELLOW+"MINUTE TO HOUR\n",Fore.GREEN+"[5]",Fore.YELLOW+"MINUTE TO SECOND\n",Fore.GREEN+"[6]",Fore.YELLOW+"MINUTE TO MILISECOOND ==>")
                # print("")
                tcov= int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"[*]CONVERTING........")

                print("")

                time.sleep(1.5)


                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.90258752/1000000,"Y")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.92063492/100000,"WK")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.000694444444,"d")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0166666667,"H")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*60,"S")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*60000,"MS")
            elif timr == 6:

                print(Fore.RED + '┌─[@Home\TIME\SECOND]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "SECOND TO YEAR")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "SECOND TO WEEK")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "SECOND TO HOUR")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "SECOND TO MINUTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "SECOND TO DAY ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "SECOND TO MILISECOOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"SECOND TO YEAR\n",Fore.GREEN+"[2]",Fore.YELLOW+"SECOND TO WEEK\n",Fore.GREEN+"[3]",Fore.YELLOW+"SECOND TO DAY\n",Fore.GREEN+"[4]",Fore.YELLOW+"SECOND TO HOUR\n",Fore.GREEN+"[5]",Fore.YELLOW+"SECOND TO MINUTE\n",Fore.GREEN+"[6]",Fore.YELLOW+"SECOND TO MILISECOOND ==>")
                # print("")
                tcov= int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"[*]CONVERTING........")

                print("")

                time.sleep(1.5)


                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.1709792/100000000,"Y")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.65343915/1000000,"WK")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.15740741/100000,"d")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.000277777778,"H")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0166666667,"MIN")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"MS")
            elif timr == 7:

                print(Fore.RED + '┌─[@Home\TIME\MILISECOOND]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MILISECOOND TO YEAR")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MILISECOOND TO WEEK")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MILISECOOND TO HOUR")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MILISECOOND TO MINUTE")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MILISECOOND TO DAY ")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "MILISECOOND TO SECOND ")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MILISECOOND TO YEAR\n",Fore.GREEN+"[2]",Fore.YELLOW+"MILISECOOND TO WEEK\n",Fore.GREEN+"[3]",Fore.YELLOW+"SECOND TO DAY\n",Fore.GREEN+"[4]",Fore.YELLOW+"MILISECOOND TO HOUR\n",Fore.GREEN+"[5]",Fore.YELLOW+"MILISECOOND TO MINUTE\n",Fore.GREEN+"[6]",Fore.YELLOW+"SECOND TO MILISECOOND ==>")
                # print("")
                tcov= int(input("<=>"))

                print(Fore.CYAN+"------------------------------------------")


                print(Fore.RED+"[*]CONVERTING........")

                print("")

                time.sleep(1.5)


                if tcov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.1709792/100000000000,"Y")
                if tcov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.65343915/1000000000,"WK")
                if tcov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.15740741/100000000,"d")
                if tcov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*2.77777778/10000000,"H")
                if tcov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.66666667/100000,"MIN")
                if tcov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"S")
        #area
        elif namecover == "4":
            os.system("cls")
            print(Fore.RED + '┌─[@Home\AREA]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.RESET + "SQUARE KILOMETER")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.RESET + "SQUARE METR")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.RESET + "SQUARE MILIMETER")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.RESET + "SQUARE CENTIMETER")
            time.sleep(0.1)
            print(Fore.GREEN + "[5]", Fore.RESET + "SQUARE FT²")
            time.sleep(0.1)
            print(Fore.GREEN + "[6]", Fore.RESET + "HECTARE")
            print("")
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"SQUARE KILOMETER\n",Fore.GREEN+"[2]",Fore.CYAN+"SQUARE METR\n",Fore.GREEN+"[3]",Fore.CYAN+"SQUARE MILIMETER\n",Fore.GREEN+"[4]",Fore.CYAN+"SQUARE CENTIMETER\n",Fore.GREEN+"[5]",Fore.CYAN+"SQUARE CENTIMETER\n",Fore.GREEN+"[6]",Fore.CYAN+"SQUARE MILE\n",Fore.GREEN+"[7]",Fore.CYAN+"HECTARE")
            # print("")
            area = int(input("<=>"))
            if area == 1:

                print(Fore.RED + '┌─[@Home\AREA\KM²]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KM² TO M²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KM² TO MM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KM² TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "KM² TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "KM² TO FT²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "KM² TO HECTARE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"KM² TO M²\n",Fore.GREEN+"[2]",Fore.YELLOW+"KM² TO M²\n",Fore.GREEN+"[3]",Fore.YELLOW+"KM² TO MM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"KM² TO MILE²\n",Fore.GREEN+"[5]",Fore.YELLOW+"KM² TO FT²\n",Fore.GREEN+"[6]",Fore.YELLOW+"KM² TO HECTARE")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"M²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10000000000,"CM²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000000000,"MM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.386102159,"MILE²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10763910.4,"FT²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100,"HA")
            elif area == 2:

                print(Fore.RED + '┌─[@Home\AREA\M²]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "M² TO KM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "M² TO MM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "M² TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "M² TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "M² TO FT²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "M² TO HECTARE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"M² TO KM²\n",Fore.GREEN+"[2]",Fore.YELLOW+"M² TO CM²\n",Fore.GREEN+"[3]",Fore.YELLOW+"M² TO MM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"M² TO MILE²\n",Fore.GREEN+"[5]",Fore.YELLOW+"M² TO FT²\n",Fore.GREEN+"[6]",Fore.YELLOW+"M² TO HECTARE")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/1000000,"KM²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"CM²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000000,"MM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.86102159/100000,"MILE²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1076.39104,"FT²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.01,"HA")
            elif area == 3:

                print(Fore.RED + '┌─[@Home\AREA\CM²]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "CM² TO KM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "CM² TO MM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "CM² TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "CM² TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "CM² TO FT²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "CM² TO HECTARE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"CM² TO KM²\n",Fore.GREEN+"[2]",Fore.YELLOW+"CM² TO M²\n",Fore.GREEN+"[3]",Fore.YELLOW+"CM² TO MM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"CM² TO MILE²\n",Fore.GREEN+"[5]",Fore.YELLOW+"CM² TO FT²\n",Fore.GREEN+"[6]",Fore.YELLOW+"CM² TO HECTARE")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/10000000000,"KM²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.00001,"M²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100,"MM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.86102159/100000000000,"MILE²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.00107639104,"FT²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/100000000,"HA")
            elif area == 4:

                print(Fore.RED + '┌─[@Home\AREA\MM²]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MM² TO KM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MM² TO M²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MM² TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MM² TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MM² TO CM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "MM² TO HECTARE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MM² TO KM²\n",Fore.GREEN+"[2]",Fore.YELLOW+"MM² TO M²\n",Fore.GREEN+"[3]",Fore.YELLOW+"MM² TO CM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"MM² TO MILE²\n",Fore.GREEN+"[5]",Fore.YELLOW+"MM² TO FT²\n",Fore.GREEN+"[6]",Fore.YELLOW+"MM² TO HECTARE")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/1000000000000,"KM²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/1000000,"M²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.01,"CM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.86102159/10000000000000,"MILE²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.07639104/100000,"FT²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number/10000000000,"HA")
            elif area == 6:

                print(Fore.RED + '┌─[@Home\AREA\MILE²]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MILE² TO KM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MILE² TO M²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MILE² TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MILE² TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MILE² TO FT²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "MILE² TO HECTARE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MILE² TO KM²\n",Fore.GREEN+"[2]",Fore.YELLOW+"MILE² TO M²\n",Fore.GREEN+"[3]",Fore.YELLOW+"MILE² TO CM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"MILE² TO MM²\n",Fore.GREEN+"[5]",Fore.YELLOW+"MILE² TO FT²\n",Fore.GREEN+"[6]",Fore.YELLOW+"MILE² TO HECTARE")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*2.58998811,"KM²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*2589988.11,"M²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*2.58998811*10000000000,"CM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*2.58998811*1000000000000,"MM²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*27878400,"FT²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*258.998811,"HA")
            elif area == 5:

                print(Fore.RED + '┌─[@Home\AREA\FT²]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "FT² TO KM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "FT² TO M²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "FT² TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "FT² TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "FT² TO MM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "FT² TO HECTARE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"FT² TO KM²\n",Fore.GREEN+"[2]",Fore.YELLOW+"FT² TO M²\n",Fore.GREEN+"[3]",Fore.YELLOW+"FT² TO CM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"FT² TO MM²\n",Fore.GREEN+"[5]",Fore.YELLOW+"FT² TO MILE²\n",Fore.GREEN+"[6]",Fore.YELLOW+"FT² TO HECTARE")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.290304/100000000,"KM²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.09290304,"M²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*929.0304,"CM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*92903.04,"MM²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.58700643/100000000,"MILE²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*9.290304/1000000,"HA")
            elif area == 7:

                print(Fore.RED + '┌─[@Home\AREA\HA]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "HA TO KM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "HA TO M²")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "HA TO MILE²")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "HA TO CENTIMETER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "HA TO MM²")
                time.sleep(0.1)
                print(Fore.GREEN + "[6]", Fore.RESET + "HA TO FT²")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"HA TO KM²\n",Fore.GREEN+"[2]",Fore.YELLOW+"HA TO M²\n",Fore.GREEN+"[3]",Fore.YELLOW+"HA TO CM²\n",Fore.GREEN+"[4]",Fore.YELLOW+"HA TO MM²\n",Fore.GREEN+"[5]",Fore.YELLOW+"HA TO MILE²\n",Fore.GREEN+"[6]",Fore.YELLOW+"HA TO FT²")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)
                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.01, "KM²")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10000, "M²")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100000000, "CM²")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10000000000, "MM²")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0270271511, "MILE²")
                if acov == 6:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*753473.729, "FT²")
        #voulm
        elif namecover == '5':
            os.system("cls")

            print(Fore.RED + '┌─[@Home\VOLUME]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.RESET + "LITER")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.RESET + "CUBIC METER")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.RESET + "CUBIC MILIMETER")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.RESET + "CUBIC CENTIMETER")
            time.sleep(0.1)
            print(Fore.GREEN + "[5]", Fore.RESET + "MILILITER")
            time.sleep(0.1)
            print(Fore.GREEN + "[6]", Fore.RESET + "CENTILIER")
            print('')
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"LITER\n",Fore.GREEN+"[2]",Fore.CYAN+"CUBIC METER\n",Fore.GREEN+"[3]",Fore.CYAN+"CUBIC MILIMETER\n",Fore.GREEN+"[4]",Fore.CYAN+"CUBIC CENTIMETER\n",Fore.GREEN+"[5]",Fore.CYAN+"MILILITER\n",Fore.GREEN+"[6]",Fore.CYAN+"CENTILIER")
            # print("")

            volum = int(input("<=>"))
            if volum == 1:

                print(Fore.RED + '┌─[@Home\AREA\LITER]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "LITER TO M³")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "LITER TO CM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "LITER TO  MM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "LITER TO MILILITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "LITER TO CENTILIER")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"LITER TO M³\n",Fore.GREEN+"[2]",Fore.YELLOW+"LITER TO CM³\n",Fore.GREEN+"[3]",Fore.YELLOW+"LITER TO MM³\n",Fore.GREEN+"[4]",Fore.YELLOW+"LITER TO MILILITER\n",Fore.GREEN+"[5]",Fore.YELLOW+"LITER TO CENTILIER ")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"M³")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"CM³")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"MM³")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"ML")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100,"CL")
            elif volum == 2:

                print(Fore.RED + '┌─[@Home\AREA\M³]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "M³ TO LITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "M³ TO CM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "M³ TO  MM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "M³ TO MILILITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "M³ TO CENTILIER")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"M³ TO LITER\n",Fore.GREEN+"[2]",Fore.YELLOW+"M³ TO CM³\n",Fore.GREEN+"[3]",Fore.YELLOW+"M³ TO MM³\n",Fore.GREEN+"[4]",Fore.YELLOW+"M³ TO MILILITER\n",Fore.GREEN+"[5]",Fore.YELLOW+"M³ TO CENTILIER ")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"L")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"CM³")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000000,"MM³")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"ML")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100000,"CL")
            elif volum == 3:

                print(Fore.RED + '┌─[@Home\AREA\CM³]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "CM³ TO LITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "CM³ TO M³")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "CM³ TO  MM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "CM³ TO MILILITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "CM³ TO CENTILIER")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"CM³ TO LITER\n",Fore.GREEN+"[2]",Fore.YELLOW+"CM³ TO M³\n",Fore.GREEN+"[3]",Fore.YELLOW+"CM³ TO MM³\n",Fore.GREEN+"[4]",Fore.YELLOW+"CM³ TO MILILITER\n",Fore.GREEN+"[5]",Fore.YELLOW+"CM³ TO CENTILIER ")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"L")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"M³")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"MM³")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1,"ML")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.1,"CL")
            elif volum == 4:

                print(Fore.RED + '┌─[@Home\AREA\MM³]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MM³ TO LITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MM³ TO M³")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MM³ TO  CM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "MM³ TO MILILITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "MM³ TO CENTILIER")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MM³ TO LITER\n",Fore.GREEN+"[2]",Fore.YELLOW+"MM³ TO M³\n",Fore.GREEN+"[3]",Fore.YELLOW+"MM³ TO CM³\n",Fore.GREEN+"[4]",Fore.YELLOW+"MM³ TO MILILITER\n",Fore.GREEN+"[5]",Fore.YELLOW+"MM³ TO CENTILIER ")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"L")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000000,"M³")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"CM³")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"ML")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0001,"CL")
            elif volum == 5:

                print(Fore.RED + '┌─[@Home\AREA\ML]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "ML TO LITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "ML TO M³")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "ML TO  CM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "ML TO MM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "ML TO CENTILIER")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"ML TO LITER\n",Fore.GREEN+"[2]",Fore.YELLOW+"ML TO M³\n",Fore.GREEN+"[3]",Fore.YELLOW+"ML TO CM³\n",Fore.GREEN+"[4]",Fore.YELLOW+"ML TO MM³\n",Fore.GREEN+"[5]",Fore.YELLOW+"ML TO CENTILIER ")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"L")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"M³")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1,"CM³")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"MM³")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.1,"CL")
            elif volum == 6:

                print(Fore.RED + '┌─[@Home\AREA\CENTILIERL]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "CENTILIER TO LITER")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "CENTILIER TO M³")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "CENTILIER TO  CM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[4]", Fore.RESET + "CENTILIER TO MM³")
                time.sleep(0.1)
                print(Fore.GREEN + "[5]", Fore.RESET + "CENTILIER TO ML")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"CENTILIER TO LITER\n",Fore.GREEN+"[2]",Fore.YELLOW+"CENTILIER TO M³\n",Fore.GREEN+"[3]",Fore.YELLOW+"CENTILIER TO CM³\n",Fore.GREEN+"[4]",Fore.YELLOW+"CENTILIER TO MM³\n",Fore.GREEN+"[5]",Fore.YELLOW+"CENTILIER TO ML ")
                # print("")

                acov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if acov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.01,"L")
                if acov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*100000,"M³")
                if acov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10,"CM³")
                if acov == 4:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10000,"MM³")
                if acov == 5:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*10,"ML")
        #mass
        elif namecover == '6':
            os.system("cls")
            print(Fore.RED + '┌─[@Home\MASS]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.RESET + "TONNE")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.RESET + "KILOGRAM")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.RESET + "GRAM")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.RESET + "MILIGRAM")
            print("")
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"TONNE\n",Fore.GREEN+"[2]",Fore.CYAN+"KILOGRAM\n",Fore.GREEN+"[3]",Fore.CYAN+"GRAM\n",Fore.GREEN+"[4]",Fore.CYAN+"MILIGRAM")
            # print("")
            mas = int(input("<=>"))
            if mas == 1:


                print(Fore.RED + '┌─[@Home\MASS\TONNE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "TONNE TO KILOGRAM")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "TONNE TO GRAM")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "TONNE TO  MILIGRAM")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"TONNE TO KILOGRAM \n",Fore.GREEN+"[2]",Fore.YELLOW+"TONNE TO GRAM\n",Fore.GREEN+"[3]",Fore.YELLOW+"TONNE TO MILIGRAM")
                # print("")

                macov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if macov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"KG")
                if macov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"G")
                if macov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000000,"MG")
            elif mas == 2:

                print(Fore.RED + '┌─[@Home\MASS\KILOGRAM]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KILOGRAM TO TONNE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KILOGRAM TO GRAM")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KILOGRAM TO  MILIGRAM")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"KILOGRAM TO TONNE \n",Fore.GREEN+"[2]",Fore.YELLOW+"KILOGRAM TO GRAM\n",Fore.GREEN+"[3]",Fore.YELLOW+"KILOGRAM TO MILIGRAM")
                # print("")

                macov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if macov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"T")
                if macov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"G")
                if macov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"MG")
            elif mas == 3:

                print(Fore.RED + '┌─[@Home\MASS\GRAM]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "GRAM TO TONNE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "GRAM TO KILOGRAM")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "GRAM TO  MILIGRAM")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"GRAM TO TONNE \n",Fore.GREEN+"[2]",Fore.YELLOW+"GRAM TO KILOGRAM\n",Fore.GREEN+"[3]",Fore.YELLOW+"GRAM TO MILIGRAM")
                # print("")

                macov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if macov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"T")
                if macov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"KG")
                if macov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"MG")
            elif mas == 4:

                print(Fore.RED + '┌─[@Home\MASS\MILIGRAM]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "MILIGRAM TO TONNE")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "MILIGRAM TO KILOGRAM")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "MILIGRAM TO  GRAM")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"MILIGRAM TO TONNE \n",Fore.GREEN+"[2]",Fore.YELLOW+"MILIGRAM TO KILOGRAM\n",Fore.GREEN+"[3]",Fore.YELLOW+"MILIGRAM TO GRAM")
                # print("")

                macov = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if macov == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000000,"T")
                if macov == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000000,"KG")
                if macov == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"G")
        #speed
        elif namecover == '7':
            os.system("cls")
            print(Fore.RED + '┌─[@Home\SPEED]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.RESET + "METER PER SECOND")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.RESET + "KILOMETER PER HOUR")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.RESET + "KILOMETER PER HOUR")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.RESET + "FOOT PER SECOND")
            print("")
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"METER PER SECOND\n",Fore.GREEN+"[2]",Fore.CYAN+"KILOMETER PER HOUR\n",Fore.GREEN+"[3]",Fore.CYAN+"KILOMETER PER SECOND\n",Fore.GREEN+"[4]",Fore.CYAN+"FOOT PER SECOND")
            # print("")
            scov =int(input("<=>"))

            if scov == 1:

                print(Fore.RED + '┌─[@Home\SPEED\MM/S]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "M/S TO KM/H")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "M/S TO KM/S")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "M/S TO  FPS")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"M/S TO KM/H \n",Fore.GREEN+"[2]",Fore.YELLOW+"M/S TO KM/S\n",Fore.GREEN+"[3]",Fore.YELLOW+"M/S TO FPS")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.6,"KM/H")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.001,"KM/S")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3.2808399,"FPS")
            elif scov == 2:

                print(Fore.RED + '┌─[@Home\SPEED\KM/H]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KM/H TO M/S")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KM/H TO KM/S")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KM/H TO  FPS")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"KM/H TO M/S \n",Fore.GREEN+"[2]",Fore.YELLOW+"KM/H TO KM/S\n",Fore.GREEN+"[3]",Fore.YELLOW+"KM/H TO FPS")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.277777778,"M/S")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.000277777778,"KM/S")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.911344415,"FPS")
            elif scov == 3:

                print(Fore.RED + '┌─[@Home\SPEED\KM/S]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KM/S TO M/S")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KM/S TO KM/H")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KM/S TO  FPS")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"KM/S TO M/S \n",Fore.GREEN+"[2]",Fore.YELLOW+"KM/S TO KM/H\n",Fore.GREEN+"[3]",Fore.YELLOW+"KM/S TO FPS")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1000,"M/S")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3600,"KM/H")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*3280.8399,"FPS")
            elif namecover == 4:

                print(Fore.RED + '┌─[@Home\SPEED\FPS]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "FPS TO M/S")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "FPS TO KM/H")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "FPS TO  KM/S")
                time.sleep(0.1)
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"FPS TO M/S \n",Fore.GREEN+"[2]",Fore.YELLOW+"FPS TO KM/H\n",Fore.GREEN+"[3]",Fore.YELLOW+"FPS TO KM/S")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.3048,"M/S")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.09728,"KM/H")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.0003048,"KM/S")
        elif namecover == '8':
            os.system("cls")
            print(Fore.RED + '┌─[@Home\TR]')
            time.sleep(0.1)
            print(Fore.GREEN + "[1]", Fore.RESET + "CELSIUS")
            time.sleep(0.1)
            print(Fore.GREEN + "[2]", Fore.RESET + "FAHRENHEIT")
            time.sleep(0.1)
            print(Fore.GREEN + "[3]", Fore.RESET + "KELVIN")
            time.sleep(0.1)
            print(Fore.GREEN + "[4]", Fore.RESET + "RANKINE")
            print("")
            # print(Fore.GREEN+"[#]",Fore.RESET+"WHAT IS YOUR UNIT OF MEASUREMENT? : \n\n",Fore.GREEN+"[1]",Fore.CYAN+"CELSIUS\n",Fore.GREEN+"[2]",Fore.CYAN+"FAHRENHEIT\n",Fore.GREEN+"[3]",Fore.CYAN+"KELVIN\n",Fore.GREEN+"[4]",Fore.CYAN+"RANKINE")
            # print("")
            scov = int(input("<=>"))
            if scov == 1:

                print(Fore.RED + '┌─[@Home\TR\CELSIUS]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "CELSIUS TO FAHRENHEIT")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "CELSIUS TO KELVIN")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "CELSIUS TO RANKINE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"CELSIUS TO FAHRENHEIT \n",Fore.GREEN+"[2]",Fore.YELLOW+"CELSIUS TO KELVIN\n",Fore.GREEN+"[3]",Fore.YELLOW+"CELSIUS TO RANKINE")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*33.8,"°F")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*274.15,"K")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*493.47,"°R")
            elif scov == 2:

                print(Fore.RED + '┌─[@Home\TR\FAHRENHEIT]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "FAHRENHEIT TO CELSIUS")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "FAHRENHEIT TO KELVIN")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "FAHRENHEIT TO RANKINE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"FAHRENHEIT TO CELSIUS \n",Fore.GREEN+"[2]",Fore.YELLOW+"FAHRENHEIT TO KELVIN\n",Fore.GREEN+"[3]",Fore.YELLOW+"FAHRENHEIT TO RANKINE")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*-17.2222222,"°C")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*275.927778,"K")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*460.67,"°R")
            elif scov == 3:

                print(Fore.RED + '┌─[@Home\TR\KELVIN]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "KELVIN TO CELSIUS")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "KELVIN TO FAHRENHEIT")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "KELVIN TO RANKINE")
                print("")
                # print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"KELVIN TO CELSIUS \n",Fore.GREEN+"[2]",Fore.YELLOW+"KELVIN TO FAHRENHEIT\n",Fore.GREEN+"[3]",Fore.YELLOW+"KELVIN TO RANKINE")
                # print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*-272.15,"°C")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*-457.87,"°F")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*1.8,"°R")
            elif scov == 4:

                print(Fore.RED + '┌─[@Home\TR\RANKINE]')
                time.sleep(0.1)
                print(Fore.GREEN + "[1]", Fore.RESET + "RANKINE TO CELSIUS")
                time.sleep(0.1)
                print(Fore.GREEN + "[2]", Fore.RESET + "RANKINE TO FAHRENHEIT")
                time.sleep(0.1)
                print(Fore.GREEN + "[3]", Fore.RESET + "RANKINE TO KELVIN")
                print("")
                print(Fore.GREEN+"[#]",Fore.YELLOW+"WICH : \n\n",Fore.GREEN+"[1]",Fore.YELLOW+"RANKINE TO CELSIUS \n",Fore.GREEN+"[2]",Fore.YELLOW+"RANKINE TO FAHRENHEIT\n",Fore.GREEN+"[3]",Fore.YELLOW+"RANKINE TO KELVIN")
                print("")

                spee = int(input("<=>"))

                print("")

                print(Fore.CYAN+"------------------------------------------")

                print(Fore.RED+"[*]CONVERTING........")
                print("")

                time.sleep(1.5)

                if spee == 1:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*-272.594444,"°C")
                if spee == 2:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*-458.67,"°F")
                if spee == 3:
                    print(Fore.LIGHTGREEN_EX+"YOU HAVE",number*0.5555555556,"K")
        else:
            print(Fore.RED+'[!] please Enter your number !!!')
            time.sleep(0.5)
            converting()




        print("")
        print(Fore.YELLOW+"------------------------------------------")
        print(Fore.GREEN+"[#]",Fore.RESET+"ARE YOU NEED MORE SERVICES [1]YES OR [2]NO")
        tagin = int(input("<=>"))
        if tagin ==1:
            converting()
        elif tagin == 2:
            os.system("cls")
            sys.exit()



converting()