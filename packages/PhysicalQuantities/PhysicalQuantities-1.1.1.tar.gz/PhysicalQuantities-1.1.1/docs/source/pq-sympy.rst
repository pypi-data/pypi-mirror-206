
Sympy and PhysicalQuantities
============================

.. code:: python

    >>> from sympy import *
    >>> init_printing()
    >>> a = 1 m * Matrix([ [1,2,3], [4,5,6]])
    >>> b = 1 cm * Matrix([ [1,2,3], [4,5,6]])
    >>> a

:math:`\left[\begin{matrix}1 & 2 & 3\\4 & 5 & 6\end{matrix}\right] \text{m}`

.. code:: python

    >>> a+b

:math:`\left[\begin{matrix}1.01 & 2.02 & 3.03\\4.04 & 5.05 & 6.06\end{matrix}\right] \text{m}`


.. code:: python

    >>> x = Symbol('x')
    >>> 1 m * x

:math:`x \text{ m}`



.. code:: python

    >>> a = 2 m * x
    >>> a

:math:`2 x \text{ m}`


.. code:: python

    >>> a/3

:math:`\frac{2 x}{3} \text{m}`

.. code:: python

    >>> Integral(sqrt(1/x), x)

:math:`\int \sqrt{\frac{1}{x}}\, dx`



