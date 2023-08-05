from icecream import ic
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


class DropDownItem(ButtonBehavior, Label):
    color = ColorProperty([0, 0, 0, 1])
    text = StringProperty()
    bg_color = ListProperty([1, 1, 1, 1])

    def get_current_bg_color(self):
        print(self.state)
        if self.state == "normal":
            return self.bg_color
        else:
            return [
                self.bg_color[0] * 0.8,
                self.bg_color[1] * 0.8,
                self.bg_color[2] * 0.8,
                1,
            ]

    current_bg_color = AliasProperty(get_current_bg_color, bind=["state", "bg_color"])


# fmt: off
Builder.load_string("""
<DropDownItem>:
    size_hint_y: None
    height: dp(50)

    canvas.before:
        Color:
            rgba: root.current_bg_color or white
        Rectangle:
            size: self.size
            pos: self.pos

        Color:
            rgba: black
        Line:
            width: 1
            points: self.x, self.y+self.height, self.x+self.width, self.y+self.height

        Color:
            rgba: black
        Line:
            width: 1
            points: self.x, self.y, self.x, self.y+self.height

        Color:
            rgba: black
        Line:
            width: 1
            points: self.x+self.width, self.y, self.x+self.width, self.y+self.height
""")
# fmt: off



class CDropDown(Spinner):
    values = ListProperty()
    text_autoupdate = BooleanProperty(False)
    dropdown_cls = ObjectProperty(DropDown)
    is_open = BooleanProperty(False)

    def __init__(self, **kwargs):
        self._dropdown = None
        super(Spinner, self).__init__(**kwargs)
        fbind = self.fbind
        build_dropdown = self._build_dropdown
        fbind("on_release", self._toggle_dropdown)
        fbind("dropdown_cls", build_dropdown)
        fbind("values", self._update_dropdown)
        fbind("text_autoupdate", self._update_dropdown)
        build_dropdown()

    def _build_dropdown(self, *largs):
        print("build dropdown")
        if self._dropdown:
            self._dropdown.unbind(on_select=self._on_dropdown_select)
            self._dropdown.unbind(on_dismiss=self._close_dropdown)
            self._dropdown.dismiss()
            self._dropdown = None
        cls = self.dropdown_cls
        if isinstance(cls, str):
            cls = Factory.get(cls)
        self._dropdown = cls()
        self._dropdown.bind(on_select=self._on_dropdown_select)
        self._dropdown.bind(on_dismiss=self._close_dropdown)
        self._update_dropdown()

    def _update_dropdown(self, *largs):
        """
        Update the dropdown with the values. Each value is a dict with the
        following keys:
            - text: text displayed in the dropdown
            - viewclass: class used for displaying the text
            - anything else: added as an attribute to the viewclass

        """
        dp = self._dropdown
        values: dict[str:str] = self.values
        text_autoupdate = self.text_autoupdate
        dp.clear_widgets()
        for value in values:
            classname = value.get("viewclass")

            if not classname:
                classname = "DropDownItem"
            value.pop("viewclass", None)
            cls = Factory.get(classname)
            item = cls(**value)
            item.size_hint_y = None

            height = value.get("height")
            if height or hasattr(cls, "height"):
                item.height = height or item.height
            else:
                item.height = self.height
            item.bind(on_release=lambda option: dp.select(option.text))
            dp.add_widget(item)
        if text_autoupdate:
            if values:
                if not self.text or self.text not in values:
                    self.text = values[0]
            else:
                self.text = ""

    def _toggle_dropdown(self, *largs):
        if self.values:
            self.is_open = not self.is_open

    def _close_dropdown(self, *largs):
        self.is_open = False

    def _on_dropdown_select(self, instance: object, text: str, *largs):
        """
        Callback called when the dropdown select an option.
        e.g.: data = {'text': 'option1', 'viewclass': 'MyOption'}
        """
        self.text = text
        self.is_open = False

    def on_is_open(self, instance, value):
        if value:
            self._dropdown.open(self)
        else:
            if self._dropdown.attach_to:
                self._dropdown.dismiss()
