import os
import sys
import pyconfigurator

def test_env():
  config = pyconfigurator.Configurator()
  config.add_argument('tester', 'Test variable')
  config.add_argument('long-test', 'Long test variable')

  os.environ['LONG_TEST'] = 'var'
  sys.argv.append('--long-test')
  sys.argv.append('value')

  config.parse()
  
  assert config.long_test == 'var'

  #Cleanup
  del os.environ['LONG_TEST']
  sys.argv.pop()
  sys.argv.pop()