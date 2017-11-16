# Liczebniki:
zero = lambda f : lambda x : x
one = lambda f : lambda x : f(x)
two = lambda f : lambda x : f(f(x))

# Przydatne funkcje z Zad1:
def Compose1(f,g):
    return lambda x : f(g(x))
Compose2 = lambda f : lambda g : lambda x : f(g(x))
def Multifun(f,n):
    if n == 1 :
        return f
    else:
        return Compose1(f,Multifun(f,n-1))
#       return Compose2(f)(Multifun (f,n-1))

# Konwersje na liczebniki:
def IntToChurch(n):
    if n == 0 :
        return zero
    else :
        return lambda f : lambda x : Multifun(f,n)(x)
#       return Succ(IntToChurch(n-1))
ChurchToInt = lambda church : church(lambda x : x+1)(0)
# Poprzednik i nastepnik
Succ = lambda church : lambda f : lambda x : f(church(f)(x))
Pred = lambda church : lambda f : lambda x : church(lambda g : lambda h : h(g(f)))(lambda u : x)(lambda u : u)
# wykonuje n-1 razy funkcje f, poniewaz pierwsze wykonanie(lambda u : x) jest bezużyteczne i zwraca x 

# Alternatywny sposob konwersji:
def IntToChurchSucc(n):
    if n == 0 :
        return zero
    else :
        return Succ(IntToChurch(n-1))

# Działania na liczebnikach:
Add = lambda skladnik1 : lambda skladnik2 : skladnik1 (Succ)(skladnik2)
Sub = lambda odjemna : lambda odjemnik : odjemnik (Pred)(odjemna)
Mul = lambda czynnik1 : lambda czynnik2 : lambda f : czynnik1 (czynnik2(f))
Exp = lambda podstawa : lambda wykladnik : wykladnik (podstawa)

# Wartości logiczne:
true = lambda t: lambda f: t
false = lambda t: lambda f: f
Not = lambda a: a(false)(true)

# Konwersja na wartosci logiczne:
def BoolToChurch(a): 
    if a :
        return true
    else :
        return false
ChurchToBool = lambda a : a(True)(False)

# Operatory logiczne:
And = lambda a: lambda b: a(b)(a)	
Or = lambda a: lambda b: a(a)(b)
XOr = lambda a: lambda b: a(Not(b))(b)

NAnd = lambda a: lambda b: Not (And(a)(b))
NOr = lambda a: lambda b: Not (Or(a)(b))
NXOr = lambda a: lambda b: Not (XOr(a)(b))

# Operatory porównania i funkcje warunkowe:
If = lambda warunek : lambda a : lambda b : warunek(a)(b)

IsZero = lambda church : (church (lambda x : false))(true)
# dla church != zero, nastapi kilkukrotne zlozenie funkcji zwracajacej false, ktora dla argumentu true zwroci false
# dla church == zero, church od funkcji zwroci funkcje identycznosciowa, ktora dla argumentu true zwroci true
Equal = lambda a : lambda b : And(IsZero(Sub(a)(b)))(IsZero(Sub(b)(a)))
NotEqual = lambda a : lambda b : Not(Eq(a)(b))
GreaterOrEqual = lambda a : lambda b : IsZero(Sub(b)(a))
LessOrEqual = lambda a : lambda b : IsZero(Sub(a)(b))
Greater = lambda a : lambda b : Not(LessOrEqual(a)(b))
Less = lambda a : lambda b : Not(GreaterOrEqual(a)(b))

# Para:
Pair = lambda left : lambda right : lambda f : f(left)(right)
Left = lambda Pair : Pair (true)
Right = lambda Pair : Pair (false)

# Lista:
Empty = Pair(true)(true)
AddToList = lambda element : lambda lista : Pair(false)(Pair(element)(lista))
IsEmpty = Left
First = lambda lista : Left(Right(lista))
Rest = lambda lista : Right(Right(lista))

# Konwersja listy:
def ListToTab(lista):
    tab = []
    while ChurchToBool(Not(IsEmpty(lista))) :
        tab.append(ChurchToInt(First(lista)))
        lista=Rest(lista)
    return tab

# Pomocniki w rekurencji:
Y = lambda f:lambda x:f(x(x))(lambda x:f(x(x)))
Z = lambda church : (lambda x: church(lambda y: x(x)(y)))(lambda x: church(lambda y: x(x)(y)))

# Silnia:
Fact = Z (lambda FactZ : lambda church : \
        (If (IsZero(church)) \
            (one) \
            (lambda x : Mul(church)(FactZ(Pred(church)))(x)) \
         )     
)
GenFact = Z (lambda GenFactZ : lambda ile : \
        (If(IsZero(ile)) \
             (AddToList(one)(Empty)) \
             (lambda x : AddToList(Fact(ile))(GenFactZ(Pred(ile)))(x)) \
        )
)
# Ciag Fibonaciego:
Fib = Z (lambda FibZ : lambda church : \
        (If (LessOrEqual(church)(two)) \
            (one) \
            (lambda x : (Add(FibZ(Pred(church)))(FibZ(Pred(Pred(church)))))(x)) 
         ) 
)
# Algorytm NWD Euklidesa z definicja dla zera:
Nwd = Z (lambda NwdZ : lambda church1 : lambda church2 : \
        (If (Or(IsZero(church1))(IsZero(church2))) \
            (If (IsZero(church1)) \
                (church1) \
                (church2) \
             )
            (If (Equal(church1)(church2)) \
                (church1) \
                (If(LessOrEqual(church1)(church2)) \
                    (lambda x : NwdZ(Sub(church2)(church1))(church1)(x)) \
                    (lambda x : NwdZ(Sub(church1)(church2))(church2)(x)) \
                ) 
            ) 
        )
)
# Modulo:
Mod = Z (lambda ModZ : lambda dzielna : lambda dzielnik : \
        (If (Less(dzielna)(dzielnik)) \
            (dzielna) \
            (lambda x: (ModZ(Sub(dzielna)(dzielnik))(dzielnik))(x))
        )
)
# Pierwiastek całkowity funkcja wewnetrzna:
IntEl = Z (lambda IntElZ : lambda liczba : lambda podstawa : lambda skladnik : lambda suma : \
        (If(Less(liczba)(Add(suma)(skladnik))) \
            (podstawa) \
            (lambda x : IntElZ(liczba)(Succ(podstawa))(Add(skladnik)(two))(Add(skladnik)(suma))(x)) \
        )
)
# Pierwiastek całkowity funkcja obslugujaca:
IntElement = lambda church : IntEl(church)(zero)(one)(zero)
# Gen ciag wyrazow
Gen = Z (lambda GenZ : lambda f : lambda ile : \
        (If(IsZero(ile)) \
             (AddToList(f(one))(Empty)) \
             (lambda x : AddToList(f(ile))(GenZ(f)(Pred(ile)))(x)) \
        )
)

# Prezentacja wynikow:
eight =IntToChurch(8)
four = IntToChurch(4)
Const = 12

print("Silnia:")
for x in range(8):
    print("   ",x,"!=",ChurchToInt(Fact(IntToChurch(x))))
print(" ","Ciag wyrazow:")
print("   ",ListToTab(Gen(Fact)(IntToChurch(7))))

print("Ciag Fibonaciego:")
for x in range(Const):
    print("   ","Fib[",x,"] =",ChurchToInt(Fib(IntToChurch(x))))
print(" ","Ciag wyrazow:")
print("   ",ListToTab(Gen(Fib)(IntToChurch(Const))))

print("NWD Euklidesa:")
for x in range(Const):
    print("   ","NWD(",x,",",ChurchToInt(four),")=",ChurchToInt(Nwd(IntToChurch(x))(four)))
print(" ","Ciag wyrazow dla dzielnika 4:")
print("   ",ListToTab(Gen(Nwd(four))(IntToChurch(Const)))) 

print("Modulo:")
for x in range(Const):
    print("   ",x,"mod",ChurchToInt(four),"=",ChurchToInt(Mod(IntToChurch(x))(four)))
print(" ","Ciag wyrazow dla dzielnika 4:")
print("   ",ListToTab(Gen(lambda x : Nwd(x)(four))(IntToChurch(Const))))

print("Pierwiastek calkowitoliczbowy:")
for x in range(Const):
    print("   ",x," = ",ChurchToInt(IntElement(IntToChurch(x))),"^2")
print(" ","Ciag wyrazow:")
print("   ",ListToTab(Gen(IntElement)(IntToChurch(Const))))




