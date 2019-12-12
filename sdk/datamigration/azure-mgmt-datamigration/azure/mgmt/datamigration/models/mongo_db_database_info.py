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

from .mongo_db_object_info import MongoDbObjectInfo


class MongoDbDatabaseInfo(MongoDbObjectInfo):
    """Describes a database within a MongoDB data source.

    All required parameters must be populated in order to send to Azure.

    :param average_document_size: Required. The average document size, or -1
     if the average size is unknown
    :type average_document_size: long
    :param data_size: Required. The estimated total data size, in bytes, or -1
     if the size is unknown.
    :type data_size: long
    :param document_count: Required. The estimated total number of documents,
     or -1 if the document count is unknown
    :type document_count: long
    :param name: Required. The unqualified name of the database or collection
    :type name: str
    :param qualified_name: Required. The qualified name of the database or
     collection. For a collection, this is the database-qualified name.
    :type qualified_name: str
    :param collections: Required. A list of supported collections in a MongoDB
     database
    :type collections:
     list[~azure.mgmt.datamigration.models.MongoDbCollectionInfo]
    :param supports_sharding: Required. Whether the database has sharding
     enabled. Note that the migration task will enable sharding on the target
     if necessary.
    :type supports_sharding: bool
    """

    _validation = {
        'average_document_size': {'required': True},
        'data_size': {'required': True},
        'document_count': {'required': True},
        'name': {'required': True},
        'qualified_name': {'required': True},
        'collections': {'required': True},
        'supports_sharding': {'required': True},
    }

    _attribute_map = {
        'average_document_size': {'key': 'averageDocumentSize', 'type': 'long'},
        'data_size': {'key': 'dataSize', 'type': 'long'},
        'document_count': {'key': 'documentCount', 'type': 'long'},
        'name': {'key': 'name', 'type': 'str'},
        'qualified_name': {'key': 'qualifiedName', 'type': 'str'},
        'collections': {'key': 'collections', 'type': '[MongoDbCollectionInfo]'},
        'supports_sharding': {'key': 'supportsSharding', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(MongoDbDatabaseInfo, self).__init__(**kwargs)
        self.collections = kwargs.get('collections', None)
        self.supports_sharding = kwargs.get('supports_sharding', None)