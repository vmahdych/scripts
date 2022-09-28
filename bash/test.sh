#!/bin/bash

#Script to check different stuff


# 1. different examples of using echo and usage syntax

#
#greating="hello"
#
#    echo $greating, world \(planet\)!
#    
#    echo '$greating, world (planet)!'
#    
#    echo "$greating, world (planet)!"
#
#

# 2. Examples of variables usage/syntax

#echo "Please enter your favourite website =)"
#read website
#a=Hello
#b="Good Morning!"
#c=16
#p=$(ping -c 1 $website | grep 'bytes from' | cut -d = -f 4)
#
#echo $a
#echo $b
#echo $c
#echo -e "\n$b I have $c Gb of memory =)"
#echo "The ping of $website was $p"


# 3. Comparison operations
#
#[[ "cat" == "cat" ]]
#echo $?
#
#[[ "cat" == "dog" ]]
#echo $?
#
##here we can see that system recognize 20 as the higher value then 100 becouse of using incorrect operators
#[[ 20 > 100 ]]
#echo $?
#
##let`s use the correct one instead
#[[ 20 -gt 100 ]]
#echo $?
#
#logical operators
#echo -e "\nlogical"
#a=""
#b="Sharlock"
#[[ -z $a && -n $b ]]
#echo $?


# 4. Some usefull things related to array

a=()
b=("apple" "banana" "cherry" "orange")
b[6]="kiwi"
b+=("mango")

echo ${b[5]} ${b[6]}

echo ${b[@]}
echo ${b[@]: -1}
