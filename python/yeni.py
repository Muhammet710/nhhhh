number=[1,2,3,4,5]
x=number.copy()
print(number)
mus=int(input("inter the new number:"))
mus2=int(input("inter the index:"))
number[mus2]=mus
print(x)
print(number)



number=[1,2,3,4,5]
c=number[::-1]
for x in c:
    print(x)



numbers=[[1,2,3],[4,5,6],[7,8,9]]
print(numbers)
print()
for x in numbers:
    for c in x:
        print(c,end=" ")#end????
    print('💲')



cumle=("cumle cok ","cok")
cumle1=list(cumle)
silmeli="c"
iyi=[]
for x in cumle1:
    new=""
    for b in x:
        if b != silmeli:
            new += b
    iyi.append(new)
    son=tuple(iyi)
print(" ".join (son))



cumle=("At home, I learnt Python!")
len=len(cumle)
ind1=cumle[0]
print()
print(cumle)
print(f"length: {len} - Frist character: {ind1}")



number=[]
for a in range(0,13):
  number.append(a)
x=2
for c in number:
   if c % x == 0:
    print(f"\n{c}➡ is divisible by {x}✅")
    print (f"The result: {c/x}")
    print('='*30)
   else:
     print(f"\n{c}➡ is 'not' divisible by {x}❌")
     print('='*30)



numbers=[3,64,56,68,24,67,20]
numbers.sort()
if numbers ==[]:
   print()
   print(numbers)
else:
   print()
   print(f"max: {numbers[-1]}")

















