'''Módulo credimax, contiene la lógica de negocio para recuperar saldos de creximax de cu'''

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
class Credimax(object):
    '''Clase credimax para entregar la funcionalidad de recuperar datos de estos
    Mantenedor: EYMG
    Fecha: 2023-04-27
    OT: NA
    Ultimo cambio: Definición de documentación para sonarqube'''

    def __init__(self, cliente, apigee=Apigee(),llaves_cobranza=LlavesCobranza()):
        self.clase = "Credimax"
        self.__llaves_cobranza = llaves_cobranza
        self.__apigee = apigee
        self.__crypto = Crypto(self.__llaves_cobranza)
        self.__cliente = cliente

    def get_pagos_pendientes(self):
        '''Método para obtener los pagos pendientes de un cu
        Mantenedor: EYMG
        Fecha: 2023-04-27
        OT: NA
        Ultimo cambio: Definición de documentación para sonarqube'''

        self.__apigee.genera_access_token()

        '''Se establecen headers para request'''
        headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "Authorization": BEARER + self.__apigee.obten_access_token(),
            "x-idAcceso": self.__llaves_cobranza.get_llaves_cliente()["idAcceso"],
            "x-idPlataforma": str(N1),
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
        data = requests.post(URL_API_ABONOS_CREDIMAX + "/pagos-pendientes", json=cu, headers=headers)
        response = {
            "codigo": N0,
            "dato": json.loads(json.dumps(data.json()))
        }

        '''Se obtiene respuesta y se validan resultados'''
        if data.status_code == N200:
            response[CODIGO] = N1
            response[DATO][RESULTADO]["pagoPuntual"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["pagoPuntual"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["pagoNormal"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["pagoNormal"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["pagoSugerido"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["pagoSugerido"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["pagoRequerido"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["pagoRequerido"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["pagoLiquidar"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["pagoLiquidar"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["pagoPuntualDigital"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["pagoPuntualDigital"], self.__crypto.get_private_cert_cliente()).decode()
        else:
            print(json.loads(json.dumps(data.json())))

        '''Se entrega respuesta'''
        return response

    def get_saldos(self):
        '''Médoto saldos utilizado para obtener los saldos actuales de un cu
        Mantenedor: EYMG
        Fecha: 2023-04-27
        OT: NA
        Ultimo cambio: Definición de documentación para sonarqube'''

        self.__apigee.genera_access_token()

        '''Se establecen headers para request'''
        headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "Authorization": BEARER + self.__apigee.obten_access_token(),
            "x-idAcceso": self.__llaves_cobranza.get_llaves_cliente()["idAcceso"],
            "x-idPlataforma": str(N1),
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
        data = requests.post(URL_API_ABONOS_CREDIMAX + "/saldos", json=cu, headers=headers)
        response = {
            "codigo": N0,
            "dato": json.loads(json.dumps(data.json()))
        }

        '''Se obtiene respuesta y se validan resultados'''
        if data.status_code == N200:
            response[CODIGO] = N1
            response[DATO][RESULTADO]["montoTotal"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["montoTotal"], self.__crypto.get_private_cert_cliente()).decode()
            response[DATO][RESULTADO]["montoPlanPago"] = self.__crypto.decrypt_rsa(
                response[DATO][RESULTADO]["montoPlanPago"], self.__crypto.get_private_cert_cliente()).decode()

        else:
            print(json.loads(json.dumps(data.json())))

        '''Se entrega respuesta'''
        return response
