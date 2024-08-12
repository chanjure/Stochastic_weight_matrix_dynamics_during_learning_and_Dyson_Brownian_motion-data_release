import numpy as np
import pytest
import argparse

import os, sys
sys.path.append([".", "../source/"])

from src.check_mp_ts import main

def test_TS_gen():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bs', type=int, default=16)
    parser.add_argument('--lr', type=float, default=0.1)
    parser.add_argument('--ns', type=float, default=0.1)
    parser.add_argument('--pname', type=str, default='TS-test')
    parser.add_argument('--nseed', type=int, default=10)
    args = parser.parse_args()

    main(args)
    assert os.path.exists("./models/TS-test")
