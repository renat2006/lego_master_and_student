import logic.constants


class Camera:

    def __init__(self):
        self.dx = 0

    def apply(self, obj):
        obj.rect.x += self.dx // 2

        return obj.rect.x

    def update(self, target):
        self.dx = (-target.rect.centerx + logic.constants.WIDTH // 2)
