import requests
class Enterprise():
    url='http://api.reimaginebanking.com'
    key=''
    # Constructor.
    def __init__(self, apikey):
        self.key=apikey

    def getAllAccounts(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getAccount(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()
