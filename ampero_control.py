from ableton.v2.control_surface import ControlSurface
from ableton.v2.control_surface.input_control_element import InputControlElement, MIDI_CC_TYPE

def make_cc_button(cs, cc_number, channel=0):
    return InputControlElement(
        msg_type=MIDI_CC_TYPE,
        channel=channel,
        identifier=cc_number,
        send_midi=cs._c_instance.send_midi,
        register_control=cs._register_control
    )

class AmperoControl(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance=c_instance)
        self.show_message("✅ AmperoControl loaded")

        # Создаем кнопки
        play_button = make_cc_button(self, 61)
        stop_button = make_cc_button(self, 63)
        record_button = make_cc_button(self, 66)

        # Привязываем кнопки к функциям напрямую
        play_button.add_value_listener(self._on_play_value)
        stop_button.add_value_listener(self._on_stop_value)
        record_button.add_value_listener(self._on_record_value)

    def _on_play_value(self, value):
        if value > 0:  # Нажатие кнопки
            self.song.start_playing()

    def _on_stop_value(self, value):
        if value > 0:  # Нажатие кнопки
            self.song.stop_playing()

    def _on_record_value(self, value):
        if value > 0:  # Нажатие кнопки
            # Получаем текущий выбранный трек
            selected_track = self.song.view.selected_track
            
            # Получаем текущий выбранный слот клипа
            selected_scene = self.song.view.selected_scene
            clip_slot = selected_track.clip_slots[list(self.song.scenes).index(selected_scene)]
            
            # Начинаем запись клипа
            if clip_slot.has_clip:
                clip_slot.fire()  # Если клип уже есть, запускаем его
            else:
                clip_slot.fire()  # Начинаем запись нового клипа