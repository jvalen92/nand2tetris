comp={}
dest={}
jump={}

#bit [12] on

comp["0"]="101010"
comp["1"]="111111"
comp["-1"]="111010"
comp["D"]="001100"
comp["M"]="110000"
comp["!D"]="001101"
comp["!M"]="110001"
comp["-D"]="001111"
comp["-M"]="110011"
comp["D+1"]="011111"
comp["M+1"]="110111"
comp["D-1"]="001110"
comp["M-1"]="110010"
comp["D+M"]="000010"
comp["D-M"]="010011"
comp["M-D"]="000111"
comp["D&M"]="000000"
comp["D|M"]="010101"

#bit[12] off
comp["A"]="110000"
comp["!D"]="001101"
comp["!A"]="110001"
comp["-D"]="001111"
comp["-A"]="110011"
comp["D+1"]="011111"
comp["A+1"]="110111"
comp["D-1"]="001110"
comp["A-1"]="110010"
comp["D+A"]="000010"
comp["D-A"]="010011"
comp["A-D"]="000111"
comp["D&A"]="000000"
comp["D|A"]="010101"

#dest [A,D,M,AD,AM,ADM,MD,null]
dest["0"]="000"
dest["M"]="001"
dest["D"]="010"
dest["MD"]="011"
dest["A"]="100"
dest["AM"]="101"
dest["AD"]="110"
dest["AMD"]="111"

jump["null"]="000"
jump["JGT"]="001"
jump["JEQ"]="010"
jump["JGE"]="011"
jump["JLT"]="100"
jump["JNE"]="101"
jump["JLE"]="110"
jump["JMP"]="111"


cadena='M'

if cadena in comp:
    print(comp[cadena])
