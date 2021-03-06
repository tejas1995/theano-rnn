"""Module that contains functionality for lstm RNNs."""


__author__ = 'Justin Bayer, bayer.justin@googlemail.com'


import theano
import theano.tensor as T
sig = T.nnet.sigmoid


def make_expr(lstminpt, state):
  lstminpt_squashed = sig(lstminpt)
  slicesize = lstminpt.shape[0] / 4
  inpt = lstminpt_squashed[:slicesize]
  ingate = lstminpt_squashed[slicesize: 2 * slicesize]
  forgetgate = lstminpt_squashed[2 * slicesize:3 * slicesize]
  outgate = lstminpt_squashed[3 * slicesize:4 * slicesize]

  new_state = inpt * ingate + state * forgetgate
  output = sig(new_state) * outgate
  return [new_state, output]

inpt = T.vector('lstm-input')
state = T.vector('lstm-state')
func = theano.function([inpt, state], make_expr(inpt, state))
