#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast


class BaseVisitor(object):
    """A base visitor class for an abstract syntax tree created by ast module.

    The default implementation of visit method calls a method named
    'visit_{0}'.format(node.__class__.__name__) with arguments,
    node and data. For example, when a node is instance of ast.If,
    the visit method invoked with arguments node and data
    will call a visit_If(node, data) method.
    When there is no visit_If method, the generic_visit method will be
    called.

    The generic_visit method is for visiting children nodes
    of the visited node. This method determine a class of the node to
    traverse nodes of an abstract syntax tree properly.
    When the node has a child node which is instance of list,
    this method will call the visit method for each elements in that list
    iteratively. Otherwise just call the visit method for
    the child node.

    [implementation sample]
    def visit_If(self, node, data=None):
        print('If')
        generic_visit(node)
    """
    def visit(self, node, data=None):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, data)

    def generic_visit(self, node, data=None):
        """Called if no explicit visitor function exists for a node."""
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item, data)
            elif isinstance(value, ast.AST):
                self.visit(value, data)


class PrintVisitor(ast.NodeVisitor):
    def simple_print(self, node):
        self.visit(node)

    def visit(self, node):
        print(node)
        self.generic_visit(node)


class PPrintVisitor(BaseVisitor):
    TAB = '    '
    def pprint(self, node):
        self.visit(node, '')

    def visit_Module(self, node, data=None):
        print(data + '[Module]')
        self.generic_visit(node, data + PPrintVisitor.TAB)

    def visit_Assign(self, node, data=None):
        print(data + '[Assign] targets: {0}, value: {1}' \
                  .format(node.targets, node.value))
        self.generic_visit(node, data + PPrintVisitor.TAB)

    def visit_Name(self, node, data=None):
        print(data + '[Name] id: {0}'.format(node.id))
        self.generic_visit(node, data + PPrintVisitor.TAB)

    def visit_Store(self, node, data=None):
        print(data + '[Store]')

    def visit_Num(self, node, data=None):
        print(data + '[Num] n: {0}'.format(node.n))


def _test():
    node = ast.parse('a = 1')

    pv = PrintVisitor()
    pv.simple_print(node)

    pp = PPrintVisitor()
    pp.pprint(node)

    bv = BaseVisitor()
    bv.visit(node)


def main():
    _test()


if __name__ == '__main__':
    import sys
    sys.exit(main())
