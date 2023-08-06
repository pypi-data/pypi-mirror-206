'''Módulo de constantes del proyecto
Mantenedor: EYMG
Fecha: 2023-04-27
OT: NA
Ultimo cambio: Definición de documentación para sonarqube'''

'''Constantes de ambiente'''
MOCK = "false"

'''Constantes de URLS'''
FQDN_APIGEE = "https://sandbox.bancoazteca.com"
URL_API_LLAVESSEGURIDAD = FQDN_APIGEE + "/cobranza-credito/investigacion-cobranza/seguridad/v1/aplicaciones/llaves"
URL_API_ABONOS_CLIENTES = FQDN_APIGEE + "/cobranza_credito/investigacion-cobranza/gestion-clientes/v1/clientes"
URL_API_ABONOS_CREDIMAX = FQDN_APIGEE + "/cobranza_credito/investigacion-cobranza/creditos/v3/credimax"
URL_API_CONTACT_CENTER_CLIENTES = FQDN_APIGEE + "/cobranza_credito/investigacion-cobranza/call-center/gestion-clientes/v1"
URL_APIGEE_OAUTH2 = FQDN_APIGEE + "/oauth2/v1/token"

'''Constantes de valores para evitar CDP'''
RESULTADO = "resultado"
DATO = "dato"
CODIGO = "codigo"

'''Constantes de codificado'''
ENCODING_UTF8 = "utf-8"
CONTENT_TYPE_WWWURLENCODED = "application/x-www-form-urlencoded"
CONTENT_TYPE_JSON = "application/json"

'''Constantes de seguridad
No cambiar a menos que el ambiente sea otro
Para las llaves públicas y privadas respetar
el formato para que no se rompan los correspondientes
imports de crypto
'''
CREDENCIALES = "Basic SW83VnR6b1VGRDJiRjIyMFZhQ0g3SWJOanAwSjdNU0I6dEpuWGhLQ1l4QTUyM0g0YQ=="
GRANT_TYPE = "client_credentials"
BEARER = "Bearer "
BEGIN_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n"
END_PUBLIC_KEY = "\n-----END PUBLIC KEY-----"
BEGIN_PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\n"
END_PRIVATE_KEY = "\n-----END PRIVATE KEY-----"

'''Constantes numéricas'''
N0 = 0
N1 = 1
N2 = 2
N200 = 200
