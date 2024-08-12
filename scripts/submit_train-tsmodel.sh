BINDIR=../src/
PNAME=TSmodel
BS=16
LR=0.1
NS=0.1
NSEED=10

nohup python $BINDIR/check_mp_ts.py --lr ${LR} --nseed ${NSEED} --bs ${BS} --ns ${NS} --pname ${PNAME} > ../logs/TSmodel-output.txt &
