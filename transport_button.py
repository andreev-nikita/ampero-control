from .button import Button

class TransportButton(Button):
    def __init__(self, control_surface, cc_note, type, channel = 0):
        self._type = type
        super().__init__(control_surface=control_surface, cc_note=cc_note, channel=channel)
        self._add_listener(self._on_button_press)

    def _on_button_press(self):
        if (self._type == 'play'):
            self._song.start_playing()
        elif (self._type == 'stop'):
            self._song.stop_playing()
        elif (self._type == 'record'):
            self._song.record_mode = not self._song.record_mode