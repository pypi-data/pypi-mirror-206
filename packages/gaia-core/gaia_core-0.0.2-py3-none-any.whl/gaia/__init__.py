from .gaia import Gaia
def init(api_token='', api_keys={}, debug=False):
    return Gaia(api_token=api_token, api_keys=api_keys, debug=debug)
    pass