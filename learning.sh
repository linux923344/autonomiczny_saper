#!/bin/bash

cat sampleDatas/* > sampleDatasAll
vw sampleDatasAll -f ./models/walking.model
rm -rf sampleDatasAll
