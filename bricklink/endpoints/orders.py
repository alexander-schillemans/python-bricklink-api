from .base import APIEndpoint

from bricklink.models.orders import Order, OrderList

class OrderMethods(APIEndpoint):

    def __init__(self, api):
        super(OrderMethods, self).__init__(api, "orders")

    def list(self, direction="in", status=None, filled=False):
        url = self.endpoint
        data = {}

        if direction: data['direction'] = direction
        if status: data['status'] = status
        if filled: data['filled'] = filled

        status, headers, respJson = self.api.get(url, data)
        internalStatusCode = respJson['meta']['code']
        if internalStatusCode in [400, 401, 403, 404, 405, 415, 422]: return Order().parseError(respJson['meta'])

        return OrderList().parse(respJson['data'])

    def get(self, id):

        url = '{endpoint}/{id}'.format(endpoint=self.endpoint, id=id)
        data = None

        status, headers, respJson = self.api.get(url, data)
        internalStatusCode = respJson['meta']['code']
        if internalStatusCode in [400, 401, 403, 404, 405, 415, 422]: return Order().parseError(respJson['meta'])

        return Order().parse(respJson['data'])

    def update(self,
        id,
        date_shipped=None,
        tracking_no=None,
        tracking_link=None,
        shipping_method_id=None,
        cost_shipping=None,
        cost_insurance=None,
        cost_credit=None,
        cost_etc1=None,
        cost_etc2=None,
        is_filed=None,
        remarks=None,
        shipping=None,
        cost=None
    ):

        url = '{endpoint}/{id}'.format(endpoint=self.endpoint, id=id)

        if shipping:
            shippingJson = shipping.getJSON()
        else:
            shippingJson = {}
            if date_shipped: shippingJson['date_shipped'] = date_shipped
            if tracking_no: shippingJson['tracking_no'] = tracking_no
            if tracking_link: shippingJson['tracking_link'] = tracking_link
            if shipping_method_id: shippingJson['method_id'] = shipping_method_id
        
        if cost:
            costJson = cost.getJSON()
        else:
            costJson = {}
            if cost_shipping: costJson['shipping'] = cost_shipping
            if cost_insurance: costJson['insurance'] = cost_insurance
            if cost_credit: costJson['credit'] = cost_credit
            if cost_etc1: costJson['etc1'] = cost_etc1
            if cost_etc2: costJson['etc2'] = cost_etc2
        
        data = {
            'shipping' : shippingJson,
            'cost' : costJson,
        }

        if is_filed: data['is_filed'] = is_filed
        if remarks: data['remarks'] = remarks

        status, headers, respJson = self.api.put(url, data)
        internalStatusCode = respJson['meta']['code']
        if internalStatusCode in [400, 401, 403, 404, 405, 415, 422]: return Order().parseError(respJson['meta'])

        return Order().parse(respJson['data'])
    
    def updateStatus(self, id, status):

        url = '{endpoint}/{id}/status'.format(endpoint=self.endpoint, id=id)
        data = { 'field' : 'status', 'value' : status }

        status, headers, respJson = self.api.put(url, data)
        internalStatusCode = respJson['meta']['code']
        if internalStatusCode in [400, 401, 403, 404, 405, 415, 422]: return Order().parseError(respJson['meta'])

        return Order().parse(respJson['data'])
    
    def updatePayment(self, id, status):
        url = '{endpoint}/{id}/status'.format(endpoint=self.endpoint, id=id)
        data = { 'field' : 'payment_status', 'value' : status }

        status, headers, respJson = self.api.put(url, data)
        internalStatusCode = respJson['meta']['code']
        if internalStatusCode in [400, 401, 403, 404, 405, 415, 422]: return Order().parseError(respJson['meta'])

        return Order().parse(respJson['data'])