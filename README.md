# odesolver

A simple tool to solve ODEs numerically and plot the solution.


## Features 
    - Solve ODEs with the Euler method 
    - Solve ODEs with the RK4 method

## Installation

You can install the package via **PyPI** or from **source**.

### Install from PyPI

```bash
    pip install odesolver
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
    # plot solution
    ODESolver.plotSolution(sol, phase_space=True, save=True, filename="harm_oscillator_euler.png", fileformat="png")
```

### Creating Animated Graphs
```Python
    # plot solution
    # NOTE: the creation of the graph may take a relatively long time. Changing the fps may prove useful.
    ODESolver.plotSolution(sol, phase_space=False, save=True, filename="harm_oscillator_euler.gif", fileformat="gif", fps=500)
```