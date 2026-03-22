for i in range(10) :
    if i == 5 :
        break
    
    print(i)
    
# → berhenti di 5

for i in range(10) :
    if i % 2 == 0 :
        continue
    
    print(i)