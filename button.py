from ableton.v2.control_surface.input_control_element import InputControlElement, MIDI_CC_TYPE

class Button():
    def __init__(self, control_surface, cc_note, channel = 0):
        self._control_surface = control_surface
        self._cc_note = cc_note
        self._channel = channel
        self._button = InputControlElement(
            msg_type=MIDI_CC_TYPE,
            channel=channel,
            identifier=cc_note,
            send_midi=control_surface._c_instance.send_midi,
            register_control=control_surface._register_control
        )

    def _handle_button_press(self, value):
        if (value > 0):
            self._callback()

    def _add_listener(self, callback):
        self._callback = callback
        self._button.add_value_listener(self._handle_button_press)
    
    @property
    def _song(self):
        return self._control_surface.song
