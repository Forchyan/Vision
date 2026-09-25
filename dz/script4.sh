#!/bin/bash
INPUTFILE="fr_001.png"
FACTOR=0.75
CURRENTFILE=$INPUTFILE

for ((i=1; i<=5; i++)); do
    convert "$CURRENTFILE" -resize 75% "scaled_$i.png"
    CURRENTFILE="scaled_$i.png"
    echo "Итерация $i завершена. Файл: $CURRENTFILE"
done

echo "Масштабирование завершено"
