#!/bin/bash
# выделение границ sharpen
INPUTFILE="fr_017.png"
OUTPUTFILE="output_filtered.png"
MATRIX="3x3: -1 -1 -1 -1 8 -1 -1 -1 -1"

convert "$INPUTFILE" -morphology Convolve "$MATRIX" "$OUTPUTFILE"
echo "Фильтр применен"
