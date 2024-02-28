from zeep import Client


client = Client('http://localhost:8000/?wsdl')
print(client.service.calculate(2, 8, '*'))
