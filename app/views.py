import requests

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .serializers import EmployeeSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'Zip Code Api endpoint': '/getzipcode/string:zipcode'
        }
    )


class GetZipCode(generics.CreateAPIView):
    '''
    Class to request to the base url api to retrieve the zip code

    /getzipcode/<string:zipcode>

    Parameters
    ----------
    zipcode : string
        Zipcode from Brazil know as CEP in format '00000000'
    '''

    base_url = 'https://api.postmon.com.br/v1/cep/{}'
    serializer_class = EmployeeSerializer

    def post(self, request, zipcode):
        # cleaning the zipcode string
        if '-' in zipcode:
            zipcode = zipcode.replace('-', '')

        # validating params
        if not isinstance(zipcode, str) or not zipcode.isdigit():
            raise ValidationError(
                {
                    'error': 'Invalid type of parameter.',
                    'message': 'The zipcode must be string and only numbers'
                }
            )

        # verifying zipcode length
        if len(zipcode) > 8 or len(zipcode) < 8:
            raise ValidationError(
                {
                    'error': 'Invalid length',
                    'message': 'CEP must be 8 characters long.'
                }
            )

        # trying to get the response from the zipcode requested
        try:
            # sending the request to retrieve the zipcode
            zipcode_resp = requests.get(self.base_url.format(zipcode))

            # getting the json data from the Response object
            zipcode_resp = zipcode_resp.json()

            # serializing the data to get only the fields needed
            serialized_data = {
                'cep': zipcode_resp['cep'],
                'address': zipcode_resp['logradouro'],
                'neighborhood': zipcode_resp['bairro'],
                'city': zipcode_resp['cidade'],
                'state': zipcode_resp['estado']
            }

        # catching the exception
        except Exception as e:
            # raising the exception with the message and 400 as status code
            raise ValidationError(
                {
                    'error': e,
                    'message': 'Something went wrong, verify the parameter. ' +
                    'If the error persists maybe the zipcode does not exist.'
                }
            )

        return Response(serialized_data, status=status.HTTP_200_OK)
