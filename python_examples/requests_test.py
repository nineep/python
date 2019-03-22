from requests import Request, Session

s = Session()
req = Request('GET', url,
              data = data,
              headers = header
             )
prepped = req.prepare()


resp = s.send(prepped,
              stream = stream,
              verify = verify
