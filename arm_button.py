from .button import Button

class ArmButton(Button):
    def __init__(self, control_surface, cc_note, channel = 0):
        super().__init__(control_surface=control_surface, cc_note=cc_note, channel=channel)
        self._add_listener(self._on_button_press)

    def _on_button_press(self):
        selected_track = self._song.view.selected_track
        if (selected_track.can_be_armed):
            selected_track.arm = not selected_track.arm
