#!/usr/bin/python3
"""Unittest for console"""
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(cmd.Cmd):
    """
    testing all commands
    """
    def test_docstring(self):
        """docstring"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create State")
            value_state = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create Place")
            value_place = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create BaseModel")
            value_basemodel = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create User")
            value_user = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create Amenity")
            value_amenity = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create Review")
            value_review = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create City")
            value_city = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create State name="California"")
            value_state = capt.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create City state_id="0001" name="San_Francisco")
            value_state = capt.getvalue().strip()
