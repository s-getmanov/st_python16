class Turtle(object):
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Количество клеточек s не может стать меньше или равно 0")

    def count_moves(self, x2, y2):
        d_x = abs(x2 - self.x)
        d_y = abs(y2 - self.y)

        min_moves = d_x // self.s + d_y // self.s

        #Случай, когда нельза достичь указанной позиции за целое число шагов (дельта не кратна размеру шага)
        if d_x % self.s != 0:
            min_moves += 1
        if d_y % self.s != 0:
            min_moves += 1

        return min_moves