# gym-block-push

A gym environment for Block Push

[You may want to replace this image with one relevant to Block Push]
<!-- <img src="https://diffusion-policy.cs.columbia.edu/videos/block_push.mp4" width="50%" alt="Block Push environment"/> -->

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
Block Push environment.

[Add a brief description of the Block Push task here. For example:]
In this environment, a robotic arm must push a block to a target location on a table.

### Action Space
[Modify this section to describe the action space for Block Push. For example:]
The action space consists of continuous values for the robotic arm, resulting in an X-dimensional vector:
- [List the components of the action space]

### Observation Space
Observations are provided as a dictionary with the following keys:

- `robot_state`: Position and velocity data for the robot arm.
- `block_state`: Position and orientation of the block.
- `target_state`: Position of the target.
- `images`: Camera feeds from different angles (if applicable).

### Rewards
[Describe the reward structure for Block Push. For example:]
- X points for moving the block closer to the target.
- Y points for successfully pushing the block to the target location.
- Negative rewards for actions that move the block away from the target or out of bounds.

### Success Criteria
[Define what constitutes success in this environment]

### Starting State
[Describe the initial configuration of the environment]

### Arguments

```python
>> > import gymnasium as gym
>> > import gym_blockpush
>> > env = gym.make("gym_block_push/BlockPush-v0", obs_type="state", render_mode="rgb_array")
>> > env
< TimeLimit < OrderEnforcing < PassiveEnvChecker < BlockPushEnv < gym_blockpush / BlockPush - v0 >> >> >
```

* `obs_type`: (str) The observation type. Can be either `state` or `pixels`. Default is `state`.

* `render_mode`: (str) The rendering mode. Only `rgb_array` is supported for now.

* [List any other arguments specific to the Block Push environment]

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
