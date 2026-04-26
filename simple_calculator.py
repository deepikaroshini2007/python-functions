def add(a,b):
return a+b
def subtract(a,b):
return a-b
def multiply(a,b):
return a*b
def divide(a,b):
if b == 0:
return &quot;division by zero not possible&quot;
else:
return a/b
def square(a):
return a*a
while True:
print(&quot;\n....simple calculator....&quot;)
print(&quot;1.Add&quot;)
print(&quot;2.Subtract&quot;)
print(&quot;3.Multiple&quot;)
print(&quot;4.Divide&quot;)
print(&quot;5.Square&quot;)

choice = int(input(&quot;Enter your choice:&quot;))
if choice == 6:
print(&quot;Program End&quot;)
break
if choice == 5:
a=int(input(&quot;Enter your first number:&quot;))

print(&quot;square:&quot;,square(a))
else:
a=int(input(&quot;Enter your first number:&quot;))
b=int(input(&quot;Enter your second number:&quot;))
if choice == 1:
print(&quot;addition:&quot;,add(a,b))
elif choice == 2:
print(&quot;subtract:&quot;,subtract(a,b))
elif choice == 3:
print(&quot;multiplication:&quot;,multiply(a,b))
elif choice == 4:
print(&quot;divide:&quot;,divide(a,b))
else:
print(&quot;Invalid choice&quot;)
