# hash_expiry_gears

This is a script that will remove a hash key name from a set (secondary index) upon expiry of the hash.

# Install

## Setup redis instance/cluster with RedisGears
See https://oss.redis.com/redisgears/quickstart.html

## Setup virtual env
```sh
python3 -m venv gears 
pip install -U pip
pip install -U wheel setuptools 
source gears/bin/activate
```

## Clients

```sh
pip install redis
pip install git+https://github.com/RedisGears/redisgears-py.git
```

# Run
```sh
python3 gears.py
```

# Test
- In redis-cli, check set members before and after expiry of the "test1" hash (15seconds TTL).