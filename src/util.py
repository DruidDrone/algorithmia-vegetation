from Algorithmia.errors import import AlgorithmException

def sanity(input):
    if type(input) is not dict:
        raise AlgorithmException("Only JSON accepted", 'UnsupportedError')
