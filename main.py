"""Entry point."""

from controllers.base import Controller
from views.base import View


def main():
    view = View()
    game = Controller(view)
    game.run()


if __name__ == "__main__":
    main()