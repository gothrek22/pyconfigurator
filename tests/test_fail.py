import os
import sys
import pyconfigurator

def test_fail():
  config = pyconfigurator.Configurator()
  config.add_argument('tester', 'Test variable')
  config.add_argument('long-test', 'Long test variable')

  config.parse()
  print(getattr(config, "tester"))
  assert getattr(config, "tester") == None
  assert getattr(config, "long_test") == None