import os
import sys
import pyconfigurator

def test_cli():
  config = pyconfigurator.Configurator(cli=True)
  config.add_argument('tester', 'Test variable')
  config.add_argument('long-test', 'Long test variable')

  os.environ['TESTER'] = 'var'
  sys.argv.append('--tester')
  sys.argv.append('value')

  config.parse()
  
  assert config.tester == 'value'

  #Cleanup
  del os.environ['TESTER']
  sys.argv.pop()
  sys.argv.pop()