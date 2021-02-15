from collections import Counter
string = {
}

non_letter = ["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")",":","'",".",",",";","|","?","*","-","+","=","_"]

text = input("Enter a word or phrase to count the Occurrence of each letter: ")
for non_letter in non_letter:
        text = text.replace(non_letter,"")

len_letters = len(text)
count = Counter(text)

string.update(count)


print("letter\t\tOccurrence\t\tPercentage")
for k,v in string.items():
    percentage = 100*v / len_letters
    print(str(k)+"\t\t"+str(v)+"\t\t\t"+str(round(percentage,2))+"%")


count2 = count.most_common()
counter1 = []
for i in count2:
    counter1.append(i[0])

print("Letters from highest occurrence to lowest:")
for i in counter1:
    print(i,end="")

