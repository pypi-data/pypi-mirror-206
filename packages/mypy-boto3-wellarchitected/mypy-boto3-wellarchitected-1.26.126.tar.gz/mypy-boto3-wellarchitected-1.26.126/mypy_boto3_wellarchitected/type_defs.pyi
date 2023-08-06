"""
Type annotations for wellarchitected service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/type_defs/)

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import ChoiceContentTypeDef

    data: ChoiceContentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AdditionalResourceTypeType,
    AnswerReasonType,
    CheckFailureReasonType,
    CheckStatusType,
    ChoiceReasonType,
    ChoiceStatusType,
    DefinitionTypeType,
    DifferenceStatusType,
    DiscoveryIntegrationStatusType,
    ImportLensStatusType,
    LensStatusType,
    LensStatusTypeType,
    LensTypeType,
    NotificationTypeType,
    OrganizationSharingStatusType,
    PermissionTypeType,
    ReportFormatType,
    RiskType,
    ShareInvitationActionType,
    ShareResourceTypeType,
    ShareStatusType,
    TrustedAdvisorIntegrationStatusType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ChoiceContentTypeDef",
    "ChoiceAnswerSummaryTypeDef",
    "ChoiceAnswerTypeDef",
    "AssociateLensesInputRequestTypeDef",
    "BestPracticeTypeDef",
    "CheckDetailTypeDef",
    "CheckSummaryTypeDef",
    "ChoiceImprovementPlanTypeDef",
    "ChoiceUpdateTypeDef",
    "CreateLensShareInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateLensVersionInputRequestTypeDef",
    "CreateMilestoneInputRequestTypeDef",
    "WorkloadDiscoveryConfigTypeDef",
    "CreateWorkloadShareInputRequestTypeDef",
    "DeleteLensInputRequestTypeDef",
    "DeleteLensShareInputRequestTypeDef",
    "DeleteWorkloadInputRequestTypeDef",
    "DeleteWorkloadShareInputRequestTypeDef",
    "DisassociateLensesInputRequestTypeDef",
    "ExportLensInputRequestTypeDef",
    "GetAnswerInputRequestTypeDef",
    "GetConsolidatedReportInputRequestTypeDef",
    "GetLensInputRequestTypeDef",
    "LensTypeDef",
    "GetLensReviewInputRequestTypeDef",
    "GetLensReviewReportInputRequestTypeDef",
    "LensReviewReportTypeDef",
    "GetLensVersionDifferenceInputRequestTypeDef",
    "GetMilestoneInputRequestTypeDef",
    "GetWorkloadInputRequestTypeDef",
    "ImportLensInputRequestTypeDef",
    "LensReviewSummaryTypeDef",
    "PillarReviewSummaryTypeDef",
    "LensShareSummaryTypeDef",
    "LensSummaryTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersInputRequestTypeDef",
    "ListCheckDetailsInputRequestTypeDef",
    "ListCheckSummariesInputRequestTypeDef",
    "ListLensReviewImprovementsInputRequestTypeDef",
    "ListLensReviewsInputRequestTypeDef",
    "ListLensSharesInputRequestTypeDef",
    "ListLensesInputRequestTypeDef",
    "ListMilestonesInputRequestTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "ListShareInvitationsInputRequestTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListWorkloadSharesInputRequestTypeDef",
    "WorkloadShareSummaryTypeDef",
    "ListWorkloadsInputRequestTypeDef",
    "WorkloadSummaryTypeDef",
    "QuestionDifferenceTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateLensReviewInputRequestTypeDef",
    "UpdateShareInvitationInputRequestTypeDef",
    "UpdateWorkloadShareInputRequestTypeDef",
    "WorkloadShareTypeDef",
    "UpgradeLensReviewInputRequestTypeDef",
    "AdditionalResourcesTypeDef",
    "QuestionMetricTypeDef",
    "ImprovementSummaryTypeDef",
    "UpdateAnswerInputRequestTypeDef",
    "CreateLensShareOutputTypeDef",
    "CreateLensVersionOutputTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportLensOutputTypeDef",
    "ImportLensOutputTypeDef",
    "ListCheckDetailsOutputTypeDef",
    "ListCheckSummariesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "CreateWorkloadInputRequestTypeDef",
    "UpdateWorkloadInputRequestTypeDef",
    "WorkloadTypeDef",
    "GetLensOutputTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "ListLensReviewsOutputTypeDef",
    "LensReviewTypeDef",
    "ListLensSharesOutputTypeDef",
    "ListLensesOutputTypeDef",
    "NotificationSummaryTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "ListWorkloadsOutputTypeDef",
    "MilestoneSummaryTypeDef",
    "PillarDifferenceTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "ChoiceTypeDef",
    "PillarMetricTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "GetWorkloadOutputTypeDef",
    "MilestoneTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "GetLensReviewOutputTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListMilestonesOutputTypeDef",
    "VersionDifferencesTypeDef",
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "LensMetricTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "ListAnswersOutputTypeDef",
    "GetAnswerOutputTypeDef",
    "UpdateAnswerOutputTypeDef",
    "ConsolidatedReportMetricTypeDef",
    "GetConsolidatedReportOutputTypeDef",
)

ChoiceContentTypeDef = TypedDict(
    "ChoiceContentTypeDef",
    {
        "DisplayText": str,
        "Url": str,
    },
    total=False,
)

ChoiceAnswerSummaryTypeDef = TypedDict(
    "ChoiceAnswerSummaryTypeDef",
    {
        "ChoiceId": str,
        "Status": ChoiceStatusType,
        "Reason": ChoiceReasonType,
    },
    total=False,
)

ChoiceAnswerTypeDef = TypedDict(
    "ChoiceAnswerTypeDef",
    {
        "ChoiceId": str,
        "Status": ChoiceStatusType,
        "Reason": ChoiceReasonType,
        "Notes": str,
    },
    total=False,
)

AssociateLensesInputRequestTypeDef = TypedDict(
    "AssociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": Sequence[str],
    },
)

BestPracticeTypeDef = TypedDict(
    "BestPracticeTypeDef",
    {
        "ChoiceId": str,
        "ChoiceTitle": str,
    },
    total=False,
)

CheckDetailTypeDef = TypedDict(
    "CheckDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Provider": Literal["TRUSTED_ADVISOR"],
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
        "Status": CheckStatusType,
        "AccountId": str,
        "FlaggedResources": int,
        "Reason": CheckFailureReasonType,
        "UpdatedAt": datetime,
    },
    total=False,
)

CheckSummaryTypeDef = TypedDict(
    "CheckSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Provider": Literal["TRUSTED_ADVISOR"],
        "Description": str,
        "UpdatedAt": datetime,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
        "Status": CheckStatusType,
        "AccountSummary": Dict[CheckStatusType, int],
    },
    total=False,
)

ChoiceImprovementPlanTypeDef = TypedDict(
    "ChoiceImprovementPlanTypeDef",
    {
        "ChoiceId": str,
        "DisplayText": str,
        "ImprovementPlanUrl": str,
    },
    total=False,
)

_RequiredChoiceUpdateTypeDef = TypedDict(
    "_RequiredChoiceUpdateTypeDef",
    {
        "Status": ChoiceStatusType,
    },
)
_OptionalChoiceUpdateTypeDef = TypedDict(
    "_OptionalChoiceUpdateTypeDef",
    {
        "Reason": ChoiceReasonType,
        "Notes": str,
    },
    total=False,
)

class ChoiceUpdateTypeDef(_RequiredChoiceUpdateTypeDef, _OptionalChoiceUpdateTypeDef):
    pass

CreateLensShareInputRequestTypeDef = TypedDict(
    "CreateLensShareInputRequestTypeDef",
    {
        "LensAlias": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

_RequiredCreateLensVersionInputRequestTypeDef = TypedDict(
    "_RequiredCreateLensVersionInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateLensVersionInputRequestTypeDef = TypedDict(
    "_OptionalCreateLensVersionInputRequestTypeDef",
    {
        "IsMajorVersion": bool,
    },
    total=False,
)

class CreateLensVersionInputRequestTypeDef(
    _RequiredCreateLensVersionInputRequestTypeDef, _OptionalCreateLensVersionInputRequestTypeDef
):
    pass

CreateMilestoneInputRequestTypeDef = TypedDict(
    "CreateMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneName": str,
        "ClientRequestToken": str,
    },
)

WorkloadDiscoveryConfigTypeDef = TypedDict(
    "WorkloadDiscoveryConfigTypeDef",
    {
        "TrustedAdvisorIntegrationStatus": TrustedAdvisorIntegrationStatusType,
        "WorkloadResourceDefinition": Sequence[DefinitionTypeType],
    },
    total=False,
)

CreateWorkloadShareInputRequestTypeDef = TypedDict(
    "CreateWorkloadShareInputRequestTypeDef",
    {
        "WorkloadId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ClientRequestToken": str,
    },
)

DeleteLensInputRequestTypeDef = TypedDict(
    "DeleteLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "ClientRequestToken": str,
        "LensStatus": LensStatusTypeType,
    },
)

DeleteLensShareInputRequestTypeDef = TypedDict(
    "DeleteLensShareInputRequestTypeDef",
    {
        "ShareId": str,
        "LensAlias": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadInputRequestTypeDef = TypedDict(
    "DeleteWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadShareInputRequestTypeDef = TypedDict(
    "DeleteWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DisassociateLensesInputRequestTypeDef = TypedDict(
    "DisassociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": Sequence[str],
    },
)

_RequiredExportLensInputRequestTypeDef = TypedDict(
    "_RequiredExportLensInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalExportLensInputRequestTypeDef = TypedDict(
    "_OptionalExportLensInputRequestTypeDef",
    {
        "LensVersion": str,
    },
    total=False,
)

class ExportLensInputRequestTypeDef(
    _RequiredExportLensInputRequestTypeDef, _OptionalExportLensInputRequestTypeDef
):
    pass

_RequiredGetAnswerInputRequestTypeDef = TypedDict(
    "_RequiredGetAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalGetAnswerInputRequestTypeDef = TypedDict(
    "_OptionalGetAnswerInputRequestTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)

class GetAnswerInputRequestTypeDef(
    _RequiredGetAnswerInputRequestTypeDef, _OptionalGetAnswerInputRequestTypeDef
):
    pass

_RequiredGetConsolidatedReportInputRequestTypeDef = TypedDict(
    "_RequiredGetConsolidatedReportInputRequestTypeDef",
    {
        "Format": ReportFormatType,
    },
)
_OptionalGetConsolidatedReportInputRequestTypeDef = TypedDict(
    "_OptionalGetConsolidatedReportInputRequestTypeDef",
    {
        "IncludeSharedResources": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetConsolidatedReportInputRequestTypeDef(
    _RequiredGetConsolidatedReportInputRequestTypeDef,
    _OptionalGetConsolidatedReportInputRequestTypeDef,
):
    pass

_RequiredGetLensInputRequestTypeDef = TypedDict(
    "_RequiredGetLensInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalGetLensInputRequestTypeDef = TypedDict(
    "_OptionalGetLensInputRequestTypeDef",
    {
        "LensVersion": str,
    },
    total=False,
)

class GetLensInputRequestTypeDef(
    _RequiredGetLensInputRequestTypeDef, _OptionalGetLensInputRequestTypeDef
):
    pass

LensTypeDef = TypedDict(
    "LensTypeDef",
    {
        "LensArn": str,
        "LensVersion": str,
        "Name": str,
        "Description": str,
        "Owner": str,
        "ShareInvitationId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredGetLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredGetLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalGetLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalGetLensReviewInputRequestTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)

class GetLensReviewInputRequestTypeDef(
    _RequiredGetLensReviewInputRequestTypeDef, _OptionalGetLensReviewInputRequestTypeDef
):
    pass

_RequiredGetLensReviewReportInputRequestTypeDef = TypedDict(
    "_RequiredGetLensReviewReportInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalGetLensReviewReportInputRequestTypeDef = TypedDict(
    "_OptionalGetLensReviewReportInputRequestTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)

class GetLensReviewReportInputRequestTypeDef(
    _RequiredGetLensReviewReportInputRequestTypeDef, _OptionalGetLensReviewReportInputRequestTypeDef
):
    pass

LensReviewReportTypeDef = TypedDict(
    "LensReviewReportTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "Base64String": str,
    },
    total=False,
)

_RequiredGetLensVersionDifferenceInputRequestTypeDef = TypedDict(
    "_RequiredGetLensVersionDifferenceInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalGetLensVersionDifferenceInputRequestTypeDef = TypedDict(
    "_OptionalGetLensVersionDifferenceInputRequestTypeDef",
    {
        "BaseLensVersion": str,
        "TargetLensVersion": str,
    },
    total=False,
)

class GetLensVersionDifferenceInputRequestTypeDef(
    _RequiredGetLensVersionDifferenceInputRequestTypeDef,
    _OptionalGetLensVersionDifferenceInputRequestTypeDef,
):
    pass

GetMilestoneInputRequestTypeDef = TypedDict(
    "GetMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
    },
)

GetWorkloadInputRequestTypeDef = TypedDict(
    "GetWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)

_RequiredImportLensInputRequestTypeDef = TypedDict(
    "_RequiredImportLensInputRequestTypeDef",
    {
        "JSONString": str,
        "ClientRequestToken": str,
    },
)
_OptionalImportLensInputRequestTypeDef = TypedDict(
    "_OptionalImportLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class ImportLensInputRequestTypeDef(
    _RequiredImportLensInputRequestTypeDef, _OptionalImportLensInputRequestTypeDef
):
    pass

LensReviewSummaryTypeDef = TypedDict(
    "LensReviewSummaryTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "UpdatedAt": datetime,
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

PillarReviewSummaryTypeDef = TypedDict(
    "PillarReviewSummaryTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "Notes": str,
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

LensShareSummaryTypeDef = TypedDict(
    "LensShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "Status": ShareStatusType,
        "StatusMessage": str,
    },
    total=False,
)

LensSummaryTypeDef = TypedDict(
    "LensSummaryTypeDef",
    {
        "LensArn": str,
        "LensAlias": str,
        "LensName": str,
        "LensType": LensTypeType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "LensVersion": str,
        "Owner": str,
        "LensStatus": LensStatusType,
    },
    total=False,
)

LensUpgradeSummaryTypeDef = TypedDict(
    "LensUpgradeSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadName": str,
        "LensAlias": str,
        "LensArn": str,
        "CurrentLensVersion": str,
        "LatestLensVersion": str,
    },
    total=False,
)

_RequiredListAnswersInputRequestTypeDef = TypedDict(
    "_RequiredListAnswersInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalListAnswersInputRequestTypeDef = TypedDict(
    "_OptionalListAnswersInputRequestTypeDef",
    {
        "PillarId": str,
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAnswersInputRequestTypeDef(
    _RequiredListAnswersInputRequestTypeDef, _OptionalListAnswersInputRequestTypeDef
):
    pass

_RequiredListCheckDetailsInputRequestTypeDef = TypedDict(
    "_RequiredListCheckDetailsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
    },
)
_OptionalListCheckDetailsInputRequestTypeDef = TypedDict(
    "_OptionalListCheckDetailsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListCheckDetailsInputRequestTypeDef(
    _RequiredListCheckDetailsInputRequestTypeDef, _OptionalListCheckDetailsInputRequestTypeDef
):
    pass

_RequiredListCheckSummariesInputRequestTypeDef = TypedDict(
    "_RequiredListCheckSummariesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
    },
)
_OptionalListCheckSummariesInputRequestTypeDef = TypedDict(
    "_OptionalListCheckSummariesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListCheckSummariesInputRequestTypeDef(
    _RequiredListCheckSummariesInputRequestTypeDef, _OptionalListCheckSummariesInputRequestTypeDef
):
    pass

_RequiredListLensReviewImprovementsInputRequestTypeDef = TypedDict(
    "_RequiredListLensReviewImprovementsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalListLensReviewImprovementsInputRequestTypeDef = TypedDict(
    "_OptionalListLensReviewImprovementsInputRequestTypeDef",
    {
        "PillarId": str,
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLensReviewImprovementsInputRequestTypeDef(
    _RequiredListLensReviewImprovementsInputRequestTypeDef,
    _OptionalListLensReviewImprovementsInputRequestTypeDef,
):
    pass

_RequiredListLensReviewsInputRequestTypeDef = TypedDict(
    "_RequiredListLensReviewsInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListLensReviewsInputRequestTypeDef = TypedDict(
    "_OptionalListLensReviewsInputRequestTypeDef",
    {
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLensReviewsInputRequestTypeDef(
    _RequiredListLensReviewsInputRequestTypeDef, _OptionalListLensReviewsInputRequestTypeDef
):
    pass

_RequiredListLensSharesInputRequestTypeDef = TypedDict(
    "_RequiredListLensSharesInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalListLensSharesInputRequestTypeDef = TypedDict(
    "_OptionalListLensSharesInputRequestTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": ShareStatusType,
    },
    total=False,
)

class ListLensSharesInputRequestTypeDef(
    _RequiredListLensSharesInputRequestTypeDef, _OptionalListLensSharesInputRequestTypeDef
):
    pass

ListLensesInputRequestTypeDef = TypedDict(
    "ListLensesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LensType": LensTypeType,
        "LensStatus": LensStatusTypeType,
        "LensName": str,
    },
    total=False,
)

_RequiredListMilestonesInputRequestTypeDef = TypedDict(
    "_RequiredListMilestonesInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListMilestonesInputRequestTypeDef = TypedDict(
    "_OptionalListMilestonesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMilestonesInputRequestTypeDef(
    _RequiredListMilestonesInputRequestTypeDef, _OptionalListMilestonesInputRequestTypeDef
):
    pass

ListNotificationsInputRequestTypeDef = TypedDict(
    "ListNotificationsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListShareInvitationsInputRequestTypeDef = TypedDict(
    "ListShareInvitationsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": str,
        "LensNamePrefix": str,
        "ShareResourceType": ShareResourceTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ShareInvitationSummaryTypeDef = TypedDict(
    "ShareInvitationSummaryTypeDef",
    {
        "ShareInvitationId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ShareResourceType": ShareResourceTypeType,
        "WorkloadName": str,
        "WorkloadId": str,
        "LensName": str,
        "LensArn": str,
    },
    total=False,
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
    },
)

_RequiredListWorkloadSharesInputRequestTypeDef = TypedDict(
    "_RequiredListWorkloadSharesInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListWorkloadSharesInputRequestTypeDef = TypedDict(
    "_OptionalListWorkloadSharesInputRequestTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": ShareStatusType,
    },
    total=False,
)

class ListWorkloadSharesInputRequestTypeDef(
    _RequiredListWorkloadSharesInputRequestTypeDef, _OptionalListWorkloadSharesInputRequestTypeDef
):
    pass

WorkloadShareSummaryTypeDef = TypedDict(
    "WorkloadShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "Status": ShareStatusType,
        "StatusMessage": str,
    },
    total=False,
)

ListWorkloadsInputRequestTypeDef = TypedDict(
    "ListWorkloadsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

WorkloadSummaryTypeDef = TypedDict(
    "WorkloadSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "WorkloadName": str,
        "Owner": str,
        "UpdatedAt": datetime,
        "Lenses": List[str],
        "RiskCounts": Dict[RiskType, int],
        "ImprovementStatus": WorkloadImprovementStatusType,
    },
    total=False,
)

QuestionDifferenceTypeDef = TypedDict(
    "QuestionDifferenceTypeDef",
    {
        "QuestionId": str,
        "QuestionTitle": str,
        "DifferenceStatus": DifferenceStatusType,
    },
    total=False,
)

ShareInvitationTypeDef = TypedDict(
    "ShareInvitationTypeDef",
    {
        "ShareInvitationId": str,
        "ShareResourceType": ShareResourceTypeType,
        "WorkloadId": str,
        "LensAlias": str,
        "LensArn": str,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "OrganizationSharingStatus": OrganizationSharingStatusType,
        "DiscoveryIntegrationStatus": DiscoveryIntegrationStatusType,
    },
    total=False,
)

_RequiredUpdateLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredUpdateLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalUpdateLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalUpdateLensReviewInputRequestTypeDef",
    {
        "LensNotes": str,
        "PillarNotes": Mapping[str, str],
    },
    total=False,
)

class UpdateLensReviewInputRequestTypeDef(
    _RequiredUpdateLensReviewInputRequestTypeDef, _OptionalUpdateLensReviewInputRequestTypeDef
):
    pass

UpdateShareInvitationInputRequestTypeDef = TypedDict(
    "UpdateShareInvitationInputRequestTypeDef",
    {
        "ShareInvitationId": str,
        "ShareInvitationAction": ShareInvitationActionType,
    },
)

UpdateWorkloadShareInputRequestTypeDef = TypedDict(
    "UpdateWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "PermissionType": PermissionTypeType,
    },
)

WorkloadShareTypeDef = TypedDict(
    "WorkloadShareTypeDef",
    {
        "ShareId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "Status": ShareStatusType,
        "WorkloadName": str,
        "WorkloadId": str,
    },
    total=False,
)

_RequiredUpgradeLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredUpgradeLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneName": str,
    },
)
_OptionalUpgradeLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalUpgradeLensReviewInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class UpgradeLensReviewInputRequestTypeDef(
    _RequiredUpgradeLensReviewInputRequestTypeDef, _OptionalUpgradeLensReviewInputRequestTypeDef
):
    pass

AdditionalResourcesTypeDef = TypedDict(
    "AdditionalResourcesTypeDef",
    {
        "Type": AdditionalResourceTypeType,
        "Content": List[ChoiceContentTypeDef],
    },
    total=False,
)

QuestionMetricTypeDef = TypedDict(
    "QuestionMetricTypeDef",
    {
        "QuestionId": str,
        "Risk": RiskType,
        "BestPractices": List[BestPracticeTypeDef],
    },
    total=False,
)

ImprovementSummaryTypeDef = TypedDict(
    "ImprovementSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Risk": RiskType,
        "ImprovementPlanUrl": str,
        "ImprovementPlans": List[ChoiceImprovementPlanTypeDef],
    },
    total=False,
)

_RequiredUpdateAnswerInputRequestTypeDef = TypedDict(
    "_RequiredUpdateAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalUpdateAnswerInputRequestTypeDef = TypedDict(
    "_OptionalUpdateAnswerInputRequestTypeDef",
    {
        "SelectedChoices": Sequence[str],
        "ChoiceUpdates": Mapping[str, ChoiceUpdateTypeDef],
        "Notes": str,
        "IsApplicable": bool,
        "Reason": AnswerReasonType,
    },
    total=False,
)

class UpdateAnswerInputRequestTypeDef(
    _RequiredUpdateAnswerInputRequestTypeDef, _OptionalUpdateAnswerInputRequestTypeDef
):
    pass

CreateLensShareOutputTypeDef = TypedDict(
    "CreateLensShareOutputTypeDef",
    {
        "ShareId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLensVersionOutputTypeDef = TypedDict(
    "CreateLensVersionOutputTypeDef",
    {
        "LensArn": str,
        "LensVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMilestoneOutputTypeDef = TypedDict(
    "CreateMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateWorkloadOutputTypeDef = TypedDict(
    "CreateWorkloadOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateWorkloadShareOutputTypeDef = TypedDict(
    "CreateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "ShareId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExportLensOutputTypeDef = TypedDict(
    "ExportLensOutputTypeDef",
    {
        "LensJSON": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ImportLensOutputTypeDef = TypedDict(
    "ImportLensOutputTypeDef",
    {
        "LensArn": str,
        "Status": ImportLensStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCheckDetailsOutputTypeDef = TypedDict(
    "ListCheckDetailsOutputTypeDef",
    {
        "CheckDetails": List[CheckDetailTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCheckSummariesOutputTypeDef = TypedDict(
    "ListCheckSummariesOutputTypeDef",
    {
        "CheckSummaries": List[CheckSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateWorkloadInputRequestTypeDef = TypedDict(
    "_RequiredCreateWorkloadInputRequestTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "Lenses": Sequence[str],
        "ClientRequestToken": str,
    },
)
_OptionalCreateWorkloadInputRequestTypeDef = TypedDict(
    "_OptionalCreateWorkloadInputRequestTypeDef",
    {
        "AccountIds": Sequence[str],
        "AwsRegions": Sequence[str],
        "NonAwsRegions": Sequence[str],
        "PillarPriorities": Sequence[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "Tags": Mapping[str, str],
        "DiscoveryConfig": WorkloadDiscoveryConfigTypeDef,
        "Applications": Sequence[str],
    },
    total=False,
)

class CreateWorkloadInputRequestTypeDef(
    _RequiredCreateWorkloadInputRequestTypeDef, _OptionalCreateWorkloadInputRequestTypeDef
):
    pass

_RequiredUpdateWorkloadInputRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalUpdateWorkloadInputRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkloadInputRequestTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "AccountIds": Sequence[str],
        "AwsRegions": Sequence[str],
        "NonAwsRegions": Sequence[str],
        "PillarPriorities": Sequence[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "IsReviewOwnerUpdateAcknowledged": bool,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "ImprovementStatus": WorkloadImprovementStatusType,
        "DiscoveryConfig": WorkloadDiscoveryConfigTypeDef,
        "Applications": Sequence[str],
    },
    total=False,
)

class UpdateWorkloadInputRequestTypeDef(
    _RequiredUpdateWorkloadInputRequestTypeDef, _OptionalUpdateWorkloadInputRequestTypeDef
):
    pass

WorkloadTypeDef = TypedDict(
    "WorkloadTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "UpdatedAt": datetime,
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "ReviewRestrictionDate": datetime,
        "IsReviewOwnerUpdateAcknowledged": bool,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "ImprovementStatus": WorkloadImprovementStatusType,
        "RiskCounts": Dict[RiskType, int],
        "PillarPriorities": List[str],
        "Lenses": List[str],
        "Owner": str,
        "ShareInvitationId": str,
        "Tags": Dict[str, str],
        "DiscoveryConfig": WorkloadDiscoveryConfigTypeDef,
        "Applications": List[str],
    },
    total=False,
)

GetLensOutputTypeDef = TypedDict(
    "GetLensOutputTypeDef",
    {
        "Lens": LensTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLensReviewReportOutputTypeDef = TypedDict(
    "GetLensReviewReportOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewReport": LensReviewReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLensReviewsOutputTypeDef = TypedDict(
    "ListLensReviewsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewSummaries": List[LensReviewSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LensReviewTypeDef = TypedDict(
    "LensReviewTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "PillarReviewSummaries": List[PillarReviewSummaryTypeDef],
        "UpdatedAt": datetime,
        "Notes": str,
        "RiskCounts": Dict[RiskType, int],
        "NextToken": str,
    },
    total=False,
)

ListLensSharesOutputTypeDef = TypedDict(
    "ListLensSharesOutputTypeDef",
    {
        "LensShareSummaries": List[LensShareSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLensesOutputTypeDef = TypedDict(
    "ListLensesOutputTypeDef",
    {
        "LensSummaries": List[LensSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {
        "Type": NotificationTypeType,
        "LensUpgradeSummary": LensUpgradeSummaryTypeDef,
    },
    total=False,
)

ListShareInvitationsOutputTypeDef = TypedDict(
    "ListShareInvitationsOutputTypeDef",
    {
        "ShareInvitationSummaries": List[ShareInvitationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListWorkloadSharesOutputTypeDef = TypedDict(
    "ListWorkloadSharesOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShareSummaries": List[WorkloadShareSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "WorkloadSummaries": List[WorkloadSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MilestoneSummaryTypeDef = TypedDict(
    "MilestoneSummaryTypeDef",
    {
        "MilestoneNumber": int,
        "MilestoneName": str,
        "RecordedAt": datetime,
        "WorkloadSummary": WorkloadSummaryTypeDef,
    },
    total=False,
)

PillarDifferenceTypeDef = TypedDict(
    "PillarDifferenceTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "DifferenceStatus": DifferenceStatusType,
        "QuestionDifferences": List[QuestionDifferenceTypeDef],
    },
    total=False,
)

UpdateShareInvitationOutputTypeDef = TypedDict(
    "UpdateShareInvitationOutputTypeDef",
    {
        "ShareInvitation": ShareInvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateWorkloadShareOutputTypeDef = TypedDict(
    "UpdateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShare": WorkloadShareTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ChoiceTypeDef = TypedDict(
    "ChoiceTypeDef",
    {
        "ChoiceId": str,
        "Title": str,
        "Description": str,
        "HelpfulResource": ChoiceContentTypeDef,
        "ImprovementPlan": ChoiceContentTypeDef,
        "AdditionalResources": List[AdditionalResourcesTypeDef],
    },
    total=False,
)

PillarMetricTypeDef = TypedDict(
    "PillarMetricTypeDef",
    {
        "PillarId": str,
        "RiskCounts": Dict[RiskType, int],
        "Questions": List[QuestionMetricTypeDef],
    },
    total=False,
)

ListLensReviewImprovementsOutputTypeDef = TypedDict(
    "ListLensReviewImprovementsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "ImprovementSummaries": List[ImprovementSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {
        "Workload": WorkloadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MilestoneTypeDef = TypedDict(
    "MilestoneTypeDef",
    {
        "MilestoneNumber": int,
        "MilestoneName": str,
        "RecordedAt": datetime,
        "Workload": WorkloadTypeDef,
    },
    total=False,
)

UpdateWorkloadOutputTypeDef = TypedDict(
    "UpdateWorkloadOutputTypeDef",
    {
        "Workload": WorkloadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLensReviewOutputTypeDef = TypedDict(
    "GetLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReview": LensReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateLensReviewOutputTypeDef = TypedDict(
    "UpdateLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "LensReview": LensReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List[NotificationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMilestonesOutputTypeDef = TypedDict(
    "ListMilestonesOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneSummaries": List[MilestoneSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

VersionDifferencesTypeDef = TypedDict(
    "VersionDifferencesTypeDef",
    {
        "PillarDifferences": List[PillarDifferenceTypeDef],
    },
    total=False,
)

AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Choices": List[ChoiceTypeDef],
        "SelectedChoices": List[str],
        "ChoiceAnswerSummaries": List[ChoiceAnswerSummaryTypeDef],
        "IsApplicable": bool,
        "Risk": RiskType,
        "Reason": AnswerReasonType,
    },
    total=False,
)

AnswerTypeDef = TypedDict(
    "AnswerTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "QuestionDescription": str,
        "ImprovementPlanUrl": str,
        "HelpfulResourceUrl": str,
        "HelpfulResourceDisplayText": str,
        "Choices": List[ChoiceTypeDef],
        "SelectedChoices": List[str],
        "ChoiceAnswers": List[ChoiceAnswerTypeDef],
        "IsApplicable": bool,
        "Risk": RiskType,
        "Notes": str,
        "Reason": AnswerReasonType,
    },
    total=False,
)

LensMetricTypeDef = TypedDict(
    "LensMetricTypeDef",
    {
        "LensArn": str,
        "Pillars": List[PillarMetricTypeDef],
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

GetMilestoneOutputTypeDef = TypedDict(
    "GetMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "Milestone": MilestoneTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLensVersionDifferenceOutputTypeDef = TypedDict(
    "GetLensVersionDifferenceOutputTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "BaseLensVersion": str,
        "TargetLensVersion": str,
        "LatestLensVersion": str,
        "VersionDifferences": VersionDifferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAnswersOutputTypeDef = TypedDict(
    "ListAnswersOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "AnswerSummaries": List[AnswerSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAnswerOutputTypeDef = TypedDict(
    "GetAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "Answer": AnswerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAnswerOutputTypeDef = TypedDict(
    "UpdateAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "LensArn": str,
        "Answer": AnswerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConsolidatedReportMetricTypeDef = TypedDict(
    "ConsolidatedReportMetricTypeDef",
    {
        "MetricType": Literal["WORKLOAD"],
        "RiskCounts": Dict[RiskType, int],
        "WorkloadId": str,
        "WorkloadName": str,
        "WorkloadArn": str,
        "UpdatedAt": datetime,
        "Lenses": List[LensMetricTypeDef],
        "LensesAppliedCount": int,
    },
    total=False,
)

GetConsolidatedReportOutputTypeDef = TypedDict(
    "GetConsolidatedReportOutputTypeDef",
    {
        "Metrics": List[ConsolidatedReportMetricTypeDef],
        "NextToken": str,
        "Base64String": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
