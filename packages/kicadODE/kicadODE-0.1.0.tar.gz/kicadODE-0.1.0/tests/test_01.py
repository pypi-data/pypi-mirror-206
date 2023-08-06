#!/usr/bin/env python3

import kicadODE


def test_01():
    A = [
        [ -0.1, 1 ],
        [ -1, -0.1 ]
    ]

    B = [
        [ 1.0 ],
        [ 0.0 ]
    ]

    C = [ [ 0.1, -0.2 ] ]

    D = [ [ 0.1 ] ]

    data = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        "name": "lti_model_01"
    }

    kicadODE.generate(data)


def test_02():
    A = [
        [ -0.1, 1 ],
        [ -1, -0.1 ]
    ]

    B = [
        [ 1.0 ],
        [ 0.0 ]
    ]

    C = [ [ 0.1, -0.2 ] ]

    D = [ [ 0.1 ] ]

    f = [ 'exp(-x1*x2)', ''  ]
    g = [ 'x1*x2*u1' ]

    data = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        "name": "lti_model_01",
        'f': f,
        'g': g,
    }

    kicadODE.generate(data)

def test_lorenz():
    sigma = 10
    beta = 8.0 / 3.0
    rho = 28

    A = 3 * [ 3 * [ 0 ] ]
    B = 3 * [ [ 0 ] ]
    C = [
        [ 1, 0, 0 ],
        [ 0, 1, 0 ],
        [ 0, 0, 1 ]
    ]
    D = 3 * [ [ 0 ] ]

    f = [
        f"{sigma}*(x2-x1)",
        f"x1*({rho}-x3)-x2",
        f"x1*x2-{beta}*x3",
    ]

    data = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        "name": "lorenz_01",
        'f': f,
        # "to_file": True,
    }

    kicadODE.generate(data)


def test_van_der_pol():
    mu = 1

    A = 2 * [ 2 * [ 0 ] ]
    B = 2 * [ [ 0 ] ]
    C = [
        [ 1, 0 ],
        [ 0, 1 ],
    ]
    D = 2 * [ [ 0 ] ]

    f = [
        f"x2",
        f"{mu}*(1-x1^2)*x2-x1",
    ]

    data = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        "name": "van_der_pol_01",
        'f': f,
        "x0": [ 1.0, 0 ],
        #"to_file": True,
    }

    kicadODE.generate(data)

    print(data["lib"])
