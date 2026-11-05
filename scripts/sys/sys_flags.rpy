init python:








    class FlagVault:
        def __init__(self):
            self.vault = set()
        
        def Raise(self, flag):
            self.vault.add(flag)
        
        def Drop(self, flag):
            self.vault.discard(flag)
        
        def Has(self, flag):
            return flag in self.vault
        
        def Seen(self, flag):
            ret = self.Has(flag)
            self.Raise(flag)
            return ret
        
        def Reset(self):
            self.vault.clear()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
