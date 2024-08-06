# Stochastic weight matrix dynamics during learning and Dyson Brownian motion

Data and code release for [arXiv:2407.16427](https://arxiv.org/abs/2407.16427)

Trained models
--------------

Trained SRBM and TS models are in ```data/```.

1. SRBM-long: SRBM trained with a fixed step size of 0.1 and batch size of 16 with better statistics.
2. SRBM-scale: SRBM trained at different values of step size and batch sizes.
3. TSmodel: Teacher Student model trained at different values of step size and batch sizes.

Reproducing the plots
---------------------

The plots in the article can be reproduced by Jupyter notebooks in ```scripts/```.

1. SRBM-scaling_analysis.ipynb: Reproducing the plots for SRBM data
2. TSmodel-scaling_analysis.ipynb: Reproducing the plots for teacher-student model data.

Regenerating the trained models
-------------------------------

The models saved in ```data/``` are generated from the training script in ```scripts/```.

1. submit_train-scalar_phase.sh: Train SRBM with the given step size, batch size, epochs, and the number of seeds. [SRBM](https://github.com/chanjure/SRBM) package is needed.
2. submit_train-tsmodel.sh: Train the teacher-student model with the given step size, batch size, and the number of seeds. 
