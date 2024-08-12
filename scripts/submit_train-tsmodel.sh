BINDIR=../src/
PNAME=TSmodel # Project name. The data will be saved in ./models/${PNAME}
BS=16 # Batch size
LR=0.1 # Learning rate
NS=0.1 # Strength of the induced noise
NSEED=10 # Size of the ensemble

nohup python $BINDIR/check_mp_ts.py --lr ${LR} --nseed ${NSEED} --bs ${BS} --ns ${NS} --pname ${PNAME} > ../logs/TSmodel-output.txt &
