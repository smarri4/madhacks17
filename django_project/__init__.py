from django_project.Enterprise import *
apikey = '4068fb9868181126f8b7bd67a0dd9306'
if __name__=='__main__':
    json_data = Enterprise(apikey).getAllAccounts()
    print(json_data)
