try:
    import mega
    print("mega.py OK, version module loaded")
    from mega import Mega
    print("Mega class OK")
except Exception as e:
    print("mega import FAIL:", repr(e))
# check requests
try:
    import requests
    print("requests OK")
except Exception as e:
    print("requests MISSING:", repr(e))
