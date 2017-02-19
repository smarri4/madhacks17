from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from Customer import *
import logging
import json

apikey = '4068fb9868181126f8b7bd67a0dd9306'
logger = logging.getLogger(__name__)

def purchases_for_month(request,pk):
    print(pk)
    month = int(request.GET.get('month'))

    res=Customer(apikey).getAllAccounts()
    id=res[0]['_id']
    cust_id=res[0]['customer_id']
    print("id", id, cust_id)

    res=Customer(apikey).getAllCustPurchases(id)
    print("purchases", res)
    print("res 0", res[0])
    #res.get('merchant_id')

    data = {}
    transList= []
    for item in res:
        transaction={}
        print("item", item['merchant_id'], item['purchase_date'])
        mer=Customer(apikey).getMerchantDetByID(item['merchant_id'])
        print("mer: ", mer)
        print("mer details:",mer['category'],mer['name'])
        # print(res['purchase_date'], res['amount'])
        transaction['category'] = mer['category']
        transaction['name'] = mer['name']
        transaction['purchase_date'] = item['purchase_date']
        transaction['amount'] = item['amount']
        # send 'customer id, puchase date, amount , category, name'

        transList.append(transaction)
    data['monthly_transaction'] = transList
    logger.info('dsfdsffd')
    logger.info(json.dumps(data))
    return HttpResponse(json.dumps(data))
