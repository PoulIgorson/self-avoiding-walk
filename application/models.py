from random import choice, shuffle
from copy import deepcopy

import pygame

from constants import *


def minmax(*args):
    return min(args), max(args)


class PGPoint:
    color = WHITE
    SCALE = 0.7
    def __init__(self, j=0, i=0, size=2, dirs=[], visited=False):
        self.x = j*size + size//2
        self.y = i*size + size//2
        self.size = size
        self.r = self.SCALE * size//2
        self.visited = visited
        self.dirs = deepcopy(dirs)
        
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def i(self):
        return self.y//self.size
    
    @property
    def j(self):
        return self.x//self.size
    
    @property
    def pos_iter(self):
        return self.j, self.i
    
    def process_draw(self, screen, fill=False, color=None):
        if fill or self.visited:
            w = 0
        else:
            w = 3
        color = color if color is not None else self.color
        x, y = self.pos
        y += self.size
        pygame.draw.circle(
            screen, color,
            (x, y), self.r, w
        )

    def copy(self):
        return PGPoint(self.i, self.j, self.size, self.dirs, self.visited)

    def set(self, other):
        self.x = other.x
        self.y = other.y
        self.size = other.size
        self.r = other.r
        self.visited = other.visited

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j and\
                self.size == other.size and self.r == other.r

    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return f'pos: {self.j, self.i}, visited: {self.visited}'
    
    def __repr__(self):
        return str(self)


class PGModel:
    COL, ROW = 10, 10
    SIZE = 30
    
    dirs = [
        [0, -1],
        [-1, 0],
        [0, 1],
        [1, 0]
    ]
    
    def __init__(self):
        self.grid = PGModel.create_grid()
        self.head = PGPoint(0, 0, self.SIZE, self.dirs)
        self.head.color = modBLUE
        self.path = [self.grid[0][0].copy()]
        self.lasts = [[]]
    
    @staticmethod
    def create_grid():
        grid = []
        for i in range(PGModel.COL):
            if i == len(grid):
                grid.append([])
            for j in range(PGModel.ROW):
                grid[i].append(PGPoint(i, j, PGModel.SIZE, PGModel.dirs))
        grid[0][0].visited = True
        return grid
    
    def process_logic(self):
        valid_dirs = []
        while (not valid_dirs) and (not self.finish):
            j, i = self.head.pos_iter
            for dir in self.dirs:
                dx, dy = dir
                if not (0 <= j + dx < self.ROW and\
                        0 <= i + dy < self.COL):
                    continue
                next_cell = self.grid[j + dx][i + dy]
                if (not next_cell.visited) and (-1 == index(self.lasts, self.path + [self.head])):
                    valid_dirs.append(dir)
            
            if not valid_dirs:
                if self.finish:
                    break
                self.lasts.append([])
                last = self.path.pop()
                self.grid[last.j][last.i].visited = False
                self.head.x = last.x
                self.head.y = last.y
                
        if valid_dirs:
            dx, dy = choice(valid_dirs)
            j, i = self.head.pos_iter
            self.head.move(dx*self.SIZE, dy*self.SIZE)
            last = self.grid[j][i]
            last.visited = True
            self.path.append(last)
            self.lasts[-1] = self.path[::1]
    
    def process_draw(self, screen):
        for row in self.grid:
            for point in row:
                point.process_draw(screen)
        for i in range(1, len(self.path)):
            beg = [*self.path[i-1].pos]
            end = [*self.path[i].pos]
            beg[0], end[0] = minmax(beg[0], end[0])
            beg[1], end[1] = minmax(beg[1], end[1])
            w = end[0] - beg[0]
            h = end[1] - beg[1]
            beg[1] += self.path[i].size
            if not w:
                w = 2
                h -= 2*self.path[i].r
                beg[1] += self.path[i].r
            elif not h:
                h = 2
                w -= 2*self.path[i].r
                beg[0] += self.path[i].r
            pygame.draw.rect(
                screen, WHITE,
                (*beg, w, h)
            )
            self.path[i].process_draw(screen, True, color=modGREEN)
        self.path[0].process_draw(screen, True, color=modGREEN)
        self.head.process_draw(screen, True)
        
    def reset(self):
        self.__init__()
    
    @property
    def finish(self):
        return len(self.path) == (self.ROW * self.COL)


def index(where, obj):
    return_res = -1
    for i, item in enumerate(where):
        if len(item) != len(obj):
            continue
        f = 0
        for j, cell in enumerate(obj):
            if cell.pos_iter == item[j].pos_iter:
                f += 1
        if f == len(obj):
            return_res = i
            break
    return return_res
