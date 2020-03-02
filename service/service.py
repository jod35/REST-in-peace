from flask import Flask
from flask_restful import Api,abort,fields,marshal_with,reqparse,Resource
from datetime import datetime
from .http_status import HttpStatus
from pytz import utc

class NotificationManager():
    last_id=0
    def __init__(self):
        self.notiications={}

    def insert_nofication(self,notifiation):
        self.__class__.last_id +=1
        notifiation.id=self.__class__.last_id
        self.notiications[self.__class__.last_id]=notifiation

    def get_notification(self,id):
        return self.notiications[id]

    def delete_notifications(self):
        del self.notiications[id]