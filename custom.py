class Youtube:
	def __init__(self,channel_name,subscribers,views):
		self.channel_name=channel_name
		self.subscribers=subscribers
		self.views=views

	def bigger(self,other):
		if(other.subscribers>self.subscribers):
			print("the {} channel is bigger than {} channel".format(other.channel_name,self.channel_name))
		else:
			print("the {} channel is bigger than {} channel".format(self.channel_name,other.channel_name))

	def __str__(self):
		return '{}:{}:{}'.format(self.channel_name,self.subscribers,self.views)
		

traversy_media=Youtube('TM',1000,1000)
farhanerd=Youtube('farhanerd',188,8100)

print(farhanerd)
traversy_media.bigger(farhanerd)

		