# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

file = open('text.txt', 'r', encoding='utf-8')
data = file.read()
lst_word = data.split()
file.close

print(lst_word)

new_lst_word = []
for i in lst_word:
    del_bool = False
    for k in i:
        if k.isdigit():
            del_bool = True
            break
    if del_bool == False:
        new_lst_word.append(i)            
print(new_lst_word)
