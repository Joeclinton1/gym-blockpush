## gym-block-push

A gym environment for Block Push

<img src="https://github.com/user-attachments/assets/78de63f7-868c-49b4-8482-4ce25ff3a014" width="400">

## Installation

Create a virtual environment with Python 3.10 and activate it, e.g. with [`miniconda`](https://docs.anaconda.com/free/miniconda/index.html):
```bash
conda create -y -n block-push python=3.10 && conda activate block-push
```

Install gym-block-push:
```bash
pip install gym-block-push
```

## Quickstart

```python
# example.py
import imageio
import gymnasium as gym
import numpy as np
import gym_blockpush

env = gym.make("gym_blockpush/BlockPush-v0", obs_type="environment_state_agent_pos")
observation, info = env.reset()
frames = []

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    image = env.render()
    frames.append(image)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
imageio.mimsave("example.mp4", np.stack(frames), fps=25)
```

## Description
Block Push environment. In this environment, a robotic arm must push a block to a target location on a table. The agent is a circle and the block is a tee shape.

### Action Space
The action space consists of continuous values for the robotic arm, resulting in a 2-dimensional vector:
- `x`: Represents the target position of the agent in the x-coordinate. Values are in the range [0, 512].
- `y`: Represents the target position of the agent in the y-coordinate. Values are in the range [0, 512].

### Observation Space
Observations are provided as a dictionary with the following keys:

- `environment_state`: A 16-dimensional vector representing the keypoint locations of the T shape block (in [x0, y0, x1, y1, ...] format). The values are in the range [0, 512]. (when obs_type is set to `environment_state_agent_pos`)
- `agent_pos`: A 2-dimensional vector representing the position of the robot end-effector. (when obs_type is set to `environment_state_agent_pos`)
- `robot_state`: Position and velocity data for the robot arm. (if applicable and part of the state).
- `block_state`: Position and orientation of the block. When `obs_type` is set to `state`, it is a 5-dimensional vector representing the state of the environment: [agent_x, agent_y, block_x, block_y, block_angle]. The values are in the range [0, 512] for the agent and block positions and [0, 2*pi] for the block angle.
- `target_state`: Position of the target.
- `images`: Camera feeds from different angles (if applicable). When `obs_type` is set to `pixels`, the observation space is a 96x96 RGB image of the environment.

### Rewards
The reward is based on the coverage of the block in the goal zone:
- Reward is 1.0 if the block is fully in the goal zone.
- Negative rewards for actions that move the block away from the target or out of bounds (if applicable).

### Success Criteria
The environment is considered solved if the block is at least 95% in the goal zone.

### Starting State
The agent starts at a random position, and the block starts at a random position and angle. The target position is also randomly generated.

### Arguments

```python
>> > import gymnasium as gym
>> > import gym_blockpush
>> > env = gym.make("gym_block_push/BlockPush-v0", obs_type="state", render_mode="rgb_array")
>> > env
< TimeLimit < OrderEnforcing < PassiveEnvChecker < BlockPushEnv < gym_blockpush / BlockPush - v0 >> >> >
```

* `obs_type`: (str) The observation type. Can be either `state`, `environment_state_agent_pos`, `pixels` or `pixels_agent_pos`. Default is `state`.
* `render_mode`: (str) The rendering mode. Can be either `human` or `rgb_array`. Default is `rgb_array`.
* `block_cog`: (tuple) The center of gravity of the block if different from the center of mass. Default is `None`.
* `damping`: (float) The damping factor of the environment if different from 0. Default is `None`.
* `observation_width`: (int) The width of the observed image. Default is 96.
* `observation_height`: (int) The height of the observed image. Default is 96.
* `visualization_width`: (int) The width of the visualized image. Default is 680.
* `visualization_height`: (int) The height of the visualized image. Default is 680.

## Contribute

Instead of using `pip` directly, we use `poetry` for development purposes to easily track our dependencies.
If you don't have it already, follow the [instructions](https://python-poetry.org/docs/#installation) to install it.

Install the project with dev dependencies:
```bash
poetry install
```

### Follow our style

```bash
# install pre-commit hooks
pre-commit install

# apply style and linter checks on staged files
pre-commit
```

## Acknowledgment

gym-block-push is adapted from [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) (which itself is adpated from [BET](https://github.com/notmahi/bet) and [IBC](https://github.com/google-research/ibc)).
