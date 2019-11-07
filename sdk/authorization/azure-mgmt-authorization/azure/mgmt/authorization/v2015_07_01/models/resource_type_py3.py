# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceType(Model):
    """Resource Type.

    :param name: The resource type name.
    :type name: str
    :param display_name: The resource type display name.
    :type display_name: str
    :param operations: The resource type operations.
    :type operations:
     list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[ProviderOperation]'},
    }

    def __init__(self, *, name: str=None, display_name: str=None, operations=None, **kwargs) -> None:
        super(ResourceType, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.operations = operations