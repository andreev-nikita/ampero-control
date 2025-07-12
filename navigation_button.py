from .button import Button

class NavigationButton(Button):
    def __init__(self, control_surface, cc_note, direction, channel = 0):
        self._direction = direction
        super().__init__(control_surface=control_surface, cc_note=cc_note, channel=channel)
        self._add_listener(self._on_button_press)

    def _on_button_press(self):
        if (self._direction == 'left'):
            self._control_surface.application.view.scroll_view(2, "Session", False)
        elif (self._direction == 'right'):
            self._control_surface.application.view.scroll_view(3, "Session", False)
        elif (self._direction == 'up'):
            self._control_surface.application.view.scroll_view(0, "Session", False)
        elif (self._direction == 'down'):
            self._control_surface.application.view.scroll_view(1, "Session", False)
