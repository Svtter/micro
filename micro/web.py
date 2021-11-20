# create a app inside.
# for debug convinence.

from flask import Flask


class App:
    def __init__(self) -> None:
        # load from configfile?
        self.inner_app = Flask(__name__)

    def run(self):
        self.inner_app.run()


def set_core():
    pass


app = App()
