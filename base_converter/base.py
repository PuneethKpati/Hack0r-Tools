
import base58
import base64

# class that provides methods for encoding and decoding strings using multiple bases
class BaseConverter():
	def __init__(self):
		# Store the functions for encoding and decoding for ease of access to the functions
		self.encoderF = {'Base64': base64.b64encode, 'Base16': base64.b16encode, 'Base32': base64.b32encode, 'Base58': base58.b58encode}
		self.decoderF = {'Base64': base64.b64decode, 'Base16': base64.b16decode, 'Base32': base64.b32decode, 'Base58': base58.b58decode}

	# Takes a message and encodes it in Base16, 32, 58 and 64 
	# Returns a list of all the encoded strings
	def encode(self, message, base=None):
		res = []
		# loop through all the encoding functions and encode the messages
		for func in self.encoderF:
			# Get the encoded output in bytes and convert it back to a string
			encodedBytes = self.encoderF[func](bytes(message, 'utf-8'))
			encoded = str(encodedBytes, 'utf-8' )
			# Puts the string in format,  Base[num] : [encoded string]
			res.append(func + ' : ' + encoded)

		return res

	# Takes a encoded string and finds the base it is encoded with
	# returns the decoded string and the base information
	def decode(self, message):
		# loop through all the decoding functions and try to apply decoding
		for func in self.decoderF:
			# Try to decode the string with one of the decoding functions stored above
			try:
				decodedb = self.decoderF[func](bytes(message, 'utf-8'))
				decoded = str(decodedb, 'utf-8' )
				return 'Decoded with ' + func + ' : ' + decoded
			# If the decoding functions don't match the encoding padding
			# the decoding functions throw exceptions
			# ignore that base number and move to the next decoding function
			except:
				continue

		# If the message is not encoded in any of the above bases 
		# then return this message for user info
		return 'Message is not Base Encoded! Nice try Hack0r!'



