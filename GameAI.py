﻿#!/usr/bin/env python

"""GameAI.py: INF1771 GameAI File - Where Decisions are made."""
#############################################################
# Copyright 2020 Augusto Baffa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#############################################################
from pdb import Restart
from Map.Position import Position
import random
__author__ = "Augusto Baffa"
__copyright__ = "Copyright 2020, Rio de janeiro, Brazil"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "abaffa@inf.puc-rio.br"
#############################################################

# import gym
# from gym import spaces
from enum import Enum


class Action(Enum):
    virar_direita = 0
    virar_esquerda = 1
    andar = 2
    atacar = 3
    pegar_ouro = 4
    pegar_anel = 5
    pegar_powerup = 6
    andar_re = 7
    esperar = 8

# <summary>
# Game AI Example
# </summary>


class GameAI():

    player = Position()
    state = "ready"
    dir = "north"
    score = 0
    energy = 0

    n_actions = 8

    # Rewards

    def __init__(self):
        # self.action_space = spaces.Discrete(self.n_actions)

        self.RestartPlayer()

    def RestartPlayer(self):
        self.blueLight = False
        self.redLight = False
        self.weakLight = False
        self.blocked = False
        self.dinheiro = False

        self.started = False

    # <summary>
    # Refresh player status
    # </summary>
    # <param name="x">player position x</param>
    # <param name="y">player position y</param>
    # <param name="dir">player direction</param>
    # <param name="state">player state</param>
    # <param name="score">player score</param>
    # <param name="energy">player energy</param>

    def SetStatus(self, x, y, dir, state, score, energy):

        print('\n STATUS ->', x, y, dir, state, score, energy)
        self.player.x = x
        self.player.y = y
        self.dir = dir.lower()

        self.state = state
        self.score = score
        self.energy = energy

        # if self.started and


    # <summary>
    # Get list of observable adjacent positions
    # </summary>
    # <returns>List of observable adjacent positions</returns>

    def GetObservableAdjacentPositions(self):
        ret = []

        ret.append(Position(self.player.x - 1, self.player.y))
        ret.append(Position(self.player.x + 1, self.player.y))
        ret.append(Position(self.player.x, self.player.y - 1))
        ret.append(Position(self.player.x, self.player.y + 1))

        return ret

    # <summary>
    # Get list of all adjacent positions (including diagonal)
    # </summary>
    # <returns>List of all adjacent positions (including diagonal)</returns>

    def GetAllAdjacentPositions(self):

        ret = []

        ret.Add(Position(self.player.x - 1, self.player.y - 1))
        ret.Add(Position(self.player.x, self.player.y - 1))
        ret.Add(Position(self.player.x + 1, self.player.y - 1))

        ret.Add(Position(self.player.x - 1, self.player.y))
        ret.Add(Position(self.player.x + 1, self.player.y))

        ret.Add(Position(self.player.x - 1, self.player.y + 1))
        ret.Add(Position(self.player.x, self.player.y + 1))
        ret.Add(Position(self.player.x + 1, self.player.y + 1))

        return ret

    # <summary>
    # Get next forward position
    # </summary>
    # <returns>next forward position</returns>

    def NextPosition(self):

        ret = None

        if self.dir == "north":
            ret = Position(self.player.x, self.player.y - 1)

        elif self.dir == "east":
            ret = Position(self.player.x + 1, self.player.y)

        elif self.dir == "south":
            ret = Position(self.player.x, self.player.y + 1)

        elif self.dir == "west":
            ret = Position(self.player.x - 1, self.player.y)

        return ret

    # <summary>
    # Player position
    # </summary>
    # <returns>player position</returns>

    def GetPlayerPosition(self):
        return self.player

    # <summary>
    # Set player position
    # </summary>
    # <param name="x">x position</param>
    # <param name="y">y position</param>

    def SetPlayerPosition(self, x, y):
        self.player.x = x
        self.player.y = y

    # <summary>
    # Observations received
    # </summary>
    # <param name="o">list of observations</param>

    def GetObservations(self, o):
        #cmd = "";
        print('observations ->', o)
        for s in o:

            if s == "blocked":
                self.blocked = True
                pass

            elif s == "steps":
                pass

            elif s == "breeze":
                pass

            elif s == "flash":
                pass

            elif s == "blueLight":
                self.blueLight = True
                pass

            elif s == "redLight":
                self.redLight = True
                pass

            elif s == "greenLight":
                pass

            elif s == "weakLight":
                self.weakLight = True
                pass

            elif s == "hit":
                pass

            elif s == "damage":
                pass

    # <summary>
    # No observations received
    # </summary>

    def GetObservationsClean(self):
        self.redLight = False
        self.blueLight = False
        self.weakLight = False
        self.blocked = False
        pass

    # <summary>
    # Get Decision
    # </summary>
    # <returns>command string to new decision</returns>

    def GetDecision(self):
        decision = ""
        if self.blueLight or self.weakLight:
            decision = Action.pegar_ouro
            self.dinheiro = True
        elif self.dinheiro:
            decision = Action.esperar
        elif self.redLight and self.energy < 100:
            decision = Action.pegar_powerup
        else:
            if self.blocked:
                self.blocked = False
                decision = Action.virar_esquerda
            else:
                decision = Action.andar

        # print('decision ->', decision)
        return decision
