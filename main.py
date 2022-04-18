from scaner import scanFile
from analysis import analysis
from typesList import Types
from tree import Tree
from interpretator import interpret

debug = False

fileName = "code.txt"

commands = scanFile(fileName)

result, marks = analysis(commands)

if result != 0:

    regs = [Tree(name="ax", value=0, var=True), Tree(name="bx", value=0, var=True), Tree(name="al", value=0, var=True), Tree(name="sp", value=list(), var=True), Tree(name="ah", value=0, var=True), Tree(name="zf", value=0, var=True)]

    interpret(commands, marks, regs, debug)
