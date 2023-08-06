#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (c) 2023 Okan Demir
#
# SPDX-License-Identifier: GPL-3.0-or-later


def zeros(n, m):
    mtx = [ [ 0.0 ] * m for i in range(n) ]

    return mtx


def eye(n):
    mtx = zeros(n, n)

    for i in range(n):
        mtx[i][i] = 1.0

    return mtx
