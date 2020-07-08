
import base58
import base64

class BaseConverter():
	def __init__(self):
		self.encoderF = {'Base64': base64.b64encode, 'Base16': base64.b16encode, 'Base32': base64.b32encode, 'Base58': base58.b58encode}
		self.decoderF = {'Base64': base64.b64decode, 'Base16': base64.b16decode, 'Base32': base64.b32decode, 'Base58': base58.b58decode}

	def encode(self, message, base=None):
		res = []
		count = 0
		for func in self.encoderF:
			encodedBytes = self.encoderF[func](bytes(message, 'utf-8'))
			encoded = str(encodedBytes, 'utf-8' )
			res.append(func + ' : ' + encoded)

		return res

	def decode(self, message):
		for func in self.decoderF:
			try:
				decodedb = self.decoderF[func](bytes(message, 'utf-8'))
				decoded = str(decodedb, 'utf-8' )
				return 'Decoded with ' + func + ' : ' + decoded
			except:
				continue

		return 'Message is not Base Encoded! Nice try Hack0r!'



decode = BaseConverter()


