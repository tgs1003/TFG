# coding: utf-8

"""
    AEMET OpenData

    AEMET OpenData es una API REST desarrollado por AEMET que permite la difusión y la reutilización de la información meteorológica y climatológica de la Agencia, en el sentido indicado en la Ley 18/2015, de 9 de julio, por la que se modifica la Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público. (IMPORTANTE: Para poder realizar peticiones, es necesario introducir en API Key haciendo clic en el círculo rojo de recurso REST).  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Model404(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'descripcion': 'str',
        'estado': 'int'
    }

    attribute_map = {
        'descripcion': 'descripcion',
        'estado': 'estado'
    }

    def __init__(self, descripcion='Not Found', estado=None):  # noqa: E501
        """Model404 - a model defined in Swagger"""  # noqa: E501

        self._descripcion = None
        self._estado = None
        self.discriminator = None

        self.descripcion = descripcion
        self.estado = estado

    @property
    def descripcion(self):
        """Gets the descripcion of this Model404.  # noqa: E501


        :return: The descripcion of this Model404.  # noqa: E501
        :rtype: str
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        """Sets the descripcion of this Model404.


        :param descripcion: The descripcion of this Model404.  # noqa: E501
        :type: str
        """
        if descripcion is None:
            raise ValueError("Invalid value for `descripcion`, must not be `None`")  # noqa: E501

        self._descripcion = descripcion

    @property
    def estado(self):
        """Gets the estado of this Model404.  # noqa: E501


        :return: The estado of this Model404.  # noqa: E501
        :rtype: int
        """
        return self._estado

    @estado.setter
    def estado(self, estado):
        """Sets the estado of this Model404.


        :param estado: The estado of this Model404.  # noqa: E501
        :type: int
        """
        if estado is None:
            raise ValueError("Invalid value for `estado`, must not be `None`")  # noqa: E501

        self._estado = estado

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Model404, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Model404):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
