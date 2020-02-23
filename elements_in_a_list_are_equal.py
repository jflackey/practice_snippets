lst = ['a', 'a', 'a']

len(set(lst)) == 1

all(x == lst[0] for x in lst)

lst.count(lst[0]) == len(lst)

