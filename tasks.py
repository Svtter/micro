from invoke import task
from invoke import Runner
import webbrowser
import threading


def open_docs():
    webbrowser.open("http://127.0.0.1:8000/")


@task
def docs(c):
    thread = threading.Thread(target=open_docs)
    thread.start()
    with c.cd('docs'):
        c.run('mkdocs serve')