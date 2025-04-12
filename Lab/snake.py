class Snake:
    def __init__(self, pos):
        self.body = [pos]
        self.direction = (20, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0],
                self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 400:
            return True
        if head in self.body[1:]:
            return True
        return False
