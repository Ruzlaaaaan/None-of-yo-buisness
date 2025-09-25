anime = ('One Piece', 'Solo Leveling', 'Death Note', 'One Punch Man', 'Dragon Ball Z')
#slice from 1 to 3
print(anime[1:3])

#Slice from beginning upto index 3
print(anime[:3])

#Slice from index 2 to end
print(anime[2:])

#Step slicing (Every Second Element)
print(anime[::2])

#Reverse Tuple
print(anime[::-1])

#Count Method
count_2 = anime.count(2)
print(count_2)

#Index Method
index_one_piece = anime.index('One Piece')
print(index_one_piece)
