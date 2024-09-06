from gymnasium.envs.registration import register

register(
    id="gym_blockpush/BlockPush-v0",
    entry_point="gym_blockpush.blockpush_multimodal:BlockPushMultimodal",
    max_episode_steps=350,
    kwargs={"obs_type": "state"},
)

# register(
#     id="BlockPushRgb-v0",
#     entry_point=BlockPushMultimodal,
#     max_episode_steps=350,
#     kwargs=dict(image_size=(block_pushing.IMAGE_HEIGHT, block_pushing.IMAGE_WIDTH)),
# )
