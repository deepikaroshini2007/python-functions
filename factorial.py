def factorial(n):
fact=1
for i in range(1,n+1):
fact=fact*i
return fact
n=int(input(&quot;enter number:&quot;))
for i in range(1,n+1):
print(&quot;Factorial of&quot;,i,&quot;=&quot;,factorial(i))
