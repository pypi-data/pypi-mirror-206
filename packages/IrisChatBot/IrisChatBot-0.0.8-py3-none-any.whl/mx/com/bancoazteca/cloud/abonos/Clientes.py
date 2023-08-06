'''Módulo clientes, contiene la lógica de negocio para trabajar datos de CU'''
from mx.com.bancoazteca.cloud.core.seguridad.Apigee import *
from mx.com.bancoazteca.cloud.core.seguridad.LlavesCobranza import LlavesCobranza
from mx.com.bancoazteca.cloud.core.seguridad.Crypto import Crypto

'''
Proyecto: IrisChatBot
Clase: Crypto
Mantenedor: EYMG
Fecha: 2023-04-27
OT: NA
Ultimo cambio: Definición de documentación para sonarqube 
'''
class Clientes(object):
    '''Clase Clientes para entregar la funcionalidad de recuperar datos de estos
    Mantenedor: EYMG
    Fecha: 2023-04-27
    OT: NA
    Ultimo cambio: Definición de documentación para sonarqube'''

    def __init__(self, cliente, apigee=Apigee(), llaves_cobranza=LlavesCobranza()):
        self.clase = "Clientes"
        self.__llaves_cobranza = llaves_cobranza
        self.__apigee = apigee
        self.__crypto = Crypto(self.__llaves_cobranza)
        self.__cliente = cliente

    def get_cliente_por_nombre(self):
        '''Método para obtener los datos de cliente por su nombre, fecha de nacimiento y 4 ultimos dígitos de cu
        Mantenedor: EYMG
        Fecha: 2023-04-27
        OT: NA
        Ultimo cambio: Definición de documentación para sonarqube'''
        self.__apigee.genera_access_token()

        '''Se establecen headers para request'''
        headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "Authorization": BEARER + self.__apigee.obten_access_token(),
            "x-id-acceso": self.__llaves_cobranza.get_llaves_cliente()["idAcceso"],
            "x-id-plataforma": str(N1),
            "x-ismock": MOCK
        }

        '''Se establecen valores del request'''
        data = {
            "nombreCompleto": self.__crypto.encrypt_rsa(self.__cliente["nombre"],
                                                        self.__crypto.get_public_cert_cliente()).decode(),
            "fechaNacimiento": self.__crypto.encrypt_rsa(self.__cliente["fechaNacimiento"],
                                                         self.__crypto.get_public_cert_cliente()).decode(),
            "folioClienteUnico": self.__crypto.encrypt_rsa(self.__cliente["folioCU"],
                                                           self.__crypto.get_public_cert_cliente()).decode(),
        }

        '''Se ejecuta consulta httprequest'''
        data = requests.post(URL_API_ABONOS_CLIENTES + "/busquedas/nombre", json=data, headers=headers)
        response = {
            "codigo": N0,
            "dato": json.loads(json.dumps(data.json()))
        }

        '''Se obtiene respuesta y se validan resultados'''
        if data.status_code == N200:
            response[CODIGO] = N1
            response[DATO][RESULTADO]["clientes"][N0]["nombre"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["nombre"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["apellidoPaterno"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["apellidoPaterno"],
                self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["apellidoMaterno"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["apellidoMaterno"],
                self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["fechaNacimiento"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["fechaNacimiento"],
                self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["correo"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["correo"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["idPais"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["idPais"],
                self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["idCanal"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["idCanal"],
                self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["idSucursal"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["idSucursal"],
                self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["folio"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["clientes"][N0]["clienteUnico"]["folio"],
                self.__crypto.get_private_cert_cliente()).decode()
        else:
            print(json.loads(json.dumps(data.json())))

        '''Se entrega respuesta'''
        return response

    def get_contactos_por_cu(self):
        '''Método para obtener los datos de contacto cliente por su cu
        Mantenedor: EYMG
        Fecha: 2023-04-27
        OT: NA
        Ultimo cambio: Definición de documentación para sonarqube'''
        self.__apigee.genera_access_token()

        '''Se establecen headers para request'''
        headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "Authorization": BEARER + self.__apigee.obten_access_token(),
            "x-id-acceso": self.__llaves_cobranza.get_llaves_cliente()["idAcceso"],
            "x-ismock": MOCK
        }

        '''Se establecen valores del request'''
        cu = {
            "clienteUnico": {
                "idPais": self.__crypto.encrypt_rsa(self.__cliente["idPais"],
                                                   self.__crypto.get_public_cert_cliente()).decode(),
                "idCanal": self.__crypto.encrypt_rsa(self.__cliente["idCanal"],
                                                    self.__crypto.get_public_cert_cliente()).decode(),
                "idSucursal": self.__crypto.encrypt_rsa(self.__cliente["idSucursal"],
                                                       self.__crypto.get_public_cert_cliente()).decode(),
                "folio": self.__crypto.encrypt_rsa(self.__cliente["folio"],
                                                  self.__crypto.get_public_cert_cliente()).decode()
            }
        }

        '''Se ejecuta consulta httprequest'''
        data = requests.post(URL_API_CONTACT_CENTER_CLIENTES + "/clientes/contactos/busquedas", json=cu, headers=headers)
        response = {
            "codigo": N0,
            "dato": json.loads(json.dumps(data.json()))
        }

        if data.status_code == N200:
            response[CODIGO] = N1

            for telefono in response["dato"]["resultado"]["telefonos"]:
                telefono["numero"] =  self.__crypto.decrypt_rsa(
                telefono["numero"], self.__crypto.get_private_cert_cliente()).decode()

        else:
            print(json.loads(json.dumps(data.json())))

        '''Se entrega respuesta'''
        return response
