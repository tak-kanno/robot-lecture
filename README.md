# robot-lecture
Sample codes for TITECH lecture "Interdisciplinary Research FUndamentals II 3"


# Tested environment
- Ubuntu 20.04.2 LTS on WSL2
- Python 3.8.10
- Python modules
    - numpy 1.24.3
    - matplotlib 3.7.1
    - opencv-python 4.7.0.72

# Numeric IK
## About
- `numeric_ik.py` is a sample code for numeric IK solving.
- The code solves IK for a 2-link planar robot.
- I implemented both analytical and numerical methods for getting Jabobian. Try them.

![Example animation](https://github.com/tak-kanno/robot-lecture/blob/main/docs/imgs/animation.gif)

## Usage
- Run `python numeric_ik.py`. It creates a series of images in `frames` folder, that shows the progress of IK solving.
- Use `create_animation.py` to create an animation from the saved data.
