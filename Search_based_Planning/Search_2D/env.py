"""
Env 2D
@author: huiming zhou
"""


class Env:
    def __init__(self):
        self.x_range = 51  # size of background
        self.y_range = 31
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    


    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))
        
        def add_obs(ax, ay, bx, by):
            for i in range (ay, by):
                obs.add((ax, i))
            for i in range (ay, by):
                obs.add((bx, i))
            for i in range (ax, bx):
                obs.add((i, ay))
            for i in range (ax, bx+1):
                obs.add((i, by))
        
        add_obs(10, 10, 21, 21)
        add_obs(27, 24, 35, 29)
        add_obs(30, 7, 35, 12)
 

            
        return obs
'''
        for i in range(10, 21):
            obs.add((i, 15))
        for i in range(15):
            obs.add((20, i))

        for i in range(15, 30):
            obs.add((30, i))
        for i in range(16):
            obs.add((40, i))
'''

