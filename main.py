class __KLLError:
	def __FileNotFoundErro(file):
		print("(ErrorKLL) NotFoundFile: {}".format(file))

class KLL:
	def create(file):
		with open(file, "w") as files:
			pass

	def write(file, text):
		try:
			with open(file, "w") as files:
				files.write(text)
		except FileNotFoundError:
			__KLLError.__FileNotFoundError(file)

	def remove(file):
		import os
		try:
			os.remove(file)
		except FileNotFoundError:
			__KLLError.__FileNotFoundError(file)

	def read(file):
		try:
			with open(file, "r") as files:
				for text in files:
					text
				return text
		except FileNotFoundError:
			_KLLError.__FileNotFoundError(file)

if __name__ == '__main__':
	main()
	
