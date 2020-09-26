# enumerate:


items = [ 'apple','orange','mango'] 
enu_Items = enumerate(items)
print (list(enu_Items)) #Output:[(0, 'apple'), (1, 'orange'), (2, 'mango')] 

# changing the default counter by passing START parameter 
enu_Items = enumerate(items, 10) 
print(list(enu_Items)) #Output: [(10, 'apple'), (11, 'orange'), (12, 'mango')]
------------------------------------------------------

#use a for loop over a collection 
Months = ["Jan","Feb","Mar","April","May","June"] 
for i, m in enumerate (Months): 
print(i,m)

0 Jan 
1 Feb 
2 Mar 
3 April 4 May 5 June
-----------------------------------------
