# parking-env
parking-env is a gymnasium-based environment for reinforcement learning, written in a single Python file and accelerated by Numba. The environment is designed to simulate the task of parking a vehicle in a parking lot, where the agent controls the steering angle and the speed to park the vehicle successfully.

## Installation
To install parking-env, you can clone the repository from GitHub:

```
git clone https://github.com/KexianShen/parking-env.git
```
Then, navigate to the root directory of the repository and run:

```
pip install -e .
```
This will install the environment and all its dependencies.

## Usage
To use parking-env, you can import it in your Python code as follows:

```
import gymnasium as gym
import parking_env

env = gym.make("Parking-v0", render_mode="human")
```

## Credits
parking-env is heavily inspired by the [HighwayEnv](https://github.com/eleurent/highway-env) environment, and some of its code was adapted for use in parking-env.

Additionally, parking-env uses the algorithms provided in [CleanRL](https://github.com/vwxyzjn/cleanrl), a collection of clean implementations of popular RL algorithms.

## License
This project is licensed under the MIT License - see the LICENSE file for details.