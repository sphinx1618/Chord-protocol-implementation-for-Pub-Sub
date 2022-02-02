import socket
import time
import random
import pickle

class Publisher:
	def __init__(self,Name,port):
		self.Name = Name
		self.port = port
	
	def pub_register(self):
		print("Publisher",self.Name,"Registered at port",self.port)
		text = 'insert_pub|'+self.Name
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		port = self.port  # ports of the servers
		sock.connect(('127.0.0.1',port))
		sock.send(text.encode('utf-8'))

	def send_articles(self,text):
		
		text = 'articles|' + self.Name + ":" + text
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		port = self.port  # ports of the servers
		sock.connect(('127.0.0.1',port))
		sock.send(text.encode('utf-8'))

db = open('pk','rb')
st = pickle.load(db)[0]
db.close()

channel_name=input("Enter the name of your channel :")
pub = Publisher(channel_name,list(st)[random.randint(0,len(st)-1)])
pub.pub_register()
# time.sleep(15)

print("Hey! Your channel name is ",channel_name)
print("Type the article to publish \n type exit to close!")
while True:
	message=input("Enter the message: ")
	pub.send_articles(message)


