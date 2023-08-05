
Basics
======

This page describes the basic use and some internals of the Python module.

Installation
------------

The PhysicalQuantities module can be installed like any other Python module:

.. code::

    pip install PhysicalQuantities

Loading the Python Module
-------------------------

.. code:: python

    >>> import PhysicalQuantities as pq

Basic Use
---------

You can now define physical quantities using the
``PhysicalQuantity(value, unit)`` constructor:

.. code:: python

    >>> a = pq.PhysicalQuantity(1.1, 'm')
    >>> a
    >>> 1.1 m

or using the shortcut ``q``:

.. code:: python

    >>> from PhysicalQuantities import q
    >>> a = 1 * q.mm
    >>> b = 2 * q['mm']
    >>> a, b
    (1 mm, 2 mm)



Calling ``a = 1 * q.mm`` creates a new ``PhysicalQuantity`` object:

.. code:: python

    >>> print("object: %s" % a)
    object: 1 mm
    >>> print("object type: %s" % type(a))
    object type: <class 'PhysicalQuantities.Quantity.PhysicalQuantity'>


The value and unit are stored as attributes of the class:

.. code:: python

    >>> print("value: %s" % a.value)
    value: 1
    >>> print("value type: %s" % type(a.value))
    value type: <class 'int'>
    >>> print("unit: %s" % a.unit)
    unit: mm
    >>> print("unit type: %s" % type(a.unit))
    unit type: <class 'PhysicalQuantities.Unit.PhysicalUnit'>


Using ``.to()`` let's you convert to other representations of the unit.
This can be used for scaling or to express the quantity in a derived
unit. The ``.base`` property will convert

.. code:: python

    >>> g = pq.PhysicalQuantity(1.1, 'm')
    >>> print("g = %s" % g)
    g = 1.1 m
    >>> print("g in mm = %s" %g.to('mm'))
    g in mm = 1100.0 mm
    >>> x = pq.PhysicalQuantity(2, 'm*kg/s**2')
    >>> print("x = %s" %x)
    x = 2 kg*m/s^2
    >>> print("x in N = %s" % x.to('N'))
    x in N = 2.0 N
    >>> u = 1 V
    >>> print("u = %s" %u)
    u = 1 V
    >>> print("u in base units = %s" %u.base)
    u in base units = 1.0 kg*m^2/s^3/A


Scaling of simple units is easy using scaling attributes:

.. code:: python

    >>> print(g.nm)
    1100000000.0 nm
    >>> print(g.um)
    1100000.0 um
    >>> print(g.mm)
    1100.0 mm
    >>> print(g.cm)
    110.00000000000001 cm
    >>> print(g.m)
    1.1 m
    >>> print(g.km)
    0.0011 km


The physical quantity can converted back to a unitless value using the
underscore ``_`` with the scaling attribute:

.. code:: python

    >>> print(g.nm_)
    1100000000.0
    >>> print(g.um_)
    1100000.0
    >>> print(g.mm_)
    1100.0
    >>> print(g.cm_)
    110.00000000000001
    >>> print(g.m_)
    1.1
    >>> print(g.km_)
    0.0011


It is also possible to remove the unit without implicit scaling, however
this might be **dangerous**:

.. code:: python

    >>> g._
    1.1

Internal Representation
-----------------------

Internally, a physical quantity is represented using two classes: \*
``PhysicalQuantity`` holding the value and the unit \* ``PhysicalUnit``
describing the unit

.. code:: python

    >>> a = pq.Q([1, 2, 3], 'm**2*s**3/A**2/kg')
    >>> a.value
    [1, 2, 3]

The ``value`` attribute is basically only a container, allowing
different types of values. Tested types are:
* integers
* floats
* complex numbers
* uncertainties
* numpy arrays
* lists

.. code:: python

    >>> a.unit

:math:`\frac{\text{s}^{3}\cdot \text{m}^{2}}{\text{kg}\cdot \text{A}^2}`


.. code:: python

    >>> type(a.unit)
    PhysicalQuantities.Unit.PhysicalUnit


The unit is stored in a ``PhysicalUnit`` class. This class has a number
of attributes:
* ``factor`` - scaling factor from base units
* ``powers`` - list of SI base units contained in unit. All other units can be reduced to these base units.
* ``prefixed`` - unit is a scaled version of a base unit

.. code:: python

    >>> pq.Q(1,'mm').unit.factor, pq.Q(1,'mm').unit.prefixed
    (0.001, True)


.. code:: python

    >>> from PhysicalQuantities.unit import base_names
    >>> print(base_names) # list containing names of base units
    ['m', 'kg', 's', 'A', 'K', 'mol', 'cd', 'rad', 'sr']
    >>> a = q.m
    >>> print(a.unit.powers)
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> print(a.unit.baseunit)
    m


A more complex example:



    >>> from PhysicalQuantities.unit import base_names
    >>> print(base_names) # list containing names of base units
    ['m', 'kg', 's', 'A', 'K', 'mol', 'cd', 'rad', 'sr']
    >>> a = q.m
    >>> print(a.unit.powers)
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> print(a.unit.baseunit)
    m


A more complex example:



    >>> from PhysicalQuantities.Unit import base_names
    >>> print(base_names) # list containing names of base units
    ['m', 'kg', 's', 'A', 'K', 'mol', 'cd', 'rad', 'sr']
    >>> a = q.m
    >>> print(a.unit.powers)
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> print(a.unit.baseunit)
    m


A more complex example:

.. code:: python

    >>> a = pq.Q([1,2,3], 'm**2*s**3/A**2/kg')
    >>> print(base_names)
    ['m', 'kg', 's', 'A', 'K', 'mol', 'cd', 'rad', 'sr']
    >>> print(a.unit.powers)
    [2, -1, 3, -2, 0, 0, 0, 0, 0]
    >>> print(a.unit.baseunit)
    s^3*m^2/kg/A^2
