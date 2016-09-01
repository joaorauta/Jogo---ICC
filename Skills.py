class Skills():
	soco = 0
	chute = 0
	especial = 0
	radouken = 0
	x = 0
	y = 310
	x0 = 0
	y0 = 0
	vx = 0
	vy = 0
	
	def __init__(self, soco, chute, especial, radouken):
		self.soco = soco
		self.chute = chute
		self.especial = especial
		self.radouken = radouken
	
	def getX(self):
		return self.x

	def getY(self):
		return self.y
    
	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y
	
	def move(self):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
	
	def soco_direita(self):
		self.vx = 10
	
	def soco_esquerda(self):
		self.vx = -10
	
	def chute_direita(self):
		self.vx = 15
		
	def chute_esquerda(self):
		self.vx = -15
	
	def especial_direita(self):
		self.vx = 15
	
	def especial_esquerda(self):
		self.vx = -15
		
	#def radouken(self):
	#	self.vx = 30
	
	def move(self):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
	
