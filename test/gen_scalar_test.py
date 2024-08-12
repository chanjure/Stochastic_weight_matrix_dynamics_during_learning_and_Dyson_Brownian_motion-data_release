import numpy as np
import pytest
import argparse

import os, sys
sys.path.append([".", "../source/"])

from src.check_mp_scalar import main

def test_SRBM_gen():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rbm_path', type=str, default="./SRBM")
    parser.add_argument('--lr', type=float, default=0.1)
    parser.add_argument('--bs', type=int, default=16)
    parser.add_argument('--pname', type=str, default='SRBM-test')
    parser.add_argument('--nseed', type=int, default=3)
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()

    main(args)
    assert os.path.exists("./models/SRBM-test")
