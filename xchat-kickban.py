__module_name__ = "xchat-kickban" 
__module_version__ = "1.0" 
__module_description__ = "Kick-bans chimpout spammers on the #gultij channel"
__module_author__ = "Octavio Alvarez <alvarezp@alvarezp.com>"

import xchat
import time
import re

channels = ["#gultij", "#banning-test", "#banning-test-2"]

def cb_server_privmsg(word, word_eol, userdata):

    ident = word[0];
    nick = word[0].split(":")[1].split("!")[0];
    command = word[1]; #Should be "PRIVMSG"
    target = word[2]; #Channel or me
    message = word_eol[3].replace(" ", "").lower();

    me = xchat.get_info("nick")

    if target not in channels:
        return xchat.EAT_NONE

    if re.search(r'chimpout\.com\/forum', message):
        print "Spammer detected: " + nick + ". He will be kick-banned."
        xchat.command("msg ChanServ op " + target + " " + me)
        time.sleep(3)
        xchat.command("kickban " + nick + " 2")
        xchat.command("msg ChanServ deop " + target + " " + me)
    return xchat.EAT_NONE

xchat.hook_server("PRIVMSG", cb_server_privmsg)

print "Plugin xchat-kickban-reaction loaded!"

