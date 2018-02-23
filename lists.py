from visual import *
numbers = []
beauty = "A spectre is haunting Europe - the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies."
i = len(beauty)

for x in range(0,6):
    i = i + 1
    numbers.append(i)
print(numbers)
for number in numbers:
    number = number + 5
    print("Here is the blessed number:" + str(number))
raw_input()
