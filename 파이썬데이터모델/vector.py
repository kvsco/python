
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):
        from math import hypot
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scaler):
        x = self.x * scaler
        y = self.y * scaler
        return Vector(x, y)

if __name__ == "__main__":
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print(f"v1 + v2 : {v1 + v2}")