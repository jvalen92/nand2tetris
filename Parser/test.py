class Instrucion:
    def __init__(self, arg, index):
        self.ins = arg
        self.index = 0
        self.typeA = False
        self.label=False
        self.out = "0000000000000000"

        if self.ins.find('@') != int(-1):
            self.typeA = True

        if self.ins.find('(') != int(-1):
            if self.ins.find(')') != int(-1):
                self.label=True

    def setAut(self,value):
        self._Aout=value

    def setLabel(self,value):
        self._label=value

    @property
    def getLabel(self):
        return self.label.lower()

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

    def pcLabel(self):
        if self.label:
            label=self.ins[1:len(self.ins)]
            low=label.lower()



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

"""

a = Instrucion("@loop", 0)
d=Instrucion("(LOOP)",1)
b=Instrucion("@100",2)
c=Instrucion("@i",3)


ins=[a,b,c]
symbol={}
symbol["i"]=16
symbol["loop"]=17
print(symbol)

for x in ins:
    if x.getType:
        if len(x.Aout)<16:
            #print(x.Aout)
            if x.Aout in symbol:
                key=x.Aout
                var=convertirBase(symbol[key],2)
                var=str(var)
                i = 16 - len(var)
                bin=x.getOut[0:i]+var
                print(bin)
        else:
            print(x.Aout)
"""


f=open('Entrada.txt','r')
linea=f.readlines()
f.close()
print ("lista de lineas ",linea)

for l in linea:
    print("en el ciclo")
    if l.find('//') != int(-1):
        print("comentario ",l)
        linea.remove(l)
        print("nueva lista ",linea)
    else:
        print("linea normal ",l)
        s=open("Salida.txt",'a')
        #print(l)
        s.write(l)


print (linea)