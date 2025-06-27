from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

# Sample subject-teacher data (slots + teacher name)
subject_data = {
    "Complex Mathematics": [
        ("A2+TA2+TAA2", "RAJASEKARAN G"),
        ("A2+TA2+TAA2", "RADHIKA T"),
        ("A2+TA2+TAA2", "TAMIZHARASI R"),
        ("A2+TA2+TAA2", "ARUN CHOUDHARY"),
        ("A2+TA2+TAA2", "JAGADEESHKUMAR K"),
        ("A2+TA2+TAA2", "KAVITHA A"),
        ("A2+TA2+TAA2", "PALANIVEL K")
    ],
    "JAVA": [
        ("L3+L4+L29+L30", "SATHIYA KUMAR C"),
        ("L9+L10+L23+L24", "SIVA SANKARI S"),
        ("L9+L10+L27+L28", "VINILA JINNY"),
        ("L5+L6+L21+L22", "PRIYA G"),
        ("L3+L4+L21+L22", "JAISANKAR N")
    ],
    "DSA": [
        ("E2+TE2+L5+L6", "ANINDITA KUNDU"),
        ("E2+TE2+L3+L4", "KARTHIK G M"),
        ("E2+TE2+L15+L16", "ILANTHENRAL K P S K")
    ],
    "Discrete Mathematics": [
        ("C2+TC2+TCC2", "GOWSALYA M"),
        ("C2+TC2+TCC2", "MONICA C"),
        ("C2+TC2+TCC2", "ANKUSH CHANDA"),
        ("C2+TC2+TCC2", "MANIMARAN A"),
        ("C2+TC2+TCC2", "UMAKANTA MISHRA"),
        ("C2+TC2+TCC2", "CLEMENT J"),
        ("C2+TC2+TCC2", "AMRIT DAS")
    ],
    "DSD": [
        ("F2+TF2+L5+L6", "LAVANYA N"),
        ("F2+TF2+L5+L6", "HEMALATHA K"),
        ("F2+TF2+L9+L10", "ARUN DEV DHAR DWIVEDI")
    ]
}


def parse_slots(slot_str):
    return set(slot_str.replace('+', ' ').split())


class TeacherSelector(BoxLayout):
    selected_subjects = []
    selected_teachers = {}
    used_slots = set()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.subject_spinner = Spinner(
            text="Select subject order",
            values=list(subject_data.keys()),
            size_hint=(1, None),
            height=50
        )
        self.subject_order = []
        self.subject_spinner.bind(text=self.add_subject_to_order)
        self.add_widget(self.subject_spinner)

        self.subject_label = Label(text="\nSubject-wise Teacher Selection\n", size_hint=(1, 0.1))
        self.add_widget(self.subject_label)

        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.scroll_grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.scroll_grid.bind(minimum_height=self.scroll_grid.setter('height'))
        self.scroll.add_widget(self.scroll_grid)
        self.add_widget(self.scroll)

        self.btn_next = Button(text="Next", size_hint=(1, 0.1))
        self.btn_next.bind(on_press=self.proceed_to_next_subject)
        self.add_widget(self.btn_next)

    def add_subject_to_order(self, spinner, text):
        if text in self.subject_order:
            return
        self.subject_order.append(text)
        if len(self.subject_order) == len(subject_data):
            self.remove_widget(self.subject_spinner)
            self.subject_label.text = f"Choose teacher for: {self.subject_order[0]}"
            self.show_teachers_for_subject(0)

    def show_teachers_for_subject(self, index):
        self.scroll_grid.clear_widgets()
        subject = self.subject_order[index]
        for slots, name in subject_data[subject]:
            if not parse_slots(slots).intersection(self.used_slots):
                btn = Button(text=f"{name} [{slots}]", size_hint_y=None, height=60)
                btn.bind(on_press=lambda btn, s=subject, n=name, sl=slots: self.select_teacher(s, n, sl))
                self.scroll_grid.add_widget(btn)

    def select_teacher(self, subject, name, slots):
        self.selected_teachers[subject] = name + f" [{slots}]"
        self.used_slots.update(parse_slots(slots))
        next_index = self.subject_order.index(subject) + 1
        if next_index < len(self.subject_order):
            self.subject_label.text = f"Choose teacher for: {self.subject_order[next_index]}"
            self.show_teachers_for_subject(next_index)
        else:
            self.show_summary()

    def proceed_to_next_subject(self, instance):
        pass  # Placeholder if needed for future use

    def show_summary(self):
        content = "\n".join([f"{subj}: {self.selected_teachers.get(subj, 'Not Selected')}" for subj in self.subject_order])
        popup = Popup(title='Summary',
                      content=Label(text=content),
                      size_hint=(0.8, 0.8))
        popup.open()


class TeacherSelectorApp(App):
    def build(self):
        return TeacherSelector()


if __name__ == '__main__':
    TeacherSelectorApp().run()
