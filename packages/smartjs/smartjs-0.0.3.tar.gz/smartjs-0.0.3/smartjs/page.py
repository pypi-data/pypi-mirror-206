import os

from smartjs.base import *
from smartjs.constants import *
from smartjs.functions import *
from smartjs.elements import *
from smartjs.style import *
from smartjs.javascript import *
from smartjs.env import Env
from pathlib import PurePath, Path

env_path = PurePath(os.getcwd()).parent / '.env'
env = Env(env_path=env_path)

def html_page(title: str):
    head = Head(title=title)
    body = Body(Nav(ContainerFluid(NavList(NavItem(NavLink(href='/', elements='Essência Psiquiatria'))))), Main(), Footer())
    return HTML(head=head, body=body)


if __name__ == '__main__':
    print(env.static_logo_path())