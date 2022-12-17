# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:28:59 2022

@author: heath
"""

import numpy as np
import math as m
import xlsxwriter as xl

#want the model to be 15in -- scale everything by 15
a = 1
b = 0.75
h = 0.4
row1 = 0

# # contour where x(t)=0.2
# wb1 = xl.Workbook('curve_02.xlsx')
# ws1 = wb1.add_worksheet()
# x_t = 0.2
# for p in np.linspace(0, 2*3.1416, 100):
#     b1 = (1-(1-x_t)**(2*a))**(1/(2*a))
#     h1 = (0.2969*m.sqrt(x_t)-0.126*x_t-0.3516*x_t**2+0.2843*x_t**3-0.105*x_t**4)*5
#     y = b*b1*m.sin(p)
#     z = h*h1*m.cos(p)
#     ws1.write(row1, 0, x_t)
#     ws1.write(row1, 1, round(y,5))
#     ws1.write(row1, 2, round(z, 5))
#     row1 += 1
    
# wb1.close()
    
# #Contour where x(t) = 0.4
# wb1 = xl.Workbook('curve_04.xlsx')
# ws1 = wb1.add_worksheet()
# x_t = 0.4
# for p in np.linspace(0, 2*3.1416, 100):
#     b1 = (1-(1-x_t)**(2*a))**(1/(2*a))
#     h1 = (0.2969*m.sqrt(x_t)-0.126*x_t-0.3516*x_t**2+0.2843*x_t**3-0.105*x_t**4)*5
#     y = b*b1*m.sin(p)
#     z = h*h1*m.cos(p)
#     ws1.write(row1, 0, x_t)
#     ws1.write(row1, 1, round(y, 5))
#     ws1.write(row1, 2, round(z, 5))
#     row1 += 1
    
# wb1.close()

# # contour where x(t)=0.6
# wb1 = xl.Workbook('curve_06.xlsx')
# ws1 = wb1.add_worksheet()
# y_t = []
# z_t = []
# a = 1
# b = 0.75
# h = 0.4
# x_t = 0.6
# row1 = 0

# for p in np.linspace(0, 2*3.1416, 100):
#     b1 = (1-(1-x_t)**(2*a))**(1/(2*a))
#     h1 = (0.2969*m.sqrt(x_t)-0.126*x_t-0.3516*x_t**2+0.2843*x_t**3-0.105*x_t**4)*5
#     y = b*b1*m.sin(p)
#     z = h*h1*m.cos(p)
#     ws1.write(row1, 0, x_t)
#     ws1.write(row1, 1, round(y,5))
#     ws1.write(row1, 2, round(z, 5))
#     row1 += 1
    
# wb1.close()

# # contour where x(t)=0.8
# x_t = 0.8
# for p in np.linspace(0, 2*3.1416, 100):
#     b1 = (1-(1-x_t)**(2*a))**(1/(2*a))
#     h1 = (0.2969*m.sqrt(x_t)-0.126*x_t-0.3516*x_t**2+0.2843*x_t**3-0.105*x_t**4)*5
#     y = b*b1*m.sin(p)
#     z = h*h1*m.cos(p)
#     ws1.write(row1, 0, x_t)
#     ws1.write(row1, 1, round(y,5))
#     ws1.write(row1, 2, round(z, 5))
#     row1 += 1
    
# wb1.close()

# for x_t in range(15):
#     wb1 = xl.Workbook('curve_' + str(x_t) + '.xlsx')
#     ws1 = wb1.add_worksheet()
#     for p in np.linspace(0, 2*3.1416, 100):
#         b1 = (1-(1-x_t)**(2*a))**(1/(2*a))
#         h1 = (0.2969*m.sqrt(x_t)-0.126*x_t-0.3516*x_t**2+0.2843*x_t**3-0.105*x_t**4)*5
#         y = 15*b*b1*m.sin(p)
#         z = 15*h1*m.cos(p)
#         ws1.write(row1, 0, 15*x_t)
#         ws1.write(row1, 1, round(y,5))
#         ws1.write(row1, 2, round(z, 5))
#         row1 += 1
#     wb1.close()

for i in np.linspace(0.1, 1, 10):
    print(round(i,1))

