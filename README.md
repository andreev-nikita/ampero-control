# Hotone Ampero Control – Ableton Live Integration

This is an Ableton Remote Script for the Hotone Ampero Control. It allows you to assign various DAW functions (such as clips navigation, transport buttons, etc.) to the Ampero Control buttons without using MIDI mappings. Some of these functions aren't accessible even through MIDI mapping, so this script provides deeper integration of your device with the DAW.

## Support the Project

If you like this project, please consider giving it a ⭐️ — it helps others discover it!

If you find any bugs, feel free to open an [Issue](https://github.com/andreev-nikita/ampero-control/issues).  
Got feature requests or suggestions? Start a new [Discussion](https://github.com/andreev-nikita/ampero-control/discussions) — I’ll do my best to implement them when possible.

Thank you for your support!

## Script installation

1. Click the green "Code" button.
2. Select "Download ZIP".
3. Unzip the downloaded file.
4. Rename the root folder to "Ampero Control"
5. Follow this [guide](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts) to install the script.
6. Connect your device to the copmuter.
7. Launch Ableton Live.
8. Open the MIDI settings and make sure that "Ampero Control" is selected in the "Control Surface" list, and that the "Input" and "Output" fields are assigned to the "Ampero Control" device. If not, assign them manually.

## Ampero Control Setup

Now you need to bind the buttons to Ableton functions. Open the "Ampero Control" app and connect to the device.

To assign a button to one of the supported actions, configure it as follows:
- Mode: Momentary
- Add an "A Group" message
- CH. - 1, Type - CC, Data 1 - [ACTION_ID], Data 2 - 127, Output to - "USB"
- Save the preset

Now you can use your Ampero Control with Ableton Live.

## Supported actions

| ACTION_ID | Description |
| --- | --- |
| 87 | "Play" button. |
| 88 | "Stop" button. |
| 89 | "Record" button. |
| 85 | "Arm Recording" button. |
| 86 | "Fire" button. When in Session View, it allows you to record / play / stop the selected clip. |
| 28 | Clips navigation: usefull for the Session View. navigate left |
| 29 | Clips navigation: usefull for the Session View. navigate right |
| 30 | Clips navigation: usefull for the Session View. navigate up |
| 31 | Clips navigation: usefull for the Session View. navigate down |
| 20 - 27 | Live Looping buttons for the Session View. Each button is assigned to a different track(20 - first track, 21 - second track, etc.). When you press a button, the following actions occur. All currently armed for recording tracks become disarmed. The track assigned to the pressed button becomes armed for recording. Recording of the newly armed track begins. If your press the same button again (or another track button), the recording of the current clip stops.|