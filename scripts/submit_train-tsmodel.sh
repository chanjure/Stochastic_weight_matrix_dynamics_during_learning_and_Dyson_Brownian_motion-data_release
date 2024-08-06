BINDIR=../bin
PNAME=TSmodel
BS=16
LR=0.1
NS=0.1
NSEED=10

nohup python3 $BINDIR/TS-model_no-checkmp-b_dep-noise.py --lr ${LR} --nseed ${NSEED} --bs ${BS} --ns ${NS} --pname ${PNAME} > ../logs/TSmodel-output.txt &
