import random

words = {
    "happy":["cheerful","contented","ecstatic","joyous"],
    "cold":["bitter","chill","coldish","arctic"],
    "hot":["boiling","scorching","torrid","tropical"],
    "sad":["dismal","somber","wistful","melancholy"],
}
print("\nwelcom to the synonym thesaurus")
print("\nchoose the words from the thesaurus and i will give you a synonym")
print("here are the world in the thesaurus: ")

for word_key in words.keys():
    print("\t",word_key)

word_choos = input("what word would you like to synonym for: ").lower()

for k , v in words.items():
    if word_choos in k:
        ran = random.choice(v)
        print("A synonym for "+ k + " is " + ran)

        all_keys = input("would you like to see the whole thesaurus(y/n)").lower()
        if all_keys == "y":
            for k , v in words.items():
                print("\n"+ k.title() + " synonym are: ")
                for val in v:
                    print("\t-"+ val)

        else:
            print("thank you for using our app Goodbye")

if word_choos not in words.keys():
    print("not in thesaurus")

