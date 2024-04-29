def assert_env(env: str):
    assert env in ["development", "production", "e2e"], f"Not valid env: {env}"
