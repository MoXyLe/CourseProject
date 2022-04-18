import enum

class Types(enum.Enum):
    newVariable = 1
    variable = 2
    newMark = 3
    mark = 4
    pointer = 5
    number = 6
    string = 7
    mov = 8
    cmp = 9
    je = 10
    push = 11
    db = 12
    inter = 13
    pop = 14
    inc = 15
    jmp = 16
    dec = 17
    error = 100
