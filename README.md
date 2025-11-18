# odesolver

A simple tool to solve ODEs numerically and plot the solution.


## Features 
    - Solve ODEs with the Euler method 
    - Solve ODEs with the RK4 method

## Installation

You can install the package via **PyPI** or from **source**.

### Install from PyPI

```bash
    pip install jp-odesolver
```

### Install from Source (GitHub)

```bash
    git clone https://github.com/patrikj-info/odesolver.git
    cd odesolver
    pip install .
```

## Usage

### Creating ODE

```Python
    from odesolver.ode import ODE

    # load homogenous ODE
    ode = ODE.readHomogenousODE("4.0x'' + 0.1x' + 2.0x")

    import numpy as np

    def funct(t,x):
        return np.cos(t)

    # load inhomogenous ODE
    ode = ODE.readODE("4.0x'' + 0.1x' + 2.0x", inhom=funct)
```


### Solving using Euler's Method

```Python
    from odesolver.odesolver import ODESolver

    # find solution using Euler's method
    sol = ODESolver.solveODE(ode=ode, method="euler", initial_conditions=[1.0, 0.0], t0=0, t_final=10, h=0.01)
```

### Solving using Runge-Kutta Order 4
```Python
    # find solution using Runge-Kutta 4
    sol = ODESolver.solveODE(ode=ode, method="rk4", initial_conditions=[1.0, 0.0], t0=0, t_final=10, h=0.01)
```

### Plotting Solution 
```Python
    from odesolver.solver import unpackData
    from odesolver.plotter import Plotter

    # retrieve data from solution
    t,x = unpackData(data=sol, axes=(0,1))

    # plot solution
    Plotter.plot(t, x, filename="harm_oscillator_euler.png", fileformat="png")
```

### Creating Animated Graphs
```Python
    # plot solution
    # NOTE: the creation of the graph may take a relatively long time. Changing the fps may prove useful.
    Plotter.plot(t, x, animation=True, filename="harm_oscillator_euler.gif", fileformat="gif")
```

### N-dimensional ODEs
Following, an example with N = 2 will be regarded.

```Python
    from numpy import sqrt
    import numpy as np
    from odesolver.ode import ODE
    from odesolver.plotter import Plotter
    from odesolver.odesolver import ODESolver

    g = 4 * np.pi ** 2  # Gravitational constant Astronomical Units
    m = 3.00349e-6      # Earth's mass in solar mass units (sun=1 mass)
    dist = 1         # Earth-Sun distance AU
    v = 2 * np.pi       # Orbital speed Earth (r=1AU) T=1 yr

    def betrag(x):
        sum = 0
        for i in range(len(x)):
            sum += x[i]**2
        return sqrt(sum)

    x0 = np.array([0, 0])

    def funct(t, x):
        return -g * x[0]/betrag(x[0] - x0)**3


    ode = ODE(2, funct, 2)
    sol = ODESolver.solveODE(ode, method="rk4", initial_conditions = [[0,dist], [v,0]], t0=0, t_final=200, h=0.01)
    t, r, v = unpackData(sol)
    
    Plotter.plot(xdata=r.T[0], ydata=r.T[1], filename="test.png", fileformat="png", xlabel="x", ylabel="y")
```