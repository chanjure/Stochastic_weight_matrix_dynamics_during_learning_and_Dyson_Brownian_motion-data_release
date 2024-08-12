SRBMDIR=../SRBM # Change this to your SRBM directory
BINDIR=../src/
PNAME=SRBM-scalar # Project name. The data will be saved in ./models/${PNAME}
BS=16 # Batch size
LR=0.1 # Learning rate
NSEED=10 # Change the size of ensemble accordingly
EP=10 # Change the number of epochs accordingly

nohup python $BINDIR/check_mp_scalar.py --rbm_path ${SRBMDIR} --lr ${LR} --nseed ${NSEED} --bs ${BS} --epochs ${EP} --pname ${PNAME} > ../logs/${PNAME}-output.txt 2>&1 &
