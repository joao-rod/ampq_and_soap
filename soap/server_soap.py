"""
"""
from xml.dom import minidom
from lxml import etree
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class CalculatorService(ServiceBase):
    """_summary_

    Args:
        ServiceBase (ServiceBase): Próprio do mólulo spyne

    Returns:
        Integer: Retorno do método deve ser inteiro
    """

    @rpc(Integer, Integer, str, _returns=float)
    def calculate(ctx, op1, op2, operation) -> float:
        """_summary_

        Args:
            ctx (Context): Contexto do método
            op1 (Integer): Primeiro operando
            op2 (Integer): Segundo operando
            operation (str): Operação a ser realizada

        Returns:
            Integer: Resultado da operação
        """

        if operation == '+':
            result = op1 + op2
        if operation == '-':
            result = op1 - op2
        if operation == '*':
            result = op1 * op2
        if operation == '/':
            result = op1 / op2

        xml_str = minidom.parseString(etree.tostring(
            ctx.in_document)).toprettyxml(indent="  ")

        print(ctx.in_document, end='\n\n')
        print(xml_str)

        return result


application = Application([CalculatorService], 'Calculator', in_protocol=Soap11(
    validator='lxml'), out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('localhost', 8000, wsgi_app)

    print('Server running in localhost:8000')

    server.serve_forever()
