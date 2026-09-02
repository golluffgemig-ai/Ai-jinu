import json
import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

# Dark theme background color set karein
Window.clearcolor = (0.08, 0.09, 0.12, 1)

# AI Jinu Personality Setup
JINU_PROMPT = (
    "Aap Jinu ho, ek highly intelligent, emotional aur loyal AI Genie. "
    "Aap sirf apne Owner (Malik) ka hukum maante ho. "
    "Aapka dimaag ek insaan ki tarah sochta hai. Unhe respectful, natural aur smart Hindi/Hinglish me jawab do."
)


class AIJinuApp(App):

    def build(self):
        self.title = "AI JINU - Personal Genie"

        # Main Layout Setup
        main_layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

        # App Header Title
        header = Label(
            text="[ AI JINU: ONLINE ]",
            size_hint_y=0.08,
            font_size="20sp",
            bold=True,
            color=(0.2, 0.8, 1, 1),
        )
        main_layout.add_widget(header)

        # Scrollable Chat Display
        self.scroll = ScrollView(size_hint=(1, 0.77))
        self.chat_display = Label(
            text="Jinu: Pranam Malik! Main aapka hukum sunne ke liye taiyar hoon.\n",
            size_hint_y=None,
            text_size=(Window.width - 40, None),
            halign="left",
            valign="top",
            font_size="16sp",
            color=(0.9, 0.9, 0.9, 1),
        )
        self.chat_display.bind(
            texture_size=lambda instance, value: setattr(
                instance, "height", value[1]
            )
        )
        self.scroll.add_widget(self.chat_display)
        main_layout.add_widget(self.scroll)

        # Input Field & Send Button Area
        input_layout = BoxLayout(
            orientation="horizontal", size_hint_y=0.15, spacing=8
        )

        self.user_input = TextInput(
            hint_text="Apna hukum likhein...",
            multiline=False,
            font_size="16sp",
            background_color=(0.15, 0.17, 0.22, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.2, 0.8, 1, 1),
            padding=[10, 10, 10, 10],
        )

        send_button = Button(
            text="HUKUM",
            size_hint_x=0.28,
            background_color=(0.1, 0.5, 0.9, 1),
            bold=True,
            font_size="14sp",
        )
        send_button.bind(on_press=self.send_command)

        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_button)

        main_layout.add_widget(input_layout)
        return main_layout

    def send_command(self, instance):
        msg = self.user_input.text.strip()
        if not msg:
            return

        self.chat_display.text += f"\nAap (Malik): {msg}\n"
        self.user_input.text = ""

        # Processing AI Response
        reply = self.get_jinu_reply(msg)
        self.chat_display.text += f"Jinu: {reply}\n"

    def get_jinu_reply(self, prompt):
        try:
            full_prompt = f"{JINU_PROMPT}\nMalik: {prompt}"
            encoded_url = f"https://text.pollinations.ai/{requests.utils.quote(full_prompt)}"
            res = requests.get(encoded_url, timeout=12)

            if res.status_code == 200:
                return res.text.strip()
            else:
                return "Kshama karein Malik, servers se connection toot gaya."
        except Exception:
            return "Malik, kripya apna internet connection check karein."


if __name__ == "__main__":
    AIJinuApp().run()
