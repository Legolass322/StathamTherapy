import pytest

from contextlib import nullcontext as does_not_raise

from config.meta import Meta


class TestMeta:
    @pytest.mark.parametrize(
        "env,ctx",
        [
            ("some", pytest.raises(AssertionError)),
            ("development", does_not_raise()),
            ("production", does_not_raise()),
        ],
    )
    def test_input_envs(self, env, ctx):
        with ctx:
            Meta().set(env, {}).set_from(env, env, lambda x: x)
    
    def test_undefined_env(self):
        with pytest.raises(AssertionError):
            Meta().set("production", {}).get_config("development")

    def test_config(self):
        def updater(it):
            it["a"] = 2
            if "dict" in it:
                it["dict"]["b"] = 3

        meta = (
            Meta()
            .set("production", {"a": 1})
            .set_from("development", "production", updater)
        )
        config_prod = meta.get_config("production")
        config_dev = meta.get_config("development")

        assert len(config_prod) == len(config_dev)
        assert len(config_prod) == 2

        assert config_prod["env"] == "production"
        assert config_dev["env"] == "development"

        assert config_prod["a"] == 1
        assert config_dev["a"] == 2
        
        input_config = {"a": 1, "str": "string", "bool": True, "num": 12, "dict": {"b": 2}}
        config = Meta().set("production", input_config).set_from("development", "production", updater).get_config("development")
        
        assert config["a"] == 2
        assert config["str"] == "string"
        assert config["bool"] == True
        assert config["num"] == 12
        assert config["dict"]["b"] == 3
