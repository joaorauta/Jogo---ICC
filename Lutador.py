class Lutador():
    hp = 100
    mp = 0
    x = 0
    y = 0
    x0 = 0
    y0 = 0
    vx = 0
    vy = 0
    angle = 60
    
    def __init__(self, hp, mp, x, y):
        self.hp = hp
        self.mp = mp
        self.x = x
        self.y = y           
            
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y    
        
    def walk_right(self):
        self.vx = 2
     
    def walk_left(self):
        self.vx = -2
        
    def move(self):
	if (self.x == 0):
		self.x = self.x + 2
	if (self.x == 512):
		self.x = self.x - 2
	else:
		self.x = self.x + self.vx
    	self.y = self.y + self.vy
    
    def jump(self):
        
        self.y0 = self.y
        
        
