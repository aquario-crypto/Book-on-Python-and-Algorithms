#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def fibonacci(n):

    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
