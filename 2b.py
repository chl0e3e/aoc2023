from dataclasses import dataclass

class ImpossibleGameException(Exception):
    pass

@dataclass(frozen=True)
class Cube:
    colour: str

class Constraint:
    def apply(self, cube, n):
        raise Exception("Constraint not implemented")

class CubeConstraint(Constraint):
    def __init__(self, cube):
        self.cube = cube

class TotalCubeConstraint(CubeConstraint):
    def __init__(self, cube, max):
        super().__init__(cube)
        self.max = max
        self.value = 0
        self.cube = cube

    def apply(self, cube, n):
        if cube == self.cube:
            self.value += n
            if self.value > self.max:
                raise ImpossibleGameException()
    
    def reset(self):
        self.value = 0

class Game:
    def __init__(self):
        self.constraints = []
        self.uniquity = {}

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
    
    def next_set(self):
        for constraint in self.constraints:
            constraint.reset()
    
    def take_n(self, cube, n):
        # for constraint in self.constraints:
        #     constraint.apply(cube, n)

        if not cube in self.uniquity.keys():
            self.uniquity[cube] = n
        elif self.uniquity[cube] < n:
            self.uniquity[cube] = n

possible_game_index_total = 0
game_power_total = 0

with open("2.input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        if not ":" in line:
            raise Exception("Invalid input")
        
        game = Game()
        # game.add_constraint(TotalCubeConstraint(Cube(colour="red"), 12))
        # game.add_constraint(TotalCubeConstraint(Cube(colour="green"), 13))
        # game.add_constraint(TotalCubeConstraint(Cube(colour="blue"), 14))

        game_number, game_data = line.split(":", 1)
        try:
            for game_set in game_data.split(";"):
                game_set = game_set.strip()
                for game_cubes_in_set in game_set.split(","):
                    game_cubes_in_set = game_cubes_in_set.strip()
                    cube_amount, cube_colour = game_cubes_in_set.split(" ")
                    game.take_n(Cube(cube_colour), int(cube_amount))

                # game.next_set()
                        
            # print("%s: possible" % game_number)
            # print(game.uniquity)
            power = 1
            for key, value in game.uniquity.items():
                power = power * value
            print("%s power: %d " % (game_number, power))
            game_power_total += power
            # possible_game_index_total += int(game_number.replace("Game ", ""))
        except ImpossibleGameException as impossible_e:
            print("%s: impossible" % game_number)

# print(possible_game_index_total)
print(game_power_total)