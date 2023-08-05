
Autoscaling units
=================


Using the ``autoscale`` method, quantities can be automatically scaled:

.. code:: python

    >>> a = 1e-3 m
    >>> a.autoscale

:math:`1.0 \text{mm}`



.. code:: python

    >>> a = 0.0003 s
    >>> a.autoscale

:math:`300.0 \text{µs}`

.. code:: python

    >>> a = 1.0m
    >>> a.autoscale

:math:`1.0 \text{m}`


.. code:: python

    >>> %precision 2
    >>> a = 3e-9 F
    >>> a.autoscale

:math:`3.00 \text{nF}`



