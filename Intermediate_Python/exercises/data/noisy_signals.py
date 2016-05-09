# -*- coding: utf-8 -*-
# 
# Noisy signal generator for creating data for exercise 3 (signal processing
# class exercise)
#
# @Author: paul
# @Date:   2016-05-09 15:02:43
# @Last Modified by:   Paul Chambers
# @Last Modified time: 2016-05-09 15:39:49
import numpy as np
import matplotlib.pyplot as plt


def noisy_signal_generator(x, freq):
	"""creates a noisy sin signal with frequency freq

	Parameters
	----------
	x : array of float
	    signal x values
	freq : scalar
	    the signal frequency

	Returns
	-------
	y : array of float
	    array of sin(x * freq) plus a gaussian distributed noise
	"""
	noise = np.random.normal(0, 0.2, np.size(x))
	return np.sin(freq*x) + noise


if __name__ == '__main__':
	x = np.linspace(0, np.pi*2, 512)

	for i in range(1, 6):
		y = noisy_signal_generator(x, np.pi*i)
		data = np.vstack([x, y]).T
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(x, y)
		fig.show()
		np.savetxt('ex3_signal_'+str(i), data)

