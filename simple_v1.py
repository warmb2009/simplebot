# -*- coding: utf-8 -*-
import requests

url = 'http://127.0.0.1:8080/ajax/tbadd/'
group_list = [{'name' : '淘客助手大牌采集7群', 'sender' : '达哥大牌发布员008'}, {'name' : '淘客助手精品采集82群', 'sender' : '达哥发布员08'}]

def postInfo(name, content, sender):
    data = {'name' : name, 'content' : content, 'sender' : sender}
    r = requests.post(url, data = data)
    
def onQQMessage(bot, contact, member, content):
    contact_type = contact.ctype

    if contact_type == 'group':
        groupname = contact.name
        groupsender = member.name

        dic = {'name' : groupname, 'sender' : groupsender}
        if dic in group_list:

            postInfo(groupname, content, groupsender)
