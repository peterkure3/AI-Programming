import gym
env = gym.make("CarRacing-v2", render_mode="human")
env.action_space.seed(42)

observation, info = env.reset(seed=42)
# action = policy(observation)  # User-defined policy function
for _ in range(5000):
   
   observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

   if terminated or truncated:
      observation, info = env.reset()
env.close()