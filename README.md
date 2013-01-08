## Tattler

A nose plugin that tattles on functions.

Tattler was built to find tests that call functions during their execution.
When the test module is imported, those functions can be called without being
tattled on.

### Installation

    $ pip install tattler

### Usage

Have nose tell you about function and method usage like so:

    $ nosetests --with-tattler -t path.to.function -t path.to.object.method

A tattler.TattleTale exception will then be raised whenever one of those
functions gets called during test execution, and those tests will be reported
as errors.
