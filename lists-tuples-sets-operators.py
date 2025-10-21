numeros=[1,2,3]
letras=['a','b','c']
mistura=[1.0,'a', True]
print("lista de numeros:", numeros)
print("lista de letras:", letras)
print("lista de mistura:", mistura)
numeros.append(4)
numeros[0]=99
print("lista alternada:", numeros)
tupla=("What","Who","Where")
print("Tupla:", tupla)
frutas = set (['batata','alface','uva', 'uva'])
print("Set sem duplicados:", frutas)
frutas.add("banana")
print("set após add:", frutas)
conjunto=frozenset(['batata','alface','uva'])
print("frozenset:", conjunto)
a={1,2,3,}
b={3,4,5}
print("\nUnião de a com b:", a|b)
print("Interseção:", a & b)
print("Diferença:", a-b)
x,y=10,5
print:(x==y,x!=y,x>y,x<y,x>=y,x<y)
p,q=True, False
print("\np And q:", p or q)
print("p OR q:", p or q)
print("not p:", not p)
