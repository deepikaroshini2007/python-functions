def fibonacci(n):
if n&lt;=1:
return n
else:
return fibonacci(n-1) + fibonacci(n-2)
n=int(input(&quot;enter number:&quot;))
for i in range(n):
print(fibonacci(i),end=&quot; &quot;)
