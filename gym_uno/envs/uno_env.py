import gymnasium as gym
import numpy as np
import pexpect
from gymnasium import spaces
import os


class UnoEnv(gym.Env):
    metadata = {'render_modes': ['human']}

    def __init__(self):
        self.obs = []
        self.reward = 0
        self.done = False
        self.action_space = spaces.Discrete(40)
        self.observation_space = spaces.Box(low=0, high=600, shape=(22,), dtype=np.uint16)

    def step(self, action):
        self.actions(action)
        self.commout()
        terminated = self.done
        truncated = False  # Set this according to your environment's logic if needed
        info = {}
        return self.obs, self.reward, terminated, truncated, info

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        jar_path = os.path.join(os.path.dirname(__file__), 'uno.jar')
        self.pext = pexpect.spawn(f'java -jar {jar_path}', encoding='utf-8')
        self.done = False
        self.commout()
        info = {}
        return self.obs, info

    def render(self, mode='human', close=False):
        return None

    def actions(self, action):
        newstring = str(action)
#        print (newstring)
        if (len(newstring) == 1):
            newstring = "0" + newstring
        self.pext.sendline(newstring)

    def commout(self):
#        print ("comms start")
        obs = []
        self.reward = 1
        for x in range(30):
            self.pext.expect("Machine")
            line = self.pext.readline()[2:4]
            if ("no" in line):
#                print ("noreward")
                self.reward = 0
                continue
            if ("v" in line):
#                print ("voitto")
                if ("0" in line):
                    self.reward=200
                self.pext.close()
                self.done = True
                break
            if ("en" in line):
                break
#            print (str(x) + ": " + line)
#            print (line)
            int(line)
            obs.append(line)
        if (len(obs) == 22):
            self.obs = obs
#        print (len(self.obs))
#        print (self.done)
#        if (not len(self.obs) == 22):
#        for g in range(len(self.obs)):
#           print(self.obs[g])

#x = UnoEnv()
#for m in range(5):
#    x.reset()
#    while (not x.done):
#        x.step(34)
