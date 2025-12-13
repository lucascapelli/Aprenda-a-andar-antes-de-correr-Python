print("tabuada em tabela")
print("-" * 100)

for i in range(1,11):
        for j in range(1, 11):
            print(f"{i} X {j} = {i * j:<3}",end="\t")
        print()
input()