#Python program to calculate rotation matrix from centre of a sphere and point cloud coordinates:

import math
import numpy as np
from sphere_fitting import x0,y0,z0


def eulerAnglesToRotationMatrix(theta):

	R_x = np.array([[1,         0,                  0                   ],

	                    [0,         math.cos(theta[0]), -math.sin(theta[0]) ],

	                    [0,         math.sin(theta[0]), math.cos(theta[0])  ]

	                    ])



	R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],

	                    [0,                     1,      0                   ],

	                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]

	                    ])



	R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],

	                    [math.sin(theta[2]),    math.cos(theta[2]),     0],

	                    [0,                     0,                      1]

	                    ])





	R = np.dot(R_z, np.dot( R_y, R_x ))



	return R


#X,Y,Z are the point cloud co-ordinates determined by the deep learning method, we have to replace them in place of 50,40,30.
x = (50 - x0)
y = (40 - y0)
z = (30 - z0)

padj = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

theta = math.atan2(y/padj,x/padj)*(180.0/math.pi)

padj1 = math.sqrt(math.pow(x, 2) + math.pow(y, 2)+ math.pow(z,2))

phi = math.atan2(z/padj1, padj/padj1) *(180.0/math.pi)

roll = 0

theta = [roll,phi,theta]

print(eulerAnglesToRotationMatrix(theta))
