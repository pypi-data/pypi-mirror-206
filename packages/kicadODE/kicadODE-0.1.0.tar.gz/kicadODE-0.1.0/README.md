# Spice model generator for Kicad's NGSpice solver

Generates a Kicad model and corresponding ngspice model from the provided
ordinary differential equation (ODE) to be solved by NGspice. Considered ODEs
are defined in this general form.

$$\dot{x}=Ax+Bu+f(x,u)$$

$$y=Cx+Du+g(x,u)$$

where 

- $x\in\mathbb{R}^n$ is the $n$ dimensional state vector
- $u\in\mathbb{R}^m$ is the $m$ dimensional input vector
- $y\in\mathbb{R}^r$ is the $r$ dimensional output vector
- $A\in\mathbb{R}^{n \times n}$ is the state matrix
- $B\in\mathbb{R}^{n \times m}$ is the input matrix
- $C\in\mathbb{R}^{r \times n}$ is the output matrix
- $D\in\mathbb{R}^{r \times m}$ is the input-to-output matrix
- $f(x,u)$ vector of functions of state and input vectors
- $g(x,u)$ vector of functions of state and input vectors

## Example

Let us define an ODE where $n=2$, $m=1$, $r=2$.

``` python
import kicadODE

data = {
    'A': [
        [ -0.1, 1 ],
        [ 0, -0.1 ],
    ],
    'B': [
        [ 1 ],
        [ 0 ],
    ],
    'C': [
        [ 1e-2, 0 ],
        [ 0, 1e-2 ],
    ],
    'D': [
        [ 0 ],
        [ 0 ],
    ],
    'f': [
        '-0.01*x1^3-x2^3/33',
        'exp(-u1)',
    ],
    'g': [
        'sin(x1*x2)',
        'x1/(x2^2+1)',
    ],
    "x0": [ 1.0, -0.3 ], # Initial conditions
    "name": "test_model", # Name of Kicad model
    "to_file": True, # Exports 'test_model.lib' and 'test_model.kicad_sym'
}

kicadODE.generate(data)
print(data["lib"])
print(data["sym"])
```

Parameters `A, B, C, D` are required. If your model does not need the linear part, set `A,B,C,D` zero
matrices with appropriate dimensions.

Parameters `f` and `g` can contain math terms which are supported by ngspice. Please, visit
[this page](https://ngspice.sourceforge.io/docs/ngspice-html-manual/manual.xhtml#magicparlabel-5564)
for a list of all supported functions.
