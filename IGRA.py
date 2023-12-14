import math
from abc import ABC, abstractmethod


class Location:
    def __init__(self, name: str, width: int, height: int, length: int):
        self.name = name
        self._width = width
        self._height = height
        self._length = length
        self._objs = []

    def addObject(self, obj):
        if obj not in self._objs:
            self._objs.append(obj)

    def clear(self):
        self._objs = None

    def isInside(self, x, y, z) -> bool:
        return ((x > 0 and x < self._length)
                and (y > 0 and y < self._width)
                and (z > 0 and z < self._height))

    @property
    def width(self):
        return self._width

    @property
    def length(self) -> int:
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def volume(self):
        return self.height * self.length * self.width


class GameObject:
    def __init__(self, name: str, loc: Location, x, y, z):
        self.name = name
        self._loc = loc
        self._loc.addObject(self)
        self.x, self.y, self.z = x, y, z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def distance(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))


class LivingObject(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        super().__init__(name, loc, x, y, z)
        self._max_hp = hp
        self._hp = hp
        self.inventory = []
        self.weapon = None

    @property
    def maxHP(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    def changeHP(self, change):
        if not self.alive:
            return
        self._hp += change
        if self._hp <= 0:
            self._hp = 0
            for item in self.inventory:
                self.drop_to_inventory(item)
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def alive(self):
        return self._hp > 0

    def eat(self, obj):
        if self.distance(obj) > 1:
            return
        self.changeHP(obj.eatMe())

    def add_to_inventory(self, item: GameObject):
        if self.distance(item) <= 1:
            self.inventory.append(item)
            item.x = self.x
            item.y = self.y
            item.z = self.z
        else:
            print(f'{item.name} is too far')

    def drop_to_inventory(self, item: GameObject):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f'{self.name} does not have {item.name}')

    def use_item(self, item: GameObject):
        if item not in self.inventory:
            print(f'{self.name} does not have {item.name}')
        if isinstance(item, Eatable):
            self.eat(item)
        if isinstance(item, Burnable):
            item.burnMe()
        if isinstance(item, Weapon):
            self.weapon = item
            print(f'{item.name} equipped')

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
        for item in self.inventory:
            item.x += x
            item.y += y
            item.z += z


class Weapon(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        return self._damage

    @property
    def radius(self):
        return self._radius

    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage)


class MeleeWeapon(Weapon):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z, damage, radius)


class RangedWeapon(Weapon):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z, damage, radius)

    def shoot(self, x_target, y_target, z_target):
        min_distance = self.radius
        on_the_shot = []
        targets = [obj for obj in self._loc._objs if isinstance(obj, LivingObject) and self not in obj.inventory]
        for obj in targets:
            if obj.x == self.x and obj.y == self.y and obj.z == self.z:
                min_distance = 0
                on_the_shot.append(obj)
                continue
            if (self.x - x_target) / (self.x - obj.x) == (self.y - y_target) / (self.y - obj.y) == (
                    self.z - z_target) / (self.z - obj.z) and self.distance(obj) <= self.radius:
                min_distance = min(min_distance, self.distance(obj))
                on_the_shot.append(obj)
        for obj in on_the_shot:
            if self.distance(obj) <= min_distance:
                obj.changeHP(-self.damage)


class Eatable(ABC):
    def __init__(self, hp: int):
        self._hp = hp
        self._eaten = False

    @property
    def eaten(self):
        return self._eaten

    @abstractmethod
    def eatMe(self):
        if not self.eaten:
            self._eaten = True
            return self._hp
        else:
            return 0


class Food(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        return Eatable.eatMe(self)


class Poison(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        return -Eatable.eatMe(self)


class Burnable(ABC):
    def __init__(self):
        self._burned = False

    @property
    def burned(self):
        return self._burned

    @abstractmethod
    def burnMe(self):
        self._burned = True


class Cookable(GameObject, Eatable, Burnable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)
        Burnable.__init__(self)

    @classmethod
    def growMushroom(cls, loc, x, y, z):
        return cls('mushroom', loc, x, y, z, 20)

    def burnMe(self):
        Burnable.burnMe(self)

    def eatMe(self):
        hp = Eatable.eatMe(self)
        return hp if self.burned else -hp

#Test
Whiterun = Location('Whiterun', 100, 100, 100)
Ulfrik = LivingObject('Ulfrik', Whiterun, 10, 10, 10, 100)
Dovakin = LivingObject('Dovakin', Whiterun, 20, 20, 20, 100)
Luk_Aurielya = RangedWeapon('Luk_Aurielya', Whiterun, 15, 15, 15, 50, 3)
Britva_Merunesa = MeleeWeapon('Britva_Merunesa', Whiterun, 11, 11, 11, 50, 1)
Sweet_Roulette = Food('Sweet_Roulette', Whiterun, 12, 12, 12, 20)
Poisoned_Sweet_Roulette = Poison('Poisoned_Sweet_Roulette', Whiterun, 11, 11, 11, 2000)

Ulfrik.add_to_inventory(Britva_Merunesa)
Dovakin.move(-4, -4, -4)
Dovakin.add_to_inventory(Luk_Aurielya)
Dovakin.use_item(Luk_Aurielya)
Dovakin.weapon.shoot(10, 10, 10)
Ulfrik.move(4, 4, 4)
Dovakin.weapon.shoot(13, 13, 13)
Ulfrik.use_item(Britva_Merunesa)
Ulfrik.move(2, 2, 2)
Ulfrik.weapon.attack(Dovakin)
Dovakin.weapon.shoot(10, 10, 10)
Dovakin.move(-4, -4, -4)
Dovakin.eat(Sweet_Roulette)
Dovakin.eat(Poisoned_Sweet_Roulette)













