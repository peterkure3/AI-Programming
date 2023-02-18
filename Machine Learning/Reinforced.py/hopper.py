import gym

env = gym.make("Hopper-v3", render_mode="human")
env.action_space.seed(82)

observation, info = env.reset(seed=82)
# action = policy(observation)  # User-defined policy function
for _ in range(1000):
   
   observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

   if terminated or truncated:
      observation, info = env.reset()
env.close()