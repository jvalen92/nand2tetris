class Instrucion:
    def __init__(self, arg, i):
        self.ins = arg
        self.index = i
        self.typeA = False
        self.label = False
        self.out = "0000000000000000"

        if self.ins.find('@') != int(-1):
            self.typeA = True

        if self.ins.find('(') != int(-1):
            if self.ins.find(')') != int(-1):
                self.label=True

    @property
    def getLabel(self):
        return self.label

    def pcLabel(self):
        if self.label:
            label=self.ins[1:len(self.ins)-1]
            low=label.lower()
            return low

    def setAut(self,value):
        self._Aout=value

    def setIndex(self,value):
        self._index=value

    @property
    def getOut(self):
        return self.out

    @property
    def getType(self):

        return self.typeA

    @property
    def getIndex(self):
        return self.index

    @property
    def Aout(self):
        #verificar si es tipo A
        if self.typeA:
            #separar la variable del @
            s = self.ins.split('@')
            var=s[1]
            i=0
            #verificar que la variable sea un entero
            for num in var:
                if num.isdigit():
                    i = i + 1
            if len(var)==i:
                #print("es entero")
                var=int(var)
                #en caso de que sea un numero, pasar a binario
                digitos = "0123456789ABCDEF"
                pilaResiduo = []
                while var > 0:
                    residuo = var % 2
                    pilaResiduo.append(residuo)
                    var = var // 2

                nuevaCadena = ""
                while len(pilaResiduo) != 0:
                    nuevaCadena = nuevaCadena + digitos[pilaResiduo.pop()]


                #numero de bits
                i=16-len(nuevaCadena)
                #agruegar ceros a la izquierda para formar los 16 bits
                self.out= self.out[0:i]+nuevaCadena
                #print(len(self.out))
                return self.out

            else:
                #print(var)
                return str(var)


def convertirBase(numeroDecimal,base):
    digitos = "0123456789ABCDEF"

    pilaResiduo = []

    while numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.append(residuo)
        numeroDecimal = numeroDecimal // base

    nuevaCadena = ""
    while len(pilaResiduo) != 0:
        nuevaCadena = nuevaCadena + digitos[pilaResiduo.pop()]

    return nuevaCadena


def write(line):
    archivo=open("Salida.txt","a")
    archivo.writelines(line+'\n')
    archivo.close()

#llenar la tabla se simbolos
def fillSymbol():
    pc = 0
    varRAM = 16
    cout = "111a"

    archivo=open("Entrada.txt","r")
    lineas=archivo.readlines()
    for linea in lineas:

        if linea.find("//") == int(-1) and linea !='\n':
            l2.append(linea)

    print("nueva lista ",l2)
    for linea in l2:
        r=len(linea)
        x=Instrucion(linea[:int(r-1)],pc)

        #si es una instruccion tipo A

        if x.getType:
            if len(x.Aout) < 16:
                #print("no es entero")
                s=linea.split('@')
                #lo que hay despues del @
                sym=s[1][:int(r-2)]
                if sym in symbol:
                    break
                else:
                    symbol[sym]=varRAM
                    varRAM=varRAM+1
            pc = pc + 1





        if x.label:
            sym=x.pcLabel()
            if sym in symbol:
                break
            else:
                symbol[sym] = pc







def read():
    pc = 0
    cout="111a"
    archivo=open("Entrada.txt","r")
    for linea in l2:
        r=len(linea)
        x=Instrucion(linea[:int(r-1)],pc)
        if x.getType:
            if len(x.Aout) < 16:
                if x.Aout in symbol:
                    key = x.Aout
                    var = convertirBase(symbol[key], 2)
                    var = str(var)
                    i = 16 - len(var)
                    bin = x.getOut[0:i] + var
                    print(bin,x.getIndex)

            else:
                print(x.Aout,x.getIndex)
        elif linea.find('=')!= -1:
                sym=linea.split('=')
                c =sym[1][:len(sym[1])-1]
                #print(c)

                if sym[1].find('M') !=-1:
                    cout=cout.replace('a','1')
                else:
                    cout=cout.replace('a','0')

                if c in comp:
                    #print("comp ",comp[c])
                    cout=cout+comp[c]
                    #print("cadena ",cout)
                #print(sym[0])
                if sym[0] in dest:
                    #print("destino ",dest[sym[0]])
                    d= sym[0]
                    cout=cout+dest[d]+"000"
                    #print("cadena ",cout)
                pc=pc+1
                print(cout)
                cout="111a"


        if x.getLabel:
            #print(x.pcLabel(),x.getIndex)
            pc=pc-1
        pc=pc+1


#variables empiezan en la pos 16
varRAM=16
l2 = []
symbol={}
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
fillSymbol()

print(symbol)
read()






