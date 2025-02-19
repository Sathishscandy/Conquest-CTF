import pyshark, base64

#################
# Decoder       #
#################

def Base64Decoder(text):
	#base64_bytes = text.encode('ascii')
  
	sample_string_bytes = base64.b64decode(text) 
	sample_string = sample_string_bytes.decode('ascii')

	print('[+] Base64 decoded.')
	return sample_string

# .pcap file
pcap_file = input('File captured: ')

# File output
OUTPUT_FILE = input('Filename output: ')

# Domain Name used for Exfil
DOMAIN_NAME = input('Domain Name:')
print(f'[+] Domain Name set to {DOMAIN_NAME}')

packets_capture= pyshark.FileCapture(pcap_file, keep_packets=False)
extract_text = []


def result_packet(packet):
	try:
		# Write code to filter for Threat Actor Domain from .pcap file
	except AttributeError:
		pass

packets_capture.apply_on_packets(result_packet)

Text_decode = ''

	# Write code to remove added Encryptor from Outgoing_packet.pcap

print('[+] Extracting Text....')
# Write result to user's output file
with open(OUTPUT_FILE, 'w') as wr:
	wr.write(Base64Decoder(Text_decode))
print(f'[+] Output to {OUTPUT_FILE}')
