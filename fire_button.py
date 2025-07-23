from .button import Button

class FireButton(Button):
    def __init__(self, control_surface, cc_note, channel = 0):
        super().__init__(control_surface=control_surface, cc_note=cc_note, channel=channel)
        self._add_listener(self._on_button_press)

    def _on_button_press(self):
        current_scene_index = list(self._song.scenes).index(self._song.view.selected_scene)
        clip_slots = self._song.view.selected_track.clip_slots

        if (current_scene_index < len(clip_slots)):
            target_clip_slot = clip_slots[current_scene_index]
            if (target_clip_slot):
            	target_clip_slot.fire()
