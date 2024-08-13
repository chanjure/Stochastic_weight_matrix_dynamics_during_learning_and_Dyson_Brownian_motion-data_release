[![DOI](https://zenodo.org/badge/837909488.svg)](https://zenodo.org/doi/10.5281/zenodo.13294081)
[![Run tests](https://github.com/chanjure/Stochastic_weight_matrix_dynamics_during_learning_and_Dyson_Brownian_motion-data_release/actions/workflows/pytest.yaml/badge.svg?event=push)](https://github.com/chanjure/Stochastic_weight_matrix_dynamics_during_learning_and_Dyson_Brownian_motion-data_release/actions/workflows/pytest.yaml)
[![codecov](https://codecov.io/github/chanjure/Stochastic_weight_matrix_dynamics_during_learning_and_Dyson_Brownian_motion-data_release/graph/badge.svg?token=WNARB26ICQ)](https://codecov.io/github/chanjure/Stochastic_weight_matrix_dynamics_during_learning_and_Dyson_Brownian_motion-data_release)

# Stochastic weight matrix dynamics during learning and Dyson Brownian motion

Data and code release for [arXiv:2407.16427](https://arxiv.org/abs/2407.16427)

Cloning the repository
----------------------

Gaussian RBM data is generated using the [SRBM](https://github.chanjure/SRBM) package, which is included in this repository as a submodule.

To download the repository with the submodule, use the following command:

```git clone --recurse-submodules git@github.com:chanjure/Stochastic_weight_matrix_dynamics_during_learning_and_Dyson_Brownian_motion-data_release.git```

Trained models
--------------

Trained SRBM and TS models are in ```data/```.

1. SRBM-long: SRBM trained with a fixed step size of 0.1 and batch size of 16 with better statistics.
2. SRBM-scale: SRBM trained at different values of step size and batch sizes.
3. TSmodel: Teacher Student model trained at different values of step size and batch sizes.

Setting up the environment
--------------------------

The code is tested on Python 3.8, 3.9, and 3.10.

For conda users, you can create a new environment with the following command:

```conda env create -f env/environment.yml -n qftml```

Then, activate the environment:

```conda activate qftml```

For pip users, you can install the required packages with the following command:

```python -m pip install -r env/requirements.txt```

Reproducing the plots
---------------------

The plots in the article can be reproduced by Jupyter notebooks in ```scripts/```.

To run the notebooks, you need to install packages in ```requirements.txt```.

If some packages are missing, the full list of packages is described in ```environment.yml```.

1. SRBM-scaling_analysis.ipynb: Reproducing the plots for SRBM data
2. TSmodel-scaling_analysis.ipynb: Reproducing the plots for teacher-student model data.

Regenerating the trained models
-------------------------------

The models saved in ```data/``` are generated from the training script in ```scripts/```.

The SRBM package is needed to regenerate trained models for Gaussian RBM case.
It is included in this repository as a submodule but it can be also directly installed from [SRBM](https://github.com/chanjure/SRBM).

Then change the ```$SRBMDIR``` in ```scripts/submit_train-scalar_phase.sh``` to the path where you installed the SRBM package.


1. submit_train-scalar_phase.sh: Train SRBM with the given step size, batch size, epochs, and the number of seeds. [SRBM](https://github.com/chanjure/SRBM) package is needed.
2. submit_train-tsmodel.sh: Train the teacher-student model with the given step size, batch size, and the number of seeds. 

