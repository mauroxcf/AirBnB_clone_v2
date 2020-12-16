#!/usr/bin/python3
"""Unittest for console"""
import cmd
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json

run = os.system


class TestHBNBCommand(unittest.TestCase):
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

    def test_aa_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run("echo 'create State' | ./console.py" + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_aa_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run('echo create State name="California" | ./console.py' + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

'''
    def test_ab_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create Place")
            value_place = capt.getvalue().strip()
            self.assertTrue(value_place)

    def test_ac_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create BaseModel")
            value_basemodel = capt.getvalue().strip()

    def test_ad_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create User")
            value_user = capt.getvalue().strip()

    def test_ae_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create Amenity")
            value_amenity = capt.getvalue().strip()

    def test_af_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create Review")
            value_review = capt.getvalue().strip()

    def test_ag_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd("create City")
            value_city = capt.getvalue().strip()

    def test_ah_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd('create State name="California"')
            value_state = capt.getvalue().strip()

    def test_ai_create(self):
        """ create tests """
        with patch("sys.stdout", new=StringIO()) as capt:
            self.HBNB.onecmd('create City state_id="1" name="San_Francisco"')
            value_state = capt.getvalue().strip()
'''