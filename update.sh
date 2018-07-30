#!/bin/bash

./stats > stats.txt

git add */*.md
git add stats.txt

git commit -m "Update `date`"
git push origin master