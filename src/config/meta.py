import copy
from typing import Callable

from utils.env import assert_env


class Meta:
    def __init__(self):
        self.configs = {}

    def set(self, env: str, config: dict):
        assert_env(env)

        self.configs[env] = copy.deepcopy(config)
        self.configs[env]["env"] = env

        return self

    def set_from(self, env: str, from_env: str, updater: Callable[[dict], None]):
        assert_env(env)
        assert_env(from_env)

        assert (
            self.configs[from_env] is not None
        ), f"Config for {from_env} is not defined"

        self.configs[env] = copy.deepcopy(self.configs[from_env])
        self.configs[env]["env"] = env
        updater(self.configs[env])

        return self

    def get_config(self, env: str) -> dict:
        assert_env(env)
        assert env in self.configs and self.configs[env] is not None, f"Config for {env} is not defined"

        return self.configs[env]
