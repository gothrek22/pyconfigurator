import os
import sys
import pyconfigurator

def test_parser():
  config = pyconfigurator.Configurator()
  config.add_argument('tester', 'Test variable')
  config.add_argument('long-test', 'Long test variable')

  os.environ['TESTER'] = 'var'
  sys.argv.append('--long-test')
  sys.argv.append('value')

  config.parse()
  
  assert config.long_test == 'value'
  assert config.tester == 'var'

  del os.environ['TESTER']
  sys.argv.pop()
  sys.argv.pop()