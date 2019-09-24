"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade #imports arcade, which is used for 2d games

SCREEN_WIDTH = 640 #sets width of window to 640
SCREEN_HEIGHT = 480 #sets height of game windwo to 480
SCREEN_TITLE = "Move Keyboard Example" #the title will show at top of window
MOVEMENT_SPEED = 3 #this is the speed that the frames change


class Ball: #this is the class of the object
    def __init__(self, position_x, position_y, change_x, change_y, radius, color): #initializes the ball and its attributes

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #location on x axis
        self.position_y = position_y #location on y axis
        self.change_x = change_x #position change on x axis
        self.change_y = change_y #position change on y axis
        self.radius = radius #radius of the ball shape
        self.color = color #color of ball

    def draw(self): #defines the rendering
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) #renders the ball

    def update(self): #defines what updating does
        # Move the ball
        self.position_y += self.change_y #the ball changes position on y axis when keyboard arrow button(up down) is pressed
        self.position_x += self.change_x ##the ball changes position on x axis when keyboard arrow button(left right) is pressed

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius: #if the position on x axis less than radius
            self.position_x = self.radius #can not move past radius on x axis

        if self.position_x > SCREEN_WIDTH - self.radius: #if the ball location is to go past the width of screen
            self.position_x = SCREEN_WIDTH - self.radius #the ball will stop at the width and the radius will not go past corners

        if self.position_y < self.radius: #if position of ball is less than radius on y axis
            self.position_y = self.radius #cannot move past radius on y axis

        if self.position_y > SCREEN_HEIGHT - self.radius: #if ball location is to go past height of screen
            self.position_y = SCREEN_HEIGHT - self.radius #ball will stop at corner so that the radius of ball from all sides will be shown


class MyGame(arcade.Window): #the class of the game window

    def __init__(self, width, height, title): #initializes window and its attributes

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #background set to grey

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN) #size and color of ball

    def on_draw(self): #drawing ball in window
        """ Called whenever we need to draw the window. """
        arcade.start_render() #renders the window
        self.ball.draw() #draws ball in window

    def update(self, delta_time): #moving ball at a certain speed according to update
        self.ball.update() #update ball

    def on_key_press(self, key, modifiers): #what will happen when keys are pressed
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT: #if left arrow
            self.ball.change_x = -MOVEMENT_SPEED #ball moves left
        elif key == arcade.key.RIGHT: #if right arrow
            self.ball.change_x = MOVEMENT_SPEED #ball moves right
        elif key == arcade.key.UP: #if up arrow 
            self.ball.change_y = MOVEMENT_SPEED #ball moves up
        elif key == arcade.key.DOWN: #if down arrow
            self.ball.change_y = -MOVEMENT_SPEED #ball moves down

    def on_key_release(self, key, modifiers): #when you are not pressing any keys
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT: #if left and right key not pressed, ball does not move on x axis
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN: #if up and down key not pressed, ball does not move on y axis
            self.ball.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #the main game window
    arcade.run() #must have to run game


if __name__ == "__main__": #if you are in main file, main() attributes apply
    main()