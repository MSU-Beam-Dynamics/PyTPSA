# PyTPSA

PyTPSA is a Python/C++ package that provides a library for performing Turncated Power Series Algebra (TPSA).  

## Installation

You will need cython for compiling the package.  Cython can be install by `pip`, as instructed [here](https://cython.readthedocs.io/en/stable/src/quickstart/install.html).

To install PyTPSA, simply run the following command:

```
python setup.py install
```

## How to use

PyTPSA supports both float and complex number as the derivatives of the function, arithmatic operations and fundamental mathmatical function.

* First, the package must be initialized to specify the polynomial's maximum order and number of variables.

    ```
    import PyTPSA
    num_var=4
    max_order=7
    PyTPSA.initialize(num_var, max_order)
    ```

* A constant can be either defined as number in python or a constant TPSA object:
    ```
    a = PyTPSA.tpsa(3.0)
    b = PyTPSA.tpsa(-1.0)
    k = PyTPSA.tpsa(2.0)
    ```

* The variable should be initialized as first order TPSA object.  For example, if the variables $(x, p_x, y, p_y)$ with float type is used to represent 6-D phase space, to study the derivative in the vicinity of $(0.0, 0.0, 0.0, 0.0)$, they should be initialized as:

    ```
    x=PyTPSA.tpsa(0.0, 1)
    px=PyTPSA.tpsa(0.0, 2)
    y=PyTPSA.tpsa(0.0, 3)
    py=PyTPSA.tpsa(0.0, 4)
    ```

    Alternatively, they can be defined as a list:

    ```
    vars=[PyTPSA.tpsa(0.0, i+1) for i in range(4)]
    ```

* Other quantities can be defined based on the variables and constants, for example the Hamiltonian is defined:
    ```
    Hamiltonian = (px*px + py*py)/2.0 + a * x * x + b * cos (k * y)
    ```

    Then the derivative of the Hamiltonian $\partial H / \partial y $ can be calculated as
    ```
    dHdy = Hamiltonian.derivative(3)
    ```
    Note that after deriviative, although the maximum order remains the same, the **useful** order is reduced by 1.

* To use complex number TPSA, use `dtype` argument in the initialization, for example:
    ```
    x=PyTPSA.tpsa(0.0, 1, dtype=complex)
    ```


