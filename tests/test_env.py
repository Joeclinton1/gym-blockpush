import gymnasium as gym
import pytest
from gymnasium.utils.env_checker import check_env

import gym_blockpush  # noqa: F401


@pytest.mark.parametrize(
    "env_task, obs_type",
    [
        ("BlockPush-v0", "state"),
    ],
)
def test_blockpush(env_task, obs_type):
    env = gym.make(f"gym_blockpush/{env_task}", obs_type=obs_type)
    check_env(env.unwrapped)
