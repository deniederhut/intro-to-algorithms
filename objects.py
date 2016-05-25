#!/bin/env python

class DoublyLinkedList(object):

    def __init__(self):
        self.data = [[0, 'sentinel', 0]]
        self.empties = []

    def __iter__(self):
        index = 0
        while index != self.data[0][0]:
            index = self.data[index][2]
            value = self.data[index][1]
            yield index, value

    def __repr__(self):
        return str(self.data)

    def delete(self, item):
        key = self.search(item)
        if key:
            prev_item = self.data[key][0]
            next_item = self.data[key][2]
            self.data[prev_item][2] = next_item
            self.data[next_item][0] = prev_item
            self.empties.append(key)
        else:
            raise BaseException("No such item")

    def insert(self, item):
        if self.empties:
            key = self.empties.pop()
        else:
            key = len(self.data)
            self.data.append([None, None, None])
        self.data[key][0] = self.data[0][0]
        self.data[key][1] = item
        self.data[key][2] = 0
        self.data[self.data[0][0]][2] = key
        self.data[0][0] = key

    def search(self, value):
        for index, result in self:
            if result == value:
                return index
        return None
