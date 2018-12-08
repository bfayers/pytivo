import re
from telnetlib import Telnet
import json
import os
import time

class TivoClient():
    def __init__(self, ip, port):
        """Init client"""
        self.ip = ip
        self.port = port
        keycode_path = os.path.join(os.path.dirname(__file__), 'keycodes.json')
        with open(keycode_path) as kcf:
            keycodes = json.load(kcf)
            IRCodes = keycodes["IRCodes"]
            AllIRCodes = IRCodes["NavButtons"]
            AllIRCodes = AllIRCodes + IRCodes["ControlButtons"]
            AllIRCodes = AllIRCodes + IRCodes["VideoModeButtons"]
            AllIRCodes = AllIRCodes + IRCodes["AspectButtons"]
            AllIRCodes = AllIRCodes +  IRCodes["PlaybackButtons"]
            AllIRCodes = AllIRCodes +  IRCodes["NumButtons"]
            AllIRCodes = AllIRCodes +  IRCodes["ShortcutButtons"]

            KeyboardCodes = keycodes["KeyboardCodes"]
            AllKeyboardCodes = KeyboardCodes["SpecialCharacters"]
            AllKeyboardCodes = AllKeyboardCodes + KeyboardCodes["NavButtons"]
            AllKeyboardCodes = AllKeyboardCodes + KeyboardCodes["EditButtons"]
            AllKeyboardCodes = AllKeyboardCodes + KeyboardCodes["ControlButtons"]

            self.AllIRCodes = AllIRCodes
            self.AllKeyboardCodes = AllKeyboardCodes
            self.TeleportAreas = keycodes["TeleportAreas"]


    def getStatus(self):
        channelNumberRegex = '[0-9]{4}'
        try:
            with Telnet(self.ip, self.port) as tn:
                status = tn.read_until(b"\r").decode("utf-8")
                channel_num = re.search(channelNumberRegex, status).group(0)
            return channel_num
        except EOFError:
            return "Timed Out"
        except ConnectionResetError:
            return "Timed Out"

    def sendCommand(self, command):
        try:
            with Telnet(self.ip, self.port) as tn:
                tn.write(str.encode(command))
                time.sleep(0.5)
                response = tn.read_until(b"\r", timeout=2).decode("utf-8")
            return response
        except EOFError:
            return "Timed Out"
        except ConnectionResetError:
            return "Timed Out"
    
    def teleport(self, area):
        if area not in self.TeleportAreas:
            return "FAILED_INVALID_AREA"
        
        command = "TELEPORT "+area
        response = self.sendCommand(command)
        if area == "LIVETV" :
            if "LIVETV_READY" in response:
                #LiveTV Change is ready
                return "SUCCESS_LIVETV_READY"
        else:
            if response == "Timed Out":
                return "Timed Out"
            else:
                return "SUCCESS"

    def setChannel(self, channelNumber):
        """Set the channel of the TiVo box"""
        command = "SETCH "+channelNumber+"\r\n"
        response = self.sendCommand(command)
        if "CH_FAILED" in response:
            #Changing channel failed
            #Let's find out why
            failedRegex = "(?<=CH_FAILED )(.*)"
            reasonForFail = re.search(failedRegex, response).group(0)
            failString = "FAILED_"+reasonForFail
            return failString
        else:
            if response == "Timed Out":
                return "Timed Out"
            else:
                return "SUCCESS"

    def sendIRCode(self, ircode):
        if ircode not in self.AllIRCodes:
            return "FAILED_INVALID_IRCODE"

        command = "IRCODE "+ircode+"\r\n"
        response = self.sendCommand(command)

    def sendKeyboardCode(self, keybcode):
        if keybcode not in self.AllKeyboardCodes:
            return "FAILED_INVALID_KEYBOARD_CODE"

        command = "KEYBOARD "+keybcode+"\r\n"
        response = self.sendCommand(command)