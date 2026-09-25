#!/bin/bash
INPUTFILE="vid.mp4"
ffmpeg -i "$INPUTFILE" -r 1 "fr_%03d.png"
echo "Done"
