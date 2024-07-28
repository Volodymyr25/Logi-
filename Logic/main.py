from kivy.app import App  
from kivy.uix.label import Label  
from kivy.uix.button import Button  
from kivy.uix.textinput import TextInput  
from kivy.uix.screenmanager import ScreenManager,Screen  
from kivy.uix.floatlayout import FloatLayout 
from kivy.core.window import Window
from kivy.animation import Animation

class Zero(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_logika = Label(text = "Задачі на Logik'у", size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        lab_for_name = Label(text = "Введіть ім'я", size_hint = (0.25, 0.15), pos_hint ={'y':0.4, "x":0.12})
        name = TextInput(text = '', size_hint = (0.3, 0.05), pos_hint = {'y': 0.45, "x": 0.3 })
        lab_for_gmail = Label(text = "Введіть пошту", size_hint = (0.3, 0.05), pos_hint = {'y': 0.4, "x": 0.10})
        gmail = TextInput(text = "", size_hint = (0.3, 0.05), pos_hint = {'y': 0.40, "x": 0.3 })
        but_for_sec_win = Button(text = "Початок", size_hint = (0.2, 0.15), pos_hint ={'y':0.17, "x":0.4})

        line.add_widget(lab_logika)
        line.add_widget(lab_for_name)
        line.add_widget(name)
        line.add_widget(lab_for_gmail)
        line.add_widget(gmail)
        line.add_widget(but_for_sec_win)
        self.add_widget(line)

        but_for_sec_win.on_press = self.next
    def next(self):
        self.manager.transition.direction = "up"
        self.manager.current = "one"

class One(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q1 = Label(text = "Годинник показує чверть на 9.\n Який час буде показувати годинник через п'яту частину години?", size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q1_correct = Button(text = '8:27', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2 })
        q1_uncorrect_1 = Button(text = '8.30', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7 }) 
        q1_uncorrect_2 = Button(text = '8:37', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 })
        q1_uncorrect_3 = Button(text = '8.40', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7 })       

        line.add_widget(lab_q1)
        line.add_widget(q1_correct)
        line.add_widget(q1_uncorrect_1)
        line.add_widget(q1_uncorrect_2)
        line.add_widget(q1_uncorrect_3)
        self.add_widget(line)

        q1_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "down"
        self.manager.current = "two"

class Two(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q2 = Label(text = 'Щука важить 1кг та ще половину своєї маси.\nЯка загальна маса щуки?', size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q2_uncorrect_2 = Button(text = '1', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2})
        q2_uncorrect_1 = Button(text = '1.75', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7}) 
        q2_correct = Button(text = '2', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 })
        q2_uncorrect_3 = Button(text = '1.5', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7})

        line.add_widget(lab_q2)
        line.add_widget(q2_correct)
        line.add_widget(q2_uncorrect_1)
        line.add_widget(q2_uncorrect_2)
        line.add_widget(q2_uncorrect_3)
        self.add_widget(line)

        q2_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "right"
        self.manager.current = "three"

class Three(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q3 = Label(text = 'На дереві сиділи 2 білки, одна з них вирішила стрибнути по горішок.\n Скільки білок залишилось на дереві?', size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q3_uncorrect_2 = Button(text = '0', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2})
        q3_uncorrect_1 = Button(text = '1', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7}) 
        q3_correct = Button(text = '2', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 })
        q3_uncorrect_3 = Button(text = '3', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7})

        line.add_widget(lab_q3)
        line.add_widget(q3_uncorrect_2)
        line.add_widget(q3_uncorrect_1)
        line.add_widget(q3_correct)
        line.add_widget(q3_uncorrect_3)
        self.add_widget(line)

        q3_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "four"

class Four(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q4 = Label(text = 'Петро вирішив купити яблуко, але йому не вистачає 3 грн, Оленка теж хоче купити яблуко, але їй не вистачає 1 грн.\n Тоді Петро та Оленка вирішили купити одне яблуко на двох, але їм все одно не вистачає 1 грн. \n Скільки коштує яблуко?', size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q4_uncorrect_2 = Button(text = '1', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2})
        q4_uncorrect_1 = Button(text = '4', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7}) 
        q4_correct = Button(text = '3', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 })
        q4_uncorrect_3 = Button(text = '5', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7})

        line.add_widget(lab_q4)
        line.add_widget(q4_uncorrect_2)
        line.add_widget(q4_uncorrect_1)
        line.add_widget(q4_correct)
        line.add_widget(q4_uncorrect_3)
        self.add_widget(line)

        q4_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "right"
        self.manager.current = "five"

class Last(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        lab_q5 = Label(text = 'Дякую за проходження тесту. Результати прийдуть на gmail :)', size_hint = (0.2, 0.15), pos_hint ={'y':0.50, "x":0.4})

        line = FloatLayout()



        self.add_widget(lab_q5)
        self.add_widget(line)

class MyApp(App):
    def build(self):
        main_screen = ScreenManager()
        main_screen.add_widget(Zero(name = 'zero'))
        main_screen.add_widget(One(name = 'one'))
        main_screen.add_widget(Two(name = 'two'))
        main_screen.add_widget(Three(name = 'three'))
        main_screen.add_widget(Four(name = 'four'))
        main_screen.add_widget(Last(name = 'five'))
        return main_screen



app = MyApp()
app.run()