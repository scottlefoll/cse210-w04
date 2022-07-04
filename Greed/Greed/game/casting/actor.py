from game.shared.color import Color
from game.shared.point import Point


class Actor:
    """A visible, moveable thing that participates in the game.

    The responsibility of Actor is to keep track of its appearance, position
    and velocity in 2d space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._score = 0

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).

        Returns:
            Color: The actor's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the actor's font size.

        Returns:
            Point: The actor's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the actor's position in 2d space.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_text(self):
        """Gets the actor's textual representation.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_score(self):
        """Gets the actor's score.

        Returns:
            int: The actor's score.
        """
        return self._score

    def get_velocity(self):
        """Gets the actor's speed and direction.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity.
        Will wrap the position from one side of the screen to the other when
        it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        sp = self._position
        sv = self._velocity
        x = (sp.get_x() + sv.get_x()) % max_x
        y = (sp.get_y() + sv.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.

        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.

        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_font_size(self, font_size):
        """Updates the font size to the given one.

        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size

    def set_text(self, text):
        """Updates the text to the given value.

        Args:
            text (string): The given value.
        """
        self._text = text

    def set_score(self, value):
        """Updates the score to the given one.

        Args:
            value (int): the value to increment or decrement the score by - 
            a positive value for a gem or a negative value for a stone
        """
        input("Score: " + str(self._score))
        self._score += value

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.

        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
