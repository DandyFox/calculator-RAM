#import json


def program():    
    return calculator()


def calculator():
    print("RAM Calculator v0.1 by DF")
    
    #with open("data.json", "w") as write_file:
    #    json.dump(data, write_file)

    name = input("Введите название памяти:")
    frequency = int(input("Введите частоту памяти:"))
    question_cl = int(input("Вы будете вводдить данные все вместе (1) или по отдельности (2)?"))

    # name_pefect = "G.SKILL TRIDENT Z 3600MHz CL14"
    # frequency_perfect = 3600
    # cl_perfect = 14 
    # trsd_perfect = 14
    # trp_perfect = 14
    # tras_perfect = 34

    
    
    if question_cl == 1:
        cl_all = input("Введите тайминги, через дефис:")
        cl_all.split("-")
        cl = int(cl_all[1]) 
        trsd = int(cl_all[2])
        trp = int(cl_all[3])
        tras = int(cl_all[4])

    elif question_cl == 2:
        cl = int(input("Введите CL:")) 
        trsd = int(input("Введите tRCD:"))
        trp = int(input("Введите tRP:"))
        tras = int(input("Введите tRAS:"))

    result1=(1/(frequency/2))*1000*cl
    result2=(1/(frequency/2))*1000*trsd
    result3=(1/(frequency/2))*1000*trp
    result4=(1/(frequency/2))*1000*tras

    print("Частота памяти:", frequency,"Mhz")
    print("CL:", cl, "Задержка такта:", round(result1,2),"ns")
    print("tRCD:", trsd, "Задержка такта:", round(result2,2),"ns")
    print("tRP:", trp, "Задержка такта:", round(result3,2),"ns")
    print("tRAS:", tras, "Задержка такта:", round(result4,2),"ns")


    while True:
        answer = input("Попробовать снова (Y/N)?:")
        if answer not in {"y","n","Y","N"}:
            print("Была введена ерунда. Введите корректную команду")
        elif answer == "n" or "N":
            print("Bye!")
            return False
        elif answer == "Y" or "y":
            return program()

program()

    


