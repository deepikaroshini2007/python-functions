def sumdigits(n):
if n==0:
return 0
else:
return (n%10)+sumdigits(n//10)
num=int(input(&quot;enter number:&quot;))

print(&quot;Sum of digits:&quot;,sumdigits(num))
