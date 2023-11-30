# Phong Nguyen, Yurock Heo, Bill Tran
# 12/6/2019

from models.Bar import *
from models.Bird import *
from controllers import *
import secrets


class FlappyBird:
    """ This class implements the basic rules of the game"""

    def __init__(self, y_bottom_bird, y_top_bird):
        """ Save the top and bottom y coordinates of the bird """
        self.y_bottom_bird = y_bottom_bird
        self.y_top_bird = y_top_bird

    def touchGround(self, y_b_bird):
        """ Check if the bird hits the ground or not """
        if y_b_bird <= 0:
            return True
        else:
            return False

    def ifCollidebottom(self, x_l_bird, x_r_bird, y_b_bird, y_t_bird, x_l_Bbar, x_r_Bbar, y_t_Bbar):
        """Check if the bird hits the bottom bar"""

        if (x_l_Bbar <= x_r_bird and x_l_bird <= x_r_Bbar) and y_b_bird <= y_t_Bbar:
            return True

        elif y_b_bird <= y_t_Bbar and (x_l_Bbar <= x_l_bird <= x_r_Bbar or x_l_Bbar <= x_r_bird <= x_r_Bbar):
            return True

    def ifCollidetop(self, x_l_bird, x_r_bird, y_b_bird, y_t_bird, x_l_Bbar, x_r_Bbar, y_b_Bbar):
        """Check if the bird hits the top bar"""

        if (x_l_Bbar <= x_r_bird and x_l_bird <= x_r_Bbar) and y_t_bird >= y_b_Bbar:
            return True
        elif y_t_bird >= y_b_Bbar and (x_l_Bbar <= x_l_bird <= x_r_Bbar or x_l_Bbar <= x_r_bird <= x_r_Bbar):
            return True


def countScore(x_r_bird, x_l_Bbar, score):
    """ Calculate and return the score """

    if x_r_bird - 5 == x_l_Bbar:
        score += 1
    return score


def intro(win):
    """Creates an introduction screen of flappy bird"""

    title = Image(Point(50, 125), "title.png")
    rule = Text(Point(50, 95), "Use mouse click to fly the bird\nand avoid hitting bars!")
    rule.setSize(18)
    rule.setFill("gold1")
    rule.setFace("courier")
    rule.setStyle("bold")
    prompt = Text(Point(50, 75), "<Click anywhere to begin>")
    prompt.setFill("salmon")
    prompt.setStyle("bold")
    prompt.setSize(20)
    prompt.setFace("courier")
    prompt.draw(win)
    rule.draw(win)
    title.draw(win)

    return prompt, rule, title


def scoreScreen(score, win):
    """ Displays the Score with a medel and draw the scoreboard, quitbutton,
    and restartButton. Return the image variables """

    gameover = Image(Point(50, 110), "over.png")
    scoreboard = Image(Point(50, 80), "scoreboard.png")
    restart = Image(Point(35, 50), "restart.png")
    quitButton = Image(Point(65, 50), "quit.png")

    # Give a medal depending on the score
    if score < 5:
        medal = Image(Point(30, 80), "nothing.png")
    elif 5 <= score <= 10:
        medal = Image(Point(30, 78), "bronze.png")
    elif 11 <= score <= 20:
        medal = Image(Point(30, 78), "silver.png")
    else:
        medal = Image(Point(30, 78), "gold.png")

    scoreboard.draw(win)
    medal.draw(win)
    restart.draw(win)
    quitButton.draw(win)
    gameover.draw(win)
    score = Text(Point(70, 78), score)
    score.setSize(60)
    score.setStyle("bold")
    score.setFace("courier")
    score.setFill("brown")
    score.draw(win)

    return restart, quitButton, gameover, scoreboard, medal


def main():
    win = GraphWin("Flappy Bird", 500, 700)
    win.setCoords(0, 0, 100, 150)

    # set the backgrounds
    background = Image(Point(180, 60), "back.png")
    background.draw(win)
    background1 = Image(Point(558, 60), "backreverse.png")
    background1.draw(win)
    background2 = Image(Point(906, 60), "back.png")
    background2.draw(win)

    prompt, rule, title = intro(win)
    game = FlappyBird(75, 85)
    center_bar = Point(110, 0)

    count = 0  # counting the score

    score = Text(Point(50, 130), count)
    score.setSize(60)
    score.setFace("courier")
    score.setStyle("bold")
    score.setFill("gold")

    # A boolean for the status of the bird (died or not)
    died = False
    pt = win.getMouse()

    bird = Bird(40, 75, win)
    x_l_bird = bird.Bird.getAnchor().getX() - 5
    x_r_bird = bird.Bird.getAnchor().getX() + 5
    y_b_bird = bird.Bird.getAnchor().getY() - 5
    y_t_bird = bird.Bird.getAnchor().getY() + 5

    bar1 = Bars(win, center_bar, 20, 150, 190)
    x_l_Bbar = bar1.rect.getCenter().getX() - 10
    x_r_Bbar = bar1.rect.getCenter().getX() + 10
    y_t_Bbar = bar1.rect.getCenter().getY() + 75

    prompt.undraw()
    rule.undraw()
    title.undraw()
    score.draw(win)
    restartClicked = False
    quitClicked = False

    # Conditions to keep the game running
    while (not game.touchGround(y_b_bird)
           and not game.ifCollidebottom(x_l_bird, x_r_bird, y_b_bird, y_t_bird, x_l_Bbar, x_r_Bbar, y_t_Bbar)
           and not game.ifCollidetop(x_l_bird, x_r_bird, y_b_bird, y_t_bird, x_l_Bbar, x_r_Bbar, y_t_Bbar + 40)):
        # Move the bar leftward and create new bars
        while x_r_Bbar > 0:
            score.setText(count)
            fly = bird.fly()
            count = countScore(x_r_bird, x_l_Bbar, count)
            bar1.move(-3, 0)

            x_l_bird = bird.Bird.getAnchor().getX() - 5
            x_r_bird = bird.Bird.getAnchor().getX() + 5
            y_b_bird = bird.Bird.getAnchor().getY() - 5
            y_t_bird = bird.Bird.getAnchor().getY() + 5

            x_l_Bbar = bar1.rect.getCenter().getX() - 10
            x_r_Bbar = bar1.rect.getCenter().getX() + 10
            y_t_Bbar = bar1.rect.getCenter().getY() + 75

            background.move(-0.08, 0)
            background1.move(-0.08, 0)
            background2.move(-0.08, 0)
            game = FlappyBird(y_b_bird, y_t_bird)

            # Break the loop when the bird hit the bars or the ground
            if game.touchGround(y_b_bird) \
                or game.ifCollidebottom(x_l_bird, x_r_bird, y_b_bird, y_t_bird, x_l_Bbar, x_r_Bbar, y_t_Bbar) \
                or game.ifCollidetop(x_l_bird, x_r_bird, y_b_bird, y_t_bird, x_l_Bbar, x_r_Bbar, y_t_Bbar + 40):
                died = True
                break

            sleep(0.01)

        bar1.undraw()
        center = Point(110, secrets.SystemRandom().randrange(-50, 20, 20))  # creates two bars in random positions
        bar1 = Bars(win, center, 20, 150, 190)
        score.undraw()
        score.draw(win)
        x_l_Bbar = bar1.rect.getCenter().getX() - 10
        x_r_Bbar = bar1.rect.getCenter().getX() + 10
        y_t_Bbar = bar1.rect.getCenter().getY() + 75

        # Break the larger loop when the bird hit the bars or the ground
        if died:
            break

    # Create a Score Board, quit and restart button when the game ends
    restartClicked = True
    quitClicked = True
    score.undraw()
    bird.Bird.undraw()
    restart, quitButton, gameover, scoreboard, medal = scoreScreen(count, win)
    pt = win.getMouse()

    # Check the mouse clicks
    while not ((58 <= pt.getX() <= 72 and 46 <= pt.getY() <= 54) or (25 <= pt.getX() <= 45 and 46 <= pt.getY() <= 54)):
        pt = win.getMouse()
    # The game is closed when the Quit button is clicked
    if 58 <= pt.getX() <= 72 and 46 <= pt.getY() <= 54 and quitClicked:
        win.close()
    # The game restarts when the Restart button is clicked
    elif 25 <= pt.getX() <= 45 and 46 <= pt.getY() <= 54 and restartClicked:
        win.close()
        main()


main()
