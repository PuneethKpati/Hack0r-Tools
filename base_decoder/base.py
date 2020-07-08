
import base58
import base64

class BaseConverter():
	def __init__(self):
		self.encoderF = {'Base64': base64.b64encode, 'Base16': base64.b16encode, 'Base32': base64.b32encode, 'Base58': base58.b58encode}
		self.decoderF = {'Base64': base64.b64decode, 'Base16': base64.b16decode, 'Base32': base64.b32decode, 'Base58': base58.b58decode}

	

	def decode(self, message):
		for func in self.decoderF:
			try:
				decodedb = self.decoderF[func](bytes(message, 'utf-8'))
				decoded = str(decodedb, 'utf-8' )
				return func + ' : ' + decoded
			except:
				continue

		return 'Message is not Base Encoded! Nice try Hack0r!'



decode = BaseConverter()
print(decode.decode('what?'))
print(decode.decode('YmFzZTY0'))
print(decode.decode('626173653136'))
print(decode.decode('MJQXGZJTGI======'))
print(decode.decode('qzTiEHgB'))

print(decode.encode('Hello!'))


