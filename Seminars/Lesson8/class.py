some_list = ['eat', 'tea', 'tan', 'sdfsdf dsfsfwe e', 'ate', 'nat', 'bat', 'SDFSDF']
res_list = []
temp_list = []
char_list = list(some_list[0])
add_words = set()
for i in range(len(some_list)):
    if some_list[i] not in add_words:
        temp_list = [some_list[i]]
        add_words.add(some_list[i])
        for j in range(i, len(some_list)):
            if some_list[j] not in add_words:
                if len(some_list[i]) == len(some_list[j]):
                    for item in some_list[i]:
                        if item not in set(some_list[j]):
                            break
                    else:
                        temp_list.append(some_list[j])
                        add_words.add(some_list[j])
        res_list.append(temp_list)

print(res_list)
