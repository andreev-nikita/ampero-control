from .button import Button

class ArmButton(Button):
    def __init__(self, control_surface, cc_note, channel = 0):
        super().__init__(control_surface=control_surface, cc_note=cc_note, channel=channel)
        self._add_listener(self._on_button_press)

    def _on_button_press(self):
        self._song.view.selected_track.arm = not self._song.view.selected_track.arm
