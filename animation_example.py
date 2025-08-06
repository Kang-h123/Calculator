from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, SwapTransition
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation



class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button1 = Button(text = "1", background_normal = "", background_down = "", background_color = (0.93, 0.90, 0.67, 0.67))
        self.button1.on_press = self.pressed14
        button2 = Button(text = "2", background_normal = "", background_down = "", background_color = (0.80, 0.51, 0.52, 0.67))
        button2.on_press = self.pressed2
        self.button3 = Button(text = "3", background_normal = "", background_down = "", background_color = (0.67, 0.77, 0.65, 0.67))
        self.button4 = Button(text = "4", background_normal = "", background_down = "", background_color = (0.34, 0.60, 0.71, 0.67))
        self.button4.on_press = self.pressed14

        vlayout = BoxLayout(orientation="vertical")
        hlayout1 = BoxLayout(orientation="horizontal", padding = 16, spacing = 16)
        hlayout2 = BoxLayout(orientation="horizontal", padding = 16, spacing = 16)

        hlayout1.add_widget(self.button1)
        hlayout1.add_widget(button2)
        hlayout2.add_widget(self.button3)
        hlayout2.add_widget(self.button4)
        vlayout.add_widget(hlayout1)
        vlayout.add_widget(hlayout2)

        self.add_widget(vlayout)

    def pressed14(self):
        self.old_button1_x = self.button1.x
        self.old_button1_y = self.button1.y
        self.old_button4_x = self.button4.x
        self.old_button4_y = self.button4.y
        anim = Animation(x=self.old_button4_x, y=self.old_button4_y, duration = 0.2)
        anim.start(self.button1)
        anim = Animation(x=self.old_button1_x, y=self.old_button1_y, duration = 0.2)
        anim.start(self.button4)


    def pressed2(self):
        self.old_button3_x = self.button3.x
        self.old_button3_y = self.button3.y
        self.old_button3_background_color = self.button3.background_color
        anim = Animation(x=0, y=0, background_color = (0.74, 0.54, 0.67, 0.67), duration = 0.5)
        anim.on_complete = self.next_animation3  
        anim.start(self.button3)
       

    def next_animation3(self, widget):
        anim = Animation(x=self.old_button3_x, y=self.old_button3_y, background_color = self.old_button3_background_color, duration = 0.5)
        anim.start(self.button3)

class AnimExample(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name = "screen1"))
        return sm
    
app = AnimExample()
app.run()   
