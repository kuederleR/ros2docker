# Use the official ROS2 Docker image as the base image
FROM ros:humble

# Set the working directory
WORKDIR /workspace

# Install additional dependencies if needed
RUN apt-get update

# Copy your ROS2 workspace into the container
COPY . /workspace

# Build your ROS2 workspace
RUN colcon build
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN apt-get update && apt-get install -y python3-pip
# Install Python packages from python_packages.txt
# RUN pip install -r /workspace/python_packages.txt
# Install necessary dependencies for running PyQt6 GUI applications
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-xfixes0 \
    libxcb-xkb1 \
    xauth

# ENV DISPLAY=:0

RUN pip install pyqt6
# Set the entrypoint command
CMD ["bash"]