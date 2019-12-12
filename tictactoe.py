#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:06:18 2019

@author: igdaniel
"""

### base tic tac toe code for Final Proj

#import os
import time
#import random
title = "_______   ____    ______      _______      ____         ______       _______     ______     ________ \n\
|\_____ \  |\__\  /\_____\    |\_____ \    /\___\       /\_____\     |\_____ \   /\_____\    |\______| \n\
\|__  __|  ||  | | /  ___\    \|__  __|   / / __ \     | /  ___\     \|__  __|  / /  __  \   ||   ___| \n\
  ||  |    ||  | | | |          ||  |    / / /__\ \    | | |           ||  |    | | |  | |   ||  |___ \n\
  ||  |    ||  | | | |          ||  |   / /  ____  \   | | |           ||  |    | | |__| |   ||   ___| \n\
  ||  |    ||  | \ | |____      ||  |  / /  /    |  \  \ | |____       ||  |    | |      |   ||  |___ \n\
  \|__|    \|__|   \_____/      \|__| /_/__/     /___\   \_____/       \|__|      \______/   \|______| \n"

class TicTacToe:
    def __init__(self):
        # when chat user selects "t" from the menu, they join this list
        # the list is indexed {"playerNum":"X/O"}
        self.users = []
        self.board = [" "," ", " ", " ", " ", " ", " ", " ", " "]
        self.markers = {}

    def join(self, client):
        self.users.append(client)
        return

    def set_marker(self):
        self.markers[self.users[0]] = "X"
        self.markers[self.users[1]] = "O"
        return

    def get_board(self):
        b = "   |   |   \n" \
            + " " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " \n" \
            + "   |   |   \n" \
            + "------------\n" \
            + "   |   |   \n" \
            + " " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " \n" \
            + "   |   |   \n" \
            + "------------\n" \
            + "   |   |   \n" \
            + " " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " \n" \
            + "   |   |   \n"
        return b

    def available(self, place):
        #check if free
        #send to place_maker if free
        # else ask for new place
        if self.board[place] != " ":
            return False
        else:
            self.place_marker(place)
            return True

    def place_marker(self, client, place):
        marker = self.markers[client]
        self.board[int(place) - 1] = marker
        return

    def result(self):
        winner_exists = False
        winner = ""
        for marker in self.markers.values():
            if (self.board[0] == marker and self.board[1] == marker and self.board[2] == marker) or \
                    (self.board[3] == marker and self.board[4] == marker and self.board[5] == marker) or \
                    (self.board[6] == marker and self.board[7] == marker and self.board[8] == marker) or \
                    (self.board[0] == marker and self.board[3] == marker and self.board[6] == marker) or \
                    (self.board[1] == marker and self.board[4] == marker and self.board[7] == marker) or \
                    (self.board[2] == marker and self.board[5] == marker and self.board[8] == marker) or \
                    (self.board[0] == marker and self.board[4] == marker and self.board[8] == marker) or \
                    (self.board[2] == marker and self.board[4] == marker and self.board[6] == marker):
                winner_exists = True
                winner = marker
        return winner_exists, winner

    def tie(self):
        if (self.board[0] != " " and self.board[1] != " " and self.board[2] != " " and \
                self.board[3] != " " and self.board[4] != " " and self.board[5] != " " and \
                self.board[6] != " " and self.board[7] != " " and self.board[8] != " "):
            return True
        return False

    def reset(self):
        self.users = []
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]