import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the NPY file
file_path = "dhp19_joints.npy"
data = np.load(file_path)

print(f"Data shape: {data.shape}")
# expected shape: (T, J, 3) where T is timesteps, J is joints, and 3 are 3D coordinates

# preview the data (first frame and first joint)
print("First frame, all joints:\n", data[0])  # Shape: (J, 3)
print("First joint over all frames:\n", data[:, 0])  # Shape: (T, 3)

# Optional: Visualize the joint positions for a single frame
frame_idx = 0  # Choose a frame to visualize
frame_data = data[frame_idx]  # Shape: (J, 3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for joints
ax.scatter(frame_data[:, 0], frame_data[:, 1], frame_data[:, 2], color='blue', label='Joints')

# Annotate joint indices (optional)
for i, (x, y, z) in enumerate(frame_data):
    ax.text(x, y, z, f"{i}", color='red')

# Set labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"3D Joint Positions - Frame {frame_idx}")
plt.legend()
plt.show()
