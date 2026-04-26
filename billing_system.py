def subtotal(qty,price):
r=qty*price
return r
def total(s):
sum=0
for i in s:
sum=sum+i
return sum
def discount(tot):
if tot&gt;=3000:
amount=tot-(tot*10/100)
return amount
else:
amount=tot

return amount
def gst(price):
return price+(price*5/100)

n=int(input(&quot;enter no of items:&quot;))
t=[]
for i in range(n):

item=input(&quot;enter item name:&quot;)
quantity=int(input(&quot;enter quantity:&quot;))
price=int(input(&quot;enter price:&quot;))
t.append((item,quantity,price))
for i in t:
print(i)
s=[]

for i in t:

sub=subtotal(i[1],i[2])

s.append(sub)
tot=total(s)
price=discount(tot)
rupee=gst(price)
print(&quot;\n-------------YOUR BILL----------------&quot;)
print(&quot;Item\tqty\tprice\tsubtotal&quot;)
for i in t:
sub=i[1]*i[2]
print(f&quot;{i[0]}\t{i[1]}\t{i[2]}\t{sub}&quot;)
print(&quot;------------------------------------&quot;)
print(&quot;Total amount:&quot;,tot)

print(&quot;After discount:&quot;,price)
print(&quot;Final amount with gst:&quot;,rupee)
print(&quot;-------------------------------------&quot;)
