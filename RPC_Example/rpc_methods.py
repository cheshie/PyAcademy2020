class RPCMethods:
    def __init__(self):
        self.registry = {}
    def __call__(self, method):
        self.registry[method.__name__] = method
    #
#
rpc_method = RPCMethods()

@rpc_method
def add(a, b):
    return a + b

@rpc_method
def upper(string):
    return string.upper()