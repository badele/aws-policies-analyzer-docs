# Service: securityhub

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/SecurityAudit` | [SecurityAudit](../policies.md#securityaudit) |
| `arn:aws:iam::aws:policy/aws-service-role/AmazonSSMServiceRolePolicy` | [AmazonSSMServiceRolePolicy](../policies.md#amazonssmservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy` | [AWSConfigServiceRolePolicy](../policies.md#awsconfigservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSecurityHubServiceRolePolicy` | [AWSSecurityHubServiceRolePolicy](../policies.md#awssecurityhubservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSSecurityHubFullAccess` | [AWSSecurityHubFullAccess](../policies.md#awssecurityhubfullaccess) |
| `arn:aws:iam::aws:policy/AWSSecurityHubReadOnlyAccess` | [AWSSecurityHubReadOnlyAccess](../policies.md#awssecurityhubreadonlyaccess) |
| `arn:aws:iam::aws:policy/service-role/AWS_ConfigRole` | [AWS_ConfigRole](../policies.md#aws_configrole) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSAuditManagerServiceRolePolicy` | [AWSAuditManagerServiceRolePolicy](../policies.md#awsauditmanagerservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSystemsManagerOpsDataSyncServiceRolePolicy` | [AWSSystemsManagerOpsDataSyncServiceRolePolicy](../policies.md#awssystemsmanageropsdatasyncservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSControlTowerAccountServiceRolePolicy` | [AWSControlTowerAccountServiceRolePolicy](../policies.md#awscontroltoweraccountservicerolepolicy) |
| `arn:aws:iam::aws:policy/ResourceGroupsTaggingAPITagUntagSupportedResources` | [ResourceGroupsTaggingAPITagUntagSupportedResources](../policies.md#resourcegroupstaggingapitaguntagsupportedresources) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSecurityIncidentResponseTriageServiceRolePolicy` | [AWSSecurityIncidentResponseTriageServiceRolePolicy](../policies.md#awssecurityincidentresponsetriageservicerolepolicy) |
| `arn:aws:iam::aws:policy/AIOpsAssistantPolicy` | [AIOpsAssistantPolicy](../policies.md#aiopsassistantpolicy) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [securityhub:*](../actions.md#securityhub:all) | securityhub |
| [securityhub:BatchDisableStandards](../actions.md#securityhub:batchdisablestandards) | securityhub |
| [securityhub:BatchEnableStandards](../actions.md#securityhub:batchenablestandards) | securityhub |
| [securityhub:BatchGet*](../actions.md#securityhub:batchgetall) | securityhub |
| [securityhub:BatchGetAutomationRules](../actions.md#securityhub:batchgetautomationrules) | securityhub |
| [securityhub:BatchGetConfigurationPolicyAssociations](../actions.md#securityhub:batchgetconfigurationpolicyassociations) | securityhub |
| [securityhub:BatchGetControlEvaluations](../actions.md#securityhub:batchgetcontrolevaluations) | securityhub |
| [securityhub:BatchGetSecurityControls](../actions.md#securityhub:batchgetsecuritycontrols) | securityhub |
| [securityhub:BatchGetStandardsControlAssociations](../actions.md#securityhub:batchgetstandardscontrolassociations) | securityhub |
| [securityhub:BatchUpdateFindings](../actions.md#securityhub:batchupdatefindings) | securityhub |
| [securityhub:BatchUpdateStandardsControlAssociations](../actions.md#securityhub:batchupdatestandardscontrolassociations) | securityhub |
| [securityhub:CreateMembers](../actions.md#securityhub:createmembers) | securityhub |
| [securityhub:DeleteMembers](../actions.md#securityhub:deletemembers) | securityhub |
| [securityhub:Describe*](../actions.md#securityhub:describeall) | securityhub |
| [securityhub:DescribeHub](../actions.md#securityhub:describehub) | securityhub |
| [securityhub:DescribeOrganizationConfiguration](../actions.md#securityhub:describeorganizationconfiguration) | securityhub |
| [securityhub:DescribeStandards](../actions.md#securityhub:describestandards) | securityhub |
| [securityhub:DescribeStandardsControls](../actions.md#securityhub:describestandardscontrols) | securityhub |
| [securityhub:DisableSecurityHub](../actions.md#securityhub:disablesecurityhub) | securityhub |
| [securityhub:DisassociateFromAdministratorAccount](../actions.md#securityhub:disassociatefromadministratoraccount) | securityhub |
| [securityhub:DisassociateMembers](../actions.md#securityhub:disassociatemembers) | securityhub |
| [securityhub:EnableSecurityHub](../actions.md#securityhub:enablesecurityhub) | securityhub |
| [securityhub:Get*](../actions.md#securityhub:getall) | securityhub |
| [securityhub:GetConfigurationPolicy](../actions.md#securityhub:getconfigurationpolicy) | securityhub |
| [securityhub:GetConfigurationPolicyAssociation](../actions.md#securityhub:getconfigurationpolicyassociation) | securityhub |
| [securityhub:GetEnabledStandards](../actions.md#securityhub:getenabledstandards) | securityhub |
| [securityhub:GetFindingAggregator](../actions.md#securityhub:getfindingaggregator) | securityhub |
| [securityhub:GetFindings](../actions.md#securityhub:getfindings) | securityhub |
| [securityhub:GetInsights](../actions.md#securityhub:getinsights) | securityhub |
| [securityhub:List*](../actions.md#securityhub:listall) | securityhub |
| [securityhub:ListEnabledProductsForImport](../actions.md#securityhub:listenabledproductsforimport) | securityhub |
| [securityhub:ListSecurityControlDefinitions](../actions.md#securityhub:listsecuritycontroldefinitions) | securityhub |
| [securityhub:ListStandardsControlAssociations](../actions.md#securityhub:liststandardscontrolassociations) | securityhub |
| [securityhub:TagResource](../actions.md#securityhub:tagresource) | securityhub |
| [securityhub:UntagResource](../actions.md#securityhub:untagresource) | securityhub |
| [securityhub:UpdateFindings](../actions.md#securityhub:updatefindings) | securityhub |
| [securityhub:UpdateOrganizationConfiguration](../actions.md#securityhub:updateorganizationconfiguration) | securityhub |
| [securityhub:UpdateSecurityControl](../actions.md#securityhub:updatesecuritycontrol) | securityhub |
| [securityhub:UpdateSecurityHubConfiguration](../actions.md#securityhub:updatesecurityhubconfiguration) | securityhub |
| [securityhub:UpdateStandardsControl](../actions.md#securityhub:updatestandardscontrol) | securityhub |
| [securityhub:batchGetConfigurationPolicyAssociations](../actions.md#securityhub:batchgetconfigurationpolicyassociations) | securityhub |
| [securityhub:describeOrganizationConfiguration](../actions.md#securityhub:describeorganizationconfiguration) | securityhub |
| [securityhub:getConfigurationPolicy](../actions.md#securityhub:getconfigurationpolicy) | securityhub |
| [securityhub:getConfigurationPolicyAssociation](../actions.md#securityhub:getconfigurationpolicyassociation) | securityhub |
| [securityhub:getEnabledStandards](../actions.md#securityhub:getenabledstandards) | securityhub |
| [securityhub:getFindingAggregator](../actions.md#securityhub:getfindingaggregator) | securityhub |
| [securityhub:getFindings](../actions.md#securityhub:getfindings) | securityhub |
| [securityhub:getInsightResults](../actions.md#securityhub:getinsightresults) | securityhub |
| [securityhub:getInsights](../actions.md#securityhub:getinsights) | securityhub |
| [securityhub:getMasterAccount](../actions.md#securityhub:getmasteraccount) | securityhub |
| [securityhub:getMembers](../actions.md#securityhub:getmembers) | securityhub |
| [securityhub:listConfigurationPolicies](../actions.md#securityhub:listconfigurationpolicies) | securityhub |
| [securityhub:listConfigurationPolicyAssociations](../actions.md#securityhub:listconfigurationpolicyassociations) | securityhub |
| [securityhub:listEnabledProductsForImport](../actions.md#securityhub:listenabledproductsforimport) | securityhub |
| [securityhub:listFindingAggregators](../actions.md#securityhub:listfindingaggregators) | securityhub |
| [securityhub:listInvitations](../actions.md#securityhub:listinvitations) | securityhub |
| [securityhub:listMembers](../actions.md#securityhub:listmembers) | securityhub |