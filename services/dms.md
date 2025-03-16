# Service: dms

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/SecurityAudit` | [SecurityAudit](../policies.md#securityaudit) |
| `arn:aws:iam::aws:policy/job-function/ViewOnlyAccess` | [ViewOnlyAccess](../policies.md#viewonlyaccess) |
| `arn:aws:iam::aws:policy/job-function/SupportUser` | [SupportUser](../policies.md#supportuser) |
| `arn:aws:iam::aws:policy/service-role/AWSMigrationHubDiscoveryAccess` | [AWSMigrationHubDiscoveryAccess](../policies.md#awsmigrationhubdiscoveryaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy` | [AWSConfigServiceRolePolicy](../policies.md#awsconfigservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/MigrationHubServiceRolePolicy` | [MigrationHubServiceRolePolicy](../policies.md#migrationhubservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWS_ConfigRole` | [AWS_ConfigRole](../policies.md#aws_configrole) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy` | [AWSResourceExplorerServiceRolePolicy](../policies.md#awsresourceexplorerservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSDMSServerlessServiceRolePolicy` | [AWSDMSServerlessServiceRolePolicy](../policies.md#awsdmsserverlessservicerolepolicy) |
| `arn:aws:iam::aws:policy/ResourceGroupsTaggingAPITagUntagSupportedResources` | [ResourceGroupsTaggingAPITagUntagSupportedResources](../policies.md#resourcegroupstaggingapitaguntagsupportedresources) |
| `arn:aws:iam::aws:policy/AWSPartnerLedSupportReadOnlyAccess` | [AWSPartnerLedSupportReadOnlyAccess](../policies.md#awspartnerledsupportreadonlyaccess) |
| `arn:aws:iam::aws:policy/AIOpsAssistantPolicy` | [AIOpsAssistantPolicy](../policies.md#aiopsassistantpolicy) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [dms:AddTagsToResource](../actions.md#dms:addtagstoresource) | dms |
| [dms:CreateReplicationInstance](../actions.md#dms:createreplicationinstance) | dms |
| [dms:CreateReplicationTask](../actions.md#dms:createreplicationtask) | dms |
| [dms:DeleteConnection](../actions.md#dms:deleteconnection) | dms |
| [dms:DeleteReplicationInstance](../actions.md#dms:deletereplicationinstance) | dms |
| [dms:DeleteReplicationTask](../actions.md#dms:deletereplicationtask) | dms |
| [dms:Describe*](../actions.md#dms:describeall) | dms |
| [dms:DescribeCertificates](../actions.md#dms:describecertificates) | dms |
| [dms:DescribeEndpoints](../actions.md#dms:describeendpoints) | dms |
| [dms:DescribeEventSubscriptions](../actions.md#dms:describeeventsubscriptions) | dms |
| [dms:DescribeReplicationInstances](../actions.md#dms:describereplicationinstances) | dms |
| [dms:DescribeReplicationSubnetGroups](../actions.md#dms:describereplicationsubnetgroups) | dms |
| [dms:DescribeReplicationTaskAssessmentRuns](../actions.md#dms:describereplicationtaskassessmentruns) | dms |
| [dms:DescribeReplicationTasks](../actions.md#dms:describereplicationtasks) | dms |
| [dms:List*](../actions.md#dms:listall) | dms |
| [dms:ListTagsForResource](../actions.md#dms:listtagsforresource) | dms |
| [dms:ModifyReplicationInstance](../actions.md#dms:modifyreplicationinstance) | dms |
| [dms:ModifyReplicationTask](../actions.md#dms:modifyreplicationtask) | dms |
| [dms:RemoveTagsFromResource](../actions.md#dms:removetagsfromresource) | dms |
| [dms:StartReplicationTask](../actions.md#dms:startreplicationtask) | dms |
| [dms:StartReplicationTaskAssessmentRun](../actions.md#dms:startreplicationtaskassessmentrun) | dms |
| [dms:StopReplicationTask](../actions.md#dms:stopreplicationtask) | dms |
| [dms:Test*](../actions.md#dms:testall) | dms |
| [dms:TestConnection](../actions.md#dms:testconnection) | dms |
| [dms:describeAccountAttributes](../actions.md#dms:describeaccountattributes) | dms |
| [dms:describeApplicableIndividualAssessments](../actions.md#dms:describeapplicableindividualassessments) | dms |
| [dms:describeConnections](../actions.md#dms:describeconnections) | dms |
| [dms:describeEndpointSettings](../actions.md#dms:describeendpointsettings) | dms |
| [dms:describeEndpointTypes](../actions.md#dms:describeendpointtypes) | dms |
| [dms:describeEndpoints](../actions.md#dms:describeendpoints) | dms |
| [dms:describeEventCategories](../actions.md#dms:describeeventcategories) | dms |
| [dms:describeEventSubscriptions](../actions.md#dms:describeeventsubscriptions) | dms |
| [dms:describeEvents](../actions.md#dms:describeevents) | dms |
| [dms:describeFleetAdvisorCollectors](../actions.md#dms:describefleetadvisorcollectors) | dms |
| [dms:describeFleetAdvisorDatabases](../actions.md#dms:describefleetadvisordatabases) | dms |
| [dms:describeFleetAdvisorLsaAnalysis](../actions.md#dms:describefleetadvisorlsaanalysis) | dms |
| [dms:describeFleetAdvisorSchemaObjectSummary](../actions.md#dms:describefleetadvisorschemaobjectsummary) | dms |
| [dms:describeFleetAdvisorSchemas](../actions.md#dms:describefleetadvisorschemas) | dms |
| [dms:describeOrderableReplicationInstances](../actions.md#dms:describeorderablereplicationinstances) | dms |
| [dms:describePendingMaintenanceActions](../actions.md#dms:describependingmaintenanceactions) | dms |
| [dms:describeRefreshSchemasStatus](../actions.md#dms:describerefreshschemasstatus) | dms |
| [dms:describeReplicationInstanceTaskLogs](../actions.md#dms:describereplicationinstancetasklogs) | dms |
| [dms:describeReplicationInstances](../actions.md#dms:describereplicationinstances) | dms |
| [dms:describeReplicationSubnetGroups](../actions.md#dms:describereplicationsubnetgroups) | dms |
| [dms:describeReplicationTaskAssessmentResults](../actions.md#dms:describereplicationtaskassessmentresults) | dms |
| [dms:describeReplicationTaskAssessmentRuns](../actions.md#dms:describereplicationtaskassessmentruns) | dms |
| [dms:describeReplicationTaskIndividualAssessments](../actions.md#dms:describereplicationtaskindividualassessments) | dms |
| [dms:describeReplicationTasks](../actions.md#dms:describereplicationtasks) | dms |
| [dms:describeSchemas](../actions.md#dms:describeschemas) | dms |
| [dms:describeTableStatistics](../actions.md#dms:describetablestatistics) | dms |