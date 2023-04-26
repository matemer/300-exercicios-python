'''4 - Crie um array Numpy de formato 4x4 preenchida com elementos de valor
inicial zero. Tais elementeos devem ser de tipo inteiro'''

import numpy as np

array = np.zeros(shape = (4,4),
                 dtype = int)

print(array)
print(type(array))
print(type(array[0,0]))