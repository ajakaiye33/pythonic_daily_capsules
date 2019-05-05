
class Calculator(object):
    def __init__(self):
        self.cached = {}

    def _find_cached_compution(self, operation, params):
        if operation not in self.cached:
            return None
        for prev_computation in self.cached[operation]:
            if prev_computation[:2] == params:
                return prev_computation[2]

    def _append_to_cached(self, operation, cached_values):
        self.cached.setdefault(operation, [])
        self.cached[operation].append(cached_values)

    def add(self, num1, num2):
        cachey = self._find_cached_compution("add",  (num1, num2))
        if not cachey:
            chachey = num1 + num2
            self._append_to_cached("add", (num1, num2))
        return cachey

    def substract(self, num1, num2):
        cachey = self._find_cached_compution("subtract", (num1, num2))
        if not cachey:
            chachey = num1 - num2
            self._append_to_cached("subtract", (num1, num2, cachey))
        return cachey


c1 = Calculator()
print(c1.cached)
print(c1.add(2, 3))
print(c1.cached)
print(c1.substract(8, 2))
print(c1.cached)
print(c1.add(9, 3))
print(c1.cached)
