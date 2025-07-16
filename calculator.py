from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="1 + 2", font_size="40sp")
        button_1 = Button(text="1", font_size="40sp")
        button_1.on_press = self.click_1
        button_2 = Button(text="2", font_size="40sp")
        button_2.on_press = self.click_2
        button_3 = Button(text="3", font_size="40sp")
        button_3.on_press = self.click_3
        button_plus = Button(text="+", font_size="40sp")
        button_plus.on_press = self.click_plus
        button_4 = Button(text="4", font_size="40sp")
        button_4.on_press = self.click_4
        button_5 = Button(text="5", font_size="40sp")
        button_5.on_press = self.click_5
        button_6 = Button(text="6", font_size="40sp")
        button_6.on_press = self.click_6
        button_minus = Button(text="-", font_size="40sp")
        button_minus.on_press = self.click_minus
        button_7 = Button(text="7", font_size="40sp")
        button_8 = Button(text="8", font_size="40sp")
        button_9 = Button(text="9", font_size="40sp")
        button_multiply = Button(text="*", font_size="40sp")
        button_0 = Button(text="0", font_size="40sp")
        button_C = Button(text="C", font_size="40sp")
        button_C.on_press = self.click_C
        button_equals = Button(text="=", font_size="40sp")
        button_divide = Button(text="/", font_size="40sp")
       

        layout = BoxLayout(orientation="vertical")
        row1 = BoxLayout(orientation="horizontal")
        row2 = BoxLayout(orientation="horizontal")
        row3 = BoxLayout(orientation="horizontal")
        row4 = BoxLayout(orientation="horizontal")

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

        layout.add_widget(self.label)
        layout.add_widget(row1)
        layout.add_widget(row2)
        layout.add_widget(row3)
        layout.add_widget(row4)

        self.add_widget(layout)

    def click_1(self):
        self.label.text = "1"
    def click_2(self):
        self.label.text = "2"
    def click_3(self):
        self.label.text = "3"
    def click_plus(self):
        self.label.text = "+"
    def click_4(self):
        self.label.text = "4"
    def click_5(self):
        self.label.text = "5"
    def click_6(self):
        self.label.text = "6"
    def click_minus(self):
        self.label.text = "-"
        
    def click_C(self):
        self.label.text = ""
         
class Calculator(App):
    def build(self):
            sm = ScreenManager()
            sm.add_widget(Screen1())
            #sm.add_widget(Screen2())
            #sm.add_widget(Screen3())
            #sm.add_widget(Screen4())
            return sm
    
app = Calculator()
app.run()