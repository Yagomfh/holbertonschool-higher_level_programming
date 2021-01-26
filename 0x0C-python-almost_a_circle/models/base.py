#!/usr/bin/python3
"""Module for class base"""
import json
import csv
import turtle
import random


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Class to json string method"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        dicts = []
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
        json_string = Base.to_json_string(dicts)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_string)

    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates and instance from a dict"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        res = []
        try:
            with open(filename, "r") as f:
                dicts = Base.from_json_string(f.read())
            for dic in dicts:
                res.append(cls.create(**dic))
        except:
            pass
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save class to csv file method"""
        dicts = []
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as csv_f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
            writer.writeheader()
            for dic in dicts:
                writer.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from cvs file"""
        filename = cls.__name__ + ".csv"
        dicts = []
        with open(filename, 'r') as csv_f:
            for line in csv.DictReader(csv_f):
                for keys in line:
                    line[keys] = int(line[keys])
                dicts.append(cls.create(**line))
        return dicts

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        zoom = 4
        win = turtle.getscreen()
        pen = turtle.Turtle()
        for rct in list_rectangles:
            R = random.random()
            G = random.random()
            B = random.random()
            pen.color(R, G, B)
            pen.penup()
            start_x = -1 * ((rct.width * zoom) / 2)
            start_y = (rct.height * zoom) / 2
            pen.goto(start_x, start_y)
            pen.pendown()
            for x in range(4):
                if x % 2 == 0:
                    pen.forward(rct.width * zoom)
                    pen.right(90)
                else:
                    pen.forward(rct.height * zoom)
                    pen.right(90)
            pen.penup()
            pen.home()
            pen.pendown()
        for sqr in list_squares:
            R = random.random()
            G = random.random()
            B = random.random()
            pen.color(R, G, B)
            pen.penup()
            start_x = -1 * ((sqr.width * zoom) / 2)
            start_y = (sqr.height * zoom) / 2
            pen.goto(start_x, start_y)
            pen.pendown()
            for x in range(4):
                if x % 2 == 0:
                    pen.forward(sqr.width * zoom)
                    pen.right(90)
                else:
                    pen.forward(sqr.height * zoom)
                    pen.right(90)
            pen.penup()
            pen.home()
            pen.pendown()
        turtle.done()
