from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.order_management_exception import OrderManagementException
"""
        def find_item_by_key(self, key:str):
            if found_item:
                proid = item["_OrderRequest__product_id"]
                address = item["_OrderRequest__delivery_address"]
                reg_type = item["_OrderRequest__order_type"]
                phone = item["_OrderRequest__phone_number"]
                order_timestamp = item["_OrderRequest__time_stamp"]
                zip_code = item["_OrderRequest__zip_code"]
                # set the time when the order was registered for checking the md5
                with freeze_time(datetime.fromtimestamp(order_timestamp).date()):
                    order = OrderRequest(product_id=proid,
                                         delivery_address=address,
                                         order_type=reg_type,
                                         phone_number=phone,
                                         zip_code=zip_code)

                if order.order_id != data["OrderID"]:
                    raise OrderManagementException("Orders' data have been manipulated")
                else:
                    

        def add_item(self, new_item):
            found = False
            for item in self.data:
                if item["_OrderRequest__order_id"] = new_item.order_id:
                    found = True
                if not found:
                    self.data.append(new_item.__dict__)
                else:
                    raise OrderManagementException("order_id is already registered in orders_store")
                
                self.save()
"""
