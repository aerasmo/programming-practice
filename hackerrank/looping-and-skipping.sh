#!/bin/bash

counter=1
while [ $counter -le 99 ]
do
    echo $counter
    ((counter+=2))
done