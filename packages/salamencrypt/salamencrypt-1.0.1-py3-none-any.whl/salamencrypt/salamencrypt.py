import marshal,os,sys,random,pyfiglet,colorama
import time,datetime,re,rich
from user_agent import generate_user_agent
from colorama import *



class salamencrypt():
	def enc(code):
		b = compile(code, "<a>", "exec")
		data = marshal.dumps(b)
		rr = repr(data)
		return rr
		
	def run(code):
		codee = (f'import marshal\nexec(marshal.loads({code}))')
		exec(codee)
		