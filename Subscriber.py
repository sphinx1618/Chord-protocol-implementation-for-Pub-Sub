import socket
import hashlib
import pickle
import time
import json
import sys
import random
class Subscriber:
	
	def __init__(self):
		self.ip = '127.0.0.1'
		self.Port = 1618 + int(sys.argv[1])
		self.key = int(sys.argv[1])
		

		text = 'insert|' + str(self.key) +":" +str(self.Port)
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		db = open('pk','rb')
		st = pickle.load(db)[0]
		db.close()
		port = list(st)[random.randint(0,len(st)-1)]  # ports of the servers

		sock.connect(('127.0.0.1',port))
		sock.send(text.encode('utf-8'))
		
	def get_publishers(self):
		

		s = socket.socket()
		s.bind(('', sub.Port))
		s.listen()


		# Establish connection with client.
		
		c, addr = s.accept()    
		# print ('Got connection from', addr )

		# send a thank you message to the client. encoding to send byte type.
		x = c.recv(1024)
		x = json.loads(x)
		
		
		# Close the connection with the client
		c.close()

		return x

	def send_subscriptions(self,Names):

		text = 'subscriptions_helper|' + str(self.key) + ":" + Names
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		port = 3030  # ports of the servers
		sock.connect(('127.0.0.1',port))
		sock.send(text.encode('utf-8'))

	def receive_articles(self):

		s = socket.socket()
		s.bind(('', sub.Port))
		s.listen()

		while True:
			c, addr = s.accept()    

			x = c.recv(1024)
			
			print("Hey!! An article is Received")

			print(str(x)[1:])
			
			time.sleep(0.5)
			

sub = Subscriber() 
pub_list = sub.get_publishers()

print("WELCOME TO OUR TEXTUAL YOUTUBE APPLICATION")
print("\nHere, we deliver quality articles from our publishers.")
print("You can subscribe to as many subscribers as you want.")
print("Here's the list of our publishers as of now:")
print("______________________________________________________________________")
print("|                   PUBLISHERS:-                                     | Wanna Subscribe?")
print("|____________________________________________________________________|(yes/no)")
names=""
for i in range(len(pub_list)):
	Subscribed=input("|      "+str(i)+"). | "+pub_list[i]+" |                                         |")
	if(Subscribed=="Yes" or Subscribed=="yes" or Subscribed=="YES"):
		names+=pub_list[i]+" "
print("|__________|_______________|_________________________________________|")
print("\n                 Great setting things up for you!!")
print("                            ALL DONE!! ")
print("\n___________________________Your Feed____________________________________")

# print(names[:-1])

names = names[:-1]

sub.send_subscriptions(names)
time.sleep(0.5)
sub.receive_articles()
