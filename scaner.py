from typesList import Types

def scanFile(file):
    f = open(file=file, mode="r+")
    keywords = dict()
    count = 0

    for i in f.readlines():
        if len(i) > 1:
            dictionary = dict()
            count2 = 0
            for j in i[:-1].split(" "):
                dictionary[count2] = (j, findType(j))
                count2 += 1
            keywords[count] = dictionary
            count += 1

    for i in keywords.items():
        print(i)
    f.close()

    return keywords

def findType(command):
    if command[:2] == "@@":
        if command[-1] == ":":
            return Types.newMark
        else:
            return Types.mark
    elif command == "mov":
        return Types.mov
    elif command == "cmp":
        return Types.cmp
    elif command == "je":
        return Types.je
    elif command == "push":
        return Types.push
    elif command == "int":
        return Types.inter
    elif command == "pop":
        return Types.pop
    elif command == "inc":
        return Types.inc
    elif command == "dec":
        return Types.dec
    elif command == "jmp":
        return Types.jmp
    elif command == "db":
        return Types.db
    elif command[0].isdigit():
        return Types.number
    elif command[0] == "[":
        return Types.pointer
    elif command[-1] == ":":
        return Types.newVariable
    elif '"' in command or "'" in command:
        return Types.string
    else:
        return Types.variable
