# 1. Import np

import numpy as np
import logging

filename = "exercise_1_logfile.log"

#setup logging file
#setup log file
logging.basicConfig(format='%(asctime)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
                filename=filename,
                filemode='w',
                level=logging.INFO)

# 2. Create an array of 10 zeros

array_zeros=np.zeros(10)
print(array_zeros)
logging.info(array_zeros)


# 3. Create an array of 10 ones

array_ones=np.ones(10)
print(array_ones)
logging.info(array_ones)

# 4. Create an array of 10 fives

array_fives=np.ones(10)*5
print(array_fives)
logging.info(array_fives)


#5. Create an array of integers from 10 to 50

array_10_50 = np.arange(10,50)
print(array_10_50)
logging.info(array_10_50)


# 6. Create an array of even integers from 10 to 50

array_10_50_even = np.arange(10, 50, 2)
print(array_10_50_even)
logging.info(array_10_50_even)


# 7. Create a 3x3 matrix with values ranging from 0 to 8

array_3_3 = np.arange(9).reshape(3,3)
print(array_3_3)
logging.info(array_3_3)

# 8. Create a 3x3 identity matrix

array_identity=np.identity(3)
print(array_identity)
logging.info(array_identity)

# 9. Use numpy to randomly generate a number between 0 and 1

random_num = np.random.rand(1)
print(random_num)
logging.info(random_num)

