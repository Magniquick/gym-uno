import logging
from gymnasium.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Uno-v0',
    entry_point='gym_uno.envs:UnoEnv',
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
