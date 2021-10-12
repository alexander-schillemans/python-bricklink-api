from .base import BaseModel, ObjectListModel

class OrderList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Order)

class Order(BaseModel):

    def __init__(self,
        order_id=None,
        date_ordered=None,
        date_status_changed=None,
        seller_name=None,
        store_name=None,
        buyer_name=None,
        buyer_email=None,
        require_insurance=None,
        status=None,
        is_invoiced=None,
        remarks=None,
        total_count=None,
        unique_count=None,
        total_weight=None,
        buyer_order_count=None,
        is_filed=None,
        drive_thru_sent=None,
        payment=None,
        shipping=None,
        cost=None,
        disp_cost=None
    ):

        super().__init__()

        self.order_id = order_id
        self.date_ordered = date_ordered
        self.date_status_changed = date_status_changed
        self.seller_name = seller_name
        self.store_name = store_name
        self.buyer_name = buyer_name
        self.buyer_email = buyer_email
        self.require_insurance = require_insurance
        self.status = status
        self.is_invoiced = is_invoiced
        self.remarks = remarks
        self.total_count = total_count
        self.unique_count = unique_count
        self.total_weight = total_weight
        self.buyer_order_count = buyer_order_count
        self.is_filed = is_filed
        self.drive_thru_sent = drive_thru_sent
        self.payment = payment if payment else Payment()
        self.shipping = shipping if shipping else Shipping()
        self.cost = cost if cost else Cost()
        self.disp_cost = disp_cost if disp_cost else Cost()

class Payment(BaseModel):

    def __init__(self,
        method=None,
        currency_code=None,
        date_paid=None,
        status=None
    ):

        self.method = method
        self.currency_code = currency_code
        self.date_paid = date_paid
        self.status = status

class Shipping(BaseModel):

    def __init__(self,
        method_id=None,
        method=None,
        tracking_no=None,
        tracking_link=None,
        date_shipped=None,
        address=None,
        full=None,
        country_code=None
    ):

        self.method_id = method_id
        self.method = method
        self.tracking_no = tracking_no
        self.tracking_link = tracking_link
        self.date_shipped = date_shipped
        self.address = address if address else Address()
        self.full = full
        self.country_code = country_code

class Cost(BaseModel):

    def __init__(self,
        currency_code=None,
        subtotal=None,
        grand_total=None,
        etc1=None,
        etc2=None,
        insurance=None,
        shipping=None,
        credit=None,
        coupon=None,
        vat_rate=None,
        vat_amount=None
    ):

        self.currency_code = currency_code
        self.subtotal = subtotal
        self.grand_total = grand_total
        self.etc1 = etc1
        self.etc2 = etc2
        self.insurance = insurance
        self.shipping = shipping
        self.credit = credit
        self.coupon = coupon
        self.vat_rate = vat_rate
        self.vat_amount = vat_amount

class Address(BaseModel):

    def __init__(self,
        name=None,
        full=None,
        address1=None,
        address2=None,
        country_code=None,
        city=None,
        state=None,
        postal_code=None
    ):

        self.name = name if name else Name()
        self.full = full
        self.address1 = address1
        self.address2 = address2
        self.country_code = country_code
        self.city = city
        self.state = state
        self.postal_code = postal_code

class Name(BaseModel):

    def __init__(self,
        full=None,
        first=None,
        last=None
    ):

        self.full = full
        self.first = first
        self.last = last

class OrderItem(BaseModel):

    def __init__(self,
        inventory_id=None,
        item=None,
        color_id=None,
        color_name=None,
        quantity=None,
        new_or_used=None,
        completeness=None,
        unit_price=None,
        unit_price_final=None,
        disp_unit_price=None,
        disp_unit_price_final=None,
        currency_code=None,
        disp_currency_code=None,
        remarks=None,
        description=None,
        weight=None
    ):

        super().__init__()

        self.inventory_id = inventory_id
        self.item = item if item else Item()
        self.color_id = color_id
        self.color_name = color_name
        self.quantity = quantity
        self.new_or_used = new_or_used
        self.completeness = completeness
        self.unit_price = unit_price
        self.unit_price_final = unit_price_final
        self.disp_unit_price = disp_unit_price
        self.disp_unit_price_final = disp_unit_price_final
        self.currency_code = currency_code
        self.disp_currency_code = disp_currency_code
        self.remarks = remarks
        self.description = description
        self.weight = weight

class Item(BaseModel):

    def __init__(self,
        no=None,
        name=None,
        type=None,
        category_id=None
    ):

        self.no = no
        self.name = name
        self.type = type
        self.category_id = category_id

class OrderMessage(BaseModel):

    def __init__(self,
        subject=None,
        body=None,
        _from=None,
        to=None,
        dateSent=None
    ):

        super().__init__()

        self.subject = subject
        self.body = body
        self._from = _from
        self.to = to
        self.dateSent = dateSent

class OrderProblem(BaseModel):

    def __init__(self,
        type=None,
        message=None,
        reason_id=None
    ):

        self.type = type
        self.message = message
        self.reason_id = reason_id