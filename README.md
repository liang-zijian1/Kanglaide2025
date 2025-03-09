# Kanglaide Project-AquaSentry

## Project Overview

The Kanglaide project is designed to develop a robotic control system that utilizes computer vision and advanced control algorithms. The robot is equipped with modules for flywheel control, pitch adjustment, yaw control, and auto-aim functionality, making it suitable for various applications in robotics and automation.

## Key Features

- **Real-time Control**: Operate the robot using an Xbox controller for precise control over its movements.
- **Flywheel Control**: Adjust the speed of the flywheel for optimal performance.
- **Pitch and Yaw Control**: Control the pitch and yaw angles of the robot to aim accurately at targets.
- **Auto-Aim Functionality**: Automatically adjust the aim based on sensor data, enhancing targeting accuracy.
- **NetworkTables Integration**: Share sensor data and control commands using NetworkTables for real-time updates.

## Tech Stack

- Python 3.12
- WPILib
- NetworkTables
- Custom modules for shooter, pitch, yaw, and auto-aim functionalities

## Installation Guide

1. **Clone the repository**:

   ```bash
   git clone https://github.com/liang-zijian1/Kanglaide2025.git
   cd Kanglaide2025
   ```

2. **Install dependencies**:

   Make sure you have Python 3.12 installed. Then, install any necessary dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup NetworkTables**:

   Ensure that the NetworkTables server address in the code matches your setup. Modify the `server` parameter in the `NetworkTables.initialize()` method if necessary.

## Usage

1. **Connect the Xbox Controller**: Ensure the controller is connected to the robot's control system.
2. **Run the Robot Code**:

   ```bash
   python main.py
   ```

3. **Control the Robot**:
   - Use the right trigger to control the flywheel speed.
   - Use the Y and A buttons to control the pitch angle.
   - Use the X and B buttons to control the yaw angle.
   - Toggle auto-aim mode with the designated button.

4. **Exit the Program**: Press `q` to safely exit the program when finished.

## Code Structure

```
Kanglaide2025/
│
├── main.py                  # Main robot control program
├── requirements.txt         # List of dependencies
├── shooter.py               # Flywheel control module
├── pitch.py                 # Pitch control module
├── yaw.py                   # Yaw control module
├── autoaim.py               # Auto-aim module
└── README.md                # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.



