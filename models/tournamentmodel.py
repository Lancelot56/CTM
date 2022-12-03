# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:01:36 2022

@author: m
"""



from tinydb import TinyDB
from tinydb.table import Document


class TournamentModel:
    """ Class of Tournament
    Time control: 1min - Bullet, 5min - Blitz, 10min - Rapid
    Time_control: Bullet, Blitz, Rapid"""

    def __init__(self,idt, name,date, location, description, rounds,
                 players, time_control):

        self.idt = idt
        self.name = name
        self.date = date
        self.location = location
        self.description = description
        self.nb_rounds = 4
        self.rounds = rounds
        self.players = players
        self.time_control = time_control

    def __str__(self):
        return (
            f"NAME : {self.name}\n LOCATION : {self.location}\n MODE : {self.time_control}\n"
            f"DESCRIPTION : {self.description} \n"
            f"DATE : {self.date}\n ROUNDS : {self.rounds} "
            f"\n PLAYERS : {self.players}\n")

    @staticmethod
    def get_tournaments():
        """ Return all thetournaments of the table tournaments"""
        db = TinyDB('db.json')
        return db.table('tournaments').all()

    @staticmethod
    def get_tournament_by_id(idt:int) -> Document:
        """ Return tournament details for a precise id """
        db = TinyDB('db.json')
        print('\nDetails of tournament :',idt)
        return db.table('tournaments').get(doc_id = idt)
