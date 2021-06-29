LVIS_PATH=/opt/largeVis
INPUT=./temp_data/vectors.txt
OUTPUT=./temp_data/vectors_2d.txt

$LVIS_PATH -input $INPUT -output $OUTPUT -threads 4 -outdim 2
