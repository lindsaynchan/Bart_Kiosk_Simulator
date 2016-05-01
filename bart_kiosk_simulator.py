DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

def load_card(ones,fives,tens,twenties):
	ones_total = ones
	fives_total = fives*5
	tens_total = tens*10
	twenties_total = twenties*20
	card_value = ones_total+fives_total+tens_total+twenties_total
	return card_value

def travel_to_destination(fare_price,card_value):
	if card_value >= fare_price:
		print "Welcome aboard, enjoy your trip!"
	elif card_value < fare_price:
		print "You need more money!"

clipper_card = load_card(2,0,1,0)
travel_to_destination(FRUITVALE_TO_UNION_CITY,clipper_card)
