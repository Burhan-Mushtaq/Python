def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["Burhan" , "Hadi" , "Wahid" , "an"]

print(rem(l , "an"))