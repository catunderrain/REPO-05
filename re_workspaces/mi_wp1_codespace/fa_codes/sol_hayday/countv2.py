

import os






def profit(x):
    return x() - x(1)
# default = 0 is False, else is True
cost = 3
sell = 5
sample = lambda n = 0: sell if (n == 0) else n*(cost) #


# do an lam tu trai hai tren cay duoc cong them tien
# cay trong....................................................................................
wheat = lambda n = 0: 3 if (n == 0) else n*(3) #0
corn = lambda n = 0: 7 if (n == 0) else n*(7) #0
soybean = lambda n = 0: 10 if (n == 0) else n*(10) #0
sugarcane = lambda n = 0: 14 if (n == 0) else n*(14) #0
carrot = lambda n = 0: 7 if (n == 0) else n*(7) #0
indigo = lambda n = 0: 25 if (n == 0) else n*(25) #0
pumpkin = lambda n = 0: 32 if (n == 0) else n*(32) #0
apple = lambda n = 0: 39 if (n == 0) else n*(39) #0
cotton = lambda n = 0: 28 if (n == 0) else n*(28) #0
raspberry = lambda n = 0: 46 if (n == 0) else n*(46) #0
cherry = lambda n = 0: 68 if (n == 0) else n*(68) #0
chilipepper = lambda n = 0: 36 if (n == 0) else n*(36) #0
blackberry = lambda n = 0: 82 if (n == 0) else n*(82) #0
tomato = lambda n = 0: 43 if (n == 0) else n*(43) #0
strawberry = lambda n = 0: 50 if (n == 0) else n*(50) #0
potato = lambda n = 0: 36 if (n == 0) else n*(36) #0
cacao = lambda n = 0: 86 if (n == 0) else n*(86) #0
honeycomb = lambda n = 0: 68 if (n == 0) else n*(68) #0
# khoang san..........................................................................................
silverore = lambda n = 0: 18 if (n == 0) else n*(0) #18
goldore = lambda n = 0: 24 if (n == 0) else n*(0) #24
platinumore = lambda n = 0: 32 if (n == 0) else n*(0) #32
coal = lambda n = 0: 10 if (n == 0) else n*(0) #10
ironore = lambda n = 0: 14 if (n == 0) else n*(0) #14
diamond = lambda n = 0: 0 if (n == 0) else n*(0) #0
# fish.......................................................................................
fishfillet = lambda n = 0: 54 if (n == 0) else n*(0) #54
# thuc an........................................................................................
chickenfeed = lambda n = 0: 7 if (n == 0) else n*(corn(1) + wheat(2)) #-6
cowfeed = lambda n = 0: 14 if (n == 0) else n*(corn(1) + soybean(2)) #-13
pigfeed = lambda n = 0: 14 if (n == 0) else n*(carrot(2) + soybean(1)) #-10
sheepfeed = lambda n = 0: 14 if (n == 0) else n*(soybean(1) + wheat(3)) #-5
goatfeed = lambda n = 0: 14 if (n == 0) else n*(carrot(2) + corn(1) + wheat(1)) #-10
wheatbundle = lambda n = 0: 50 if (n == 0) else n*(wheat(75)) #-175
meatbucket = lambda n = 0: 72 if (n == 0) else n*(fishfillet(3) + carrot(5)) #37
# san pham trung gian................................................................................
egg = lambda n = 0: 18 if (n == 0) else n*(chickenfeed(1)) #5
bread = lambda n = 0: 21 if (n == 0) else n*(wheat(3)) #12
milk = lambda n = 0: 32 if (n == 0) else n*(cowfeed(1)) #5
cream = lambda n = 0: 50 if (n == 0) else n*(milk(1)) #23
brownsugar = lambda n = 0: 32 if (n == 0) else n*(sugarcane(1)) #18
butter = lambda n = 0: 82 if (n == 0) else n*(milk(2)) #28
bacon = lambda n = 0: 50 if (n == 0) else n*(pigfeed(1)) #26
cheese = lambda n = 0: 122 if (n == 0) else n*(milk(3)) #41
whitesugar = lambda n = 0: 50 if (n == 0) else n*(sugarcane(2)) #22
wool = lambda n = 0: 54 if (n == 0) else n*(sheepfeed(1)) #35
syrup = lambda n = 0: 90 if (n == 0) else n*(sugarcane(4)) #34
cottonfabric = lambda n = 0: 108 if (n == 0) else n*(cotton(3)) #24
silverbar = lambda n = 0: 147 if (n == 0) else n*(silverore(3)) #147
goldbar = lambda n = 0: 180 if (n == 0) else n*(goldore(3)) #180
platinumbar = lambda n = 0: 205 if (n == 0) else n*(platinumore(3)) #205
goatmilk = lambda n = 0: 64 if (n == 0) else n*(goatfeed(1)) #40
goatcheese = lambda n = 0: 162 if (n == 0) else n*(goatmilk(2)) #114
refinedcoal = lambda n = 0: 108 if (n == 0) else n*(coal(3)) #108
ironbar = lambda n = 0: 129 if (n == 0) else n*(ironore(3)) #129
honey = lambda n = 0: 154 if (n == 0) else n*(honeycomb(2)) #18
# san pham tieu thu....................................................................................
cornbread = lambda n = 0: 72 if (n == 0) else n*(corn(2) + egg(2)) #32
popcorn = lambda n = 0: 32 if (n == 0) else n*(corn(2)) #18
pancake = lambda n = 0: 108 if (n == 0) else n*(brownsugar(1) + egg(3)) #55
cookie = lambda n = 0: 104 if (n == 0) else n*(brownsugar(1) + egg(2) + wheat(2)) #58
baconandeggs = lambda n = 0: 201 if (n == 0) else n*(bacon(2) + egg(4)) #101
carrotpie = lambda n = 0: 82 if (n == 0) else n*(carrot(3) + egg(1) + wheat(2)) #42
pumpkinpie = lambda n = 0: 158 if (n == 0) else n*(egg(1)+ pumpkin(3) + wheat(2)) #43
butteredpopcorn = lambda n = 0: 126 if (n == 0) else n*(butter(1) + corn(2)) #58
sweater = lambda n = 0: 151 if (n == 0) else n*(wool(2)) #113
baconpie = lambda n = 0: 219 if (n == 0) else n*(bacon(3) + egg(1) + wheat(2)) #128
hamburger = lambda n = 0: 180 if (n == 0) else n*(bacon(2) + bread(2)) #114
raspberrymuffin = lambda n = 0: 140 if (n == 0) else n*(egg(1) + raspberry(2) + wheat(2)) #29
bluewoollyhat = lambda n = 0: 111 if (n == 0) else n*(indigo(1) + wool(1)) #67
cottonshirt = lambda n = 0: 241 if (n == 0) else n*(cottonfabric(2)) #73
bluesweater = lambda n = 0: 208 if (n == 0) else n*(indigo(2) + wool(2)) #120
carrotcake = lambda n = 0: 165 if (n == 0) else n*(brownsugar(1) + butter(1) + carrot(2)) #83
woolychaps = lambda n = 0: 309 if (n == 0) else n*(cottonfabric(1) + wool(3)) #168
creamcake = lambda n = 0: 219 if (n == 0) else n*(cream(1) + whitesugar(1) + wheat(5)) #149
redberrycake = lambda n = 0: 255 if (n == 0) else n*(cherry(2) + milk(1) + egg(1) + raspberry(1)) #33
cheesecake = lambda n = 0: 284 if (n == 0) else n*(cheese(1) + cookie(1)) #157
chilipopcorn = lambda n = 0: 122 if (n == 0) else n*(chilipepper(2) + corn(2)) #36
violetdress = lambda n = 0: 327 if (n == 0) else n*(cottonfabric(2) + indigo(1) + raspberry(1)) #88
blackberrymuffin = lambda n = 0: 226 if (n == 0) else n*(blackberry(2) + egg(2) + wheat(1)) #33
carrotjuice = lambda n = 0: 46 if (n == 0) else n*(carrot(3)) #25
fishburger = lambda n = 0: 226 if (n == 0) else n*(bread(2) + chilipepper(1) + fishfillet(2)) #172 
applepie = lambda n = 0: 270 if (n == 0) else n*(apple(3) + egg(1) + syrup(1) + wheat(2)) #78
fishpie = lambda n = 0: 226 if (n == 0) else n*(egg(1) + fishfillet(3) + wheat(2)) #207
applejuice = lambda n = 0: 129 if (n == 0) else n*(apple(2)) #51
vanillaicecream = lambda n = 0: 172 if (n == 0) else n*(cream(1) + milk(1) + whitesugar(1)) #90
roastedtomatoes = lambda n = 0: 118 if (n == 0) else n*(tomato(2)) #32
cherryjuice = lambda n = 0: 216 if (n == 0) else n*(cherry(2)) #80
tomatojuice = lambda n = 0: 162 if (n == 0) else n*(tomato(3)) #33
berryjuice = lambda n = 0: 205 if (n == 0) else n*(blackberry(1) + raspberry(1)) #77
pizza = lambda n = 0: 190 if (n == 0) else n*(cheese(1) + tomato(1) + wheat(2)) #60
cherrypopsicle = lambda n = 0: 352 if (n == 0) else n*(cherryjuice(1) + syrup(1)) #160
fetapie = lambda n = 0: 223 if (n == 0) else n*(egg(1) + goatcheese(1) + wheat(2)) #156
strawberryicecream = lambda n = 0: 331 if (n == 0) else n*(cream(1) + milk(1) + strawberry(3) + whitesugar(1)) #99
strawberrycake = lambda n = 0: 316 if (n == 0) else n*(cream(1) + strawberry(2) + wheat(3) + whitesugar(1)) #152
bakedpotato = lambda n = 0: 298 if (n == 0) else n*(cheese(1) + chilipepper(1) + cream(1) + potato(2)) #82
applejam = lambda n = 0: 219 if (n == 0) else n*(apple(3)) #102
chocalatecake = lambda n = 0: 320 if (n == 0) else n*(brownsugar(1) + butter(1) + cacao(2)) #80
casserole = lambda n = 0: 367 if (n == 0) else n*(bacon(2) + cheese(1) + egg(2) + potato(2)) #140
raspberryjam = lambda n = 0: 252 if (n == 0) else n*(raspberry(3)) #114
spicypizza = lambda n = 0: 226 if (n == 0) else n*(cheese(1) + chilipepper(1) + tomato(1) + wheat(2)) #60
blackberryjam = lambda n = 0: 388 if (n == 0) else n*(blackberry(3)) #142
potatofetacake = lambda n = 0: 309 if (n == 0) else n*(egg(4) + goatcheese(1) + potato(1)) #173
cherryjam = lambda n = 0: 334 if (n == 0) else n*(cherry(3)) #130
bracelet = lambda n = 0: 514 if (n == 0) else n*(goldbar(1) + silverbar(2)) #514
potatobread = lambda n = 0: 284 if (n == 0) else n*(butter(1) + egg(3) + potato(2) + whitesugar(1)) #91
shepherdspie = lambda n = 0: 280 if (n == 0) else n*(bacon(2) + carrot(2) + potato(2) + pumpkin(2)) #82
chocalateicecream = lambda n = 0: 342 if (n == 0) else n*(cream(1) + cacao(2) + milk(1) + whitesugar(1)) #88
necklace = lambda n = 0: 727 if (n == 0) else n*(goldbar(1) + platinumbar(1) + silverbar(2)) #727
honeypopcorn = lambda n = 0: 360 if (n == 0) else n*(corn(2) + honey(2)) #74
diamondring = lambda n = 0: 824 if (n == 0) else n*(diamond(1) + goldbar(2) + platinumbar(2)) #824
fishandchips = lambda n = 0: 244 if (n == 0) else n*(fishfillet(2) + potato(3)) #136
ironbracelet = lambda n = 0: 658 if (n == 0) else n*(ironbar(2) + refinedcoal(2) + silverbar(1)) #658 NOTE
# print...................................................................................................
os.system('cls')
x = fishandchips
print(f'Sell: +{x()}\nx1: -{x(1)}\nx2:-{x(2)}\nProfit: {profit(x)}')
