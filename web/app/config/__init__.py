import os
from app.config.default import Config as DefaultConfig

_config = None

class MixedConfig(DefaultConfig):
    inited = False

def get_config():
    """
    单例配置加载
    :return: Config 类实例
    """
    if MixedConfig.inited:
        return MixedConfig
    else:
        mode = os.environ.get('MODE')
        _override_config = {}

        try:
            if mode == "DEVELOPMENT":
                from app.config.development import DevelopmentConfig
                _override_config = DevelopmentConfig
                MixedConfig.CONFIG_NAME = 'development'
            elif mode == "PRODUCTION":
                from app.config.production import ProductionConfig
                _override_config = ProductionConfig
                MixedConfig.CONFIG_NAME = 'production'
            else:
                MixedConfig.CONFIG_NAME = 'default'
        except ImportError:
            print("Config Loading Error!!")
            exit(1)

        for key in dir(_override_config):
            if key.isupper():
                if isinstance(getattr(_override_config, key), dict) \
                        and key in dir(MixedConfig) \
                        and isinstance(getattr(MixedConfig, key), dict):
                    dict_to_modify = getattr(MixedConfig, key)
                    for key, value in getattr(_override_config, key).items():
                        dict_to_modify[key] = value
                    setattr(MixedConfig, key, dict_to_modify)
                else:
                    setattr(MixedConfig, key, getattr(_override_config, key))
        MixedConfig.inited = True
        return MixedConfig
