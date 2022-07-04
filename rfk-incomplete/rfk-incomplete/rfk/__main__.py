"""RobotFindsKitten (Rfk) Specification
The smallest feline is a masterpiece.

- Leonardo da Vinci -
Overview
Rfk is a game in which the player seeks to find the kitten among many
artifacts. That's it!

Rules
Rfk is played according to the following rules.

Several artifacts are randomly positioned on the screen.
Each artifact has a randomly chosen symbol and message.
The player moves the robot (#) around the screen.
When the robot touches an artifact, the message is displayed.
If the robot touches the kitten, "You found kitten!" is displayed.
There is no winning, losing or game over. This is the zen of rfk.


Requirements

The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least eight classes.
The program must remain true to game play described in the overview.

Have Some Fun
Have some fun by enhancing the game any way you like. A few ideas are as
follows.

Enhanced input validation.
Enhanced game play and game over messages.
Enhanced game display, e.g. artifacts
"""

import os
import random
from xml.etree.ElementPath import get_parent_map

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
SPEED = 1
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        text = chr(random.randint(33, 126))
        message = messages[n]

        x = random.randint(1, COLS - 1)
        # y = random.randint(1, ROWS - 1)
        y = -1
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()