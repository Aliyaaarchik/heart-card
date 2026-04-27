from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.clock import Clock
import random, math, time

class Card(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drops = [random.randint(0, 40) for _ in range(120)]
        Clock.schedule_interval(self.update, 0.05)

    def heart(self, cx, cy, s):
        pts=[]
        for t in range(0,360,3):
            r=math.radians(t)
            x=16*math.sin(r)**3
            y=13*math.cos(r)-5*math.cos(2*r)-2*math.cos(3*r)-math.cos(4*r)
            pts += [cx+x*s, cy+y*s]
        Line(points=pts, width=2)

    def k(self, cx, cy, s):
        Line(points=[cx-10*s,cy-20*s,cx-10*s,cy+20*s], width=3)
        Line(points=[cx-10*s,cy,cx+15*s,cy+20*s], width=3)
        Line(points=[cx-10*s,cy,cx+15*s,cy-20*s], width=3)

    def rain(self):
        for i in range(len(self.drops)):
            x=i*10
            y=self.height-self.drops[i]*10
            if y<0: self.drops[i]=0
            else: self.drops[i]+=1
            Color(0,1,0,1)
            Rectangle(pos=(x,y), size=(8,8))

    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(0,0,0,1)
            Rectangle(pos=self.pos,size=self.size)
            self.rain()
            cx=self.width/2
            cy=self.height/2
            s=1.5+0.3*math.sin(time.time()*3)
            Color(0,1,0,1)
            self.heart(cx,cy,s)
            self.k(cx,cy,s)

class AppMain(App):
    def build(self):
        return Card()

AppMain().run()
