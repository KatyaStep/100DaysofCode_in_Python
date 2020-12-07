objects,students  = map(int, input().split()) 

sheet = []
for _ in range(students):
    sheet.append( map(float, input().split()) ) 

for i in zip(*sheet): 
    print( sum(i)/len(i) )