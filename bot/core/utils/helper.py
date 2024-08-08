import re
import dns.resolver
from ..models import USER

def strip_script_tags(page):
    pattern = re.compile(r'\s?on\w+="[^"]+"\s?')
    result = re.sub(pattern, "", page)
    pattern2 = re.compile(r'<script[\s\S]+?/script>')
    result = re.sub(pattern2, "", result)
    return result
  
def make_filter(userID):
  if isinstance(userID, str) and userID.startswith("@"):
    filter = {"username": userID[1:]}
  elif isinstance(userID, str) and userID.isdigit():
    filter = {'userid': int(userID)}
  else:
    filter = {'userid': userID}

  return filter

def get_user(message):
  userID = None
  args = message.text.split(" ")
  if len(args) > 1:
    userID = args[1]
    return userID
  elif message.reply_to_message:
    if message.reply_to_message.forward_from:
      userID = message.reply_to_message.forward_from.id

      return userID
  else:
    return None


def generate_user(userinfo, userdata):
   data = {
     "userid": userinfo['userid'],
     "username": userinfo['username'][-1] if userinfo['username'] else "",
     "dc": userinfo['dc'],
     "name": userinfo['name'][-1] if userinfo['username'] else "",
     "is_banned": bool(userinfo.get("is_banned",False))
     or bool(userdata.get("is_banned",False)),
     "warns": userdata.get("warns",0),
     "subscription": userdata.get("subscription", {"name": "free"}),
     "status": userdata.get("status","active"),
     "data": userdata.get("data", {}),
     "settings": userdata.get("settings",{}),
     "firstseen": userdata['firstseen'],
     "lastseen": userdata['lastseen']
   }
   if data["subscription"] == {}:
     data["subscription"]  = {"name": "free"}
   return USER(data)

def chunkstring(string, length):
  return (string[0+i:length+i] for i in range(0, len(string), length))