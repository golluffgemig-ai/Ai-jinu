import json
import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

# App ka background color set karein
Window.clearcolor = (0.08, 0.09, 0.12, 1)

# AI Jinu Personality Prompt
JINU_PROMPT = (
    "Aap Jinu ho, ek highly intelligent, loyal, aur persona-driven AI assistant."
    " Aap sirf apne Owner (Malik) ka hukum mante ho."
    " Aapka dimaag ek insaan ki tarah sochta hai. Apne malik ko hamesha respect aur loyalty se answer do."
)

class JinuApp(App):
    def build(self):
        self.title = "AI Jinu"
        
        # Main Layout
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header / Title Label
        title_label = Label(
            text="[b]AI JINU[/b]\n[size=12]Your Personal Smart Assistant[/size]",
            markup=True,
            size_hint_y=None,
            height=60,
            color=(0.2, 0.7, 1, 1),
            halign='center'
        )
        main_layout.add_widget(title_label)
        
        # Chat Scroll View
        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat_history = Label(
            text="[b]Jinu:[/b] Haan Malik! Hukm karein, main aapki kya seva karoon?\n\n",
            markup=True,
            size_hint_y=None,
            color=(0.9, 0.9, 0.9, 1),
            valign='top',
            halign='left'
        )
        self.chat_history.bind(size=self.update_text_width)
        self.scroll.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll)
        
        # Input Section
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        self.user_input = TextInput(
            hint_text="Apna hukum likhein, Malik...",
            multiline=False,
            background_color=(0.15, 0.17, 0.22, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.2, 0.7, 1, 1),
            padding=[10, 12, 10, 10]
        )
        self.user_input.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text="Send",
            size_hint_x=None,
            width=80,
            background_color=(0.2, 0.6, 1, 1),
            background_normal='',
            bold=True
        )
        send_btn.bind(on_release=self.send_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        
        main_layout.add_widget(input_layout)
        return main_layout

    def update_text_width(self, instance, value):
        self.chat_history.text_size = (self.chat_history.width - 20, None)
        self.chat_history.height = self.chat_history.texture_size[1]
        self.scroll.scroll_y = 0

    def send_message(self, instance):
        query = self.user_input.text.strip()
        if not query:
            return
        
        # Add user query to chat
        self.chat_history.text += f"[b]Aap:[/b] {query}\n"
        self.user_input.text = ""
        
        # Get AI Response from Pollinations API
        try:
            prompt_text = f"{JINU_PROMPT}\n\nMalik: {query}\nJinu:"
            url = f"https://text.pollinations.ai/{requests.utils.quote(prompt_text)}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                reply = response.text.strip()
            else:
                reply = "Kshama karein Malik, server se sampark nahi ho pa raha hai."
        except Exception:
            reply = "Network error! Kripya apna internet connection jaanch lein."
            
        self.chat_history.text += f"[b]Jinu:[/b] {reply}\n\n"

if __name__ == "__main__":
    JinuApp().run()
