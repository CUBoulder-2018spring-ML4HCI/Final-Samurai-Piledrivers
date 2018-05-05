# Final-Samurai-Piledrivers
Control specific games with controller for different abilities of movement

## Video
https://youtu.be/G5DaMzXrImA

## Dependencies
All can be installed with pip:
- `pythonosc` to control Wekinator from UI, revice messages from Wekinator
- `pyautogui` to send keystrokes to emulator

At the current state of this project Windows is required to run the python scripts

## Emulator
We used the [snes9x](https://chrome.google.com/webstore/detail/super-nintendo-emulator-s/ckpjobcmemfpfeaeolhhjkjdpfnkngnd?hl=en) Super Nintendo Emulator for chrome along with a ROM (this is in the repo) for street fighter to play the game.

## Running the Program
Basic summary of instructions to use our application
1. Open both Wekinator projects in Myoband Wekinato Proj
2. Move to UI directory: `cd UI\ things/` then run `python UI.py`
3. Go to Build Schema, follow instructions to train wekinator model
4. Launch and run myo_smoothing_pde.pde and microbit_3to5Inputs.pde processing scripts.
5. Launch the game from the UI
6. Run `python temp.py`
7. Make sure the SNES emulator is in focus on computer, the game is ready to be played


