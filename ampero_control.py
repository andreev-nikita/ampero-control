from ableton.v2.control_surface import ControlSurface
from ableton.v2.control_surface.input_control_element import InputControlElement, MIDI_CC_TYPE
from .track_fire_button import TrackFireButton
from .navigation_button import NavigationButton
from .arm_button import ArmButton
from .fire_button import FireButton
from .transport_button import TransportButton

TRACK_FIRE_BUTTONS_CONFIG = [
    { 'cc_note': 20, 'track': 0 },
    { 'cc_note': 21, 'track': 1 },
    { 'cc_note': 22, 'track': 2 },
    { 'cc_note': 23, 'track': 3 },
    { 'cc_note': 24, 'track': 4 },
    { 'cc_note': 25, 'track': 5 },
    { 'cc_note': 26, 'track': 6 },
    { 'cc_note': 27, 'track': 7 },
]

class AmperoControl(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance=c_instance)
        self.show_message("'AmperoControl' Control Surface has been loaded.")
        self._track_fire_buttons = [TrackFireButton(self, config['cc_note'], config['track']) for config in TRACK_FIRE_BUTTONS_CONFIG] 
        self._navigate_left_button = NavigationButton(self, 28, 'left')
        self._navigate_right_button = NavigationButton(self, 29, 'right')
        self._navigate_up_button = NavigationButton(self, 30, 'up')
        self._navigate_down_button = NavigationButton(self, 31, 'down')
        self._arm_button = ArmButton(self, 85)
        self._fire_button = FireButton(self, 86)
        self._play_button = TransportButton(self, 87, 'play')
        self._stop_button = TransportButton(self, 88, 'stop')
        self._record_button = TransportButton(self, 89, 'record')