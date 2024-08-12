#!/usr/bin/env python
# coding: utf-8

import argparse

import numpy as np
import os

from scipy.stats import ortho_group

def main(args):

  batch_size = args.bs
  lr = args.lr
  noise = args.ns

  project = args.pname
  project_name = project+'_lr'+str(lr)+'n'+str(noise)+'bs'+str(batch_size)
  print(project_name)
  model_dir = "./models/" + project + '/' + project_name + '/'

  os.system("mkdir -p "+model_dir)

  m = 2.
  N = 2
  D_t = np.empty(N)
  for i in range(N):
      D_t[i] = 2.
      
  D_t = np.sort(D_t)
  O = ortho_group.rvs(dim=len(D_t))
  W_t = O @ np.diag(D_t) @ O.T
  print('d:',D_t)
  print(W_t)
  print(len(D_t)**2)

  n_data = batch_size*500
  dim_x = len(D_t)
  x = np.random.normal(loc=0,scale=1,size=(n_data, dim_x, 1),)
  y = np.einsum('ij,njk->nik',W_t,x)
  print(y.shape)
  print(x.shape)

# Check normalization
  print(np.mean(np.einsum('nik,njk->nij', x, x), axis=0))


# # 4. Training

  n_seed = args.nseed
  epochs = 10
  save_int = 2

  train_param = {'lr':lr, 'batch_size':batch_size, 'epochs':epochs, 'noise':noise, 'save_int':save_int}

  history = {'loss':np.empty((n_seed, epochs//save_int + 1)), 
           'W':np.empty((n_seed, epochs//save_int + 1, dim_x, dim_x)), 
           'grad':np.empty((n_seed, epochs//save_int + 1, dim_x, dim_x))}

  for s in range(n_seed):
      a = np.random.normal(0., noise, size=((n_data,)+W_t.shape))

      seed = np.random.randint(0,10000*n_seed)
      print(s, seed)

      eps = 0.1
      W_s = np.random.normal(loc=0, scale=eps,size=(dim_x,dim_x))
      
      # batch loss
      def L(x, y):
          y_s = np.einsum('ij,njk->nik',W_s,x)
          return np.mean(0.5*(y - y_s)**2)

      # Batch gradient
      def dL(x, W, a):
          cov = np.einsum('nij,nkj->nik',x,x)
          grad = np.einsum('ij,njk->nik',W - W_s,cov) + a
          return - np.mean(grad, axis=0)

      m = np.random.normal(0., noise, size=((n_data, ) + W_t.shape))
      # 2x2 case
      a = np.tril(m) + np.transpose(np.tril(m, -1), (0,2,1))
      
      ################
      # Masking part #
      ################
      # x sqrt(2) on diagonal 
      mask = np.ones_like(a)
      mask_idx = np.eye(mask.shape[1], dtype=bool)
      mask[:,mask_idx] = np.sqrt(2.)

      # apply mask
      a *= mask
      ################

      print('sig:',np.mean(np.std(a, axis=0)),'=',noise)
      
      # minibatch
      mb_data = x.reshape((-1,batch_size, dim_x, 1))

      n_batch = n_data//batch_size
      mb_predict = np.einsum('ij,njk->nik',W_s,x)
      loss = L(x, y)
      grad = dL(x, W_t, a)

      for i in range(epochs):

          if i % save_int == 0:
              print('e: %d loss:%.5f'%(i,loss))
              history['loss'][s][i//save_int] = loss
              history['W'][s][i//save_int] = W_s.copy()
              history['grad'][s][i//save_int] = grad.copy()

          for j in range(n_batch):
              # Target having intrinsic noise
                      
              mb_target = np.einsum('ij,bnjk->bnik',W_t, mb_data)

              b_loss = L(mb_data[j], mb_target[j])
              
              A = a[j * batch_size : (j+1) * batch_size]
              b_grad = dL(mb_data[j], W_t, A)

              W_s -= lr*b_grad

              loss += b_loss
              grad += b_grad

          loss /= n_batch
          grad /= n_batch
          
      print('e: %d loss:%.5f'%(i,loss))
      history['loss'][s][-1] = loss
      history['W'][s][-1] = W_s.copy()
      history['grad'][s][-1] = grad.copy()


  data_name = model_dir+project_name+'.npz'
  np.savez(data_name, **history, **train_param)
  print('saved '+data_name)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="TSmodel scaling 6 modes 4 degenerate")
  parser.add_argument("--bs", type=int, default=16, help="Batch Size")
  parser.add_argument("--lr", type=float, default=1e-1, help="Learning Rate")
  parser.add_argument("--ns", type=float, default=0.1, help="Induced noise")
  parser.add_argument("--pname", type=str, default="test", help="Project name")
  parser.add_argument("--nseed", type=int, default=200, help="Number of seeds")

  args = parser.parse_args()

  main(args)
