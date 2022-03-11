from random import choice

import pygame

from constants import *


def minmax(*args):
    return min(args), max(args)


class PGPoint:
    color = WHITE
    def __init__(self, i=0, j=0, size=2, visited=False):
        self.x = i*size + size//2
        self.y = j*size + size//2
        self.size = size
        self.r = size//2
        self.visited = visited
        
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
        pygame.draw.circle(
            screen, color,
            self.pos, 0.7*self.r, w
        )
    
    def copy(self):
        return PGPoint(self.i, self.j, self.size, self.visited)
    
    def set(self, other):
        self.x = other.x
        self.y = other.y
        self.size = other.size
        self.r = other.r
        self.visited = other.visited


class PGModel:
    COL, ROW = 10, 10
    SIZE = 30
    dirs = [
        (0, -1),
        (-1, 0),
        (0, 1),
        (1, 0)
    ]
    
    def __init__(self):
        self.grid = PGModel.create_grid()
        self.head = PGPoint(0, 0, self.SIZE)
        self.head.color = modBLUE
        self.path = [self.grid[0][1].copy()]
    
    @staticmethod
    def create_grid():
        grid = []
        for i in range(PGModel.COL):
            if i == len(grid):
                grid.append([])
            for j in range(PGModel.ROW):
                grid[i].append(PGPoint(i, j, PGModel.SIZE))
        grid[0][0].visited = True
        return grid
    
    def process_logic(self):
        valid_dirs = []
        while not valid_dirs:
            pos = self.head.pos_iter
            for dir in self.dirs:
                dx, dy = dir
                if 0 <= pos[0] + dx < self.ROW and\
                        0 <= pos[1] + dy < self.COL:
                    if not self.grid[pos[0] + dx][pos[1] + dy].visited:
                        valid_dirs.append(dir)
            
            if not valid_dirs:
                last = self.path.pop()
                print(last.pos_iter, last.visited)
                self.grid[last.j][last.i].visited = False
                print(self.grid[last.j][last.i].pos_iter, last.visited, 1)
                self.head.set(self.path[-1])
        
        if valid_dirs:
            dx, dy = choice(valid_dirs)
            pos = self.head.pos_iter
            self.head.move(dx*self.SIZE, dy*self.SIZE)
            try:
                self.grid[pos[0]][pos[1]].visited = True
            except:
                input()
            self.path.append(self.grid[pos[1]][pos[0]].copy())
    
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
            w += 2*(w == 0)
            h += 2*(h == 0)
            pygame.draw.rect(
                screen, WHITE,
                (*beg, w, h)
            )
            self.path[i].process_draw(screen, True, color=modGREEN)
        self.path[0].process_draw(screen, True, color=modGREEN)
        self.head.process_draw(screen, True)
        
        
