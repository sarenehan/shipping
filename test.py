import xml.etree.ElementTree as ET
from zeep import Client, Settings
from zeep.exceptions import Fault, TransportError, XMLSyntaxError

# Set Connection
settings = Settings(strict=False, xml_huge_tree=True)
client = Client('SCHEMA-WSDLs/RateWS.wsdl', settings=settings)

rating_types = """
01 = Next Day Air
02 = 2nd Day Air
03 = Ground 12 = 3 Day Select
13 = Next Day Air Saver
14 = UPS Next Day Air Early
59 = 2nd Day Air A.M.

Valid international values:
07 = Worldwide Express
08 = Worldwide Expedited
11= Standard
54 = Worldwide Express Plus
65 = Saver
96 = UPS Worldwide Express Freight
71 = UPS Worldwide Express Freight
"""

# Set SOAP headers
headers = {

    'UPSSecurity': {
        'UsernameToken': {
            'Username': 'Oscardb2',
            'Password': 'AspenR00ts'
        },

        'ServiceAccessToken': {
            'AccessLicenseNumber': 'AD76F7488344DA95'
        }

    }
}

# Create request dictionary
requestDictionary = {

    "RequestOption": "Shop",
    "TransactionReference": {
        "CustomerContext": "Your Customer Context"
    }
}

# Create rate request dictionary
rateRequestDictionary = {

    "Package": {
        "Dimensions": {
            "Height": "10",
            "Length": "5",
            "UnitOfMeasurement": {
                "Code": "IN",
                "Description": "inches"
            },
            "Width": "4"
        },
        "PackageWeight": {
            "UnitOfMeasurement": {
                "Code": "Lbs",
                "Description": "pounds"
            },
            "Weight": "1"
        },
        "PackagingType": {
            "Code": "02",
            "Description": "Rate"
        }
    },
    "Service": {
        "Code": "03",
        "Description": "Service Code"
    },
    "ShipFrom": {
        "Address": {
            "AddressLine": [
                "1815 S Lane St",
            ],
            "City": "Seattle",
            "CountryCode": "US",
            "PostalCode": "98144",
            "StateProvinceCode": "WA"
        },
        "Name": "my house"
    },
    "ShipTo": {
        "Address": {
            "AddressLine": "8736 22nd Ave NW",
            "City": "Seattle",
            "CountryCode": "US",
            "PostalCode": "98117",
            "StateProvinceCode": "WA"
        },
        "Name": "parents house"
    },
    "Shipper": {
        "Address": {
            "AddressLine": [
                "1815 S Lane St",
            ],
            "City": "Seattle",
            "CountryCode": "US",
            "PostalCode": "98144",
            "StateProvinceCode": "WA"
        },
        "Name": "Stewart Renehan",
        "ShipperNumber": "R88E93"
    }
}

# Try operation
try:
    response = client.service.ProcessRate(_soapheaders=headers, Request=requestDictionary,
                                          Shipment=rateRequestDictionary)
    print(response)

except Fault as error:
    print(ET.tostring(error.detail))


