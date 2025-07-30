from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, SwapTransition
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="", font_size="40sp")
        button_1 = Button(text="1", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_1.on_press = lambda: self.append_char("1")
        button_2 = Button(text="2", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_2.on_press = lambda: self.append_char("2")
        button_3 = Button(text="3", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_3.on_press = lambda: self.append_char("3")
        button_plus = Button(text="+", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_plus.on_press = lambda: self.append_char("+")
        button_4 = Button(text="4", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_4.on_press = lambda: self.append_char("4")
        button_5 = Button(text="5", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_5.on_press = lambda: self.append_char("5")
        button_6 = Button(text="6", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_6.on_press = lambda: self.append_char("6")
        button_minus = Button(text="-", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_minus.on_press = lambda: self.append_char("-")
        button_7 = Button(text="7", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_7.on_press = lambda: self.append_char("7")
        button_8 = Button(text="8", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_8.on_press = lambda: self.append_char("8")
        button_9 = Button(text="9", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_9.on_press = lambda: self.append_char("9")
        button_multiply = Button(text="*", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_multiply.on_press = lambda: self.append_char("*")
        button_0 = Button(text="0", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_0.on_press = lambda: self.append_char("0")
        button_C = Button(text="C", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_C.on_press = self.clear
        button_equals = Button(text="=", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_equals.on_press = self.equals
        button_divide = Button(text="/", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_divide.on_press = lambda: self.append_char("/")
        button_bracketl = Button(text="(", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_bracketl.on_press = lambda: self.append_char("(")
        button_bracketr = Button(text=")", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_bracketr.on_press = lambda: self.append_char(")")
        button_square = Button(text="^", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_square.on_press = lambda: self.append_char("**")
        button_root = Button(text="\u221a", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_root.on_press = lambda: self.append_char("**0.5")
        button_history = Button(text="History", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_history.on_press = self.next_screen

        layout = BoxLayout(orientation="vertical")
        row1 = BoxLayout(orientation="horizontal", spacing=10, padding=5)
        row2 = BoxLayout(orientation="horizontal", spacing=10, padding=5)
        row3 = BoxLayout(orientation="horizontal", spacing=10, padding=5)
        row4 = BoxLayout(orientation="horizontal", spacing=10, padding=5)
        row5 = BoxLayout(orientation="horizontal", spacing=10, padding=5)
        row6 = BoxLayout(orientation="horizontal", spacing=10, padding=5)

        row1.add_widget(button_1)
        row1.add_widget(button_2)
        row1.add_widget(button_3)
        row1.add_widget(button_plus)

        row2.add_widget(button_4)
        row2.add_widget(button_5)
        row2.add_widget(button_6)
        row2.add_widget(button_minus)

        row3.add_widget(button_7)
        row3.add_widget(button_8)
        row3.add_widget(button_9)
        row3.add_widget(button_multiply)

        row4.add_widget(button_0)
        row4.add_widget(button_C)
        row4.add_widget(button_equals)
        row4.add_widget(button_divide)

        row5.add_widget(button_bracketl)
        row5.add_widget(button_bracketr)
        row5.add_widget(button_square)
        row5.add_widget(button_root)

        row6.add_widget(button_history)

        layout.add_widget(self.label)
        layout.add_widget(row1)
        layout.add_widget(row2)
        layout.add_widget(row3)
        layout.add_widget(row4)
        layout.add_widget(row5)
        layout.add_widget(row6)

        self.add_widget(layout)

    def next_screen(self):
        self.manager.transition = SlideTransition(direction="left", duration=.2)
        self.manager.current ="screen2"

    def append_char(self, c):
        self.label.text += c
    def clear(self):   
        self.label.text = ""
    def equals(self):
        equal = str(eval(self.label.text))
        self.label.text = equal
        
class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="History", font_size="40sp")
        button_return = Button(text="Return", font_size="40sp", background_color=(1, 0.5, 1, 0.5), color=(0.5, 1, 1, 0.5), background_normal="", background_down="")
        button_return.on_press = self.next_screen
        
        
        layout = BoxLayout(orientation="vertical")
        row0 = BoxLayout(orientation="horizontal", spacing=10, padding=5) 
        row0.add_widget(button_return)
        layout.add_widget(self.label)
        layout.add_widget(row0)

        self.add_widget(layout)

    def next_screen(self):
        self.manager.transition = SlideTransition(direction="right", duration=.2)
        self.manager.current ="screen1"


class Calculator(App):
    def build(self):
            sm = ScreenManager()
            sm.add_widget(Screen1(name = "screen1"))
            sm.add_widget(Screen2(name = "screen2"))
            return sm


calculation_history = []
    
app = Calculator()
app.run()