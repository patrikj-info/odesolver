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

```Python
    # load ode
    ode = ODE.readHomogenousODE("4.0x'' + 0.1x' + 2.0x")

    # find solution using Euler's method
    sol = ODESolver.solveODE(ode=ode, method="euler", initial_conditions=[1.0, 0.0], t0=0, t_final=10, h=0.01)

    # plot solution
    ODESolver.plotSolution(sol, phase_space=True, save=True, filename="harm_oscillator_euler.png", fileformat="png")
```
