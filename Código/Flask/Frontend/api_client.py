from apiclient import APIClient

class MyClient(APIClient):

    def list_customers(self):
        url = "http://example.com/customers"
        return self.get(url)

    def add_customer(self, customer_info):
        url = "http://example.com/customers"
        return self.post(url, data=customer_info)

client = MyClient()
client.add_customer({"name": "John Smith", "age": 28})
client.list_customers()