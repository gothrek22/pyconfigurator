#!python3
__version__ = "0.0.1"

import os
from argparse import ArgumentParser


class Configurator():
    """Wrapper for ArgumentParser and os.getenv(), intending to provide
    an easier way to get configuration.
    Shorthand flags are currently not supported.

    Keyword arguments:
    - cli -- cli takes precedence over env vars. Default: False
    """

    def __init__(self, cli=False):
        self._osEnv = {}
        self._ap = ArgumentParser()
        self._cli = cli

    def add_argument(self,
                     dest,
                     help):

        key = dest.replace('-', '_')
        if len(dest) < 2:
          print("dest can't be shorter than 2 characters")
        self._osEnv[key] = key.upper()
        self._ap.add_argument("--" + dest, dest=key, action='store', help=help)

    def parse(self):
        """ Parse options for both cli args and env vars, 
        and return them as attributes of Configurator.
        Env vars take precedence by default."""
        _args = self._ap.parse_args()
        _envs = dict()
        
        for k in self._osEnv.keys():
          _temp = os.getenv(self._osEnv[k])
          if _temp:
            _envs[k] = _temp
          else:
            pass
        _td = vars(_args)
        if self._cli:
          _envs.update(_td)
          for key in _envs:
            setattr(self, key, _envs[key])
        else:
          _td.update(_envs)
          for key in _td:
            setattr(self, key, _td[key])

        
