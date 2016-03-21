import map
import application
from random import randint
import sound
from sound_positioning import position_sound_1d
import player
from pyglet.window import key
from speak import speak
import pyglet
m=map.map()
me=player.player()
en=player.player()
en.x=-15
gun=sound.sound()
step=sound.sound()
death=sound.sound()
amb=sound.sound()
pain=sound.sound()
enemyhit=sound.sound()
enemydeath=sound.sound()
jump=sound.sound()
amb.load("sounds/amb.wav")
enemy=sound.sound()
jump.load("sounds/jump.wav")
enemy.load("sounds/enemy.wav")
death.load("sounds/playerdeath.ogg")
enemydeath.load("sounds/enemydeath.wav")
enemyhit.load("sounds/enemyhit.wav")
gun.load("sounds/gun.wav")
def positions():
	position_sound_1d(enemy.handle,me.x,en.x,1,0.5)
	position_sound_1d(enemydeath.handle,me.x,en.x,1,0.5)
	position_sound_1d(enemyhit.handle,me.x,en.x,1,0.5)
def moveenemy(self):
	if en.spawned==1:
		if en.x>=me.x:
			en.x-=1
			positions()
		if en.x<=me.x:
			en.x+=1
			positions()
def attackplayer(self):
	if en.x>=me.x-2 and en.x<=me.x+2 and en.spawned==1:
		pain.stop()
		pain.load("sounds/pain"+str(randint(1,5))+".ogg")
		pain.play()
		me.health-=randint(1,3)+en.level
		if me.health<=0:
			death.play_wait()
			pygame.exit()
def attackenemy():
	if en.x>=me.x-3 and en.x<=me.x+3:
		enemyhit.stop()
		enemyhit.play()
		en.health-=randint(1,3)
		if en.health<=0 and en.spawned==1:
			enemy.stop()
			enemydeath.play()
			en.spawned=0
			en.x=-15
			schedule_spawn()
def schedule_events():
	pyglet.clock.schedule_interval(moveenemy,0.6)
	pyglet.clock.schedule_interval(attackplayer,0.6)
def spawnenemy(self):
	en.level+=1
	en.health=20+en.level
	enemy.x=randint(0,m.maxx)
	enemy.play_looped()
	en.spawned=1
def playerland(self):
	me.jumping=0
	step.stop()
	step.load("sounds/steps/"+str(randint(1,5))+".wav")
	step.play()
def schedule_spawn():
	pyglet.clock.schedule_once(spawnenemy,randint(100,150)/10)
def schedule_land():
	pyglet.clock.schedule_once(playerland,0.9)
window = pyglet.window.Window(caption=application.name+" version "+application.version)
amb.play_looped()
positions()
schedule_events()
schedule_spawn()
@window.event

def on_key_press(symbol, modifiers):
	if symbol == key.LEFT and me.x>0:
		if me.jumping==0:
			step.stop()
			step.load("sounds/steps/"+str(randint(1,5))+".wav")
			step.play()
		me.x-=1
		positions()
	if symbol == key.RIGHT:
		if me.x<m.maxx:
			if me.jumping==0:
				step.stop()
				step.load("sounds/steps/"+str(randint(1,5))+".wav")
				step.play()
			me.x+=1
			positions()
	if symbol == key.H:
		speak(str(int(me.health))+" HP")
	if symbol == key.L:
		speak("You are fighting level "+str(int(en.level))+" enemies.")
	if symbol == key.SPACE:
		gun.stop()
		gun.play()
		attackenemy()
	if symbol == key.C:
		speak(str(int(me.x))+" of "+str(m.maxx))
	if symbol == key.UP and me.jumping==False:
		jump.stop()
		jump.play()
		me.jumping=1
		schedule_land()
pyglet.app.run()