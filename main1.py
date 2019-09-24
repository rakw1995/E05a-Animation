"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade #imports arcade, which is used for 2d games

SCREEN_WIDTH = 640#sets width of window to 640
SCREEN_HEIGHT = 480#sets height of game windwo to 480
SCREEN_TITLE = "Move Mouse Example"#the title will show at top of window


class Ball:#this is the class of the object
    def __init__(self, position_x, position_y, radius, color):#initializes the ball and its attributes

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #location on x axis
        self.position_y = position_y #location on y axis
        self.radius = radius #radius of ball
        self.color = color #color of ball

    def draw(self):#defines the rendering
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) #renders ball


class MyGame(arcade.Window): #class of the game window

    def __init__(self, width, height, title): #initializes game and attributes

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #background set to gray

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN) #ball size and color

    def on_draw(self): #drawing ball in windwo
        """ Called whenever we need to draw the window. """
        arcade.start_render() #starts render the ball in window
        self.ball.draw() #draws ball in window

    def on_mouse_motion(self, x, y, dx, dy): #what happens when mouse moves
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x #ball position follows mouse position on x axis
        self.ball.position_y = y #ball position follows mouse position on y axis

    def on_mouse_press(self, x, y, button, modifiers): #defines what happens when mouse button is pressed
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}") #prints text in terminal when button pressed
        if button == arcade.MOUSE_BUTTON_LEFT: #if the button is left mouse button
            self.ball.color = arcade.color.BLACK #ball turns black

    def on_mouse_release(self, x, y, button, modifiers): #when you release mouse button
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: #if release mouse button
            self.ball.color = arcade.color.AUBURN #ball turns auburn


def main(): #main game 
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #the window and its attributes
    arcade.run() #must be present to run


if __name__ == "__main__": #if main is open
    main() #main