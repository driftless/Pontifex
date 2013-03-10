import random

def prep_message(message):
	prepped = ""
	message = message.upper()
	for i in message:
		if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			prepped += i
		
	return prepped

def text_to_numbers(text):
	number_list = []
	for i in text:
		index = 0

		for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			index += 1
			if x == i:
				number_list.append(index)
	return number_list
	
def numbers_to_text(numbers):
	text = ""
	alpha_numbers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
		"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	for i in numbers:
		text += alpha_numbers[i - 1]
	return text
	
def create_deck(cards_in_deck):
	deck = [i for i in range(1, cards_in_deck + 1)]
	counter = 0
	while counter < 256:
		counter +=1
		point_a = random.randrange(cards_in_deck)
		point_b = random.randrange(cards_in_deck)
		deck[point_a], deck[point_b] = deck[point_b], deck[point_a]
	return deck
	
	


def copy_deck(original):
	copy = []
	for i in original:
		copy.append(i)
	return(copy)


def first_joker_down_one(deck):
	joker_index = deck.index(joker_one)
	if joker_index != len(deck) - 1:
		swap_index = (joker_index + 1) % len(deck)
		deck[joker_index], deck[swap_index] = deck[swap_index], deck[joker_index]
	else:
		temp_deck = [i for i in range(len(deck))]
		temp_deck[0] = deck[0]
		temp_deck[1] = deck[joker_index]
		#print("Deck: ", deck)
		#print("Temp deck: ", temp_deck)
		for i in range(2, len(deck)):
			#print(i, deck[i-1])
			temp_deck[i] = deck[i - 1]
		deck = temp_deck
	return deck

def second_joker_down_two(deck):
	joker_index = deck.index(joker_two)
	if joker_index != (len(deck) - 1) and joker_index != (len(deck) - 2):
		temp = deck[joker_index]
		deck[joker_index] = deck[joker_index + 1]
		deck[joker_index + 1] = deck[joker_index + 2]
		deck[joker_index + 2] = temp
	elif joker_index == (len(deck) - 2):
		temp_deck = [i for i in range(len(deck))]
		temp_deck[0] = deck[0]
		temp_deck[1] = deck[joker_index]
		temp_deck[len(deck) - 1] = deck[len(deck) - 1]
		for i in range(2, len(deck) - 1):
			temp_deck[i] = deck[i - 1]
		deck = temp_deck
	elif joker_index == (len(deck) - 1):
		temp_deck = [i for i in range(len(deck))]
		temp_deck[0] = deck[0]
		temp_deck[1] = deck[1]
		temp_deck[2] = deck[joker_index]
		for i in range(3, len(deck)):
			temp_deck[i] = deck[i -1]
		deck = temp_deck
	return deck
	
def three_way_cut(deck):
	flag = False
	for i in deck:
		if i == joker_one or i == joker_two:
			if flag == False:
				first_joker_index = deck.index(i)
				flag = True
			else:
				second_joker_index = deck.index(i)
	top_slice = deck[:first_joker_index:1]
	bottom_slice = deck[second_joker_index + 1::1]
	middle_slice = deck[first_joker_index:second_joker_index + 1:1]
	#print("Top: ", top_slice)
	#print("Middle: ", middle_slice)
	#print("Bottom: ", bottom_slice)
	temp_deck = []
	for i in bottom_slice:
		temp_deck.append(i)
	for i in middle_slice:
		temp_deck.append(i)
	for i in top_slice:
		temp_deck.append(i)
	return temp_deck
	
def top_to_bottom_cut(deck):
	if deck[len(deck) - 1] == len(deck):
		value = len(deck) - 1
	else:
		value = deck[len(deck) - 1]
	top_slice = deck[:value:1]
	temp_deck = deck[value:len(deck) - 1:1]
	for i in top_slice:
		temp_deck.append(i)
	temp_deck.append(value)
	return temp_deck
	
def get_key(deck):
	top_card = deck[0]
	value = deck[top_card - 1]
	return value
	
def generate_keystream(deck):
	keystream = []
	for i in message_numbers:
		deck = first_joker_down_one(deck)
		deck = second_joker_down_two(deck)
		deck = three_way_cut(deck)
		deck = top_to_bottom_cut(deck)
		keystream.append(get_key(deck))
	return keystream
	
def encrypt_message(message, keystream):
	encrypted_message = []
	for i in range(len(message)):
		encrypted_message.append((message[i] + keystream[i]) % 26)
	return encrypted_message
		
def decrypt_message(message, keystream):
	decrypted_message = []
	for i in range(len(message)):
		number = message[i] - keystream[i]
		number_two = abs(((number // 26) * 26) - number)
		decrypted_message.append(number_two)
	return decrypted_message
	
	
		
message = input("Please enter a message to encrypt: ")
prepared_message = prep_message(message)
message_numbers = text_to_numbers(prepared_message)
print("Message to encrypt:\n", prepared_message)
print("Message converted to numbers:\n", message_numbers)
cards_in_deck = int(input("How many cards in your deck?: "))
deck = create_deck(cards_in_deck)
joker_one = len(deck) - 1
joker_two = len(deck)
print("Deck:\n", deck)
original_deck_copy = copy_deck(deck)
keystream = generate_keystream(deck)
print("Keystream:\n", keystream)
encrypted_message = encrypt_message(message_numbers, keystream)
print("Encrypted message:\n", encrypted_message)
decrypted_message = decrypt_message(encrypted_message, keystream)
print("Decrypted message, in numbers:\n", decrypted_message)
decrypted_message_text = numbers_to_text(decrypted_message)
print("Decrypted message:\n", decrypted_message_text)




	




