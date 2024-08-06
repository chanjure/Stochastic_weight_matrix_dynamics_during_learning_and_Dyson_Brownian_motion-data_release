#!/bin/bash --login

SRBMDIR=/home/chanju/Dropbox/Lab/swansea/workspace/Git/SRBM/ # Change this to your SRBM directory
BINDIR=../bin
PNAME=SRBM-scalar
BS=16
LR=0.1
NSEED=10
EP=10

nohup python3 $BINDIR/check_mp-scalar.py --rbm_path ${SRBMDIR} --lr ${LR} --nseed ${NSEED} --bs ${BS} --epochs ${EP} --pname ${PNAME} > ../logs/${PNAME}-output.txt 2>&1 &
