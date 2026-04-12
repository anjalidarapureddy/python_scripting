#! /bin/bash 
##shibang mode follwed by interactive path 
name="anjali" #assigning variable
echo "welcome, $name" #$-accesing character

read -p "Enter your position: " Position
echo " $name an $Position"

touch file.txt

if [ $name == "anjali" ]; then
	echo "eq: $name as an $Position"
elif [ $name == "kusuma" ]; then
	echo "kusuma ur not anjali"
else
	echo "none of the above"
fi
