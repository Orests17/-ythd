summa = 0
skaitli = []
with open('fails.txt', encoding = "utf-8") as f:
  for line in f:
      skaitli.append(line)
print(skaitli)
print(f' Saraksta garums = {len(skaitli)}')

for i in range(len(skaitli)):
  summa += int(skaitli[i])
print(f'Skaitļu summa ir {summa}')

