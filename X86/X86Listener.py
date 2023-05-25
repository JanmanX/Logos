from generated.LogosParser import LogosParser
from generated.LogosListener import LogosListener

class X86Listener(LogosListener):
    # Enter a parse tree produced by LogosParser#prog.
    def enterProg(self, ctx:LogosParser.ProgContext):
        print("Entering prog in x86")
        pass

