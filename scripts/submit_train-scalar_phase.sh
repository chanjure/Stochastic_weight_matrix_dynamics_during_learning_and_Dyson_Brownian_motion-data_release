SRBMDIR=/Users/chanju/Dropbox/Lab/swansea/workspace/Git/SRBM/ # Change this to your SRBM directory
BINDIR=../src/
PNAME=SRBM-scalar
BS=16
LR=0.1
NSEED=10
EP=10

nohup python $BINDIR/check_mp_scalar.py --rbm_path ${SRBMDIR} --lr ${LR} --nseed ${NSEED} --bs ${BS} --epochs ${EP} --pname ${PNAME} > ../logs/${PNAME}-output.txt 2>&1 &
