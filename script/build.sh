#!/bin/bash

# pyinstaller --name 'Huanbu' \
#             --icon 'huanbu.ico' \
#             --windowed  \
#             --add-data='./strong_beat.wav:.' \
#             --add-data='./sub_strong_beat.wav:.' \
#             --add-data='./weak_beat.wav:.' \
#             src/blog_app/__main__.py

echo '1 INFO clean folder...'
rm -rf dist build blog_app.spec

pyinstaller --name 'blog_app' \
            --icon 'resources/hugo-icon.png' \
            --windowed  \
            src/blog_app/app.py

open dist/blog_app.app