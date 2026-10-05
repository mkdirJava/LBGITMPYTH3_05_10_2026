class proxy:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, aname):
        return getattr(self.wrapped, aname)