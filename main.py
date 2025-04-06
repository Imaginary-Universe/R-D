from fasthtml.common import *
from monsterui.all import *
import os, yaml
app, rt = fast_app(hdrs=Theme.slate.headers(), live=True)

def BlogCard(fname):
    with open(f"posts/{fname}", "r") as f: content = f.read()
    meta = content.split("---")[1]
    meta = yaml.safe_load(meta)
    return Card(Grid(
        Img(src=meta["image"]),
        Div(
            H3(meta["title"]), 
            P(meta["description"]),
            P(meta["author"]),
        Div(
            P(meta["date"]),
            P(meta["categories"]))
    )))
@rt
def index():
    return (map(BlogCard, os.listdir("posts")))
serve()