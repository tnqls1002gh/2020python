prov = "A barking Dog"

length = len(prov)
print("prov의 길이는:", length)

pos1 = prov.find("b")
print("첫번째 b 문자의 위치는:", pos1)

if prov.find("Dog")>=0:
    print("Dog있음")
else:
    print("Dog없음")

   
if prov.find("Dog")>=0:
    print(prov.replace("Dog", "Cat"))
else:
    print(prov)

공백 = prov.split(" ")
for i in :
    print(i, end=", ")
