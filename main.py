from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.stacklayout import StackLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.config import Config

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')

class InputBit(ToggleButton):
    def __init__(self, name, **kwargs):
        super(InputBit, self).__init__(**kwargs)
        self.name = name
        self.active = False

    def on_press(self, *ignore):
        print(self.name)
        self.active = True
        with self.canvas:
            Color(1.,0,0, 0.5)
            Rectangle(pos=(self.center_x - 5, self.center_y - 5), size=(10,10))

def create_input_bits(n=12):
    buttonArgs = {'size': (50, 50),
                  'size_hint':(None, None)}
    return [InputBit(name=x, **buttonArgs) for x in range(n*n)]

class InputSpaceLayout(StackLayout):
    def __init__(self, **kwargs):
        super(InputSpaceLayout, self).__init__(**kwargs)
        self.orientation = 'lr-tb'
        self.spacing = 0
        self.padding = 0

        input_bits = create_input_bits()
        for bit in input_bits:
            self.add_widget(bit)


class ClaInsightApp(App):
    def build(self):
        return InputSpaceLayout()

if __name__ == '__main__':
    ClaInsightApp().run()
