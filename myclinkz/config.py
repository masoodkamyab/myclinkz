import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="myclinkz",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="myclinkz_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from myclinkz.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export myclinkz_KEY=value
export myclinkz_KEY="@int 42"
export myclinkz_KEY="@jinja {{ this.db.uri }}"
export myclinkz_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
myclinkz_ENV=production myclinkz run
```

Read more on https://dynaconf.com
"""
