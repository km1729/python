f = open('inputFile.txt','r')
passfile = open('PassFile.txt', 'w')
failfile = open('FailFile.txt', 'w')
#print(f.read())
# count =0
# for line in f:
#     print(str(count) + ' ' + line)
#     count +=1
# f.close()
'''
0 Mary 25 P
1 John 32 P
2 Dylan 19 F
3 Julia 23 F
4 Chad 17 F
5 Jack 20 F
'''

for line in f:
    line_split = line.split()

    if line_split[2] == 'P':
        passfile.write(line)
    else:
        failfile.write(line)       
f.close()
passfile.close()
failfile.close()
'''
line_split = line.split()
print(line_split)
['Mary', '25', 'P']
['John', '32', 'P']
['Dylan', '19', 'F']
['Julia', '23', 'F']

Mary 25 P
John 32 P
Hailey 26 P
Iris 23 P
Jacob 29 P
'''