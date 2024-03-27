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

This is a passion project, made independently, and exclusively by two high school students: [WhenLifeHandsYouLemons](https://github.com/WhenLifeHandsYouLemons) and [DreamingElectricSheep](https://github.com/DreamingElectricSheep). 

This project is our creation of a LED light wall-- Essentially a large screen that is able to display pretty much anything-- just like the screens on your phone, computer or TV. We've specialized ours to act as a sort of visual spectacle, inpired by the likes of Fireworks, Lazershows, and Nanoleafs. Our LED light wall displays a continous flow of random [patterns](#features)-- largely inspired by natural patterns like waves, which can also be controlled via ultrasonic sensors. This GitHub repository contains all of the code and documentation throughout the development of our project.

This enourmous project took more than a year to complete, covering far more than just the scope of Computer Science and Programming-- Enginnering, Design, Electronics, Modeling, Planning and of course, Programming and Mathematics were all integral processes in the creation of this project.

The documentation is hosted at: <https://whenlifehandsyoulemons.github.io/LED-Light-Wall/>.

This project was initially in a private repository and on May 24, 2023, it was moved to a new public repository and so much of the git history isn't present here.

## Installation

To install this project, you will need to clone the repository and then install the dependencies. To do this, run the following commands on a Raspberry Pi (RPi 3 or newer with Raspberry Pi OS installed):

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
cd LED-Light-Wall/Testing\ Version
python pygame_main.py
```

**Note**: The testing version lacks full parity with the physical version. It is only used to test patterns that can be precomputed. Images, text, ultrasonic sensors, and graphics are not supported in the testing version. The testing version doesn't include the same number of erroneous data checks as the physical version so unseen errors may occur when porting to the physical version.

## Features

- Displays a multitude of extensively customizable patterns and graphics, both continious and static:
  - [Circular waves](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/precomputations.py#L83)
  - [Square waves](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/precomputations.py#L18)
  - [Normal waves](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/precomputations.py#L162)
  - [Rain drops](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/precomputations.py#L197)
  - [Lines](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/precomputations.py#L210)
  - [Circles](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/graphics.py#L40)
  - [Rectangles](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/graphics.py#L31)
  - [Scrolling text](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/graphics.py#L51)
  - [Images](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/sblob/main/images.py)
- [Ultrasonic sensors](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/ultrasonics.py)
  - Uses ultrasonic sensors to detect when an object is near the board and starts a different pattern.
- [Power saving mode](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/blob/main/rpi_main.py#L111)
  - Turns off the display on certain days and at certain times to conserve power.
- [Includes a testing version](https://github.com/WhenLifeHandsYouLemons/LED-Light-Wall/tree/main/Testing%20Version)
  - Can be used to test patterns without the need for a physical board.




[Back to top](#led-light-wall-project)