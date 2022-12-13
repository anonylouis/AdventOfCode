#!/usr/bin/python3

f = open('input.txt')

def get_next_item(l) :
	item = ""
	inlist = 0
	for i in l :
		if i == ',' and inlist == 0 :
			break
		if i =='[' :
			inlist += 1
		if i==']' :
			inlist -= 1
		item += i
	return item

def cmp(l1, l2) :
	if l1 == "" or l2 =="" :
		return 0 if l1==l2 else 1 if l1=="" else -1
	item_1, item_2 = get_next_item(l1), get_next_item(l2)
	l1=l1.replace(item_1, "", 1).replace(',', "", 1)
	l2=l2.replace(item_2, "", 1).replace(',', "", 1)
	
	if item_1[0] != '[' and item_2[0] != '[' : # two numbers
		if int(item_1) < int(item_2) :
			return 1
		elif int(item_1) > int(item_2) :
			return -1
	else :
		if item_1[0] == "[" :
			item_1 = item_1[1:-1]
		if item_2[0] == "[" :
			item_2 = item_2[1:-1]
		r = cmp(item_1, item_2)
		if r != 0 :
			return r
	return cmp(l1, l2)

packets = ["[2]", "[6]"]

for l in f :
	if l == "\n" :
		continue
	packets.append(l[1:-2])

for i in range(len(packets)) :
	for j in range(i + 1, len(packets)) :
		if (cmp(packets[i], packets[j]) == -1) :
			packets[i], packets[j] = packets[j], packets[i]

print((packets.index("[2]") + 1) * (packets.index("[6]") + 1))
