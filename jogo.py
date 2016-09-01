from graphics import *
import time
import Tkinter
from Lutador import *
from Skills import *

def main():
	#DimensoesBalrog = 49x84
	win = GraphWin("Fighting Game", 512, 464)
	time_inicial = time.time()
	fundo = Image(Point(256,232), "FeiLongStagemaior.png")
	Image.draw(fundo,win)
	IdleImg = Image(Point(90,310), "editado.png")
	IdleImg.draw(win)	
	RightImg = Image(Point(90,310), "editado.png")
	tecla = ""
	
	l = Lutador(100, 0, 90, 310)
	s = Skills(10, 10, 30, 15)
	
	while tecla != "Escape":
		tecla = win.checkKey()
		print(tecla)
		PosX = RightImg.getAnchor().getX()
		PosY = RightImg.getAnchor().getY()
		DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")

		Hitbox1Right = RightImg.getAnchor().getX() - 24.5
		Hitbox2Right = RightImg.getAnchor().getY() - 42
		Hitbox3Right = RightImg.getAnchor().getX() + 24.5
		Hitbox4Right = RightImg.getAnchor().getY() + 42
        
		
		HitboxRightFinal = Rectangle(Point(Hitbox1Right, Hitbox2Right), Point(Hitbox3Right, Hitbox4Right))

		if tecla == "Right":
			IdleImg.undraw()
			RightImg.undraw()
			l.walk_right()
			l.move()
			RightImg = Image(Point(l.getX(), l.getY()), "editado.png")
			RightImg.draw(win)
			
		if tecla == "Left":
			IdleImg.undraw()
			DownImg.undraw()
			RightImg.undraw()
			l.walk_left()
			l.move()
			RightImg = Image(Point(l.getX(), l.getY()), "editado.png")
			RightImg.draw(win)
				
			
		if tecla == "Up":
			DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")
			UpImg = Image(Point(PosX,PosY), "balrog pulando.png")

			Hitbox1Up = UpImg.getAnchor().getX() - 24.5
			Hitbox2Up = UpImg.getAnchor().getY() - 62
			Hitbox3Up = UpImg.getAnchor().getX() + 24.5
			Hitbox4Up = UpImg.getAnchor().getY() + 22
			

			HitboxUpFinal = Rectangle(Point(Hitbox1Up, Hitbox2Up), Point(Hitbox3Up, Hitbox4Up))
			IdleImg.undraw()
			RightImg.undraw()
			DownImg.undraw()
			UpImg.draw(win)
			
			for i in range(5):
				UpImg.move(0,-20)
				time.sleep(0.079)
				UpImg.move(0,20)
				HitboxUpFinal.move(0,20)
				HitboxUpFinal.move(0,-20)
			UpImg.undraw()
			RightImg.draw(win)
			
				
		if tecla == "Down":
			DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")
			UpImg = Image(Point(PosX,PosY), "balrog pulando.png")

			Hitbox1Down = DownImg.getAnchor().getX() - 24.5
			Hitbox2Down = DownImg.getAnchor().getY() - 26
			Hitbox3Down = DownImg.getAnchor().getX() + 24.5
			Hitbox4Down = DownImg.getAnchor().getY() + 42
			
			HitboxFinalDown = Rectangle(Point(Hitbox1Down, Hitbox2Down), Point(Hitbox3Down, Hitbox4Down))
			RightImg.undraw()
			IdleImg.undraw()
			UpImg.undraw()
			DownImg.draw(win)
			for i in range(5):
				DownImg.move(0,0)
				time.sleep(0.07)
			DownImg.undraw()
			RightImg.draw(win)
		
			
		if tecla == "c":
			RightImg.undraw()
			IdleImg.undraw()
			s.setX(l.getX())
			s.soco_direita()
			s.move()
			soco = Image(Point(s.getX(), s.getY()), "chiko.gif")
			soco.draw(win)
		
		if tecla == "x":
			RightImg.undraw()
			IdleImg.undraw()
			s.setX(l.getX())
			s.chute_direita()
			s.move()
			chute = Image(Point(s.getX(), s.getY()), "taro.gif")
			chute.draw(win)
		
		if tecla == "z":
			RightImg.undraw()
			IdleImg.undraw()
			s.setX(l.getX())
			s.especial_direita()
			s.move()
			especial = Image(Point(s.getX(), s.getY()), "especial.png")
			especial.draw(win)
			
			
        print(time.time() - time_inicial)

	print(PosX)
	print(PosY)
	print(time.time() - time_inicial)
	win.close()
main()
