import http.client

conn = http.client.HTTPSConnection("opendata.aemet.es")

headers = {
    'cache-control': "no-cache"
    }
api_key="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0Z3MxMDAzQGFsdS51YnUuZXMiLCJqdGkiOiI0MTQ0YjQ3Ni1mNmQ4LTQ0ZTgtYTI0MC00MWY5M2NlOTQ2NDUiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTY4Njg0NjI2NiwidXNlcklkIjoiNDE0NGI0NzYtZjZkOC00NGU4LWEyNDAtNDFmOTNjZTk0NjQ1Iiwicm9sZSI6IiJ9.BGfrjBSA4_Ww-_SiU2cMkGpvF0Z3hw5XMDb4PF3-Xng"
conn.request("GET", "/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/?api_key="+ api_key, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))