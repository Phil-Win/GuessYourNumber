#Overview: This program will have you pick a range from 1 to a power of 10 and pick any number you want in that range
#It will take your input and ask you for the remainder after dividing it by two different numbers
#It will then guess your number correctly(Using the chinese remainder theorem) assuming you did not mess up your arithmetic

n,x,B1,B2,c1,c2,x1,x2,output = 0,0,0,0,0,0,0,0,0

x =(int(input("You want me to guess your number from 1 to 10^...")))
n = 10**x
print("Ok, now you need to pick a number(any integer) from 1 to %d" % (n))
print("Don't tell me, I'll figure out what it is... although I'll need two hints.")
B2 = 2**x
B1 = 5**x
c1 = int(input("1.) Take your number and divide it by %d and tell me the remainder.(input it here)" % (B2)))    
c2 = int(input("2.) Take your number and divide it by %d and tell me the remainder.(input it here)" % (B1)))

for i in range(0,B2):
    if ((B1)*i) % (B2) ==1:
        x1=i
        break
for i in range(0,B1):
    if ((B2)*i) % (B1) ==1:
        x2=i
        break
output = ((B1)*x1*c1 + (B2)*x2*c2) % n
if output ==0:
    output= n
print("Your number is...",output)
