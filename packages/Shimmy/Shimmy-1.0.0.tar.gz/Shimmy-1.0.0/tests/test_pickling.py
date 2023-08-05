import pickle

import pytest
from gymnasium.utils.env_checker import data_equivalence

env_ids = []
envs = []


@pytest.mark.parameterize("env", envs, ids=env_ids)
def test_pickling(env):
    pickled_env = pickle.loads(pickle.dumps(env))

    data_equivalence(env.reset(), pickled_env.reset())

    action = env.action_space.sample()
    data_equivalence(env.step(action), pickled_env.step(action))

    env.close()
    pickled_env.close()
