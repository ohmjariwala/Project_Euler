#Sort the list of names(0022_names.txt) 
#Give value to each letter
#Find where in the list the name is and multiply

#Calling the text file and sorting
with open('0022_names.txt') as f:
   names= f.read()

list=names.replace('"', '').split(',')#method chaining
list.sort()


#assign each letter to a numerical value
char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

#Solve


total=0

for i in range(len(list)):
   temp=0
   for j in range(len(list[i])):
      temp+= char_num_dict.get(list[i][j])
   total += ((i+1) * temp)
      
print(total)
