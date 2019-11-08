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

try:
    from ._models_py3 import ARMErrorResponseBody
    from ._models_py3 import ConfigData
    from ._models_py3 import ConfigDataProperties
    from ._models_py3 import MetadataEntity
    from ._models_py3 import MetadataSupportedValueDetail
    from ._models_py3 import OperationDisplayInfo
    from ._models_py3 import OperationEntity
    from ._models_py3 import Resource
    from ._models_py3 import ResourceRecommendationBase
    from ._models_py3 import ShortDescription
    from ._models_py3 import SuppressionContract
except (SyntaxError, ImportError):
    from ._models import ARMErrorResponseBody
    from ._models import ConfigData
    from ._models import ConfigDataProperties
    from ._models import MetadataEntity
    from ._models import MetadataSupportedValueDetail
    from ._models import OperationDisplayInfo
    from ._models import OperationEntity
    from ._models import Resource
    from ._models import ResourceRecommendationBase
    from ._models import ShortDescription
    from ._models import SuppressionContract
from ._paged_models import ConfigDataPaged
from ._paged_models import MetadataEntityPaged
from ._paged_models import OperationEntityPaged
from ._paged_models import ResourceRecommendationBasePaged
from ._paged_models import SuppressionContractPaged
from ._advisor_management_client_enums import (
    Scenario,
    Category,
    Impact,
    Risk,
)

__all__ = [
    'ARMErrorResponseBody',
    'ConfigData',
    'ConfigDataProperties',
    'MetadataEntity',
    'MetadataSupportedValueDetail',
    'OperationDisplayInfo',
    'OperationEntity',
    'Resource',
    'ResourceRecommendationBase',
    'ShortDescription',
    'SuppressionContract',
    'MetadataEntityPaged',
    'ConfigDataPaged',
    'ResourceRecommendationBasePaged',
    'OperationEntityPaged',
    'SuppressionContractPaged',
    'Scenario',
    'Category',
    'Impact',
    'Risk',
]