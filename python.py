f=open('questions.txt','r', encoding="utf8")
t=[]
for line in f:
    t.append(line[0:len(line)-1])
print(t)