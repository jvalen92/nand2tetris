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
        pc=pc+1

        if x.label:
            sym=x.pcLabel()
            if sym in symbol:
                break
            else:
                symbol[sym] = pc







def read():
    pc = 0
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

        if x.getLabel:
            #print(x.pcLabel(),x.getIndex)
            pc=pc-1
        pc=pc+1


#variables empiezan en la pos 16
varRAM=16
l2 = []
symbol={}
fillSymbol()
print(symbol)
read()






