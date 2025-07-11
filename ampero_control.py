from ableton.v2.control_surface import ControlSurface
from ableton.v2.control_surface.input_control_element import InputControlElement, MIDI_CC_TYPE

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

class AmperoButton():
    def __init__(self, control_surface, cc_note, track, channel = 0):
        self._control_surface = control_surface
        self.cc_note = cc_note
        self.track = track
        self.channel = channel
        self._button = InputControlElement(
            msg_type=MIDI_CC_TYPE,
            channel=channel,
            identifier=cc_note,
            send_midi=control_surface._c_instance.send_midi,
            register_control=control_surface._register_control
        )

    def _handle_button_press(self, value):
        if (value > 0):
            self._callback(self)

    def add_listener(self, callback):
        self._callback = callback
        self._button.add_value_listener(self._handle_button_press)


class AmperoControl(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance=c_instance)
        self.show_message("✅ AmperoControl loaded")

        buttons = [AmperoButton(self, button_config['cc_note'], button_config['track']) for button_config in BUTTONS_CONFIG]

        for button in buttons:
            button.add_listener(self._handle_button_press)
        
        # Создаем кнопки
        # play_button = make_cc_button(self, 61)
        # stop_button = make_cc_button(self, 63)
        # record_button = make_cc_button(self, 66)

        # # # Привязываем кнопки к функциям напрямую
        # play_button.add_value_listener(self._on_play_value)
        # stop_button.add_value_listener(self._on_stop_value)
        # record_button.add_value_listener(self._on_record_value)

        #
        # self.song.add_is_playing_listener(self._on_test)

    def _set_target_track(self, track_index):
        self._target_track = self.song.tracks[track_index]

    def _set_target_clip(self, track_index):
        current_scene_index = list(self.song.scenes).index(self.song.view.selected_scene)
        self._target_clip_slot = self._target_track.clip_slots[current_scene_index]

    def _fire_target_clip(self):
        if (self._target_clip_slot):
            self._target_clip_slot.fire()

    def _is_target_track_armed(self):
        return self._target_track.arm
    
    def _is_any_clip_recording(self):
        for track in self.song.tracks:
            for clip_slot in track.clip_slots:
                if (clip_slot.is_recording):
                    return True
        return False
    
    def _stop_any_clip_recording(self):
         for track in self.song.tracks:
            for clip_slot in track.clip_slots:
                if (clip_slot.is_recording):
                    clip_slot.fire()
    
    def _disarm_all_tracks(self):
        for track in self.song.tracks:
            track.arm = False

    def _arm_target_track(self):
        if (self._target_track and self._target_track.can_be_armed):
            self._target_track.arm = True

    def _handle_button_press(self, button):
        self._set_target_track(button.track)
        self._set_target_clip(button.track)
        if (self._is_any_clip_recording()):
            self._stop_any_clip_recording()
        else:
            self._disarm_all_tracks()
            self._arm_target_track()
            self._fire_target_clip()



            

    # def _on_test(self):
    #     self.show_message("✅ AmperoControl metronome")
    #     self.song.metronome = not self.song.metronome
        # if (self.record_mode == 1):
        #      self.song.start_playing()

    # def get_recording_clip(self):
    #     for track in self.song.tracks:
    #         if track.can_be_armed and track.arm:
    #             for clip_slot in track.clip_slots:
    #                 if clip_slot.is_recording:
    #                     return clip_slot
    #     return None

    # def _on_play_value(self, value):
    #     track = self.song.tracks[0]
    #     if (not track.arm):
    #         track.arm = True
    #     current_scene_index = list(self.song.scenes).index(self.song.view.selected_scene)
    #     current_clip_slot = track.clip_slots[current_scene_index]
    #     current_clip_slot.fire()
        
    #     # self.song.metronome = not self.song.metronome
    #     # if value > 0:  # Нажатие кнопки
    #         # self.song.start_playing()

    # def _arm_new_track(self):
    #     track = self.song.tracks[1]
    #     if (not track.arm):
    #         track.arm = True
    #     self.song.tracks[0].arm = False

    #     current_scene_index = list(self.song.scenes).index(self.song.view.selected_scene)
    #     current_clip_slot = track.clip_slots[current_scene_index]
    #     current_clip_slot.fire()

    # def _playing_status_listener(self):
    #     self.show_message("✅ AmperoControl loaded")
    #     self.schedule_message(0, self._arm_new_track)
      

    # @listens('playing_status')
    # def _on_playing_status_changed(self):
    #     self.sdfasdfads("✅ AmperoControl loaded")
        # new_track = self.song.view.selected_track
        # self._on_arm_changed.subject = None  # Отписываемся от старого трека
        # self._track = new_track
        # self._on_arm_changed.subject = new_track  # Подписываемся на новый

    # def _on_stop_value(self, value):
    #     self._current_recording_clip = self.get_recording_clip()
    #     if (self._current_recording_clip):
    #         # self.show_message(str(self._current_recording_clip.playing_status))
    #         # self._on_playing_status_changed.subject = self._current_recording_clip
    #         self._current_recording_clip.clip.add_is_recording_listener(self._playing_status_listener)
    #         self._current_recording_clip.fire()
    #     # tracks = self.song.tracks
    #     # track = tracks[1]
    #     # clip = track.clip_slots[0]
    #     # track.arm = True
    #     # clip.fire()
    #     # if value > 0:  # Нажатие кнопки
    #     #     self.song.stop_playing()

    # def _on_record_value(self, value):
    #     track = self.song.tracks[2].implicit_arm = True
    #     self.show_message(str(self._current_recording_clip.playing_status))
        # if value > 0:  # Нажатие кнопки
        #     # Получаем текущий выбранный трек
        #     selected_track = self.song.view.selected_track
            
        #     # Получаем текущий выбранный слот клипа
        #     selected_scene = self.song.view.selected_scene
        #     clip_slot = selected_track.clip_slots[list(self.song.scenes).index(selected_scene)]
            
        #     # Начинаем запись клипа
        #     if clip_slot.has_clip:
        #         clip_slot.fire()  # Если клип уже есть, запускаем его
        #     else:
        #         clip_slot.fire()  # Начинаем запись нового клипа