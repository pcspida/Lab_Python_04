'''
Kwabena Ansah
Solution File: Lab04
'''
#1
groceries=['bananas','strawberries','apples','bread']
#a
groceries.append('champagne')
print groceries
#b
groceries.remove('bread')
print groceries
#c
groceries.sort()
for item in groceries:
    print 'Go to Isle '+item[0]+' for '+item
    
#2
#a Dictionary because it maps an item to a key

#b
items={'Apples':7.3,'Bananas':5.5,'Bread':1.0,'Carrots':10.0,'Champagne':20.90,'Strawberries':32.6}
#c
items['Strawberries']=63.43
print items
#d
items['Chicken']=6.5
print items
#3
#a List

#b
in_stock=[]
for i in items.items():
    in_stock.append(i[0])
    
print in_stock
#c
always_in_stock=tuple(in_stock)
print always_in_stock
#d
print 'Come to shoprite! We always sell:'
for i in range(len(always_in_stock)):
    print always_in_stock[i]

