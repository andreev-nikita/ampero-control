from ableton.v2.control_surface import ControlSurface
from ableton.v2.control_surface.input_control_element import InputControlElement, MIDI_CC_TYPE
from .track_fire_button import TrackFireButton
from .navigation_button import NavigationButton

BUTTONS_CONFIG = [
    { 'cc_note': 61, 'track': 0 },
    { 'cc_note': 62, 'track': 1 },
    { 'cc_note': 63, 'track': 2 },
    { 'cc_note': 64, 'track': 3 },
    { 'cc_note': 65, 'track': 4 },
    { 'cc_note': 66, 'track': 5 },
    { 'cc_note': 67, 'track': 6 },
    { 'cc_note': 68, 'track': 7 },
]

class AmperoControl(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance=c_instance)
        self.show_message("'AmperoControl' Control Surface has been loaded.")
        # self._track_fire_buttons = [TrackFireButton(self, button_config['cc_note'], button_config['track']) for button_config in BUTTONS_CONFIG]
        self.navigate_left_button = NavigationButton(self, 61, 'left')
        self.navigate_right_button = NavigationButton(self, 62, 'right')
        self.navigate_top_button = NavigationButton(self, 63, 'up')
        self.navigate_down_button = NavigationButton(self, 64, 'down')
        