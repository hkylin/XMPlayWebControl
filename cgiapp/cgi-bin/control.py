import cgi
import win32ui, dde

ACTIONS = {"play_pause":"key80", "stop":"key81", "next":"key128", "random":"key313",
"prev":"key129","vol_up":"key512", "vol_down":"key513", "vol_on_off":"key523",}

class DdeExecute():
    
    def __init__(self):
        self.conversation = None
        self.app = "xmplay"
        self.topic = "system"
        self.is_connected = False
        self._setup_dde()     
    
    def _setup_dde(self):
        self.serv = dde.CreateServer()
        self.serv.Create("TC")
        try:
            self.conversation = dde.CreateConversation(self.serv)
            self.conversation.ConnectTo(self.app,self.topic)
            self.is_connected = True
        except:
            self.is_connected = False
            print("Cannot connect to XMPlay")

    def exec_command(self,command):
        try:
            self.conversation.Exec(command)
            print("ok")
        except:
            print("Cannot exec the command")

data = cgi.FieldStorage()
action = data.getvalue("action")

print("Content-Type: text;charset=windows-1252")
print()

if action in ACTIONS.keys():
    ddeClient = DdeExecute()
    if ddeClient.is_connected:
        ddeClient.exec_command(ACTIONS[action])
else:
    print("Command not found")