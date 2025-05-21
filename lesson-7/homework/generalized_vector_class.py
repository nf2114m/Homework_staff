import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] + other.components[i])
        
        return Vector(*result)

    def __sub__(self, other):
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] - other.components[i])
        
        return Vector(*result)

    def __mul__(self, other):
            result = 0
            for i in range(len(self.components)):
                result += self.components[i] * other.components[i]
            return result

    def __rmul__(self, other):
            result = []
            for i in range(len(self.components)):
                result.append(self.components[i] * other)
            return Vector(*result)

    def magnitude(self):
        result = 0
        for component in self.components:
            result += component ** 2
        return math.sqrt(result)

    def normalize(self):
        mag = self.magnitude()
        result = []
        for component in self.components:
            result.append(component / mag)
        
        return Vector(*result)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)         

v3 = v1 + v2
print(v3)       

v4 = v2 - v1
print(v4)         

dot_product = v1 * v2
print(dot_product)

v5 = 3 * v1
print(v5)        

print(v1.magnitude())

v_unit = v1.normalize()
print(v_unit)
