# pyConfigurator

Provides a simplified way to check both cli and env for variables

## Usage

    import pyconfigurator

    config = pyconfigurator.Configurator()
    config.add_argument('tester', 'Test variable')
    config.add_argument('long-test', 'Long test variable')


The code above will create two configuration parameters:

- tester
- long-test

Both are available as cli flags with `--` prefix and capitalized as env vars:

- TESTER
- LONG_TEST

To parse the config simply run:

    config.parse()

This will make both entries available as:

- config.tester
- config.long_test