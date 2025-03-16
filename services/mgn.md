# Service: mgn

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSApplicationMigrationServiceRolePolicy` | [AWSApplicationMigrationServiceRolePolicy](../policies.md#awsapplicationmigrationservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWSApplicationMigrationConversionServerPolicy` | [AWSApplicationMigrationConversionServerPolicy](../policies.md#awsapplicationmigrationconversionserverpolicy) |
| `arn:aws:iam::aws:policy/AWSApplicationMigrationFullAccess` | [AWSApplicationMigrationFullAccess](../policies.md#awsapplicationmigrationfullaccess) |
| `arn:aws:iam::aws:policy/AWSApplicationMigrationAgentPolicy` | [AWSApplicationMigrationAgentPolicy](../policies.md#awsapplicationmigrationagentpolicy) |
| `arn:aws:iam::aws:policy/AWSApplicationMigrationReadOnlyAccess` | [AWSApplicationMigrationReadOnlyAccess](../policies.md#awsapplicationmigrationreadonlyaccess) |
| `arn:aws:iam::aws:policy/service-role/AWSApplicationMigrationReplicationServerPolicy` | [AWSApplicationMigrationReplicationServerPolicy](../policies.md#awsapplicationmigrationreplicationserverpolicy) |
| `arn:aws:iam::aws:policy/AWSApplicationMigrationVCenterClientPolicy` | [AWSApplicationMigrationVCenterClientPolicy](../policies.md#awsapplicationmigrationvcenterclientpolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSMigrationHubOrchestratorServiceRolePolicy` | [AWSMigrationHubOrchestratorServiceRolePolicy](../policies.md#awsmigrationhuborchestratorservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWSApplicationMigrationAgentPolicy_v2` | [AWSApplicationMigrationAgentPolicy_v2](../policies.md#awsapplicationmigrationagentpolicy_v2) |
| `arn:aws:iam::aws:policy/AWSApplicationMigrationAgentInstallationPolicy` | [AWSApplicationMigrationAgentInstallationPolicy](../policies.md#awsapplicationmigrationagentinstallationpolicy) |
| `arn:aws:iam::aws:policy/AWSApplicationMigrationServiceEc2InstancePolicy` | [AWSApplicationMigrationServiceEc2InstancePolicy](../policies.md#awsapplicationmigrationserviceec2instancepolicy) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [mgn:*](../actions.md#mgn:all) | mgn |
| [mgn:BatchCreateVolumeSnapshotGroupForMgn](../actions.md#mgn:batchcreatevolumesnapshotgroupformgn) | mgn |
| [mgn:BatchDeleteSnapshotRequestForMgn](../actions.md#mgn:batchdeletesnapshotrequestformgn) | mgn |
| [mgn:ChangeServerLifeCycleState](../actions.md#mgn:changeserverlifecyclestate) | mgn |
| [mgn:CreateVcenterClientForMgn](../actions.md#mgn:createvcenterclientformgn) | mgn |
| [mgn:DeleteVcenterClient](../actions.md#mgn:deletevcenterclient) | mgn |
| [mgn:DescribeJobLogItems](../actions.md#mgn:describejoblogitems) | mgn |
| [mgn:DescribeJobs](../actions.md#mgn:describejobs) | mgn |
| [mgn:DescribeLaunchConfigurationTemplates](../actions.md#mgn:describelaunchconfigurationtemplates) | mgn |
| [mgn:DescribeReplicationConfigurationTemplates](../actions.md#mgn:describereplicationconfigurationtemplates) | mgn |
| [mgn:DescribeReplicationServerAssociationsForMgn](../actions.md#mgn:describereplicationserverassociationsformgn) | mgn |
| [mgn:DescribeSnapshotRequestsForMgn](../actions.md#mgn:describesnapshotrequestsformgn) | mgn |
| [mgn:DescribeSourceServers](../actions.md#mgn:describesourceservers) | mgn |
| [mgn:DescribeVcenterClients](../actions.md#mgn:describevcenterclients) | mgn |
| [mgn:FinalizeCutover](../actions.md#mgn:finalizecutover) | mgn |
| [mgn:GetAgentCommandForMgn](../actions.md#mgn:getagentcommandformgn) | mgn |
| [mgn:GetAgentConfirmedResumeInfoForMgn](../actions.md#mgn:getagentconfirmedresumeinfoformgn) | mgn |
| [mgn:GetAgentInstallationAssetsForMgn](../actions.md#mgn:getagentinstallationassetsformgn) | mgn |
| [mgn:GetAgentReplicationInfoForMgn](../actions.md#mgn:getagentreplicationinfoformgn) | mgn |
| [mgn:GetAgentRuntimeConfigurationForMgn](../actions.md#mgn:getagentruntimeconfigurationformgn) | mgn |
| [mgn:GetAgentSnapshotCreditsForMgn](../actions.md#mgn:getagentsnapshotcreditsformgn) | mgn |
| [mgn:GetChannelCommandsForMgn](../actions.md#mgn:getchannelcommandsformgn) | mgn |
| [mgn:GetLaunchConfiguration](../actions.md#mgn:getlaunchconfiguration) | mgn |
| [mgn:GetReplicationConfiguration](../actions.md#mgn:getreplicationconfiguration) | mgn |
| [mgn:GetVcenterClientCommandsForMgn](../actions.md#mgn:getvcenterclientcommandsformgn) | mgn |
| [mgn:IssueClientCertificateForMgn](../actions.md#mgn:issueclientcertificateformgn) | mgn |
| [mgn:ListApplications](../actions.md#mgn:listapplications) | mgn |
| [mgn:ListExportErrors](../actions.md#mgn:listexporterrors) | mgn |
| [mgn:ListExports](../actions.md#mgn:listexports) | mgn |
| [mgn:ListImportErrors](../actions.md#mgn:listimporterrors) | mgn |
| [mgn:ListImports](../actions.md#mgn:listimports) | mgn |
| [mgn:ListSourceServerActions](../actions.md#mgn:listsourceserveractions) | mgn |
| [mgn:ListTagsForResource](../actions.md#mgn:listtagsforresource) | mgn |
| [mgn:ListTemplateActions](../actions.md#mgn:listtemplateactions) | mgn |
| [mgn:ListWaves](../actions.md#mgn:listwaves) | mgn |
| [mgn:MarkAsArchived](../actions.md#mgn:markasarchived) | mgn |
| [mgn:NotifyAgentAuthenticationForMgn](../actions.md#mgn:notifyagentauthenticationformgn) | mgn |
| [mgn:NotifyAgentConnectedForMgn](../actions.md#mgn:notifyagentconnectedformgn) | mgn |
| [mgn:NotifyAgentDisconnectedForMgn](../actions.md#mgn:notifyagentdisconnectedformgn) | mgn |
| [mgn:NotifyAgentReplicationProgressForMgn](../actions.md#mgn:notifyagentreplicationprogressformgn) | mgn |
| [mgn:NotifyVcenterClientStartedForMgn](../actions.md#mgn:notifyvcenterclientstartedformgn) | mgn |
| [mgn:RegisterAgentForMgn](../actions.md#mgn:registeragentformgn) | mgn |
| [mgn:SendAgentLogsForMgn](../actions.md#mgn:sendagentlogsformgn) | mgn |
| [mgn:SendAgentMetricsForMgn](../actions.md#mgn:sendagentmetricsformgn) | mgn |
| [mgn:SendChannelCommandResultForMgn](../actions.md#mgn:sendchannelcommandresultformgn) | mgn |
| [mgn:SendClientLogsForMgn](../actions.md#mgn:sendclientlogsformgn) | mgn |
| [mgn:SendClientMetricsForMgn](../actions.md#mgn:sendclientmetricsformgn) | mgn |
| [mgn:SendVcenterClientCommandResultForMgn](../actions.md#mgn:sendvcenterclientcommandresultformgn) | mgn |
| [mgn:SendVcenterClientLogsForMgn](../actions.md#mgn:sendvcenterclientlogsformgn) | mgn |
| [mgn:SendVcenterClientMetricsForMgn](../actions.md#mgn:sendvcenterclientmetricsformgn) | mgn |
| [mgn:StartCutover](../actions.md#mgn:startcutover) | mgn |
| [mgn:StartTest](../actions.md#mgn:starttest) | mgn |
| [mgn:TagResource](../actions.md#mgn:tagresource) | mgn |
| [mgn:UpdateAgentBacklogForMgn](../actions.md#mgn:updateagentbacklogformgn) | mgn |
| [mgn:UpdateAgentConversionInfoForMgn](../actions.md#mgn:updateagentconversioninfoformgn) | mgn |
| [mgn:UpdateAgentReplicationInfoForMgn](../actions.md#mgn:updateagentreplicationinfoformgn) | mgn |
| [mgn:UpdateAgentReplicationProcessStateForMgn](../actions.md#mgn:updateagentreplicationprocessstateformgn) | mgn |
| [mgn:UpdateAgentSourcePropertiesForMgn](../actions.md#mgn:updateagentsourcepropertiesformgn) | mgn |
| [mgn:UpdateReplicationConfiguration](../actions.md#mgn:updatereplicationconfiguration) | mgn |
| [mgn:VerifyClientRoleForMgn](../actions.md#mgn:verifyclientroleformgn) | mgn |
| [mgn:describeJobLogItems](../actions.md#mgn:describejoblogitems) | mgn |
| [mgn:describeJobs](../actions.md#mgn:describejobs) | mgn |
| [mgn:describeLaunchConfigurationTemplates](../actions.md#mgn:describelaunchconfigurationtemplates) | mgn |
| [mgn:describeReplicationConfigurationTemplates](../actions.md#mgn:describereplicationconfigurationtemplates) | mgn |
| [mgn:describeSourceServers](../actions.md#mgn:describesourceservers) | mgn |
| [mgn:describeVcenterClients](../actions.md#mgn:describevcenterclients) | mgn |
| [mgn:getLaunchConfiguration](../actions.md#mgn:getlaunchconfiguration) | mgn |
| [mgn:getReplicationConfiguration](../actions.md#mgn:getreplicationconfiguration) | mgn |
| [mgn:listApplications](../actions.md#mgn:listapplications) | mgn |
| [mgn:listSourceServerActions](../actions.md#mgn:listsourceserveractions) | mgn |
| [mgn:listTemplateActions](../actions.md#mgn:listtemplateactions) | mgn |
| [mgn:listWaves](../actions.md#mgn:listwaves) | mgn |