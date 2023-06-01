# Author: Aaron Suchitphanit
# Date: 05/31/2X21
# Description: KubaGame can be used to play a game of Kuba

import copy


class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """

    def __init__(self):
        self.head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self.head is None:  # If the list is empty
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self.head is None:  # If the list is empty
            return

        if self.head.data == val:  # If the node to remove is the head
            self.head = self.head.next
        else:
            current = self.head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []
        current = self.head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def insert(self, val, pos):
        """
        Inserts a node containing val into the linked list at position pos
        """
        if self.head is None:  # If the list is empty
            self.add(val)
            return

        if pos == 0:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        else:
            current = self.head
            for _ in range(pos - 1):
                if current.next is None:
                    current.next = Node(val)
                    return
                current = current.next
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def reverse(self):
        """"
        Reverses the linked list
        """
        previous = None
        current = self.head

        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.head = previous

    def delete(self, position):
        """Deletes a node at a given position"""
        if self.head is None:  # If linked list is empty
            return
        temp = self.head  # store head node
        if position == 0:  # If head needs to be removed
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):  # Find previous node of the node to be deleted
            temp = temp.next
            if temp is None:
                break
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self.head is None:  # If the list is empty
            return

        if self.head.data == val:  # If the node to remove is the head
            self.head = self.head.next
        else:
            current = self.head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next


class KubaGame:
    """Represents a Kuba Game """

    def __init__(self, player_1, player_2):
        """Creates a Kuba Game"""

        self._row_0 = LinkedList()  # ["W", "W", "X", "X", "X", "B", "B"]  # Board Representation
        self._row_0.add('W')  # change back to W
        self._row_0.add('W')  # change back to W
        self._row_0.add('X')  # change to X
        self._row_0.add('X')  # change to X
        self._row_0.add('X')  # change to X
        self._row_0.add('B')  # change to B
        self._row_0.add('B')  # change back to B
        self._row_1 = LinkedList()  # ["W", "W", "X", "R", "X", "B", "B"]
        self._row_1.add('W')
        self._row_1.add('W')
        self._row_1.add('X')
        self._row_1.add('R')
        self._row_1.add('X')
        self._row_1.add('B')
        self._row_1.add('B')  # change back to B
        self._row_2 = LinkedList()  # ["X", "X", "R", "R", "R", "X", "X"]
        self._row_2.add('X')  # Change back to X
        self._row_2.add('X')
        self._row_2.add('R')
        self._row_2.add('R')
        self._row_2.add('R')
        self._row_2.add('X')
        self._row_2.add('X')  # change back to X
        self._row_3 = LinkedList()  # ["X", "R", "R", "R", "R", "R", "X"]
        self._row_3.add('X')  # Change back to X
        self._row_3.add('R')
        self._row_3.add('R')
        self._row_3.add('R')
        self._row_3.add('R')
        self._row_3.add('R')
        self._row_3.add('X')  # change back to X
        self._row_4 = LinkedList()  # ["X", "X", "R", "R", "R", "X", "X"]
        self._row_4.add('X')  # Change back to X
        self._row_4.add('X')
        self._row_4.add('R')
        self._row_4.add('R')
        self._row_4.add('R')
        self._row_4.add('X')
        self._row_4.add('X')  # Change back to x
        self._row_5 = LinkedList()  # ["B", "B", "X", "R", "X", "W", "W"]
        self._row_5.add('B')
        self._row_5.add('B')
        self._row_5.add('X')
        self._row_5.add('R')
        self._row_5.add('X')
        self._row_5.add('W')
        self._row_5.add('W')  # Change to W
        self._row_6 = LinkedList()  # ["B", "B", "X", "X", "X", "W", "W"]
        self._row_6.add('B')
        self._row_6.add('B')
        self._row_6.add('X')
        self._row_6.add('X')
        self._row_6.add('X')
        self._row_6.add('W')
        self._row_6.add('W')  # Change to W

        self._board = [self._row_0, self._row_1, self._row_2, self._row_3, self._row_4, self._row_5, self._row_6]

        self._player_1 = player_1  # This value will have two elements, the first will be player name then color
        self._player_2 = player_2

        self._turn_tracker = ""  # turn tracker

        self._player_1_cap = 0  # Number of red marbles player 1 has captured

        self._player_2_cap = 0  # Number of red marbles player 2 has captured

        self._initial_board = copy.deepcopy(self._board)  # create a deep copy of the initial board state

    def get_board(self):
        """Returns the Board"""
        print(self._board[0].to_regular_list())
        print(self._board[1].to_regular_list())
        print(self._board[2].to_regular_list())
        print(self._board[3].to_regular_list())
        print(self._board[4].to_regular_list())
        print(self._board[5].to_regular_list())
        print(self._board[6].to_regular_list())

    def get_current_turn(self):
        """Returns the current players turn"""
        if self._turn_tracker == "":  # if the turn tracker is empty return None
            return None
        else:  # else return the next players turn
            return self._turn_tracker

    def get_player_color(self, player_name):
        """Returns player color from player name"""
        if player_name == self._player_1[0]:
            return self._player_1[1]
        elif player_name == self._player_2[0]:
            return self._player_2[1]

    def next_turn(self, player_name):
        """Returns the name of the next player"""
        if player_name == self._player_1[0]:
            return self._player_2[0]
        elif player_name == self._player_2[0]:
            return self._player_1[0]

    def make_move(self, playername, coordinates, direction):
        """Lets a player make a move on the board"""
        temp_board = copy.deepcopy(self._board)  # copy of board state before the move
        if not self.win_con():  # if the game is not won
            if self._turn_tracker == playername or self._turn_tracker == "":  # if it is the first turn or players turn
                if self.get_marble(coordinates) == self.get_player_color(playername):  # if the marble color is right
                    if direction == 'R':  # insert and move pieces to the right
                        if self._board[coordinates[0]].to_regular_list()[coordinates[1] - 1] == 'X' or coordinates[
                            1] == 0:
                            # if the space to the left of the coordinate is empty or it is the first marble
                            i = coordinates[0]
                            while i <= 6:
                                if 'X' in self._board[coordinates[0]].to_regular_list()[i]:
                                    self._board[coordinates[0]].remove('X')
                                    break
                                i += 1
                            self._board[coordinates[0]].insert('X', coordinates[1])  # move the marble
                            if len(self._board[coordinates[0]].to_regular_list()) == 8:
                                if self._board[coordinates[0]].to_regular_list()[7] == 'R':  # if the last marble is red
                                    if playername == self._player_1[0]:  # if it is player 1 update score
                                        self._player_1_cap += 1
                                    elif playername == self._player_2[0]:  # if it player 2 update score
                                        self._player_2_cap += 1
                                    self._board[coordinates[0]].delete(7)  # delete the last node
                                    count = 0
                                    track = 0
                                    while count < 7:
                                        if self._board[count].to_regular_list()==self._initial_board[count].to_regular_list():  # if the new
                                            track +=1
                                        count += 1
                                    if track == 7:
                                        return False  # board reverts to an old board state
                                    self._turn_tracker = self.next_turn(playername)  # sets the turn to the next player
                                    self._initial_board = copy.deepcopy(temp_board)  # update the board
                                    return True
                                elif self._board[coordinates[0]].to_regular_list()[7] == self.get_player_color(
                                        playername):  # if the last node is the same as the player's color
                                    return False  # this is an invalid move
                                else:
                                    self._board[coordinates[0]].delete(7)
                                    count = 0
                                    track = 0
                                    while count < 7:
                                        if self._board[count].to_regular_list() == self._initial_board[
                                            count].to_regular_list():  # if the new
                                            track += 1
                                        count += 1
                                    if track == 7:
                                        return False  # board reverts to an old board state
                                    self._initial_board = copy.deepcopy(temp_board)
                                    self._turn_tracker = self.next_turn(playername)
                                    return True
                    elif direction == 'L':  # if direction is L check for blank space to the right
                        if coordinates[1] == 6 or self._board[coordinates[0]].to_regular_list()[
                            coordinates[1] + 1] == 'X':
                            i = coordinates[1]
                            while i >= 0:
                                if 'X' in self._board[coordinates[0]].to_regular_list()[
                                    i]:  # if there is a blank to the left
                                    self._board[coordinates[0]].delete(i)  # remove the blank node
                                    self._board[coordinates[0]].insert('X', coordinates[1])  # add a blank node
                                    count = 0
                                    track = 0
                                    while count < 7:
                                        if self._board[count].to_regular_list() == self._initial_board[
                                            count].to_regular_list():  # if the new
                                            track += 1
                                        count += 1
                                    if track == 7:
                                        return False  # board reverts to an old board state
                                    else:
                                        self._turn_tracker = self.next_turn(playername)
                                        self._initial_board = copy.deepcopy(
                                            temp_board)  # sets the turn to the next player
                                        return True
                                i -= 1
                            self._board[coordinates[0]].insert('X', coordinates[1] + 1)
                            if len(self._board[coordinates[0]].to_regular_list()) == 8:
                                if self._board[coordinates[0]].to_regular_list()[0] == self.get_player_color(
                                        playername):
                                    return False  # cannot remove your own marble
                                elif self._board[coordinates[0]].to_regular_list()[0] == 'R':  # if the marble is red
                                    self._board[coordinates[0]].delete(0)  # delete the marble
                                    if playername == self._player_1[0]:  # if it is player 1 update score
                                        self._player_1_cap += 1
                                    elif playername == self._player_2[0]:  # if it player 2 update score
                                        self._player_2_cap += 1
                                    count = 0
                                    track = 0
                                    while count < 7:
                                        if self._board[count].to_regular_list() == self._initial_board[
                                            count].to_regular_list():  # if the new
                                            track += 1
                                        count += 1
                                    if track == 7:
                                        return False  # board reverts to an old board state
                                if self._board == self._initial_board:
                                    return False
                                self._turn_tracker = self.next_turn(playername)  # sets the turn to the next player
                                self._initial_board = copy.deepcopy(temp_board)
                                return True
                            else:
                                count = 0
                                track = 0
                                while count < 7:
                                    if self._board[count].to_regular_list() == self._initial_board[
                                        count].to_regular_list():  # if the new
                                        track += 1
                                    count += 1
                                if track == 7:
                                    return False  # board reverts to an old board state
                                self._turn_tracker = self.next_turn(playername)  # sets the turn to the next player
                                self._initial_board = copy.deepcopy(temp_board)
                                return True  # This is a valid move
                    elif direction == 'F':  # if the direction is up check if it is the last row or blank below
                        if coordinates[0] == 6 or self._board[coordinates[0] + 1].to_regular_list()[
                            coordinates[1]] == 'X':
                            i = coordinates[0]
                            while i >= 0:
                                if 'X' in self._board[i].to_regular_list()[coordinates[1]]:
                                    self._board[i].remove('X')
                                    self._board[i].insert(self.get_marble((i + 1, coordinates[1])), coordinates[1])
                                    for j in range(i, coordinates[0]):
                                        self._board[j].delete(coordinates[1])
                                        self._board[j].insert(self.get_marble((j + 1, coordinates[1])), coordinates[1])
                                    self._board[coordinates[0]].insert('X', coordinates[1])
                                    self._board[coordinates[0]].delete(coordinates[1] + 1)
                                    count = 0
                                    track = 0
                                    while count < 7:
                                        if self._board[count].to_regular_list() == self._initial_board[
                                            count].to_regular_list():  # if the new
                                            track += 1
                                        count += 1
                                    if track == 7:
                                        return False  # board reverts to an old board state
                                    else:
                                        self._turn_tracker = self.next_turn(
                                            playername)  # sets the turn to the next player
                                        self._initial_board = copy.deepcopy(temp_board)
                                        return True
                                i -= 1
                            if self._board[0].to_regular_list()[coordinates[1]] == self.get_player_color(playername):
                                return False
                            elif self._board[0].to_regular_list()[coordinates[1]] == 'R':  # if top marble is red
                                if playername == self._player_1[0]:  # if it is player 1 update score
                                    self._player_1_cap += 1
                                elif playername == self._player_2[0]:  # if it player 2 update score
                                    self._player_2_cap += 1
                                for k in range(0, coordinates[0]):
                                    self._board[k].delete(coordinates[1])
                                    self._board[k].insert(self.get_marble((k + 1, coordinates[1])), coordinates[1])
                                self._board[coordinates[0]].insert('X', coordinates[1])
                                self._board[coordinates[0]].delete(coordinates[1] + 1)
                                count = 0
                                track = 0
                                while count < 7:
                                    if self._board[count].to_regular_list() == self._initial_board[
                                        count].to_regular_list():  # if the new
                                        track += 1
                                    count += 1
                                if track == 7:
                                    return False  # board reverts to an old board state
                            else:  # top space is a blank or other player's color
                                for k in range(0, coordinates[0]):
                                    self._board[k].delete(coordinates[1])
                                    self._board[k].insert(self.get_marble((k + 1, coordinates[1])), coordinates[1])
                                self._board[coordinates[0]].insert('X', coordinates[1])
                                self._board[coordinates[0]].delete(coordinates[1] + 1)
                                count = 0
                                track = 0
                                while count < 7:
                                    if self._board[count].to_regular_list() == self._initial_board[
                                        count].to_regular_list():  # if the new
                                        track += 1
                                    count += 1
                                if track == 7:
                                    return False  # board reverts to an old board state
                                self._turn_tracker = self.next_turn(playername)  # sets the turn to the next player
                                self._initial_board = copy.deepcopy(temp_board)
                                return True  # This is a valid move
                    elif direction == 'B':  # the direction is down check if it is in the top row or blank space above
                        if coordinates[0] == 0 or self._board[coordinates[0] - 1].to_regular_list()[
                            coordinates[1]] == 'X':
                            i = coordinates[0]  # start at the correct location
                            while i <= 6:
                                if 'X' in self._board[i].to_regular_list()[coordinates[1]]:
                                    while i > coordinates[0]:
                                        self._board[i].insert(self._board[i - 1].to_regular_list()[coordinates[1]],
                                                              coordinates[1])
                                        self._board[i].delete(coordinates[1] + 1)
                                        i -= 1
                                    self._board[coordinates[0]].delete(coordinates[1])
                                    self._board[coordinates[0]].insert('X', coordinates[1])
                                    count = 0
                                    track = 0
                                    while count < 7:
                                        if self._board[count].to_regular_list() == self._initial_board[
                                            count].to_regular_list():  # if the new
                                            track += 1
                                        count += 1
                                    if track == 7:
                                        return False  # board reverts to an old board state
                                    self._turn_tracker = self.next_turn(playername)  # sets the turn to the next player
                                    self._initial_board = copy.deepcopy(temp_board)
                                    return True  # This is a valid move
                                i += 1
                            if self._board[6].to_regular_list()[coordinates[1]] == self.get_player_color(playername):
                                return False
                            elif self._board[6].to_regular_list()[coordinates[1]] == 'R':  # if bottom marble is red
                                if playername == self._player_1[0]:  # if it is player 1 update score
                                    self._player_1_cap += 1
                                elif playername == self._player_2[0]:  # if it player 2 update score
                                    self._player_2_cap += 1
                                k = 6
                                while k > coordinates[0]:
                                    self._board[k].insert(self._board[k - 1].to_regular_list()[coordinates[1]],
                                                          coordinates[1])
                                    self._board[k].delete(coordinates[1] + 1)
                                    k -= 1
                                self._board[coordinates[0]].delete(coordinates[1])
                                self._board[coordinates[0]].insert('X', coordinates[1])
                                count = 0
                                track = 0
                                while count < 7:
                                    if self._board[count].to_regular_list() == self._initial_board[
                                        count].to_regular_list():  # if the new
                                        track += 1
                                    count += 1
                                if track == 7:
                                    return False  # board reverts to an old board state
                                self._turn_tracker = self.next_turn(playername)  # sets the turn to the next player
                                self._initial_board = copy.deepcopy(temp_board)
                                return True  # This is a valid move
                            else:
                                k = coordinates[0]
                                while k < 6:
                                    if 'X' in self._board[k].to_regular_list()[coordinates[1]]:
                                        i = k  # i is the next blank space
                                        while i > coordinates[0]:
                                            self._board[i].insert(self._board[i - 1].to_regular_list()[coordinates[1]],
                                                                  coordinates[1])
                                            self._board[i].delete(coordinates[1] + 1)
                                            i -= 1
                                        self._board[coordinates[0]].delete(coordinates[1])
                                        self._board[coordinates[0]].insert('X', coordinates[1])
                                        count = 0
                                        track = 0
                                        while count < 7:
                                            if self._board[count].to_regular_list() == self._initial_board[
                                                count].to_regular_list():  # if the new
                                                track += 1
                                            count += 1
                                        if track == 7:
                                            return False  # board reverts to an old board state
                                        self._turn_tracker = self.next_turn(
                                            playername)  # sets the turn to the next player
                                        self._initial_board = copy.deepcopy(temp_board)
                                        return True  # This is a valid move
                                    k += 1
                        else:
                            return False  # return false if it is not the players turn
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_winner(self):
        """Returns the winner of the game"""
        if not self.win_con():  # if game has not been won return None
            return None
        else:  # else return the winner
            return self.win_con()

    def get_captured(self, player_name):
        """Returns the amount of red marbles captured by the player"""
        if player_name == self._player_1[0]:  # if the player name belongs to player 1
            return self._player_1_cap  # return the amount of red marbles they captured
        elif player_name == self._player_2[0]:
            return self._player_2_cap

    def get_marble(self, coordinates):
        """Returns the marble at a game board coordinate"""
        row = self._board[coordinates[0]]  # row is the first coordinate
        return row.to_regular_list()[coordinates[1]]  # return the marble in the row from the second coordinate

    def get_marble_count(self):
        """Returns the amount of white, black and red marbles on the board"""
        b = 0  # Number of black marbles on the board
        w = 0  # Number of white marbles on the board
        r = 0  # Number of red marbles on the board
        for row in self._board:
            for marble in row.to_regular_list():
                if marble == 'B':
                    b += 1
                elif marble == 'W':
                    w += 1
                elif marble == 'R':
                    r += 1
        return w, b, r  # returns the number of White, Black, and Red Marbles

    def win_con(self):  # if the game is not won return false if it has won return the winner's name
        """Checks to see if the game has been won and if it has return the winner"""
        if self.get_marble_count()[1] == 0:  # if there are no black marbles on the board then white wins
            if self._player_1[1] == 'W':  # if Player 1 is white
                return self._player_1[0]  # then player 1 is the winner
            else:
                return self._player_2[0]  # else player 2 is white and must be the winner
        elif self.get_marble_count()[0] == 0:  # if there are no white marbles on the board then black wins
            if self._player_1[1] == 'B':  # if player 1 is black
                return self._player_1[0]  # then player 1 is the winner and we return their name
            else:
                return self._player_2[0]  # else player 2 is black and must be the winner
        elif self._player_1_cap == 7:  # if player 1 has 7 red marbles captured
            return self._player_1[0]  # they are the winner
        elif self._player_2_cap == 7:  # if player 2 has 7 red marbles
            return self._player_2[0]  # they are the winner
        else:  # else the game has not been won
            return False
