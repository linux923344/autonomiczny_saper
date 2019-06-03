#!/bin/bash

# Variables
maps=($(ls ./maps/ | tr "\n" " " | sed 's/.txt//g' ))

# Functions
createSampleDatasAll(){
for line in "${maps[@]}"; do
cat << EOF > main.py
#!/usr/bin/python
from modules.Board.Board import Board
from modules.MapObjects.Saper import Saper
from modules.Board.MapReader import *
from modules.PathFinder.PathFinder import PathFinder

board = Board(1480, 900)
mapName = "$line"
MapReader.read("maps/"+mapName + ".txt", board)
s = Saper()
#steps = PathFinder.getPathToByDfs(board, 3, 6)
#steps = PathFinder.getPathToByBFS(board, 3, 6)
steps = PathFinder.getPathToByBestFirstSearch(board, mapName)
s.addSteps(steps)
# board.setMachineLearningWalkning()
board.addPlayer(s, 5, 0)
board.start()
EOF

echo -e "Now in $line"
setsid sh -c 'python main.py'&
pgid=$!
sleep 5 && kill $pgid
done
}

vwPredictions(){
cat sampleDatas/* > sampleDatasAll
vw sampleDatasAll -l 10 -c --passes 1000000 --holdout_off -f ./models/walking.model --holdout_off 8 
}

deleteFiles(){
rm -rf main.py
rm -rf sampleDatasAll
rm -rf sampleDatasAll.cache
}

# MAIN
echo -e "-------------- Starting --------------"
echo ""
createSampleDatasAll && echo -e "$(date) Created Simple Datas"
echo ""
vwPredictions && echo -e "$(date) Done predictions"
deleteFiles
echo -e "-------------- DONE --------------"
