from typesList import Types
from tree import Tree

def analysis(commands):

    marks = list()

    for key, value in commands.items():
        if value[0][1] == Types.newMark:
            if len(value.items()) == 1:
                print("Creating tree with name " + value[0][0])
                marks.append(Tree(name=value[0][0], value=key, var=False))
            else:
                print("Ошибка в строке " + str(key))
                print("После объявления метки не должно быть операндов")
                return 0, marks

        elif value[0][1] == Types.newVariable:
            if len(value.items()) == 1:
                print("Creating tree with name " + value[0][0])
                if commands[key+1][0][1] == Types.db:
                    varValue = ""
                    for key, i in commands[key+1].items():
                        if key > 0:
                            varValue += i[0]
                            varValue += " "
                    collection = list()
                    for i in range(0,len(varValue.split('"'))):
                        if i % 2 == 1:
                            for j in varValue.split('"')[i]:
                                collection.append(j)
                        elif varValue.split('"')[i] != " ":
                            for j in varValue.split('"')[i].split(","):
                                if len(j) > 0 and j != " ":
                                    collection.append(int(j, 16))
                    marks.append(Tree(name=value[0][0], value=collection, var=True))
                else:
                    marks.append(Tree(name=value[0][0], value=key+1, var=True))
            else:
                print("Ошибка в строке " + str(key))
                print("После объявления переменной не должно быть операндов")
                return 0, marks

        elif value[0][1] == Types.mov:
            if len(value.items()) != 3:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.variable:
                print("Ошибка в строке " + str(key))
                print("После mov должна следовать переменная")
                return 0, marks
            if value[2][1] != Types.variable and value[2][1] != Types.pointer and value[2][1] != Types.number:
                print("Ошибка в строке " + str(key))
                print("Нельзя выполнить mov с типом второго операнда " + str(value[2][1]))
                return 0, marks

        elif value[0][1] == Types.cmp:
            if len(value.items()) != 3:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.variable:
                print("Ошибка в строке " + str(key))
                print("После cmp должна следовать переменная")
                return 0, marks
            if value[2][1] != Types.variable and value[2][1] != Types.number:
                print("Ошибка в строке " + str(key))
                print("Нельзя выполнить cmp с типом второго операнда " + str(value[2][1]))
                return 0, marks

        elif value[0][1] == Types.je:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.mark:
                print("Ошибка в строке " + str(key))
                print("После je должна следовать метка")
                return 0, marks

        elif value[0][1] == Types.push:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.variable:
                print("Ошибка в строке " + str(key))
                print("После push должна следовать переменная")
                return 0, marks

        elif value[0][1] == Types.inter:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.number:
                print("Ошибка в строке " + str(key))
                print("После int должно следовать число")
                return 0, marks

        elif value[0][1] == Types.pop:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.variable:
                print("Ошибка в строке " + str(key))
                print("После pop должна следовать переменная")
                return 0, marks

        elif value[0][1] == Types.inc:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.variable:
                print("Ошибка в строке " + str(key))
                print("После inc должна следовать переменная")
                return 0, marks

        elif value[0][1] == Types.dec:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.variable:
                print("Ошибка в строке " + str(key))
                print("После dec должна следовать переменная")
                return 0, marks

        elif value[0][1] == Types.jmp:
            if len(value.items()) != 2:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks
            if value[1][1] != Types.mark:
                print("Ошибка в строке " + str(key))
                print("После jmp должна следовать метка")
                return 0, marks

        elif value[0][1] == Types.db:
            if len(value.items()) == 1:
                print("Ошибка в строке " + str(key))
                print("Неправильное количество операндов")
                return 0, marks

        else:
            print("Ошибка в строке " + str(key))
            print("Неподходящий тип оператора " + str(value[0][1]))
            return 0, marks
    print("Анализатор не нашёл ошибок")
    return 1, marks
