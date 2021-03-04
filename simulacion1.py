import numpy as np
import matplotlib.pyplot as plt
import control

sysg = control.tf(4,[1,5])
print(sysg)