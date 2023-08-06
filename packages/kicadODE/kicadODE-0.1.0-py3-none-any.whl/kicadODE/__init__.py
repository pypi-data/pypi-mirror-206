#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (c) 2023 Okan Demir
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

from . import helpers as _h


def _generate_id(data, id_type):
    id = data[id_type]
    data[id_type] = id + 1

    return id


def _generate_lib_header(data, lines):
    n = data['n']
    m = data['m']
    r = data['r']
    gnd_id = data["GND_ID"]

    line = "* PINOUT ORDER GND"
    for i in range(m):
        line += f" u{i+1}"
    for i in range(r):
        line += f" y{i+1}"

    lines += [ line ]

    u_nodes = []
    line = f".SUBCKT {data['name']}"
    line += f" {gnd_id}"
    for i in range(m):
        node_id = _generate_id(data, "NODE_ID")

        line += f" {node_id}"
        u_nodes += [ node_id ]

    y_nodes = []
    for i in range(r):
        node_id = _generate_id(data, "NODE_ID")

        line += f" {node_id}"
        y_nodes += [ node_id ]

    data["u_nodes"] = u_nodes
    data["y_nodes"] = y_nodes
    lines += [ line ]

    return 0


def _generate_integrators(data, lines):
    n = data['n']
    m = data['m']
    r = data['r']
    u_nodes = data["u_nodes"]
    gnd_id = data["GND_ID"]
    in_offset = float(data["in_offset"])
    int_gain = float(data["int_gain"])
    out_lower_limit = float(data["out_lower_limit"])
    out_upper_limit = float(data["out_upper_limit"])
    limit_range = float(data["limit_range"])
    out_ic = data["x0"]

    xdot_nodes = []
    x_nodes = []

    for i in range(n):
        eint_id = _generate_id(data, "EINT_ID")
        xdot_id = _generate_id(data, "NODE_ID")
        np_id = _generate_id(data, "NODE_ID")
        x_id = _generate_id(data, "NODE_ID")

        line = f"AINT{eint_id}\t{xdot_id} {x_id} EINT{eint_id}"
        lines += [ line ]

        line = f".MODEL EINT{eint_id} INT("
        line += f"in_offset={in_offset} "
        line += f"gain={int_gain} "
        line += f"out_lower_limit={out_lower_limit} "
        line += f"out_upper_limit={out_upper_limit} "
        line += f"limit_range={limit_range} "
        line += f"out_ic={float(out_ic[i])}"
        line += ")"

        lines += [ line ]

        xdot_nodes += [ xdot_id ]
        x_nodes += [ x_id ]

    data["x_nodes"] = x_nodes
    data["xdot_nodes"] = xdot_nodes

    if 'f' in data:
        nonlin_nodes = []

        lines += [ '' ]

        for i in range(n):
            fi = data['f'][i]

            if fi:
                nonlin_E_id = _generate_id(data, "NONLIN_E_ID")
                nonlin_V_node_id = _generate_id(data, "NODE_ID")

                for j in range(n):
                    fi = fi.replace(f"x{j+1}", f"v({x_nodes[j]})")

                for j in range(m):
                    fi = fi.replace(f"u{j+1}", f"v({u_nodes[j]})")

                lines += [ f"EF{nonlin_E_id}\t{nonlin_V_node_id} {gnd_id}\tvol='{fi}'" ]

                nonlin_nodes.append(nonlin_V_node_id)
            else:
                nonlin_nodes.append(None)

        data["nonlin_nodes"] = nonlin_nodes

    if 'g' in data:
        nonlin_out_nodes = []

        for i in range(r):
            gi = data['g'][i]

            if gi:
                nonlin_E_out_id = _generate_id(data, "NONLIN_E_OUT_ID")
                nonlin_V_node_id = _generate_id(data, "NODE_ID")

                for j in range(n):
                    gi = gi.replace(f"x{j+1}", f"v({x_nodes[j]})")

                for j in range(m):
                    gi = gi.replace(f"u{j+1}", f"v({u_nodes[j]})")

                lines += [ f"EG{nonlin_E_out_id}\t{nonlin_V_node_id} {gnd_id}\tvol='{gi}'" ]

                nonlin_out_nodes.append(nonlin_V_node_id)
            else:
                nonlin_out_nodes.append(None)

        data["nonlin_out_nodes"] = nonlin_out_nodes

    return 0


def _generate_e_out(data, lines):
    n = data['n']
    m = data['m']
    r = data['r']

    C = data['C']
    D = data['D']

    eps = data["eps"]
    gnd_id = data["GND_ID"]

    x_nodes = data["x_nodes"]
    u_nodes = data["u_nodes"]
    y_nodes = data["y_nodes"]

    for i in range(r):
        eout_id = _generate_id(data, "EOUT_ID")
        line_parts = [ f"EOUT{eout_id}\t{y_nodes[i]} {gnd_id}" ]
        line_parts += [ "", "", "0.0 " ]

        k = 0

        for j in range(n):
            Cij = C[i][j]

            if abs(Cij) < eps:
                continue

            line_parts[2] += f"{x_nodes[j]} {gnd_id} "
            line_parts[3] += f"{Cij} "

            k += 1

        for j in range(m):
            Dij = D[i][j]

            if abs(Dij) < eps:
                continue

            line_parts[2] += f"{u_nodes[j]} {gnd_id} "
            line_parts[3] += f"{Dij} "

            k += 1

        nonlin_out_node = None
        if "nonlin_out_nodes" in data:
            nonlin_out_node = data["nonlin_out_nodes"][i]

        if nonlin_out_node is not None:
            line_parts[2] += f"{nonlin_out_node} {gnd_id}"
            line_parts[3] += "1.0"

            k += 1

        if k > 0:
            line_parts[1] = f"POLY({k})"

            line = '\t'.join(line_parts)

            lines += [ line ]

    return 0


def _generate_e_state(data, lines):
    n = data['n']
    m = data['m']

    A = data['A']
    B = data['B']

    eps = data["eps"]
    gnd_id = data["GND_ID"]

    x_nodes = data["x_nodes"]
    xdot_nodes = data["xdot_nodes"]
    u_nodes = data["u_nodes"]

    for i in range(n):
        estate_id = _generate_id(data, "ESTATE_ID")
        line_parts = [ f"ESTATE{estate_id}\t{xdot_nodes[i]} {gnd_id}" ]
        line_parts += [ "", "", "0.0 " ]

        k = 0

        for j in range(n):
            Aij = A[i][j]

            if abs(Aij) < eps:
                continue

            line_parts[2] += f"{x_nodes[j]} {gnd_id} "
            line_parts[3] += f"{Aij} "

            k += 1

        for j in range(m):
            Bij = B[i][j]

            if abs(Bij) < eps:
                continue

            line_parts[2] += f"{u_nodes[j]} {gnd_id} "
            line_parts[3] += f"{Bij} "

            k += 1

        nonlin_node = None
        if "nonlin_nodes" in data:
            nonlin_node = data["nonlin_nodes"][i]

        if nonlin_node is not None:
            line_parts[2] += f"{nonlin_node} {gnd_id}"
            line_parts[3] += "1.0"

            k += 1


        if k > 0:
            line_parts[1] = f"POLY({k})"

            line = '\t'.join(line_parts)

            lines += [ line ]


    return 0


def _generate_lib_footer(data, lines):
    name = data["name"]

    lines += [ ".ENDS" ]
    lines += [ "* END SPICE MODEL " + name ]

    return 0


def _print_output(data, lines):
    out_str = '\r\n'.join(lines)

    if data['to_file']:
        filename = data["output_filename"] + ".lib"

        output = open(filename, "w")

        output.write('\r\n'.join(lines))

    data['lib'] = out_str

    return 0


def _generate_lib(data):
    lines = []

    result = _generate_lib_header(data, lines)

    if result < 0:
        return result

    assert("u_nodes" in data)
    assert("y_nodes" in data)

    lines += [ '' ]

    result = _generate_integrators(data, lines)

    if result < 0:
        return result

    assert("x_nodes" in data)
    assert("xdot_nodes" in data)

    lines += [ '' ]

    result = _generate_e_out(data, lines)

    if result < 0:
        return result

    lines += [ '' ]

    result = _generate_e_state(data, lines)

    if result < 0:
        return result

    lines += [ '' ]

    result = _generate_lib_footer(data, lines)

    if result < 0:
        return result

    result = _print_output(data, lines)

    return result


def _print_sym_output(data, lines):
    out_str = '\r\n'.join(lines)

    if data["to_file"]:
        filename = data["output_filename"] + ".kicad_sym"

        output = open(filename, "w")

        output.write('\r\n'.join(lines))

    data["sym"] = out_str

    return 0


def _generate_sym(data):
    name = data["name"]
    m = data['m']
    r = data['r']

    l = max(m, r)

    if l <= 0:
        raise RuntimeError(f"Could not create kicad symbol (m={m}, r={r})")

    dl = 1.27
    y_margin = 3 * dl
    y_pin = dl * 2
    pin_len = 2 * dl
    font_size = 1.27

    y_len = (l - 1) * y_pin

    u_y_pin = 0.0 if m == 1 else y_len / (m - 1)
    y_y_pin = 0.0 if r == 1 else y_len / (r - 1)

    y_len += 2 * y_margin

    x_len = 4 * y_margin

    ref_dist = dl

    x_start = -x_len / 2
    y_start = y_len / 2
    x_end = -x_start
    y_end = -y_start

    lines = []

    lines += [ f"(kicad_symbol_lib (version 20220914) (generator kicadODE)" ]
    lines += [ f"  (symbol \"{name}\" (in_bom no) (on_board no)" ]
    lines += [ f"    (property \"Reference\" \"LTI\" (at 0 {y_start+ref_dist:.4f} 0)" ]
    lines += [ f"      (effects (font (size {font_size} {font_size})))" ]
    lines += [ f"    )" ]
    lines += [ f"    (symbol \"{name}_0_1\"" ]
    lines += [ f"      (rectangle (start {x_start:.4f} {y_start:.4f}) (end {x_end:.4f} {y_end:.4f})" ]
    lines += [ f"        (stroke (width 0) (type default))" ]
    lines += [ f"        (fill (type none))" ]
    lines += [ f"      )" ]
    lines += [ f"    )" ]

    lines += [ f"    (symbol \"{name}_1_1\"" ]

    lines += [ f"      (pin power_in line (at 0 {y_end-pin_len:.4f} 90) (length {pin_len:.4f})" ]
    lines += [ f"        (name \"GND\" (effects (font (size {font_size} {font_size}))))" ]
    lines += [ f"        (number \"1\" (effects (font (size {font_size} {font_size}))))" ]
    lines += [ f"      )" ]

    pin_index = 1

    for i in range(m):
        yi = y_start - i * u_y_pin - y_margin
        lines += [ f"      (pin input line (at {x_start-pin_len:.4f} {yi:.4f} 0) (length {pin_len:.4f})" ]
        lines += [ f"        (name \"u{i+1}\" (effects (font (size {font_size} {font_size}))))" ]
        lines += [ f"        (number \"{pin_index+i+1}\" (effects (font (size {font_size} {font_size}))))" ]
        lines += [ f"      )" ]

    pin_index += m

    for i in range(r):
        yi = y_start - i * y_y_pin - y_margin
        lines += [ f"      (pin output line (at {x_end+pin_len:.4f} {yi:.4f} 180) (length {pin_len:.4f})" ]
        lines += [ f"        (name \"y{i+1}\" (effects (font (size {font_size} {font_size}))))" ]
        lines += [ f"        (number \"{pin_index+i+1}\" (effects (font (size {font_size} {font_size}))))" ]
        lines += [ f"      )" ]

    lines += [ f"    )" ]

    lines += [ f"  )" ]
    lines += [ f")" ]

    _print_sym_output(data, lines)

    return 0


def generate(data):
    A = None
    B = None
    C = None

    if 'A' in data:
        A = data['A']

    n = -1
    try:
        n1 = len(A)
        n2 = len(A[0])

        if n1 == n2:
            n = n1
    except:
        raise RuntimeError("'A' must be a sqaure matrix.")

    if n == -1:
        raise RuntimeError("'A' must be square matrix.")
    elif n == 0:
        raise RuntimeError("'A' can not be empty.")

    if 'B' in data:
        B = data['B']
    else:
        B = _h.zeros(n, n)
        data['B'] = B

    m = -1
    try:
        n1 = len(B)
        m1 = len(B[0])

        if n1 == n:
            m = m1
    except:
        raise RuntimeError("'B' must be a matrix with the same number of rows as 'A'")

    if m == -1:
        raise RuntimeError("'B' must be a matrix with the same number of rows as 'A'")
    elif m == 0:
        raise RuntimeError("'B' can not be empty.")

    if 'C' in data:
        C = data['C']
    else:
        C = _h.eye(n)
        data['C'] = C

    r = -1
    try:
        r1 = len(C)
        n1 = len(C[0])

        if n1 == n:
            r = r1
    except:
        raise RuntimeError("'C' must be a matrix with the same number of cols as 'A'")

    if r == -1:
        raise RuntimeError("'C' must be a matrix with the same number of cols as 'A'")
    elif r == 0:
        raise RuntimeError("'C' can not be empty.")

    if 'D' in data:
        D = data['D']
    else:
        D = _h.zeros(r, m)
        data['D'] = D

    r1 = -1
    m1 = -1
    try:
        r1 = len(D)
        m1 = len(D[0])
    except:
        raise RuntimeError(f"'D' must be a matrix with dimensions '{r}x{m}'")

    if r != r1:
        raise RuntimeError("'D' must be a matrix with the same number of rows as 'C'")
    if m != m1:
        raise RuntimeError("'D' must be a matrix with the same number of cols as 'B'")

    if "x0" not in data:
        data["x0"] = [ 0 ] * n
    elif not data["x0"]:
        data["x0"] = [ 0 ] * n
    else:
        nx = -1
        try:
            nx = len(data["x0"])
        except:
            raise RuntimeError("Initial condition vector must have 'n' entries.")
        finally:
            if nx != n:
                raise RuntimeError("Initial condition vector must have 'n' entries.")

    if 'f' in data:
        if len(data['f']) != n:
            raise RuntimeError("Nonlinear part must have 'n' rows.")

    if 'g' in data:
        if len(data['g']) != r:
            raise RuntimeError("Nonlinear part for output must have 'r' rows.")

    if "name" not in data:
        data["name"] = "ltilib"

    if "output_filename" not in data:
        data["output_filename"] = data["name"]
    elif "to_file" not in data:
        data["to_file"] = True

    if "to_file" not in data:
        data["to_file"] = False

    if "out_lower_limit" not in data:
        data["out_lower_limit"] = -1e12

    if "out_upper_limit" not in data:
        data["out_upper_limit"] = 1e12

    if "limit_range" not in data:
        data["limit_range"] = 1e-9

    if "in_offset" not in data:
        data["in_offset"] = 0.0

    if "int_gain" not in data:
        data["int_gain"] = 1.0

    if "generate_sym" not in data:
        data["generate_sym"] = True

    data['n'] = n
    data['m'] = m
    data['r'] = r

    data["NODE_ID"] = 1
    data["EOUT_ID"] = 1
    data["ESTATE_ID"] = 1
    data["EINT_ID"] = 1
    data["GND_ID"] = _generate_id(data, "NODE_ID")
    data["NONLIN_E_ID"] = 1
    data["NONLIN_E_OUT_ID"] = 1
    data["eps"] = 1e-9

    result = _generate_lib(data)

    if result < 0:
        return result

    if data["generate_sym"]:
        result = _generate_sym(data)

    return result
