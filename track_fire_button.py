from .button import Button

class TrackFireButton(Button):
    def __init__(self, control_surface, cc_note, track_index, channel = 0):
        self._track_index = track_index
        super().__init__(control_surface=control_surface, cc_note=cc_note, channel=channel)
        self._add_listener(self._on_button_press)

    def _on_button_press(self):
        if (self._is_any_clip_recording):
            self._stop_any_clip_recording()
        else:
            self._disarm_all_tracks()
            self._arm_target_track()
            self._fire_target_clip()
    
    def _stop_any_clip_recording(self):
         for track in self._song.tracks:
            for clip_slot in track.clip_slots:
                if (clip_slot.is_recording):
                    clip_slot.fire()
                    
    def _disarm_all_tracks(self):
        for track in self._song.tracks:
            track.arm = False

    def _arm_target_track(self):
        if (self._target_track and self._target_track.can_be_armed):
            self._target_track.arm = True

    def _fire_target_clip(self):
        if (self._target_clip_slot):
            self._target_clip_slot.fire()

    @property
    def _target_track(self):
        return self._song.tracks[self._track_index]

    @property
    def _target_clip_slot(self):
        current_scene_index = list(self._song.scenes).index(self._song.view.selected_scene)
        return self._target_track.clip_slots[current_scene_index]

    @property
    def _is_any_clip_recording(self):
        for track in self._song.tracks:
            for clip_slot in track.clip_slots:
                if (clip_slot.is_recording):
                    return True
        return False