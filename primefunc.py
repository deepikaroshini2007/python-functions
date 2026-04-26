def prime(n):
if n&lt;2:
return False
for i in range(2,n):
if n%i==0:
return False
return True
num =int(input(&quot;Enter a number:&quot;))
for i in range(2,num):
if prime(i) and prime(num-i):
print(&quot;possible&quot;)
print(num,&quot;=&quot;,i,&quot;+&quot;,num-i)
break
else:
print(&quot;not possible&quot;)
