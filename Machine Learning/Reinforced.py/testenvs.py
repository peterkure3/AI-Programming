# Importing the gym library
import gym

# Checking the number of environemnts that can be played with
envs = gym.envs.registry
env_ids = list(envs.keys())

print(env_ids) #prints all the environments
print('Total envs available:', len(env_ids)) #Prints number of environments
