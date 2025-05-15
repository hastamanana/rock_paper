import os
from environs import Env
import pprint

env = Env()
env.read_env()

for k,v in os.environ.items():
    print(k, v)
