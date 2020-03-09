import random
from Dict import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty



class MainWindow(Screen):
    player_python = ObjectProperty(None)
    output = StringProperty('')
    ##
    def spinner_clicked(self, value):
        return
    ###
    def btn(self):

        player = self.player_python.text

        weighted_list = list(character[player].keys())

        self.output = random.choice(weighted_list)

        self.player_python.text = 'Player'

        self.show_popup()

    def show_popup(self):

        popup_window = Popup(
            title='random character',
            content=Label(text=self.output),
            size_hint=(None, None),
            size=(400, 400)
        )

        popup_window.open()

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('working.kv')


class RandomCharacterApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    RandomCharacterApp().run()