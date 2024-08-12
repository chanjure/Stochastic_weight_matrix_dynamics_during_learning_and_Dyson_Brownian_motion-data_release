#!/usr/bin/env python
# coding: utf-8


import numpy as np
import argparse
import time

import os, sys

import torch

import random

def main(args):
  
  print("Using RBM from: ", args.rbm_path)
  sys.path.append(args.rbm_path)
  import RBM

  N = 10
  Nh= 10
  mi = 3.

  now = time.strftime("%y%m%d-%H%M%S", time.gmtime())

  eps = 0.1

  batch_size = args.bs
  lr = args.lr

  project = args.pname
  project_name = project+'_lr'+str(lr)+'bs'+str(batch_size)
  print(project_name)
  model_dir = "./models/" + project + '/' + project_name + '/'
  
  os.system("mkdir -p "+model_dir)
  
  # # Define target kernel

  m = 2
  K_phi = np.zeros((N,N))

  for i in range(N):
      for j in range(N):
          if i==j:
              K_phi[i][j] = 2 + m**2
          elif (i % N == (j+1) %N) or (i % N == (j-1) %N):
              K_phi[i][j] = -1
  print(K_phi)

  eig_phi = np.empty(N)
  for i in range(N):
      eig_phi[i] = m**2 + 2 - 2*np.cos(2*np.pi*i/N)


  init_cond = {'w_sig':eps,'m':mi, 'sig':1., 'm_scheme':0}

  # normal
  epochs = args.epochs #3000000
  save_int = int(epochs/5)
  n_seed = args.nseed

  device = "cuda" if torch.cuda.is_available() else "cpu"

  K_phi_tc = torch.DoubleTensor(K_phi).to(device)

  beta = 0.
  l2 = 0.
  lr_decay=0.

  train_parm = {'init_cond':init_cond, 'epochs':epochs,
                'batch_size':batch_size, 'save_int':save_int,
                'lr':lr, 'beta':beta, 'l2':l2, 'lr_decay':lr_decay, 'n_seed':n_seed}

  w_list = {'w':[], 'u':[], 'vh':[], 's':[], 'dw':[]} # seed, epoch, shape
  succ_count = 0
  for i in range(n_seed):
      seed = np.random.randint(0,100000)
      print(i,seed)
      torch.manual_seed(seed)
      random.seed(seed)
      np.random.seed(seed)
      rbm = RBM.SRBM(n_v=N,n_h=Nh,k=3,init_cond=init_cond, device=device)

      try:
          history = rbm.unsup_fit(K_phi_tc, epochs, lr, beta=beta, l2=l2, 
                                  batch_size=batch_size, lr_decay=lr_decay, save_int=save_int)
          s_hist = np.zeros((epochs//save_int+1,rbm.n_v))
          u_hist = np.zeros((epochs//save_int+1,rbm.n_v,rbm.n_v))
          v_hist = np.zeros((epochs//save_int+1,rbm.n_v,rbm.n_v))
          
          for k in range(epochs//save_int+1):
              K = history['w'][k].T @ history['w'][k]
              vh, s_, u = np.linalg.svd(K)
              s_hist[k] = s_
              u_hist[k] = u
              v_hist[k] = vh

          w_list['w'].append(history['w']) # epoch, nh, nv
          w_list['u'].append(u_hist) # epoch, nv, nv
          w_list['vh'].append(v_hist) # epoch, nh, nh
          w_list['s'].append(s_hist) # epoch, nv
          w_list['dw'].append(history['dw'])
          succ_flag=1
          
      except:
          succ_flag=0
          pass
      
      if succ_flag:
          succ_count += 1

  succ_ratio = succ_count/n_seed
  print(succ_ratio)

  w = np.array(w_list['w'])
  u = np.array(w_list['u'])
  v = np.array(w_list['vh'])
  s = np.array(w_list['s'])
  dw = np.array(w_list['dw'])

  data_name = model_dir+project_name+'.npz'
  np.savez(data_name, 
           sr=succ_ratio, **w_list, **train_parm)
  print('saved '+data_name)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="SRBM scalar Phase")
  parser.add_argument('--rbm_path', type=str, default='../RBM/', help='Path to RBM')
  parser.add_argument('--nseed', type=int, default=1000, help='Number of realization')
  parser.add_argument('--lr', type=float, default=5e-2, help='Learning rate')
  parser.add_argument('--bs', type=int, default=16, help='Batch size')
  parser.add_argument('--epochs', type=int, default=10000, help='Epochs')
  parser.add_argument('--pname', type=str, default='scalar', help='Project name')
  args = parser.parse_args()

  main(args)
