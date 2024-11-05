#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# calculate_rigid_transform.py
# Copyright (C) 2024 Filippo Cinotti
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from scipy.spatial.transform import Rotation as R

def calculate_rigid_transform(new_origin, x_point, y_point, z_point):
    """
    Calculate the rigid body transformation (rotation and translation) 
    required to move the coordinate system from the original basis to 
    a new one defined by the given points.
    
    Parameters:
    - new_origin: The new origin of the coordinate system (numpy array).
    - x_point: A point defining the new x-axis direction (numpy array).
    - y_point: A point defining the new y-axis direction (numpy array).
    - z_point: A point defining the new z-axis direction (numpy array).

    Returns:
    - rotation_matrix: The 3x3 rotation matrix aligning the original 
      coordinate system with the new one.
    - rotation_quaternion: The quaternion representing the same rotation.
    - translation_vector: The vector representing the translation from 
      the origin to the new origin.
    """
    
    # Calculate the new basis vectors for the new coordinate system
    new_x_axis = (x_point - new_origin) / np.linalg.norm(x_point - new_origin)
    new_y_axis = (y_point - new_origin) / np.linalg.norm(y_point - new_origin)
    new_z_axis = (z_point - new_origin) / np.linalg.norm(z_point - new_origin)
    
    # Ensure orthogonality by using the cross product
    new_y_axis = np.cross(new_z_axis, new_x_axis)
    new_y_axis /= np.linalg.norm(new_y_axis)
    new_z_axis = np.cross(new_x_axis, new_y_axis)
    new_z_axis /= np.linalg.norm(new_z_axis)

    # Create the rotation matrix from the new basis vectors
    rotation_matrix = np.column_stack((new_x_axis, new_y_axis, new_z_axis))

    # Convert the rotation matrix to a quaternion for easier use in 3D transformations
    rotation_quaternion = R.from_matrix(rotation_matrix).as_quat()  # [x, y, z, w] format

    # The translation vector is simply the new origin of the coordinate system
    translation_vector = new_origin

    return rotation_matrix, rotation_quaternion, translation_vector

# Example usage of the calculate_rigid_transform function
new_origin = np.array([1.0, 2.0, 3.0])
x_point = np.array([1.0, 0.0, 0.0])
y_point = np.array([0.0, 1.0, 0.0])
z_point = np.array([0.0, 0.0, 1.0])

# Compute the transformation matrix, quaternion, and translation vector
rot_matrix, quaternion, translation = calculate_rigid_transform(new_origin, x_point, y_point, z_point)

# Construct a 4x4 transformation matrix for homogeneous coordinates
transform_matrix = np.eye(4)
transform_matrix[:3,:3] = rot_matrix  # Set the rotation part
transform_matrix[:3,3] = translation  # Set the translation part

# Print the results
print("Quaternion (x, y, z, w):", quaternion)
print("Translation vector:", translation)
print("4x4 transform matrix:")
print(transform_matrix)
