import requests
class Customer():
    url='http://api.reimaginebanking.com'
    key=''
    # Constructor.
    def __init__(self, apikey):
        self.key=apikey

    def getAllAccounts(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getAllCustPurchases(self,id):
        url=self.url+'/accounts/'+id+'/purchases'+'?'+'key='+self.key
        response=requests.get(url)
        return response.json()

    def getMerchantDetByID(self,mid):
        url=self.url+'/merchants/'+mid+'?'+'key='+self.key
        response=requests.get(url)
        return response.json()


    def getAccountByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllATMs(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getATMByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllBills(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getBillByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllBranches(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getBranchByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllCustomers(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getCustomerByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllDeposits(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getDepositByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllLoans(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getLoanByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllMerchants(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getMerchantByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllPurchases(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getPurchasesByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllTransfers(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getTransferByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

    def getAllWithdrawls(self):
        url=self.url+'/accounts'+'?'+'key='+self.key
        response = requests.get(url)
        return response.json()

    def getWithdrawlByID(self,id):
        url=self.url+'/accounts/'+id+'?'+self.key
        response = requests.get(url)
        return response.json()

