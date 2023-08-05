
ruamel.yaml.string
==================

:version:       0.1.1
:updated:       2023-05-02

This plug-in adds a method ``dump_to_string`` (and its equivalent ``dumps``)
to the ``ruamel.yaml.YAML`` instance that returns the document as
a Python ``string``.

Installation
============

The module can be installed from PyPI using::

    pip install ruamel.yaml.string

This module is dependent on ``ruamel.yaml``, so you do not have to explicitly
make your module depending on both.

Usage
=====

.. code:: python

  import ruamel.yaml

  yaml = ruamel.yaml.YAML(typ=['rt', 'string'])
  data  = dict(abc=42, help=['on', 'its', 'way'])
  print('retval', yaml.dump_to_string(data))
  print('>>>> done')

which gives::

  retval abc: 42
  help:
  - on
  - its
  - way
  >>>> done


Please note that there is no final newline added to the string
that is returned. That the ``>>>> done`` is on the next line is caused by
the `print()` function adding a newline by default. (This is different
from using PyYAML's `dump`, as e.g. the output of various ``print dump(data)`` 
examples in the documentation (2021) fail to clearly show the double newline at the
end of the examples output. It is similar to `json.dumps(data, indent=2)` that returns
a string without final newline.)

Alternatively the
first call to ``print`` could be::

  print('retval', yaml.dump_to_string(data, add_final_eol=True), end='')

with the same effect.

`.dump_to_string()` can be shortened to `.dumps()`

*Directly writing to ``sys.stdout`` using ``yaml.dump(data, sys.stdout)`` is 
much more efficient than ``print``-ing the result of ``yaml.dumps(data)``*


ChangeLog
=========

0.1.1 (2023-05-02):
  - typing added and readme corrections

0.1.0 (2022-03-17):
  - initial plug-in version
