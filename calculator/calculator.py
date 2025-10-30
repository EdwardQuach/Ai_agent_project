import ast
import operator as op

# Define the supported operators
operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.USub: op.neg
}

class Calculator:
    def evaluate(self, expression):
        try:
            return self._evaluate(ast.parse(expression, mode='eval').body)
        except Exception as e:
            print(e)
            return None

    def _evaluate(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            try:
                return operators[type(node.op)](self._evaluate(node.left), self._evaluate(node.right))
            except: return None
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](self._evaluate(node.operand))
        else:
            return None