def load_card(ones,fives,tens,twenties):
	ones_total = ones
	fives_total = fives*5
	tens_total = tens*10
	twenties_total = twenties*20
	total = ones_total+fives_total+tens_total+twenties_total
	return total

print load_card(0,0,0,0)
print load_card(0,0,0,9)
print load_card(2,3,0,0)
print load_card(3,1,1,3)
