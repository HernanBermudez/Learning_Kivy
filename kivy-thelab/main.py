
from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    estado = BooleanProperty(False)
    conteo = 0
    my_text = StringProperty("Como fue!")
    text_input_str = StringProperty("El Combazo")
    # slider_value_txt = StringProperty("")
    def on_toggle_button_state(self, widget):
        print("toggle state" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.estado = False
        else:
            widget.text = "ON"
            self.estado = True
    def on_button_click(self):
        print("Button clicked")
        if self.estado:
            self.conteo += 1
            self.my_text = str(self.conteo)
    def on_switch_active(self, widget):
        print("Switch" +str(widget.active))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        pass

    # def on_slider_value(self, widget):
      #  print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-bt"
        size = dp(100)
        for i in range(0,100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super(CanvasExample4, self).__init__(**kwargs)
        with self.canvas:
            Line(points = (100, 100, 400, 500 ), width = 2)
            Color(0, 1, 0)
            # Line(circle = (400, 200, 80), width = 2)
            #Line(rectangle=(700, 500, 150, 100), width=4)
            self.rect = Rectangle(pos = (400, 200), size = (150, 100))
            Color(0, 0, 1)
            Line(points = (100, 100, 600, 100), width = 2)
            Color(1, 1, 0)
            Rectangle(pos = (600, 100), size = (150, 80))

    def on_button_a_click(self):
        x, y = self.rect.pos
        x += dp(10)
        # y += dp(10)
        if (x < self.width- 150):
            self.rect.pos = (x, y)
        else:
            x -= dp(10)
            self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super(CanvasExample5, self).__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            Color(1, 0, 0)
            self.ball = Ellipse(pos = (self.center), size = (self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        # print("on size: " +str(self.width) + "," +str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        #print("update")
        x, y = self.ball.pos
        x += self.vx
        y += self.vy

        if (x > self.width - 50 ):
            self.vx = - self.vx
        elif (y > self.height - 50):
            self.vy = - self.vy
        elif (y <= 1):
            self.vy = - self.vy
        elif (x <= 1):
            self.vx = - self.vx
        else:
            self.ball.pos = (x, y)

        # self.ball_size / self.width
        # self.vx = - self.vx

class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass

TheLabApp().run()