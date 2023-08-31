# LED Light Wall Project

## Contents

1. [Contents](#contents)
2. [About](#about)
3. [Installation](#installation)
4. [Usage](#usage)\
    a. [Physical Version](#physical-version)\
    b. [Testing Version](#testing-version)
5. [Features](#features)

## About

This project is our attempt at creating an LED light wall that can display random patterns and also be controlled via ultrasonic sensors. This GitHub repository contains all of the code and documentation throughout the deveolpment of our project.

The documentation is hosted at: "<https://whenlifehandsyoulemons.github.io/LED-Light-Wall/>".

This project was initially in a private repository and on May 24, 2023, it was moved to a new public repository.

## Installation

To install this project, you will need to clone the repository and then install the dependencies. To do this, run the following commands on a Raspberry Pi:

```console
git clone https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall.git
cd LED-Light-Wall
pip install requirements.txt
```

**Note**: If you want to get the file that was used to create the website, then run `split_join_bsdesign_file.py` (located inside the "*Others*" folder). It should create a new file called `LED Light Wall Website.bsdesign` which can be opened using [Bootstrap Studio](https://bootstrapstudio.io/).

## Usage

### Physical Version

To run this project with a physical board, you will need to run the `rpi_main.py` file. To do this, run the following command:

```console
cd LED-Light-Wall
sudo python3 rpi_main.py
```

**Note**: If you're using the [Thonny IDE](https://thonny.org/), you need to run the `rpi_main.py` file in sudo mode. To do so, run the `open_sudo_thonny.py` file first (located inside the "*RPi Files*" folder), then open the `rpi_main.py` file inside Thonny and run it.

### Testing Version

To run the testing version, you will need to run the `pygame_main.py` file (located inside the "*Testing Version*" folder). To do this, run the following command:

```console
cd LED-Light-Wall/Pygame\ Testing
python pygame_main.py
```

**Note**: The testing version lacks full parity with the physical version. It is only used to test patterns that can be precomputed. Images, text, ultrasonic sensors, and graphics are not supported in the testing version. The testing version doesn't include the same number of erroneous data checks as the physical version so unseen errors may occur when porting to the physical version.

## Features

- Displays a multitude of patterns and graphics:
  - Circular waves
  - Square waves
  - Full screen waves
  - Rain drops
  - Lines
  - Circles
  - Rectangles
  - Scrolling text
  - Images
- Ultrasonic sensors
  - Uses ultrasonic sensors to detect when an object is near the board and starts a different pattern.
- Power saving mode
  - Turns off the display on certain days and at certain times to conserve power.
- Includes a testing version
  - Can be used to test patterns without the need for a physical board.

[Back to top](#led-light-wall-project)
