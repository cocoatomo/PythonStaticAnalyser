#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""cfg.py

Control Flow Graph module

Copyright (C) cocoatomo
"""

import psa

class CFGNode(object):
    def __init__(self, prev=[], inst=None, next=None):
        self.prev = prev
        self.inst = inst
        self.next = next

    def __str__(self):
        return 'prev: {0}, inst: {1}, next: {2}' \
            .format(self.prev, self.inst, self.next)


class CFGNode(psa.BaseVisitor):
    def visit_Module(self, node, data=None):
        return generic_visit(node, data)

    def visit_Assign(self, node, data=None):
        pass
