from typesList import Types
from tree import Tree
import os

def interpret(commands, marks, regs, debug):
    os.system("color")
    i = 0
    while i < len(commands.items()):
        if commands[i][0][1] == Types.newMark or commands[i][0][1] == Types.newVariable:
            found = False
            for j in marks:
                if j.name == commands[i][0][0]:
                    found = True
            if found == False:
                print("Не найдена метка " + commands[i][0][0])
                return 0

        elif commands[i][0][1] == Types.mov:
            found = False
            for k in marks:
                if k.name[:-1] == commands[i][1][0][:-1]:
                    found = True
                    if commands[i][2][1] == Types.number:
                        k.value = int(commands[i][2][0], 16)
                        if debug == True:
                            print("Переменной " + k.name + " присвоено значение " + str(k.value))
                    elif commands[i][2][1] == Types.pointer:
                        for j in regs:
                            if j.name == commands[i][2][0][1:-1]:
                                if type(j.value) == type(tuple()):
                                    k.value = j.value[0].value[j.value[1]]
                                else:
                                    k.value = j.value
                                if debug == True:
                                    print("Переменной " + k.name + " присвоено значение " + str(k.value))
                    elif commands[i][2][1] == Types.variable:
                        found2 = False
                        for j in regs:
                            if j.name == commands[i][2][0]:
                                found2 = True
                                k.value = j.value
                                if debug == True:
                                    print("Переменной " + k.name + " присвоено значение " + str(k.value))
                        if found2 == False:
                            for j in marks:
                                if j.name[:-1] == commands[i][2][0]:
                                    found2 = True
                                    k.value = j.value
                                    if debug == True:
                                        print("Переменной " + k.name + " присвоено значение " + str(k.value))
                            if found2 == False:
                                print("Не найдена переменная " + commands[i][2][0])
                                return 0
            if found == False:
                for k in regs:
                    if k.name == commands[i][1][0][:-1]:
                        found = True
                        if commands[i][2][1] == Types.number:
                            k.value = int(commands[i][2][0], 16)
                            if debug == True:
                                print("Переменной " + k.name + " присвоено значение " + str(k.value))
                        elif commands[i][2][1] == Types.pointer:
                            for j in regs:
                                if j.name == commands[i][2][0][1:-1]:
                                    if type(j.value) == type(tuple()):
                                        k.value = j.value[0].value[j.value[1]]
                                    else:
                                        k.value = j.value
                                    if debug == True:
                                        print("Переменной " + k.name + " присвоено значение " + str(k.value))
                        elif commands[i][2][1] == Types.variable:
                            found2 = False
                            for j in regs:
                                if j.name == commands[i][2][0]:
                                    found2 = True
                                    k.value = j.value
                                    if debug == True:
                                        print("Переменной " + k.name + " присвоено значение " + str(k.value))
                            if found2 == False:
                                for j in marks:
                                    if j.name[:-1] == commands[i][2][0]:
                                        found2 = True
                                        if type(j.value) == type(list()):
                                            k.value = (j, 0)
                                        else:
                                            k.value = j.value
                                        if debug == True:
                                            print("Переменной " + k.name + " присвоено значение " + str(k.value))
                                if found2 == False:
                                    print("Не найдена переменная " + commands[i][2][0])
                                    return 0
                if found == False:
                    print("Не найдена переменная " + commands[i][1][0][:-1])
                    return 0

        elif commands[i][0][1] == Types.cmp:
            found = False
            for k in marks:
                if k.name[:-1] == commands[i][1][0][:-1]:
                    found = True
                    if commands[i][2][1] == Types.number:
                        if k.value == int(commands[i][2][0], 16):
                            regs[-1].value = 1
                        else:
                            regs[-1].value = 0
                        if debug == True:
                            print("Флагу ZF присвоено значение " + str(regs[-1].value))
                    elif commands[i][2][1] == Types.variable:
                        found2 = False
                        for j in regs:
                            if j.name == commands[i][2][0]:
                                found2 = True
                                if k.value == j.value:
                                    regs[-1].value = 1
                                else:
                                    regs[-1].value = 0
                                if debug == True:
                                    print("Флагу ZF присвоено значение " + str(regs[-1].value))
                        if found2 == False:
                            for j in marks:
                                if j.name[:-1] == commands[i][2][0]:
                                    found2 = True
                                    if k.value == j.value:
                                        regs[-1].value = 1
                                    else:
                                        regs[-1].value = 0
                                    if debug == True:
                                        print("Флагу ZF присвоено значение " + str(regs[-1].value))
                            if found2 == False:
                                print("Не найдена переменная " + commands[i][2][0])
                                return 0
            if found == False:
                for k in regs:
                    if k.name == commands[i][1][0][:-1]:
                        found = True
                        if commands[i][2][1] == Types.number:
                            if k.value == int(commands[i][2][0], 16):
                                regs[-1].value = 1
                            else:
                                regs[-1].value = 0
                            if debug == True:
                                print("Флагу ZF присвоено значение " + str(regs[-1].value))
                        elif commands[i][2][1] == Types.variable:
                            found2 = False
                            for j in regs:
                                if j.name == commands[i][2][0]:
                                    found2 = True
                                    if k.value == j.value:
                                        regs[-1].value = 1
                                    else:
                                        regs[-1].value = 0
                                    if debug == True:
                                        print("Флагу ZF присвоено значение " + str(regs[-1].value))
                            if found2 == False:
                                for j in marks:
                                    if j.name[:-1] == commands[i][2][0]:
                                        found2 = True
                                        if k.value == j.value:
                                            regs[-1].value = 1
                                        else:
                                            regs[-1].value = 0
                                        if debug == True:
                                            print("Флагу ZF присвоено значение " + str(regs[-1].value))
                                if found2 == False:
                                    print("Не найдена переменная " + commands[i][2][0])
                                    return 0
                if found == False:
                    print("Не найдена переменная " + commands[i][1][0][:-1])
                    return 0

        elif commands[i][0][1] == Types.je:
            found = False
            for k in marks:
                if k.name[:-1] == commands[i][1][0]:
                    found = True
                    if regs[-1].value == 1:
                        i = k.value
                        if debug == True:
                            print("Совершён переход на метку " + k.name[:-1])
                        break
            if found == False:
                print("Не найдена метка " + commands[i][1][0])
                return 0

        elif commands[i][0][1] == Types.push:
            found = False
            for k in regs:
                if k.name == commands[i][1][0]:
                    found = True
                    regs[3].value.append(k.value)
                    if debug == True:
                        print("В стек помещено значение регистра " + k.name)
                    break
            if found == False:
                print("Не найден регистр " + commands[i][1][0])
                return 0

        elif commands[i][0][1] == Types.inter:
            if commands[i][1][0] == "0x10":
                if regs[-2].value == int("0x0E", 16):
                    if debug == True:
                        if regs[2].value == int("0xA", 16):
                            print("")
                        else:
                            print("\033[38;5;" + str(regs[1].value % 256) + "m" + str(regs[2].value) + "\033[0m")
                    else:
                        if regs[2].value == int("0xA", 16):
                            print("")
                        else:
                            print("\033[38;5;" + str(regs[1].value % 256) + "m" + str(regs[2].value) + "\033[0m", end="")
            elif commands[i][1][0] == "0x20":
                if debug == True:
                    print("Программа завершена прерыванием 0x20")
                return 1
            else:
                print("Неизвестное прерывание")
                return 0

        elif commands[i][0][1] == Types.pop:
            found = False
            for k in regs:
                if k.name == commands[i][1][0]:
                    found = True
                    k.value = regs[3].value[-1]
                    regs[3].value = regs[3].value[:-1]
                    if debug == True:
                        print("Из стека извлечено значение " + str(k.value) + " в регистр " + k.name)
                    break
            if found == False:
                print("Не найден регистр " + commands[i][1][0])
                return 0

        elif commands[i][0][1] == Types.inc:
            found = False
            for k in regs:
                if k.name == commands[i][1][0]:
                    found = True
                    if type(k.value) == type(tuple()):
                        k.value = (k.value[0], k.value[1] + 1)
                    else:
                        k.value += 1
                    if debug == True:
                        print("Значение регистра " + k.name + " увеличилось до " + str(k.value))
                    break
            if found == False:
                print("Не найден регистр " + commands[i][1][0])
                return 0

        elif commands[i][0][1] == Types.dec:
            found = False
            for k in regs:
                if k.name == commands[i][1][0]:
                    found = True
                    if type(k.value) == type(tuple()):
                        k.value = (k.value[0], k.value[1] - 1)
                    else:
                        k.value -= 1
                    if debug == True:
                        print("Значение регистра " + k.name + " уменьшилось до " + str(k.value))
                    break
            if found == False:
                print("Не найден регистр " + commands[i][1][0])
                return 0

        elif commands[i][0][1] == Types.jmp:
            found = False
            for k in marks:
                if k.name[:-1] == commands[i][1][0]:
                    found = True
                    i = k.value
                    if debug == True:
                        print("Совершён переход на метку " + k.name[:-1])
                    break
            if found == False:
                print("Не найдена метка " + commands[i][1][0])
                return 0

        i += 1
    return 1
