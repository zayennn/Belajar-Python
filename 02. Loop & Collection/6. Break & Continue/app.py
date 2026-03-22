for i in range(10) :
    if i == 5 :
        break
    
    print(i)
    
# → berhenti di 5

for i in range(1, 10 + 1) :
    if i % 2 == 1 :
        continue
    
    print(i)

# → skip angka ganjil