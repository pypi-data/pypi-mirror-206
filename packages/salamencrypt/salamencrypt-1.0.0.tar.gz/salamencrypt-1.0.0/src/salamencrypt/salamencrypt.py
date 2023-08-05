import marshal

class salamencrypt():
	def enc(code):
		b = compile(code, "<@T5B55>", "exec")
		data = marshal.dumps(b)
		rr = repr(data)
		return rr
		
	def run(code):
		codee = (f'import marshal\nexec(marshal.loads({code}))')
		exec(codee)
		