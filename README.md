# Rigid Transform Calculator

This repository contains a Python script for calculating the rigid body transformation, including rotation and translation, required to move from one coordinate system to another. The script computes the rotation matrix, rotation quaternion, and translation vector given a new origin and points defining the new axes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Features

- Calculate the new basis vectors (x, y, z axes) based on input points.
- Ensure orthogonality of the new basis using cross products.
- Generate a rotation matrix and convert it to a quaternion.
- Compute the translation vector from the original to the new origin.
- Output a 4x4 transformation matrix suitable for 3D transformations.

## Installation

### Prerequisites

- Python 3.x
- NumPy
- SciPy

You can install the required Python packages using pip:

```bash
pip install numpy scipy
```

# Clone the Repository
```bash
git clone https://github.com/FilippoCinotti/Generic-utilites.git
cd Generic-utilities
```
# Usage
The script is designed to be used as a module or directly as a script. Below is an example of how to use it:

``` python
import numpy as np
from calculate_rigid_transform import calculate_rigid_transform

# Define the new origin and points defining the new coordinate system
new_origin = np.array([1.0, 2.0, 3.0])
x_point = np.array([1.0, 0.0, 0.0])
y_point = np.array([0.0, 1.0, 0.0])
z_point = np.array([0.0, 0.0, 1.0])

# Compute the rotation matrix, quaternion, and translation vector
rot_matrix, quaternion, translation = calculate_rigid_transform(new_origin, x_point, y_point, z_point)

# Display the results
print("Quaternion (x, y, z, w):", quaternion)
print("Translation vector:", translation)
print("4x4 transform matrix:")
print(transform_matrix)
```

# Running the Example
The script includes an example that you can run directly:

```bash
python RotTranslMatrix.py
```
This will output:
- The quaternion representing the rotation.
- The translation vector from the original to the new origin.
- A 4x4 transformation matrix for use in 3D applications.

# License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

# Contact
For any questions or feedback, please contact:

Name: Filippo Cinotti
Company: Medacta International SA
Email: filippo.cinotti96@gmail.com
