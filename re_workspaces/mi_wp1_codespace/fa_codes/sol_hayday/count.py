

#x = 0 : mua
#x = 1 : ban

def profit(x):
    return x(1) - x(0)

# farm -------------------------------------------------------------------------------  
def corn(x):
    if x == 0:
        return 7
    else:
        return 7

def tomato(x):
    if x == 0:
        return 43
    else:
        return 43
    
def wheat(x):
    if x == 0:
        return 3
    else:
        return 3
    
def soybean(x):
    if x == 0:
        return 10
    else:
        return 10

def chilipepper(x):
    if x == 0:
        return 36
    else:
        return 36
    
def potato(x):
    if x == 0:
        return 36
    else:
        return 36
    
def sugarcane(x):
    if x == 0:
        return 14
    else:
        return 14
    
def blackberry(x):
    if x == 0:
        return 82
    else:
        return 82
    
def carrot(x):
    if x == 0:
        return 7
    else:
        return 7
    
def strawberry(x):
    if x == 0:
        return 50
    else:
        return 50
    
def cacao(x):
    if x == 0:
        return 86
    else:
        return 86
    
def cherry(x):
    if x == 0:
        return 68
    else:
        return 68
    
def raspberry(x):
    if x == 0:
        return 46
    else:
        return 46
    
def pumpkin(x):
    if x == 0:
        return 32
    else:
        return 32
# foods --------------------------------------------------------------------------
def thucanchobo(x):
    if x == 0:
        return corn(0) + 2*soybean(0)
    else:
        return 14
    
def thucanchoga(x):
    if x == 0:
        return corn(0) + 2*wheat(0)
    else:
        return 7
    
def thucanchoheo(x):
    if x == 0:
        return 2*carrot(0) + soybean(0)
    else:
        return 14
    
def thucanchode(x):
    if x == 0:
        return 2*carrot(0) + corn(0) + wheat(0)
    else:
        return 14
# animals ------------------------------------------------------------------------
def egg(x):
    if x == 0:
        return thucanchoga(0)
    else:
        return 18
    
def fish(x):
    if x == 0:
        return 54
    else:
        return 54
    
def bacon(x):
    if x == 0:
        return thucanchoheo(0)
    else:
        return 50
# primary ---------------------------------------------------------------------------------------   
def milk(x):
    if x == 0:
        return thucanchobo(0)
    else:
        return 32
    
def goatmilk(x):
    if x == 0:
        return thucanchode(0)
    else:
        return 64
    
def whitesugar(x):
    if x == 0:
        return 2*sugarcane(0)
    else:
        return 50
    
    
def cheese(x):
    if x == 0:
        return 3*milk(0)
    else:
        return 122
    
def butter(x):
    if x == 0:
        return 2*milk(0)
    else:
        return 82

def cream(x):
    if x == 0:
        return milk(0)
    else:
        return 50
    
def brownsugar(x):
    if x == 0:
        return sugarcane(0)
    else:
        return 32
    
def bread(x):
    if x == 0:
        return 3*wheat(0)
    else:
        return 21
    
def goatcheese(x):
    if x == 0:
        return 2*goatmilk(0)
    else:
        return 162
# product -------------------------------------------------------------------------------------   
def pizza(x): # 60
    if x == 0:
        return cheese(0) + tomato(0) + 2*wheat(0)
    else:
        return 190

def pizzacay(x): #60
    if x == 0:
        return cheese(0) + chilipepper(0) + tomato(0) + 2*wheat(0)
    else:
        return 226

def banhmikhoaitay(x): #91
    if x == 0:
        return butter(0) + 3*egg(0) + 2*potato(0) + whitesugar(0)
    else:
        return 284


def muffinmamxoitim(x):  #33
    if x == 0:
        return 2*blackberry(0) + 2*egg(0) + wheat(0)
    else:
        return 226
    
# bbq

def khoaitaybolo(x): #82    
    if x == 0:
        return cheese(0) + chilipepper(0) + cream(0) + 2*potato(0)
    else:
        return 298
    
def cavakhoaitaychien(x): #136--
    if x == 0:
        return 2*fish(0)*0 + 3*potato(0)
    else:
        return 244  


def banhkep(x): #55
    if x == 0:
        return brownsugar(0) + 3*egg(0)
    else:
        return 108
    
def thitxongkhoivatrungran(x): #114
    if x == 0:
        return 2*bacon(0) + 3*egg(0)
    else:
        return 201
    
def hamburger(x): #56
    if x == 0:
        return 2*bacon(0) + 2*bread(0)
    else:
        return 122
    
def burgerca(x): #64
    if x == 0:
        return 2*bread(0) + chilipepper(0) +2*fish(0)
    else:
        return 226

def cachuanuong(x): #77
    if x == 0:
        return 2*tomato(0)
    else:
        return 118

# cake oven
def banhkemdautay(x): #154
    if x == 0:
        return cream(0) + 2*strawberry(0) + 3*wheat(0) + whitesugar(0)
    else:
        return 316
    
def banhkemsocola(x): #80
    if x == 0:
        return brownsugar(0) + butter(0) + 2*cacao(0)
    else:
        return 320

def banhfetakhoaitay(x): #173
    if x == 0:
        return 4*egg(0) + goatcheese(0) + potato(0)
    else:
        return 309

def banhkemcarot(x): #83
    if x == 0:
        return brownsugar(0) + butter(0) + 2*carrot(0)
    else:
        return 165

def banhkem(x): #149
    if x == 0:
        return cream(0) + whitesugar(0) + 5*wheat(0)
    else:
        return 219
    

def banhkemdoquamong(x): #33
    if x == 0:
        return 2*cherry(0) + egg(0) + milk(0) + raspberry(0)
    else:
        return 255
    

#pie oven

def banhphomaide(x): #156
    if x == 0:
        return egg(0) + goatcheese(0) + 2*wheat(0)
    else:
        return 223
    
def monham(x): #140
    if x == 0:
        return 2*bacon(0) + cheese(0) + 2*egg(0) + 2*potato(0)
    else:
        return 367


def banhkhoaitaythitnghien(x): #82
    if x == 0:
        return 2*(bacon(0) + carrot(0) + potato(0) + pumpkin(0))
    else:
        return 280

def banhthitxongkhoi(x): #128
    if x == 0:
        return 3*bacon(0) + egg(0) + 2*wheat(0)
    else:
        return 219

def banhnhanca(x):#45
    if x == 0:
        return egg(0) + 3*fish(0) +  2*wheat(0)
    else:
        return 226
    
#popcorn

def baprangbo(x): #58
    if x == 0:
        return butter(0) + 2*corn(0)
    else:
        return 126
    
def bongngocay(x): #36
    if x == 0:
        return 2*(chilipepper(0) + corn(0))
    else:
        return 122
  
#jam
def mutanhdao(x): #123
    if x == 0:
        return 3*cherry(0)
    else:
        return 327
    
def mutmamxoitim(x): #142
    if x == 0:
        return 3*blackberry(0)
    else:
        return 388
    
def mutmamxoido(x): #114
    if x == 0:
        return 3*raspberry(0)
    else:
        return 252

x = banhmikhoaitay
print(x(0))
print(profit(x))