import gym

# Checking the number of environemnts that can be played with
envs = gym.envs.registry
env_ids = list(envs.keys()) #Stores environment ids as a list

#prints all the environments
print(env_ids) 

#Prints number of environments
print('Total envs available:', len(env_ids)) 

# Create the environemnt
env = gym.make('CartPole-v1',render_mode="rgb_array")

# Define the agent's policy
def policy(observation):
    if observation[2] > 0:
        return 1
    else:
        return 0

# Play the game with the agent
total_reward=0
observation = env.reset()
for t in range(1000):
    env.render()
    action= policy(observation)
    observation, reward, done, info, = env.step(action)
    total_reward += reward
    if done:
        break

# Print the total reward
print("TOtal reward:", total_reward)