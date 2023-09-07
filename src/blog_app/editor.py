import os

hugo_dir = "/Users/xiuhao/Work/self/hugo-blog"


def new_post(name: str):
    """create new post"""
    os.chdir(hugo_dir)
    post_path = "content/post"
    os.system((f"hugo new post/{name}"))
    os.system(f"code {post_path}/{name}")


def open_post_editor():
    os.system(f"code {hugo_dir}")
