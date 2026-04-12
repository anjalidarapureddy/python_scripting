#! /bin/bash
colors="red yellow green"

for color in $colors
do
	echo "$color"
done

ls /tmp && ls ./file.txt
echo "$?"
