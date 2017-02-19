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

    def getAccountbyID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllBills(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getBillByID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllCustomers(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getCustomerByID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllDeposits(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getDepositByID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()


    def getAllMerchants(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getMerchantByID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllTransfers(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getTransferByID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllWithdrawals(self):
        url=self.url+'/enterprise/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getWithdrawlsByID(self,id):
        url=self.url+'/enterprise/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()








