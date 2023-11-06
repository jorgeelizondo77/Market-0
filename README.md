Market-0

Es un prototipo de sistema para administrar una empresa instalada en un mercado de abastos:
Proveedores
Clientes
Ordenes de compra



pip install -r requirements.txt


crear el archivo secret.json al nivel de manage.py y completar los datos

{
    "FILENAME": "secret.json",
    "SECRET_KEY": "",
    "DB_NAME": "",
    "USER": "",
    "PASSWORD": "",
    "PORT": "5432",
}

Llenar desde el admin la tabla Orden_Compra_Estatus
1 Pendiente
2 Generada
3 Cancelada
4 En entrada
