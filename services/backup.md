# Service: backup

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/SecurityAudit` | [SecurityAudit](../policies.md#securityaudit) |
| `arn:aws:iam::aws:policy/job-function/ViewOnlyAccess` | [ViewOnlyAccess](../policies.md#viewonlyaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy` | [AWSConfigServiceRolePolicy](../policies.md#awsconfigservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup` | [AWSBackupServiceRolePolicyForBackup](../policies.md#awsbackupservicerolepolicyforbackup) |
| `arn:aws:iam::aws:policy/aws-service-role/AmazonElasticFileSystemServiceRolePolicy` | [AmazonElasticFileSystemServiceRolePolicy](../policies.md#amazonelasticfilesystemservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSBackupFullAccess` | [AWSBackupFullAccess](../policies.md#awsbackupfullaccess) |
| `arn:aws:iam::aws:policy/AWSBackupOperatorAccess` | [AWSBackupOperatorAccess](../policies.md#awsbackupoperatoraccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSBackupServiceLinkedRolePolicyForBackup` | [AWSBackupServiceLinkedRolePolicyForBackup](../policies.md#awsbackupservicelinkedrolepolicyforbackup) |
| `arn:aws:iam::aws:policy/service-role/AWS_ConfigRole` | [AWS_ConfigRole](../policies.md#aws_configrole) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSAuditManagerServiceRolePolicy` | [AWSAuditManagerServiceRolePolicy](../policies.md#awsauditmanagerservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports` | [AWSServiceRolePolicyForBackupReports](../policies.md#awsservicerolepolicyforbackupreports) |
| `arn:aws:iam::aws:policy/AWSBackupAuditAccess` | [AWSBackupAuditAccess](../policies.md#awsbackupauditaccess) |
| `arn:aws:iam::aws:policy/AWSBackupServiceRolePolicyForS3Backup` | [AWSBackupServiceRolePolicyForS3Backup](../policies.md#awsbackupservicerolepolicyfors3backup) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy` | [AWSResourceExplorerServiceRolePolicy](../policies.md#awsresourceexplorerservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSBackupRestoreAccessForSAPHANA` | [AWSBackupRestoreAccessForSAPHANA](../policies.md#awsbackuprestoreaccessforsaphana) |
| `arn:aws:iam::aws:policy/AWSResilienceHubAsssessmentExecutionPolicy` | [AWSResilienceHubAsssessmentExecutionPolicy](../policies.md#awsresiliencehubasssessmentexecutionpolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupRestoreTesting` | [AWSServiceRolePolicyForBackupRestoreTesting](../policies.md#awsservicerolepolicyforbackuprestoretesting) |
| `arn:aws:iam::aws:policy/ResourceGroupsTaggingAPITagUntagSupportedResources` | [ResourceGroupsTaggingAPITagUntagSupportedResources](../policies.md#resourcegroupstaggingapitaguntagsupportedresources) |
| `arn:aws:iam::aws:policy/AWSPartnerLedSupportReadOnlyAccess` | [AWSPartnerLedSupportReadOnlyAccess](../policies.md#awspartnerledsupportreadonlyaccess) |
| `arn:aws:iam::aws:policy/AIOpsAssistantPolicy` | [AIOpsAssistantPolicy](../policies.md#aiopsassistantpolicy) |
| `arn:aws:iam::aws:policy/AWSBackupSearchOperatorAccess` | [AWSBackupSearchOperatorAccess](../policies.md#awsbackupsearchoperatoraccess) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [backup:*](../actions.md#backup:all) | backup |
| [backup:CopyFromBackupVault](../actions.md#backup:copyfrombackupvault) | backup |
| [backup:CopyIntoBackupVault](../actions.md#backup:copyintobackupvault) | backup |
| [backup:CreateBackupPlan](../actions.md#backup:createbackupplan) | backup |
| [backup:CreateBackupSelection](../actions.md#backup:createbackupselection) | backup |
| [backup:CreateBackupVault](../actions.md#backup:createbackupvault) | backup |
| [backup:CreateFramework](../actions.md#backup:createframework) | backup |
| [backup:CreateReportPlan](../actions.md#backup:createreportplan) | backup |
| [backup:DeleteBackupSelection](../actions.md#backup:deletebackupselection) | backup |
| [backup:DeleteFramework](../actions.md#backup:deleteframework) | backup |
| [backup:DeleteReportPlan](../actions.md#backup:deletereportplan) | backup |
| [backup:Describe*](../actions.md#backup:describeall) | backup |
| [backup:DescribeBackupJob](../actions.md#backup:describebackupjob) | backup |
| [backup:DescribeBackupVault](../actions.md#backup:describebackupvault) | backup |
| [backup:DescribeCopyJob](../actions.md#backup:describecopyjob) | backup |
| [backup:DescribeFramework](../actions.md#backup:describeframework) | backup |
| [backup:DescribeGlobalSettings](../actions.md#backup:describeglobalsettings) | backup |
| [backup:DescribeProtectedResource](../actions.md#backup:describeprotectedresource) | backup |
| [backup:DescribeRecoveryPoint](../actions.md#backup:describerecoverypoint) | backup |
| [backup:DescribeRegionSettings](../actions.md#backup:describeregionsettings) | backup |
| [backup:DescribeReportJob](../actions.md#backup:describereportjob) | backup |
| [backup:DescribeReportPlan](../actions.md#backup:describereportplan) | backup |
| [backup:DescribeRestoreJob](../actions.md#backup:describerestorejob) | backup |
| [backup:Get*](../actions.md#backup:getall) | backup |
| [backup:GetBackupPlan](../actions.md#backup:getbackupplan) | backup |
| [backup:GetBackupSelection](../actions.md#backup:getbackupselection) | backup |
| [backup:GetBackupVaultAccessPolicy](../actions.md#backup:getbackupvaultaccesspolicy) | backup |
| [backup:GetBackupVaultNotifications](../actions.md#backup:getbackupvaultnotifications) | backup |
| [backup:GetRecoveryPointRestoreMetadata](../actions.md#backup:getrecoverypointrestoremetadata) | backup |
| [backup:GetRestoreTestingPlan](../actions.md#backup:getrestoretestingplan) | backup |
| [backup:GetRestoreTestingSelection](../actions.md#backup:getrestoretestingselection) | backup |
| [backup:GetSupportedResourceTypes](../actions.md#backup:getsupportedresourcetypes) | backup |
| [backup:List*](../actions.md#backup:listall) | backup |
| [backup:ListBackupJobs](../actions.md#backup:listbackupjobs) | backup |
| [backup:ListBackupPlanTemplates](../actions.md#backup:listbackupplantemplates) | backup |
| [backup:ListBackupPlanVersions](../actions.md#backup:listbackupplanversions) | backup |
| [backup:ListBackupPlans](../actions.md#backup:listbackupplans) | backup |
| [backup:ListBackupSelections](../actions.md#backup:listbackupselections) | backup |
| [backup:ListBackupVaults](../actions.md#backup:listbackupvaults) | backup |
| [backup:ListCopyJobs](../actions.md#backup:listcopyjobs) | backup |
| [backup:ListFrameworks](../actions.md#backup:listframeworks) | backup |
| [backup:ListIndexedRecoveryPointsForSearch](../actions.md#backup:listindexedrecoverypointsforsearch) | backup |
| [backup:ListLegalHolds](../actions.md#backup:listlegalholds) | backup |
| [backup:ListProtectedResources](../actions.md#backup:listprotectedresources) | backup |
| [backup:ListProtectedResourcesByBackupVault](../actions.md#backup:listprotectedresourcesbybackupvault) | backup |
| [backup:ListRecoveryPointsByBackupVault](../actions.md#backup:listrecoverypointsbybackupvault) | backup |
| [backup:ListRecoveryPointsByLegalHold](../actions.md#backup:listrecoverypointsbylegalhold) | backup |
| [backup:ListRecoveryPointsByResource](../actions.md#backup:listrecoverypointsbyresource) | backup |
| [backup:ListReportJobs](../actions.md#backup:listreportjobs) | backup |
| [backup:ListReportPlans](../actions.md#backup:listreportplans) | backup |
| [backup:ListRestoreJobs](../actions.md#backup:listrestorejobs) | backup |
| [backup:ListRestoreTestingPlans](../actions.md#backup:listrestoretestingplans) | backup |
| [backup:ListRestoreTestingSelections](../actions.md#backup:listrestoretestingselections) | backup |
| [backup:ListTags](../actions.md#backup:listtags) | backup |
| [backup:PutBackupVaultAccessPolicy](../actions.md#backup:putbackupvaultaccesspolicy) | backup |
| [backup:SearchRecoveryPoint](../actions.md#backup:searchrecoverypoint) | backup |
| [backup:StartBackupJob](../actions.md#backup:startbackupjob) | backup |
| [backup:StartCopyJob](../actions.md#backup:startcopyjob) | backup |
| [backup:StartReportJob](../actions.md#backup:startreportjob) | backup |
| [backup:StartRestoreJob](../actions.md#backup:startrestorejob) | backup |
| [backup:TagResource](../actions.md#backup:tagresource) | backup |
| [backup:UntagResource](../actions.md#backup:untagresource) | backup |
| [backup:UpdateFramework](../actions.md#backup:updateframework) | backup |
| [backup:UpdateReportPlan](../actions.md#backup:updatereportplan) | backup |
| [backup:describeBackupJob](../actions.md#backup:describebackupjob) | backup |
| [backup:describeBackupVault](../actions.md#backup:describebackupvault) | backup |
| [backup:describeCopyJob](../actions.md#backup:describecopyjob) | backup |
| [backup:describeFramework](../actions.md#backup:describeframework) | backup |
| [backup:describeGlobalSettings](../actions.md#backup:describeglobalsettings) | backup |
| [backup:describeProtectedResource](../actions.md#backup:describeprotectedresource) | backup |
| [backup:describeRecoveryPoint](../actions.md#backup:describerecoverypoint) | backup |
| [backup:describeRegionSettings](../actions.md#backup:describeregionsettings) | backup |
| [backup:describeReportJob](../actions.md#backup:describereportjob) | backup |
| [backup:describeReportPlan](../actions.md#backup:describereportplan) | backup |
| [backup:describeRestoreJob](../actions.md#backup:describerestorejob) | backup |
| [backup:getBackupPlan](../actions.md#backup:getbackupplan) | backup |
| [backup:getBackupPlanFromJSON](../actions.md#backup:getbackupplanfromjson) | backup |
| [backup:getBackupPlanFromTemplate](../actions.md#backup:getbackupplanfromtemplate) | backup |
| [backup:getBackupSelection](../actions.md#backup:getbackupselection) | backup |
| [backup:getBackupVaultAccessPolicy](../actions.md#backup:getbackupvaultaccesspolicy) | backup |
| [backup:getBackupVaultNotifications](../actions.md#backup:getbackupvaultnotifications) | backup |
| [backup:getLegalHold](../actions.md#backup:getlegalhold) | backup |
| [backup:getRecoveryPointRestoreMetadata](../actions.md#backup:getrecoverypointrestoremetadata) | backup |
| [backup:getRestoreJobMetadata](../actions.md#backup:getrestorejobmetadata) | backup |
| [backup:getRestoreTestingInferredMetadata](../actions.md#backup:getrestoretestinginferredmetadata) | backup |
| [backup:getRestoreTestingPlan](../actions.md#backup:getrestoretestingplan) | backup |
| [backup:getRestoreTestingSelection](../actions.md#backup:getrestoretestingselection) | backup |
| [backup:getSupportedResourceTypes](../actions.md#backup:getsupportedresourcetypes) | backup |
| [backup:listBackupJobs](../actions.md#backup:listbackupjobs) | backup |
| [backup:listBackupPlanTemplates](../actions.md#backup:listbackupplantemplates) | backup |
| [backup:listBackupPlanVersions](../actions.md#backup:listbackupplanversions) | backup |
| [backup:listBackupPlans](../actions.md#backup:listbackupplans) | backup |
| [backup:listBackupSelections](../actions.md#backup:listbackupselections) | backup |
| [backup:listBackupVaults](../actions.md#backup:listbackupvaults) | backup |
| [backup:listCopyJobs](../actions.md#backup:listcopyjobs) | backup |
| [backup:listFrameworks](../actions.md#backup:listframeworks) | backup |
| [backup:listLegalHolds](../actions.md#backup:listlegalholds) | backup |
| [backup:listProtectedResources](../actions.md#backup:listprotectedresources) | backup |
| [backup:listRecoveryPointsByBackupVault](../actions.md#backup:listrecoverypointsbybackupvault) | backup |
| [backup:listRecoveryPointsByLegalHold](../actions.md#backup:listrecoverypointsbylegalhold) | backup |
| [backup:listRecoveryPointsByResource](../actions.md#backup:listrecoverypointsbyresource) | backup |
| [backup:listReportJobs](../actions.md#backup:listreportjobs) | backup |
| [backup:listReportPlans](../actions.md#backup:listreportplans) | backup |
| [backup:listRestoreJobs](../actions.md#backup:listrestorejobs) | backup |
| [backup:listRestoreJobsByProtectedResource](../actions.md#backup:listrestorejobsbyprotectedresource) | backup |
| [backup:listRestoreTestingPlans](../actions.md#backup:listrestoretestingplans) | backup |
| [backup:listRestoreTestingSelections](../actions.md#backup:listrestoretestingselections) | backup |
| [backup:listTags](../actions.md#backup:listtags) | backup |