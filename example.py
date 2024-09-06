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
