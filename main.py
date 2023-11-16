from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.6})
        icon_btn = MDIconButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        float_btn = MDFloatingActionButton(icon='android', md_bg_color='orange',
                                           pos_hint={'center_x': 0.5, 'center_y': 0.4})
        flat_btn = MDFlatButton(text="Sign In", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        screen.add_widget(icon_btn)
        screen.add_widget(btn_flat)
        screen.add_widget(float_btn)
        screen.add_widget(flat_btn)
        return screen


DemoApp().run()
