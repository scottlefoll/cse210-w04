"""
Greed Specification

Overview

Greed is a game in which the player seeks to gather as many falling gems as 
possible. The game continues as long as the player wants more!

Rules

Greed is played according to the following rules.

Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
The player (#) can move left or right along the bottom of the screen.
If the player touches a gem they earn a point.
If the player touches a rock they lose a point.
Gems and rocks are removed when the player touches them.
The game continues until the player closes the window.

Requirements
Your program must also meet the following requirements.

The program must have a README file.
The program must have at least eight classes.
Each module, class and method must have a corresponding comment.
The game must remain generally true to the order of play described earlier.

Have Some Fun
Make the game your own by enhancing it any way you like. Here are a few ideas.

Enhanced gems and rocks (multiple kinds, different points).
Enhanced player movement (up and down in a limited range)
Enhanced game play and game over messages.
Enhanced gem, rock and player representation (colors or better symbols)
Enhanced game play (more than one gem, more than one rock, etc.)"""

import os
import random

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
DEFAULT_VELOCITY = 1
COLS = 60
ROWS = 40
ROCK_VALUE = -1
GEM_VALUE = 1
DEFAULT_CAPTION = "Greed:  Score = "
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 30


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
    # y = int(MAX_Y / 2)
    y = MAX_Y - 20
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    caption = f"{DEFAULT_CAPTION} {robot.get_score()}"

    # create the Director, KeyboardService and VideoService
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(caption, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)

    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        # set the icon or image for each artifact
        if n % 2 == 0:
            newType = "gem"
            # text = chr(random.randint(33, 126))
            # text = "1F48E"  # 💎
            text = "G"
        else:
            newType = "stone"
            # text = chr(random.randint(33, 126))
            # "1FAA8"  🪨
            text = "S"

        message = messages[n]

        # set the start position for each artifact
        x = random.randint(1, COLS - 1)
        y = -1 * random.randint(1, ROWS - 1)
        # y = 2
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # set the color for each artifact
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # create the artifact & set the attributes
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_type(newType)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)

        ks = keyboard_service
        velocity = ks.get_direction("artifact")
        artifact.set_velocity(velocity)


    # start the game
    director.start_game(cast)


if __name__ == "__main__":
    main()