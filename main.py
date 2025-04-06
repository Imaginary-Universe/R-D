from fasthtml.common import *
from monsterui.all import *

app, rt = fast_app(hdrs=Theme.slate.headers())

@rt
def index():
    return P("Hello, World!", style="color:blue; font-size:20px;")

serve()