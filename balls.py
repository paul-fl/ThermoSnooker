class Ball:
    def __init__(self, pos=None, vel=None, radius=None, mass=None):
        if pos is None:
            self.__pos = [0, 0]
        else:
            self.__pos = pos

        if vel is None:
            self.__vel = [1.0, 0.0]
        else:
            self.__vel = vel

        if radius is None:
            self.__radius = 1
        else:
            self.__radius = radius

        if mass is None:
            self.__mass = 1.0
        else:
            self.__mass = mass

    def pos(self):
        return self.__pos

    def radius(self):
        return self.__radius

    def mass(self):
        return self.__mass

    def vel(self):
        return self.__vel

    def set_vel(self, vel):
        if (isinstance(vel, list) and len(vel) == 2 and 
            all(isinstance(v, (int, float)) for v in vel)):
            self.__vel = vel
        else:
            raise ValueError("Velocity must be a list of two numeric values (e.g., [1.0, 0.0]).")
        return self.__vel

    def move(self, dt):
        if isinstance(dt, int) and len(dt) == 1:
            self.__pos += self.__vel * dt
        else:
            raise ValueError("dt must be an int (e.g, 1).")
        return self.__pos
