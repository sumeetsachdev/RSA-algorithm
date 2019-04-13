import math

p=int(input("Enter prime number p: "))
q=int(input("Enter another prime number q: "))

n=p*q

f=(p-1)*(q-1)

c=1
e=int(input("Enter your encryption key: "))
while(c==1):
	if(math.gcd(e,f)==1):
		print("You have choose correct encryption key")
		c=0
	else:
		e=int(input("Enter your encryption key: "))

for i in range(f):
	if((i*e)%f==1):
		d=i
		break

print("decrypted key: ",d)

t=open("file.txt","r")
text=t.readline()
print(text)

#text=input("Enter the plain text: ")

a="abcdefghijklmnopqrstuvwxyz"

#ENCRYPTION
c=[]
c1=""
for i in range(len(text)):
	ch=a.find(text[i])
	x=(pow(ch,e))%n
	c.append(x)
	y=x%26
	c1+=a[y]
	
print(c)
print("cipher text: ",c1)

w=open("new.txt","w")
w.write(c1)

#DECRYPTION
p=[]
p1=""
for i in range(len(c)):
	#ch=a.find(c[i])
	b=c[i]
	x=(pow(b,d))%n
	p.append(x)
	y=x%26
	p1+=a[y]
	
print(p)
print("Plain text: ",p1)
