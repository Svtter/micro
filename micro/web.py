# create a app inside.
# for debug convinence.

from flask import Flask


class App:
    def __init__(self) -> None:
        # load from configfile?
        self.inner_app = Flask(__name__)

    def set_core(self):
        # The core should be changable.
        pass

    def run(self):
        self.inner_app.run()

    def get_service(self, name: str='default'):
        """
        not finished yet.
        """
        # there should be a service register.
        pass


app = App()
