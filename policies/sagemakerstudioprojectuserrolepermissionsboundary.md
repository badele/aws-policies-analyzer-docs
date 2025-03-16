# Policy: SageMakerStudioProjectUserRolePermissionsBoundary

ARN: `arn:aws:iam::aws:policy/SageMakerStudioProjectUserRolePermissionsBoundary`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| q |
| application-autoscaling |
| sagemaker-mlflow |
| lakeformation |
| kms |
| cloudformation |
| lambda |
| emr-serverless |
| redshift-data |
| logs |
| redshift-serverless |
| sqs |
| ec2 |
| tag |
| s3 |
| athena |
| airflow |
| codecommit |
| codewhisperer |
| all |
| iam |
| sagemaker |
| sqlworkbench |
| elasticmapreduce |
| ecr |
| elasticfilesystem |
| bedrock |
| pricing |
| glue |
| datazone |
| secretsmanager |
| cloudwatch |
| resource-groups |
| sts |
| aoss |
| redshift |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `airflow` | [airflow:CreateWebLoginToken](../actions.md#airflow:createweblogintoken) |

| `airflow` | [airflow:GetEnvironment](../actions.md#airflow:getenvironment) |

| `airflow` | [airflow:InvokeRestApi](../actions.md#airflow:invokerestapi) |

| `airflow` | [airflow:ListEnvironments](../actions.md#airflow:listenvironments) |

| `airflow` | [airflow:UpdateEnvironment](../actions.md#airflow:updateenvironment) |

| `all` | [*](../actions.md#all) |

| `aoss` | [aoss:APIAccessAll](../actions.md#aoss:apiaccessall) |

| `application-autoscaling` | [application-autoscaling:DeleteScalingPolicy](../actions.md#application-autoscaling:deletescalingpolicy) |

| `application-autoscaling` | [application-autoscaling:DeleteScheduledAction](../actions.md#application-autoscaling:deletescheduledaction) |

| `application-autoscaling` | [application-autoscaling:DeregisterScalableTarget](../actions.md#application-autoscaling:deregisterscalabletarget) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingActivities](../actions.md#application-autoscaling:describescalingactivities) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `application-autoscaling` | [application-autoscaling:DescribeScheduledActions](../actions.md#application-autoscaling:describescheduledactions) |

| `application-autoscaling` | [application-autoscaling:PutScalingPolicy](../actions.md#application-autoscaling:putscalingpolicy) |

| `application-autoscaling` | [application-autoscaling:PutScheduledAction](../actions.md#application-autoscaling:putscheduledaction) |

| `application-autoscaling` | [application-autoscaling:RegisterScalableTarget](../actions.md#application-autoscaling:registerscalabletarget) |

| `athena` | [athena:BatchGetNamedQuery](../actions.md#athena:batchgetnamedquery) |

| `athena` | [athena:BatchGetPreparedStatement](../actions.md#athena:batchgetpreparedstatement) |

| `athena` | [athena:BatchGetQueryExecution](../actions.md#athena:batchgetqueryexecution) |

| `athena` | [athena:CreateNamedQuery](../actions.md#athena:createnamedquery) |

| `athena` | [athena:CreateNotebook](../actions.md#athena:createnotebook) |

| `athena` | [athena:CreatePreparedStatement](../actions.md#athena:createpreparedstatement) |

| `athena` | [athena:CreatePresignedNotebookUrl](../actions.md#athena:createpresignednotebookurl) |

| `athena` | [athena:DeleteNamedQuery](../actions.md#athena:deletenamedquery) |

| `athena` | [athena:DeleteNotebook](../actions.md#athena:deletenotebook) |

| `athena` | [athena:DeletePreparedStatement](../actions.md#athena:deletepreparedstatement) |

| `athena` | [athena:ExportNotebook](../actions.md#athena:exportnotebook) |

| `athena` | [athena:GetCalculationExecution](../actions.md#athena:getcalculationexecution) |

| `athena` | [athena:GetCalculationExecutionCode](../actions.md#athena:getcalculationexecutioncode) |

| `athena` | [athena:GetCalculationExecutionStatus](../actions.md#athena:getcalculationexecutionstatus) |

| `athena` | [athena:GetDataCatalog](../actions.md#athena:getdatacatalog) |

| `athena` | [athena:GetDatabase](../actions.md#athena:getdatabase) |

| `athena` | [athena:GetNamedQuery](../actions.md#athena:getnamedquery) |

| `athena` | [athena:GetNotebookMetadata](../actions.md#athena:getnotebookmetadata) |

| `athena` | [athena:GetPreparedStatement](../actions.md#athena:getpreparedstatement) |

| `athena` | [athena:GetQueryExecution](../actions.md#athena:getqueryexecution) |

| `athena` | [athena:GetQueryResults](../actions.md#athena:getqueryresults) |

| `athena` | [athena:GetQueryResultsStream](../actions.md#athena:getqueryresultsstream) |

| `athena` | [athena:GetQueryRuntimeStatistics](../actions.md#athena:getqueryruntimestatistics) |

| `athena` | [athena:GetSession](../actions.md#athena:getsession) |

| `athena` | [athena:GetSessionStatus](../actions.md#athena:getsessionstatus) |

| `athena` | [athena:GetTableMetadata](../actions.md#athena:gettablemetadata) |

| `athena` | [athena:GetWorkGroup](../actions.md#athena:getworkgroup) |

| `athena` | [athena:ImportNotebook](../actions.md#athena:importnotebook) |

| `athena` | [athena:ListDataCatalogs](../actions.md#athena:listdatacatalogs) |

| `athena` | [athena:ListDatabases](../actions.md#athena:listdatabases) |

| `athena` | [athena:ListEngineVersions](../actions.md#athena:listengineversions) |

| `athena` | [athena:ListNamedQueries](../actions.md#athena:listnamedqueries) |

| `athena` | [athena:ListNamedQueries](../actions.md#athena:listnamedqueries) |

| `athena` | [athena:ListPreparedStatements](../actions.md#athena:listpreparedstatements) |

| `athena` | [athena:ListPreparedStatements](../actions.md#athena:listpreparedstatements) |

| `athena` | [athena:ListQueryExecutions](../actions.md#athena:listqueryexecutions) |

| `athena` | [athena:ListQueryExecutions](../actions.md#athena:listqueryexecutions) |

| `athena` | [athena:ListTableMetadata](../actions.md#athena:listtablemetadata) |

| `athena` | [athena:ListTagsForResource](../actions.md#athena:listtagsforresource) |

| `athena` | [athena:ListTagsForResource](../actions.md#athena:listtagsforresource) |

| `athena` | [athena:ListWorkGroups](../actions.md#athena:listworkgroups) |

| `athena` | [athena:StartCalculationExecution](../actions.md#athena:startcalculationexecution) |

| `athena` | [athena:StartQueryExecution](../actions.md#athena:startqueryexecution) |

| `athena` | [athena:StartSession](../actions.md#athena:startsession) |

| `athena` | [athena:StopCalculationExecution](../actions.md#athena:stopcalculationexecution) |

| `athena` | [athena:StopQueryExecution](../actions.md#athena:stopqueryexecution) |

| `athena` | [athena:TerminateSession](../actions.md#athena:terminatesession) |

| `athena` | [athena:UpdateNamedQuery](../actions.md#athena:updatenamedquery) |

| `athena` | [athena:UpdateNotebook](../actions.md#athena:updatenotebook) |

| `athena` | [athena:UpdateNotebookMetadata](../actions.md#athena:updatenotebookmetadata) |

| `athena` | [athena:UpdatePreparedStatement](../actions.md#athena:updatepreparedstatement) |

| `bedrock` | [bedrock:ApplyGuardrail](../actions.md#bedrock:applyguardrail) |

| `bedrock` | [bedrock:BatchDeleteEvaluationJob](../actions.md#bedrock:batchdeleteevaluationjob) |

| `bedrock` | [bedrock:CreateAgentAlias](../actions.md#bedrock:createagentalias) |

| `bedrock` | [bedrock:CreateEvaluationJob](../actions.md#bedrock:createevaluationjob) |

| `bedrock` | [bedrock:CreateEvaluationJob](../actions.md#bedrock:createevaluationjob) |

| `bedrock` | [bedrock:CreatePrompt](../actions.md#bedrock:createprompt) |

| `bedrock` | [bedrock:CreatePromptVersion](../actions.md#bedrock:createpromptversion) |

| `bedrock` | [bedrock:DeleteAgentAlias](../actions.md#bedrock:deleteagentalias) |

| `bedrock` | [bedrock:DeleteAgentVersion](../actions.md#bedrock:deleteagentversion) |

| `bedrock` | [bedrock:DeletePrompt](../actions.md#bedrock:deleteprompt) |

| `bedrock` | [bedrock:GetAgent](../actions.md#bedrock:getagent) |

| `bedrock` | [bedrock:GetAgentActionGroup](../actions.md#bedrock:getagentactiongroup) |

| `bedrock` | [bedrock:GetAgentAlias](../actions.md#bedrock:getagentalias) |

| `bedrock` | [bedrock:GetAgentKnowledgeBase](../actions.md#bedrock:getagentknowledgebase) |

| `bedrock` | [bedrock:GetAgentVersion](../actions.md#bedrock:getagentversion) |

| `bedrock` | [bedrock:GetEvaluationJob](../actions.md#bedrock:getevaluationjob) |

| `bedrock` | [bedrock:GetInferenceProfile](../actions.md#bedrock:getinferenceprofile) |

| `bedrock` | [bedrock:GetIngestionJob](../actions.md#bedrock:getingestionjob) |

| `bedrock` | [bedrock:GetPrompt](../actions.md#bedrock:getprompt) |

| `bedrock` | [bedrock:InvokeAgent](../actions.md#bedrock:invokeagent) |

| `bedrock` | [bedrock:InvokeFlow](../actions.md#bedrock:invokeflow) |

| `bedrock` | [bedrock:InvokeInlineAgent](../actions.md#bedrock:invokeinlineagent) |

| `bedrock` | [bedrock:InvokeModel](../actions.md#bedrock:invokemodel) |

| `bedrock` | [bedrock:InvokeModel](../actions.md#bedrock:invokemodel) |

| `bedrock` | [bedrock:InvokeModelWithResponseStream](../actions.md#bedrock:invokemodelwithresponsestream) |

| `bedrock` | [bedrock:InvokeModelWithResponseStream](../actions.md#bedrock:invokemodelwithresponsestream) |

| `bedrock` | [bedrock:ListAgentActionGroups](../actions.md#bedrock:listagentactiongroups) |

| `bedrock` | [bedrock:ListAgentAliases](../actions.md#bedrock:listagentaliases) |

| `bedrock` | [bedrock:ListAgentKnowledgeBases](../actions.md#bedrock:listagentknowledgebases) |

| `bedrock` | [bedrock:ListAgentVersions](../actions.md#bedrock:listagentversions) |

| `bedrock` | [bedrock:ListEvaluationJobs](../actions.md#bedrock:listevaluationjobs) |

| `bedrock` | [bedrock:ListFoundationModels](../actions.md#bedrock:listfoundationmodels) |

| `bedrock` | [bedrock:ListIngestionJobs](../actions.md#bedrock:listingestionjobs) |

| `bedrock` | [bedrock:ListPrompts](../actions.md#bedrock:listprompts) |

| `bedrock` | [bedrock:ListTagsForResource](../actions.md#bedrock:listtagsforresource) |

| `bedrock` | [bedrock:Retrieve](../actions.md#bedrock:retrieve) |

| `bedrock` | [bedrock:RetrieveAndGenerate](../actions.md#bedrock:retrieveandgenerate) |

| `bedrock` | [bedrock:StartIngestionJob](../actions.md#bedrock:startingestionjob) |

| `bedrock` | [bedrock:StopEvaluationJob](../actions.md#bedrock:stopevaluationjob) |

| `bedrock` | [bedrock:TagResource](../actions.md#bedrock:tagresource) |

| `bedrock` | [bedrock:UpdateAgentAlias](../actions.md#bedrock:updateagentalias) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `codecommit` | [codecommit:BatchDescribeMergeConflicts](../actions.md#codecommit:batchdescribemergeconflicts) |

| `codecommit` | [codecommit:BatchGetCommits](../actions.md#codecommit:batchgetcommits) |

| `codecommit` | [codecommit:BatchGetPullRequests](../actions.md#codecommit:batchgetpullrequests) |

| `codecommit` | [codecommit:BatchGetRepositories](../actions.md#codecommit:batchgetrepositories) |

| `codecommit` | [codecommit:CreateBranch](../actions.md#codecommit:createbranch) |

| `codecommit` | [codecommit:CreateCommit](../actions.md#codecommit:createcommit) |

| `codecommit` | [codecommit:CreatePullRequest](../actions.md#codecommit:createpullrequest) |

| `codecommit` | [codecommit:DeleteBranch](../actions.md#codecommit:deletebranch) |

| `codecommit` | [codecommit:DeleteFile](../actions.md#codecommit:deletefile) |

| `codecommit` | [codecommit:DescribeMergeConflicts](../actions.md#codecommit:describemergeconflicts) |

| `codecommit` | [codecommit:DescribePullRequestEvents](../actions.md#codecommit:describepullrequestevents) |

| `codecommit` | [codecommit:GetBlob](../actions.md#codecommit:getblob) |

| `codecommit` | [codecommit:GetBranch](../actions.md#codecommit:getbranch) |

| `codecommit` | [codecommit:GetComment](../actions.md#codecommit:getcomment) |

| `codecommit` | [codecommit:GetCommentReactions](../actions.md#codecommit:getcommentreactions) |

| `codecommit` | [codecommit:GetCommentsForComparedCommit](../actions.md#codecommit:getcommentsforcomparedcommit) |

| `codecommit` | [codecommit:GetCommentsForPullRequest](../actions.md#codecommit:getcommentsforpullrequest) |

| `codecommit` | [codecommit:GetCommit](../actions.md#codecommit:getcommit) |

| `codecommit` | [codecommit:GetCommitHistory](../actions.md#codecommit:getcommithistory) |

| `codecommit` | [codecommit:GetCommitsFromMergeBase](../actions.md#codecommit:getcommitsfrommergebase) |

| `codecommit` | [codecommit:GetDifferences](../actions.md#codecommit:getdifferences) |

| `codecommit` | [codecommit:GetFile](../actions.md#codecommit:getfile) |

| `codecommit` | [codecommit:GetFolder](../actions.md#codecommit:getfolder) |

| `codecommit` | [codecommit:GetMergeCommit](../actions.md#codecommit:getmergecommit) |

| `codecommit` | [codecommit:GetMergeConflicts](../actions.md#codecommit:getmergeconflicts) |

| `codecommit` | [codecommit:GetMergeOptions](../actions.md#codecommit:getmergeoptions) |

| `codecommit` | [codecommit:GetObjectIdentifier](../actions.md#codecommit:getobjectidentifier) |

| `codecommit` | [codecommit:GetPullRequest](../actions.md#codecommit:getpullrequest) |

| `codecommit` | [codecommit:GetPullRequestApprovalStates](../actions.md#codecommit:getpullrequestapprovalstates) |

| `codecommit` | [codecommit:GetPullRequestOverrideState](../actions.md#codecommit:getpullrequestoverridestate) |

| `codecommit` | [codecommit:GetReferences](../actions.md#codecommit:getreferences) |

| `codecommit` | [codecommit:GetRepository](../actions.md#codecommit:getrepository) |

| `codecommit` | [codecommit:GetRepositoryTriggers](../actions.md#codecommit:getrepositorytriggers) |

| `codecommit` | [codecommit:GetTree](../actions.md#codecommit:gettree) |

| `codecommit` | [codecommit:GetUploadArchiveStatus](../actions.md#codecommit:getuploadarchivestatus) |

| `codecommit` | [codecommit:GitPull](../actions.md#codecommit:gitpull) |

| `codecommit` | [codecommit:GitPush](../actions.md#codecommit:gitpush) |

| `codecommit` | [codecommit:ListAssociatedApprovalRuleTemplatesForRepository](../actions.md#codecommit:listassociatedapprovalruletemplatesforrepository) |

| `codecommit` | [codecommit:ListBranches](../actions.md#codecommit:listbranches) |

| `codecommit` | [codecommit:ListFileCommitHistory](../actions.md#codecommit:listfilecommithistory) |

| `codecommit` | [codecommit:ListPullRequests](../actions.md#codecommit:listpullrequests) |

| `codecommit` | [codecommit:ListTagsForResource](../actions.md#codecommit:listtagsforresource) |

| `codecommit` | [codecommit:MergeBranchesByFastForward](../actions.md#codecommit:mergebranchesbyfastforward) |

| `codecommit` | [codecommit:MergeBranchesBySquash](../actions.md#codecommit:mergebranchesbysquash) |

| `codecommit` | [codecommit:MergeBranchesByThreeWay](../actions.md#codecommit:mergebranchesbythreeway) |

| `codecommit` | [codecommit:MergePullRequestByFastForward](../actions.md#codecommit:mergepullrequestbyfastforward) |

| `codecommit` | [codecommit:MergePullRequestBySquash](../actions.md#codecommit:mergepullrequestbysquash) |

| `codecommit` | [codecommit:MergePullRequestByThreeWay](../actions.md#codecommit:mergepullrequestbythreeway) |

| `codecommit` | [codecommit:PostCommentForComparedCommit](../actions.md#codecommit:postcommentforcomparedcommit) |

| `codecommit` | [codecommit:PostCommentForPullRequest](../actions.md#codecommit:postcommentforpullrequest) |

| `codecommit` | [codecommit:PostCommentReply](../actions.md#codecommit:postcommentreply) |

| `codecommit` | [codecommit:PutCommentReaction](../actions.md#codecommit:putcommentreaction) |

| `codecommit` | [codecommit:PutFile](../actions.md#codecommit:putfile) |

| `codecommit` | [codecommit:UpdateComment](../actions.md#codecommit:updatecomment) |

| `codecommit` | [codecommit:UpdateDefaultBranch](../actions.md#codecommit:updatedefaultbranch) |

| `codecommit` | [codecommit:UpdatePullRequestApprovalRuleContent](../actions.md#codecommit:updatepullrequestapprovalrulecontent) |

| `codecommit` | [codecommit:UpdatePullRequestApprovalState](../actions.md#codecommit:updatepullrequestapprovalstate) |

| `codecommit` | [codecommit:UpdatePullRequestDescription](../actions.md#codecommit:updatepullrequestdescription) |

| `codecommit` | [codecommit:UpdatePullRequestStatus](../actions.md#codecommit:updatepullrequeststatus) |

| `codecommit` | [codecommit:UpdatePullRequestTitle](../actions.md#codecommit:updatepullrequesttitle) |

| `codecommit` | [codecommit:UpdateRepositoryDescription](../actions.md#codecommit:updaterepositorydescription) |

| `codewhisperer` | [codewhisperer:GenerateRecommendations](../actions.md#codewhisperer:generaterecommendations) |

| `datazone` | [datazone:CreateConnection](../actions.md#datazone:createconnection) |

| `datazone` | [datazone:DeleteConnection](../actions.md#datazone:deleteconnection) |

| `datazone` | [datazone:GetConnection](../actions.md#datazone:getconnection) |

| `datazone` | [datazone:GetDomain](../actions.md#datazone:getdomain) |

| `datazone` | [datazone:GetDomainExecutionRoleCredentials](../actions.md#datazone:getdomainexecutionrolecredentials) |

| `datazone` | [datazone:GetEnvironment](../actions.md#datazone:getenvironment) |

| `datazone` | [datazone:GetEnvironmentBlueprintConfiguration](../actions.md#datazone:getenvironmentblueprintconfiguration) |

| `datazone` | [datazone:GetProject](../actions.md#datazone:getproject) |

| `datazone` | [datazone:GetUserProfile](../actions.md#datazone:getuserprofile) |

| `datazone` | [datazone:ListConnections](../actions.md#datazone:listconnections) |

| `datazone` | [datazone:ListEnvironmentBlueprints](../actions.md#datazone:listenvironmentblueprints) |

| `datazone` | [datazone:ListEnvironments](../actions.md#datazone:listenvironments) |

| `datazone` | [datazone:ListProjects](../actions.md#datazone:listprojects) |

| `datazone` | [datazone:UpdateConnection](../actions.md#datazone:updateconnection) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:AttachNetworkInterface](../actions.md#ec2:attachnetworkinterface) |

| `ec2` | [ec2:AuthorizeSecurityGroupEgress](../actions.md#ec2:authorizesecuritygroupegress) |

| `ec2` | [ec2:AuthorizeSecurityGroupIngress](../actions.md#ec2:authorizesecuritygroupingress) |

| `ec2` | [ec2:CreateFleet](../actions.md#ec2:createfleet) |

| `ec2` | [ec2:CreateLaunchTemplate](../actions.md#ec2:createlaunchtemplate) |

| `ec2` | [ec2:CreateLaunchTemplateVersion](../actions.md#ec2:createlaunchtemplateversion) |

| `ec2` | [ec2:CreateNetworkInterface](../actions.md#ec2:createnetworkinterface) |

| `ec2` | [ec2:CreateNetworkInterfacePermission](../actions.md#ec2:createnetworkinterfacepermission) |

| `ec2` | [ec2:CreatePlacementGroup](../actions.md#ec2:createplacementgroup) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateVpcEndpoint](../actions.md#ec2:createvpcendpoint) |

| `ec2` | [ec2:DeleteLaunchTemplate](../actions.md#ec2:deletelaunchtemplate) |

| `ec2` | [ec2:DeleteNetworkInterface](../actions.md#ec2:deletenetworkinterface) |

| `ec2` | [ec2:DeleteNetworkInterfacePermission](../actions.md#ec2:deletenetworkinterfacepermission) |

| `ec2` | [ec2:DeletePlacementGroup](../actions.md#ec2:deleteplacementgroup) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeCapacityReservations](../actions.md#ec2:describecapacityreservations) |

| `ec2` | [ec2:DescribeDhcpOptions](../actions.md#ec2:describedhcpoptions) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstanceTypeOfferings](../actions.md#ec2:describeinstancetypeofferings) |

| `ec2` | [ec2:DescribeInstanceTypes](../actions.md#ec2:describeinstancetypes) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeLaunchTemplates](../actions.md#ec2:describelaunchtemplates) |

| `ec2` | [ec2:DescribeNetworkAcls](../actions.md#ec2:describenetworkacls) |

| `ec2` | [ec2:DescribeNetworkInterfaces](../actions.md#ec2:describenetworkinterfaces) |

| `ec2` | [ec2:DescribePlacementGroups](../actions.md#ec2:describeplacementgroups) |

| `ec2` | [ec2:DescribeRouteTables](../actions.md#ec2:describeroutetables) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVolumeStatus](../actions.md#ec2:describevolumestatus) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcAttribute](../actions.md#ec2:describevpcattribute) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:DetachNetworkInterface](../actions.md#ec2:detachnetworkinterface) |

| `ec2` | [ec2:ModifyInstanceAttribute](../actions.md#ec2:modifyinstanceattribute) |

| `ec2` | [ec2:RevokeSecurityGroupEgress](../actions.md#ec2:revokesecuritygroupegress) |

| `ec2` | [ec2:RevokeSecurityGroupIngress](../actions.md#ec2:revokesecuritygroupingress) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `ecr` | [ecr:BatchGetImage](../actions.md#ecr:batchgetimage) |

| `ecr` | [ecr:DescribeImages](../actions.md#ecr:describeimages) |

| `ecr` | [ecr:GetAuthorizationToken](../actions.md#ecr:getauthorizationtoken) |

| `ecr` | [ecr:GetDownloadUrlForLayer](../actions.md#ecr:getdownloadurlforlayer) |

| `elasticfilesystem` | [elasticfilesystem:DescribeMountTargets](../actions.md#elasticfilesystem:describemounttargets) |

| `elasticmapreduce` | [elasticmapreduce:CreatePersistentAppUI](../actions.md#elasticmapreduce:createpersistentappui) |

| `elasticmapreduce` | [elasticmapreduce:DescribeCluster](../actions.md#elasticmapreduce:describecluster) |

| `elasticmapreduce` | [elasticmapreduce:DescribePersistentAppUI](../actions.md#elasticmapreduce:describepersistentappui) |

| `elasticmapreduce` | [elasticmapreduce:GetClusterSessionCredentials](../actions.md#elasticmapreduce:getclustersessioncredentials) |

| `elasticmapreduce` | [elasticmapreduce:GetManagedScalingPolicy](../actions.md#elasticmapreduce:getmanagedscalingpolicy) |

| `elasticmapreduce` | [elasticmapreduce:GetOnClusterAppUIPresignedURL](../actions.md#elasticmapreduce:getonclusterappuipresignedurl) |

| `elasticmapreduce` | [elasticmapreduce:GetPersistentAppUIPresignedURL](../actions.md#elasticmapreduce:getpersistentappuipresignedurl) |

| `elasticmapreduce` | [elasticmapreduce:ListBootstrapActions](../actions.md#elasticmapreduce:listbootstrapactions) |

| `elasticmapreduce` | [elasticmapreduce:ListClusters](../actions.md#elasticmapreduce:listclusters) |

| `elasticmapreduce` | [elasticmapreduce:ListInstanceFleets](../actions.md#elasticmapreduce:listinstancefleets) |

| `elasticmapreduce` | [elasticmapreduce:ListInstanceGroups](../actions.md#elasticmapreduce:listinstancegroups) |

| `elasticmapreduce` | [elasticmapreduce:ListInstances](../actions.md#elasticmapreduce:listinstances) |

| `elasticmapreduce` | [elasticmapreduce:ListReleaseLabels](../actions.md#elasticmapreduce:listreleaselabels) |

| `elasticmapreduce` | [elasticmapreduce:ListSupportedInstanceTypes](../actions.md#elasticmapreduce:listsupportedinstancetypes) |

| `elasticmapreduce` | [elasticmapreduce:TerminateJobFlows](../actions.md#elasticmapreduce:terminatejobflows) |

| `emr-serverless` | [emr-serverless:AccessInteractiveEndpoints](../actions.md#emr-serverless:accessinteractiveendpoints) |

| `emr-serverless` | [emr-serverless:AccessLivyEndpoints](../actions.md#emr-serverless:accesslivyendpoints) |

| `emr-serverless` | [emr-serverless:GetApplication](../actions.md#emr-serverless:getapplication) |

| `emr-serverless` | [emr-serverless:GetDashboardForJobRun](../actions.md#emr-serverless:getdashboardforjobrun) |

| `emr-serverless` | [emr-serverless:GetJobRun](../actions.md#emr-serverless:getjobrun) |

| `emr-serverless` | [emr-serverless:ListApplications](../actions.md#emr-serverless:listapplications) |

| `emr-serverless` | [emr-serverless:ListJobRunAttempts](../actions.md#emr-serverless:listjobrunattempts) |

| `emr-serverless` | [emr-serverless:ListJobRuns](../actions.md#emr-serverless:listjobruns) |

| `emr-serverless` | [emr-serverless:StartApplication](../actions.md#emr-serverless:startapplication) |

| `emr-serverless` | [emr-serverless:StartJobRun](../actions.md#emr-serverless:startjobrun) |

| `emr-serverless` | [emr-serverless:StopApplication](../actions.md#emr-serverless:stopapplication) |

| `glue` | [glue:BatchCreatePartition](../actions.md#glue:batchcreatepartition) |

| `glue` | [glue:BatchDeletePartition](../actions.md#glue:batchdeletepartition) |

| `glue` | [glue:BatchDeleteTable](../actions.md#glue:batchdeletetable) |

| `glue` | [glue:BatchDeleteTableVersion](../actions.md#glue:batchdeletetableversion) |

| `glue` | [glue:BatchGetPartition](../actions.md#glue:batchgetpartition) |

| `glue` | [glue:BatchGetTableOptimizer](../actions.md#glue:batchgettableoptimizer) |

| `glue` | [glue:BatchStopJobRun](../actions.md#glue:batchstopjobrun) |

| `glue` | [glue:BatchUpdatePartition](../actions.md#glue:batchupdatepartition) |

| `glue` | [glue:CancelDataQualityRuleRecommendationRun](../actions.md#glue:canceldataqualityrulerecommendationrun) |

| `glue` | [glue:CancelDataQualityRulesetEvaluationRun](../actions.md#glue:canceldataqualityrulesetevaluationrun) |

| `glue` | [glue:CancelStatement](../actions.md#glue:cancelstatement) |

| `glue` | [glue:CreateBlueprint](../actions.md#glue:createblueprint) |

| `glue` | [glue:CreateDataQualityRuleset](../actions.md#glue:createdataqualityruleset) |

| `glue` | [glue:CreateDatabase](../actions.md#glue:createdatabase) |

| `glue` | [glue:CreateDatabase](../actions.md#glue:createdatabase) |

| `glue` | [glue:CreateJob](../actions.md#glue:createjob) |

| `glue` | [glue:CreatePartition](../actions.md#glue:createpartition) |

| `glue` | [glue:CreatePartitionIndex](../actions.md#glue:createpartitionindex) |

| `glue` | [glue:CreateSession](../actions.md#glue:createsession) |

| `glue` | [glue:CreateTable](../actions.md#glue:createtable) |

| `glue` | [glue:CreateWorkflow](../actions.md#glue:createworkflow) |

| `glue` | [glue:DeleteBlueprint](../actions.md#glue:deleteblueprint) |

| `glue` | [glue:DeleteColumnStatisticsForPartition](../actions.md#glue:deletecolumnstatisticsforpartition) |

| `glue` | [glue:DeleteColumnStatisticsForTable](../actions.md#glue:deletecolumnstatisticsfortable) |

| `glue` | [glue:DeleteDataQualityRuleset](../actions.md#glue:deletedataqualityruleset) |

| `glue` | [glue:DeleteDatabase](../actions.md#glue:deletedatabase) |

| `glue` | [glue:DeleteDatabase](../actions.md#glue:deletedatabase) |

| `glue` | [glue:DeleteJob](../actions.md#glue:deletejob) |

| `glue` | [glue:DeletePartition](../actions.md#glue:deletepartition) |

| `glue` | [glue:DeletePartitionIndex](../actions.md#glue:deletepartitionindex) |

| `glue` | [glue:DeleteSession](../actions.md#glue:deletesession) |

| `glue` | [glue:DeleteTable](../actions.md#glue:deletetable) |

| `glue` | [glue:DeleteTableVersion](../actions.md#glue:deletetableversion) |

| `glue` | [glue:DeleteWorkflow](../actions.md#glue:deleteworkflow) |

| `glue` | [glue:DescribeConnectionType](../actions.md#glue:describeconnectiontype) |

| `glue` | [glue:DescribeEntity](../actions.md#glue:describeentity) |

| `glue` | [glue:GetCatalog](../actions.md#glue:getcatalog) |

| `glue` | [glue:GetCatalogImportStatus](../actions.md#glue:getcatalogimportstatus) |

| `glue` | [glue:GetCatalogs](../actions.md#glue:getcatalogs) |

| `glue` | [glue:GetClassifier](../actions.md#glue:getclassifier) |

| `glue` | [glue:GetClassifiers](../actions.md#glue:getclassifiers) |

| `glue` | [glue:GetColumnStatisticsForPartition](../actions.md#glue:getcolumnstatisticsforpartition) |

| `glue` | [glue:GetColumnStatisticsForTable](../actions.md#glue:getcolumnstatisticsfortable) |

| `glue` | [glue:GetColumnStatisticsTaskRun](../actions.md#glue:getcolumnstatisticstaskrun) |

| `glue` | [glue:GetColumnStatisticsTaskRuns](../actions.md#glue:getcolumnstatisticstaskruns) |

| `glue` | [glue:GetCompletion](../actions.md#glue:getcompletion) |

| `glue` | [glue:GetConnection](../actions.md#glue:getconnection) |

| `glue` | [glue:GetConnections](../actions.md#glue:getconnections) |

| `glue` | [glue:GetDashboardUrl](../actions.md#glue:getdashboardurl) |

| `glue` | [glue:GetDataQualityModel](../actions.md#glue:getdataqualitymodel) |

| `glue` | [glue:GetDataQualityModelResult](../actions.md#glue:getdataqualitymodelresult) |

| `glue` | [glue:GetDataQualityResult](../actions.md#glue:getdataqualityresult) |

| `glue` | [glue:GetDataQualityRuleRecommendationRun](../actions.md#glue:getdataqualityrulerecommendationrun) |

| `glue` | [glue:GetDataQualityRuleset](../actions.md#glue:getdataqualityruleset) |

| `glue` | [glue:GetDataQualityRulesetEvaluationRun](../actions.md#glue:getdataqualityrulesetevaluationrun) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetDatabases](../actions.md#glue:getdatabases) |

| `glue` | [glue:GetDatabases](../actions.md#glue:getdatabases) |

| `glue` | [glue:GetEntityRecords](../actions.md#glue:getentityrecords) |

| `glue` | [glue:GetGeneratedCode](../actions.md#glue:getgeneratedcode) |

| `glue` | [glue:GetPartition](../actions.md#glue:getpartition) |

| `glue` | [glue:GetPartitionIndexes](../actions.md#glue:getpartitionindexes) |

| `glue` | [glue:GetPartitions](../actions.md#glue:getpartitions) |

| `glue` | [glue:GetSession](../actions.md#glue:getsession) |

| `glue` | [glue:GetStatement](../actions.md#glue:getstatement) |

| `glue` | [glue:GetTable](../actions.md#glue:gettable) |

| `glue` | [glue:GetTableOptimizer](../actions.md#glue:gettableoptimizer) |

| `glue` | [glue:GetTableVersion](../actions.md#glue:gettableversion) |

| `glue` | [glue:GetTableVersions](../actions.md#glue:gettableversions) |

| `glue` | [glue:GetTables](../actions.md#glue:gettables) |

| `glue` | [glue:GetTags](../actions.md#glue:gettags) |

| `glue` | [glue:GetUserDefinedFunction](../actions.md#glue:getuserdefinedfunction) |

| `glue` | [glue:GetUserDefinedFunction](../actions.md#glue:getuserdefinedfunction) |

| `glue` | [glue:GetUserDefinedFunctions](../actions.md#glue:getuserdefinedfunctions) |

| `glue` | [glue:GetUserDefinedFunctions](../actions.md#glue:getuserdefinedfunctions) |

| `glue` | [glue:ListConnectionTypes](../actions.md#glue:listconnectiontypes) |

| `glue` | [glue:ListCrawls](../actions.md#glue:listcrawls) |

| `glue` | [glue:ListDataQualityResults](../actions.md#glue:listdataqualityresults) |

| `glue` | [glue:ListDataQualityRuleRecommendationRuns](../actions.md#glue:listdataqualityrulerecommendationruns) |

| `glue` | [glue:ListDataQualityRulesetEvaluationRuns](../actions.md#glue:listdataqualityrulesetevaluationruns) |

| `glue` | [glue:ListDataQualityRulesets](../actions.md#glue:listdataqualityrulesets) |

| `glue` | [glue:ListEntities](../actions.md#glue:listentities) |

| `glue` | [glue:ListSessions](../actions.md#glue:listsessions) |

| `glue` | [glue:ListStatements](../actions.md#glue:liststatements) |

| `glue` | [glue:ListTableOptimizerRuns](../actions.md#glue:listtableoptimizerruns) |

| `glue` | [glue:NotifyEvent](../actions.md#glue:notifyevent) |

| `glue` | [glue:PassConnection](../actions.md#glue:passconnection) |

| `glue` | [glue:PublishDataQuality](../actions.md#glue:publishdataquality) |

| `glue` | [glue:PutDataQualityProfileAnnotation](../actions.md#glue:putdataqualityprofileannotation) |

| `glue` | [glue:PutDataQualityStatisticAnnotation](../actions.md#glue:putdataqualitystatisticannotation) |

| `glue` | [glue:PutWorkflowRunProperties](../actions.md#glue:putworkflowrunproperties) |

| `glue` | [glue:ResumeWorkflowRun](../actions.md#glue:resumeworkflowrun) |

| `glue` | [glue:RunStatement](../actions.md#glue:runstatement) |

| `glue` | [glue:SearchTables](../actions.md#glue:searchtables) |

| `glue` | [glue:StartBlueprintRun](../actions.md#glue:startblueprintrun) |

| `glue` | [glue:StartCompletion](../actions.md#glue:startcompletion) |

| `glue` | [glue:StartDataQualityRuleRecommendationRun](../actions.md#glue:startdataqualityrulerecommendationrun) |

| `glue` | [glue:StartDataQualityRulesetEvaluationRun](../actions.md#glue:startdataqualityrulesetevaluationrun) |

| `glue` | [glue:StartJobRun](../actions.md#glue:startjobrun) |

| `glue` | [glue:StartWorkflowRun](../actions.md#glue:startworkflowrun) |

| `glue` | [glue:StopSession](../actions.md#glue:stopsession) |

| `glue` | [glue:StopWorkflowRun](../actions.md#glue:stopworkflowrun) |

| `glue` | [glue:TagResource](../actions.md#glue:tagresource) |

| `glue` | [glue:TagResource](../actions.md#glue:tagresource) |

| `glue` | [glue:UntagResource](../actions.md#glue:untagresource) |

| `glue` | [glue:UpdateBlueprint](../actions.md#glue:updateblueprint) |

| `glue` | [glue:UpdateCatalog](../actions.md#glue:updatecatalog) |

| `glue` | [glue:UpdateColumnStatisticsForPartition](../actions.md#glue:updatecolumnstatisticsforpartition) |

| `glue` | [glue:UpdateColumnStatisticsForTable](../actions.md#glue:updatecolumnstatisticsfortable) |

| `glue` | [glue:UpdateDataQualityRuleset](../actions.md#glue:updatedataqualityruleset) |

| `glue` | [glue:UpdateJob](../actions.md#glue:updatejob) |

| `glue` | [glue:UpdatePartition](../actions.md#glue:updatepartition) |

| `glue` | [glue:UpdateTable](../actions.md#glue:updatetable) |

| `glue` | [glue:UpdateWorkflow](../actions.md#glue:updateworkflow) |

| `glue` | [glue:UseGlueStudio](../actions.md#glue:usegluestudio) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:Encrypt](../actions.md#kms:encrypt) |

| `kms` | [kms:Encrypt](../actions.md#kms:encrypt) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKeyWithoutPlaintext](../actions.md#kms:generatedatakeywithoutplaintext) |

| `kms` | [kms:GenerateDataKeyWithoutPlaintext](../actions.md#kms:generatedatakeywithoutplaintext) |

| `kms` | [kms:GetPublicKey](../actions.md#kms:getpublickey) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `kms` | [kms:ListGrants](../actions.md#kms:listgrants) |

| `kms` | [kms:ListGrants](../actions.md#kms:listgrants) |

| `kms` | [kms:ReEncryptFrom](../actions.md#kms:reencryptfrom) |

| `kms` | [kms:ReEncryptTo](../actions.md#kms:reencryptto) |

| `kms` | [kms:RevokeGrant](../actions.md#kms:revokegrant) |

| `lakeformation` | [lakeformation:GetDataAccess](../actions.md#lakeformation:getdataaccess) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `logs` | [logs:GetLogGroupFields](../actions.md#logs:getloggroupfields) |

| `logs` | [logs:GetLogRecord](../actions.md#logs:getlogrecord) |

| `logs` | [logs:GetQueryResults](../actions.md#logs:getqueryresults) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `logs` | [logs:StartQuery](../actions.md#logs:startquery) |

| `logs` | [logs:StopQuery](../actions.md#logs:stopquery) |

| `pricing` | [pricing:GetProducts](../actions.md#pricing:getproducts) |

| `q` | [q:SendMessage](../actions.md#q:sendmessage) |

| `q` | [q:StartConversation](../actions.md#q:startconversation) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeTags](../actions.md#redshift:describetags) |

| `redshift` | [redshift:DescribeTags](../actions.md#redshift:describetags) |

| `redshift` | [redshift:GetClusterCredentialsWithIAM](../actions.md#redshift:getclustercredentialswithiam) |

| `redshift` | [redshift:GetClusterCredentialsWithIAM](../actions.md#redshift:getclustercredentialswithiam) |

| `redshift` | [redshift:GetClusterCredentialsWithIAM](../actions.md#redshift:getclustercredentialswithiam) |

| `redshift-data` | [redshift-data:BatchExecuteStatement](../actions.md#redshift-data:batchexecutestatement) |

| `redshift-data` | [redshift-data:BatchExecuteStatement](../actions.md#redshift-data:batchexecutestatement) |

| `redshift-data` | [redshift-data:BatchExecuteStatement](../actions.md#redshift-data:batchexecutestatement) |

| `redshift-data` | [redshift-data:CancelStatement](../actions.md#redshift-data:cancelstatement) |

| `redshift-data` | [redshift-data:CancelStatement](../actions.md#redshift-data:cancelstatement) |

| `redshift-data` | [redshift-data:DescribeStatement](../actions.md#redshift-data:describestatement) |

| `redshift-data` | [redshift-data:DescribeStatement](../actions.md#redshift-data:describestatement) |

| `redshift-data` | [redshift-data:DescribeTable](../actions.md#redshift-data:describetable) |

| `redshift-data` | [redshift-data:DescribeTable](../actions.md#redshift-data:describetable) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:GetStagingBucketLocation](../actions.md#redshift-data:getstagingbucketlocation) |

| `redshift-data` | [redshift-data:GetStatementResult](../actions.md#redshift-data:getstatementresult) |

| `redshift-data` | [redshift-data:GetStatementResult](../actions.md#redshift-data:getstatementresult) |

| `redshift-data` | [redshift-data:ListDatabases](../actions.md#redshift-data:listdatabases) |

| `redshift-data` | [redshift-data:ListDatabases](../actions.md#redshift-data:listdatabases) |

| `redshift-data` | [redshift-data:ListSchemas](../actions.md#redshift-data:listschemas) |

| `redshift-data` | [redshift-data:ListSchemas](../actions.md#redshift-data:listschemas) |

| `redshift-data` | [redshift-data:ListStatements](../actions.md#redshift-data:liststatements) |

| `redshift-data` | [redshift-data:ListTables](../actions.md#redshift-data:listtables) |

| `redshift-data` | [redshift-data:ListTables](../actions.md#redshift-data:listtables) |

| `redshift-serverless` | [redshift-serverless:GetCredentials](../actions.md#redshift-serverless:getcredentials) |

| `redshift-serverless` | [redshift-serverless:GetCredentials](../actions.md#redshift-serverless:getcredentials) |

| `redshift-serverless` | [redshift-serverless:GetCredentials](../actions.md#redshift-serverless:getcredentials) |

| `redshift-serverless` | [redshift-serverless:GetManagedWorkgroup](../actions.md#redshift-serverless:getmanagedworkgroup) |

| `redshift-serverless` | [redshift-serverless:GetNamespace](../actions.md#redshift-serverless:getnamespace) |

| `redshift-serverless` | [redshift-serverless:GetNamespace](../actions.md#redshift-serverless:getnamespace) |

| `redshift-serverless` | [redshift-serverless:GetNamespace](../actions.md#redshift-serverless:getnamespace) |

| `redshift-serverless` | [redshift-serverless:GetWorkgroup](../actions.md#redshift-serverless:getworkgroup) |

| `redshift-serverless` | [redshift-serverless:GetWorkgroup](../actions.md#redshift-serverless:getworkgroup) |

| `redshift-serverless` | [redshift-serverless:GetWorkgroup](../actions.md#redshift-serverless:getworkgroup) |

| `redshift-serverless` | [redshift-serverless:ListNamespaces](../actions.md#redshift-serverless:listnamespaces) |

| `redshift-serverless` | [redshift-serverless:ListTagsForResource](../actions.md#redshift-serverless:listtagsforresource) |

| `redshift-serverless` | [redshift-serverless:ListTagsForResource](../actions.md#redshift-serverless:listtagsforresource) |

| `redshift-serverless` | [redshift-serverless:ListTagsForResource](../actions.md#redshift-serverless:listtagsforresource) |

| `redshift-serverless` | [redshift-serverless:ListWorkgroups](../actions.md#redshift-serverless:listworkgroups) |

| `resource-groups` | [resource-groups:CreateGroup](../actions.md#resource-groups:creategroup) |

| `resource-groups` | [resource-groups:DeleteGroup](../actions.md#resource-groups:deletegroup) |

| `resource-groups` | [resource-groups:GetGroupQuery](../actions.md#resource-groups:getgroupquery) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `resource-groups` | [resource-groups:Tag](../actions.md#resource-groups:tag) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:DeleteObjectVersion](../actions.md#s3:deleteobjectversion) |

| `s3` | [s3:DeleteObjectVersion](../actions.md#s3:deleteobjectversion) |

| `s3` | [s3:GetAccountPublicAccessBlock](../actions.md#s3:getaccountpublicaccessblock) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetEncryptionConfiguration](../actions.md#s3:getencryptionconfiguration) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject*](../actions.md#s3:getobjectall) |

| `s3` | [s3:GetObject*](../actions.md#s3:getobjectall) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucketVersions](../actions.md#s3:listbucketversions) |

| `s3` | [s3:ListMultipartUploadParts](../actions.md#s3:listmultipartuploadparts) |

| `s3` | [s3:ListMultipartUploadParts](../actions.md#s3:listmultipartuploadparts) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:PutObjectRetention](../actions.md#s3:putobjectretention) |

| `s3` | [s3:PutObjectRetention](../actions.md#s3:putobjectretention) |

| `s3` | [s3:PutObjectTagging](../actions.md#s3:putobjecttagging) |

| `s3` | [s3:ReplicateObject](../actions.md#s3:replicateobject) |

| `s3` | [s3:ReplicateObject](../actions.md#s3:replicateobject) |

| `s3` | [s3:RestoreObject](../actions.md#s3:restoreobject) |

| `s3` | [s3:RestoreObject](../actions.md#s3:restoreobject) |

| `sagemaker` | [sagemaker:AddAssociation](../actions.md#sagemaker:addassociation) |

| `sagemaker` | [sagemaker:AddTags](../actions.md#sagemaker:addtags) |

| `sagemaker` | [sagemaker:BatchDescribeModelPackage](../actions.md#sagemaker:batchdescribemodelpackage) |

| `sagemaker` | [sagemaker:BatchGetMetrics](../actions.md#sagemaker:batchgetmetrics) |

| `sagemaker` | [sagemaker:BatchPutMetrics](../actions.md#sagemaker:batchputmetrics) |

| `sagemaker` | [sagemaker:CallPartnerAppApi](../actions.md#sagemaker:callpartnerappapi) |

| `sagemaker` | [sagemaker:CreateAction](../actions.md#sagemaker:createaction) |

| `sagemaker` | [sagemaker:CreateApp](../actions.md#sagemaker:createapp) |

| `sagemaker` | [sagemaker:CreateArtifact](../actions.md#sagemaker:createartifact) |

| `sagemaker` | [sagemaker:CreateAutoMLJob](../actions.md#sagemaker:createautomljob) |

| `sagemaker` | [sagemaker:CreateAutoMLJobV2](../actions.md#sagemaker:createautomljobv2) |

| `sagemaker` | [sagemaker:CreateContext](../actions.md#sagemaker:createcontext) |

| `sagemaker` | [sagemaker:CreateEndpoint](../actions.md#sagemaker:createendpoint) |

| `sagemaker` | [sagemaker:CreateEndpointConfig](../actions.md#sagemaker:createendpointconfig) |

| `sagemaker` | [sagemaker:CreateHyperParameterTuningJob](../actions.md#sagemaker:createhyperparametertuningjob) |

| `sagemaker` | [sagemaker:CreateInferenceComponent](../actions.md#sagemaker:createinferencecomponent) |

| `sagemaker` | [sagemaker:CreateInferenceRecommendationsJob](../actions.md#sagemaker:createinferencerecommendationsjob) |

| `sagemaker` | [sagemaker:CreateModel](../actions.md#sagemaker:createmodel) |

| `sagemaker` | [sagemaker:CreateModelPackage](../actions.md#sagemaker:createmodelpackage) |

| `sagemaker` | [sagemaker:CreateModelPackageGroup](../actions.md#sagemaker:createmodelpackagegroup) |

| `sagemaker` | [sagemaker:CreatePartnerAppPresignedUrl](../actions.md#sagemaker:createpartnerapppresignedurl) |

| `sagemaker` | [sagemaker:CreatePipeline](../actions.md#sagemaker:createpipeline) |

| `sagemaker` | [sagemaker:CreatePresignedDomainUrl](../actions.md#sagemaker:createpresigneddomainurl) |

| `sagemaker` | [sagemaker:CreatePresignedMlflowTrackingServerUrl](../actions.md#sagemaker:createpresignedmlflowtrackingserverurl) |

| `sagemaker` | [sagemaker:CreateProcessingJob](../actions.md#sagemaker:createprocessingjob) |

| `sagemaker` | [sagemaker:CreateSpace](../actions.md#sagemaker:createspace) |

| `sagemaker` | [sagemaker:CreateTrainingJob](../actions.md#sagemaker:createtrainingjob) |

| `sagemaker` | [sagemaker:CreateTransformJob](../actions.md#sagemaker:createtransformjob) |

| `sagemaker` | [sagemaker:CreateUserProfile](../actions.md#sagemaker:createuserprofile) |

| `sagemaker` | [sagemaker:DeleteAction](../actions.md#sagemaker:deleteaction) |

| `sagemaker` | [sagemaker:DeleteApp](../actions.md#sagemaker:deleteapp) |

| `sagemaker` | [sagemaker:DeleteArtifact](../actions.md#sagemaker:deleteartifact) |

| `sagemaker` | [sagemaker:DeleteAssociation](../actions.md#sagemaker:deleteassociation) |

| `sagemaker` | [sagemaker:DeleteContext](../actions.md#sagemaker:deletecontext) |

| `sagemaker` | [sagemaker:DeleteEndpoint](../actions.md#sagemaker:deleteendpoint) |

| `sagemaker` | [sagemaker:DeleteEndpointConfig](../actions.md#sagemaker:deleteendpointconfig) |

| `sagemaker` | [sagemaker:DeleteInferenceComponent](../actions.md#sagemaker:deleteinferencecomponent) |

| `sagemaker` | [sagemaker:DeleteModel](../actions.md#sagemaker:deletemodel) |

| `sagemaker` | [sagemaker:DeleteModelPackage](../actions.md#sagemaker:deletemodelpackage) |

| `sagemaker` | [sagemaker:DeleteModelPackageGroup](../actions.md#sagemaker:deletemodelpackagegroup) |

| `sagemaker` | [sagemaker:DeletePipeline](../actions.md#sagemaker:deletepipeline) |

| `sagemaker` | [sagemaker:DeleteSpace](../actions.md#sagemaker:deletespace) |

| `sagemaker` | [sagemaker:DeleteTags](../actions.md#sagemaker:deletetags) |

| `sagemaker` | [sagemaker:DeleteUserProfile](../actions.md#sagemaker:deleteuserprofile) |

| `sagemaker` | [sagemaker:DescribeAction](../actions.md#sagemaker:describeaction) |

| `sagemaker` | [sagemaker:DescribeApp](../actions.md#sagemaker:describeapp) |

| `sagemaker` | [sagemaker:DescribeArtifact](../actions.md#sagemaker:describeartifact) |

| `sagemaker` | [sagemaker:DescribeAutoMLJob](../actions.md#sagemaker:describeautomljob) |

| `sagemaker` | [sagemaker:DescribeAutoMLJobV2](../actions.md#sagemaker:describeautomljobv2) |

| `sagemaker` | [sagemaker:DescribeContext](../actions.md#sagemaker:describecontext) |

| `sagemaker` | [sagemaker:DescribeDomain](../actions.md#sagemaker:describedomain) |

| `sagemaker` | [sagemaker:DescribeEndpoint](../actions.md#sagemaker:describeendpoint) |

| `sagemaker` | [sagemaker:DescribeEndpointConfig](../actions.md#sagemaker:describeendpointconfig) |

| `sagemaker` | [sagemaker:DescribeHyperParameterTuningJob](../actions.md#sagemaker:describehyperparametertuningjob) |

| `sagemaker` | [sagemaker:DescribeImage](../actions.md#sagemaker:describeimage) |

| `sagemaker` | [sagemaker:DescribeImageVersion](../actions.md#sagemaker:describeimageversion) |

| `sagemaker` | [sagemaker:DescribeInferenceComponent](../actions.md#sagemaker:describeinferencecomponent) |

| `sagemaker` | [sagemaker:DescribeInferenceRecommendationsJob](../actions.md#sagemaker:describeinferencerecommendationsjob) |

| `sagemaker` | [sagemaker:DescribeMlflowTrackingServer](../actions.md#sagemaker:describemlflowtrackingserver) |

| `sagemaker` | [sagemaker:DescribeModel](../actions.md#sagemaker:describemodel) |

| `sagemaker` | [sagemaker:DescribeModelPackage](../actions.md#sagemaker:describemodelpackage) |

| `sagemaker` | [sagemaker:DescribeModelPackageGroup](../actions.md#sagemaker:describemodelpackagegroup) |

| `sagemaker` | [sagemaker:DescribeOptimizationJob](../actions.md#sagemaker:describeoptimizationjob) |

| `sagemaker` | [sagemaker:DescribePartnerApp](../actions.md#sagemaker:describepartnerapp) |

| `sagemaker` | [sagemaker:DescribePipeline](../actions.md#sagemaker:describepipeline) |

| `sagemaker` | [sagemaker:DescribePipelineDefinitionForExecution](../actions.md#sagemaker:describepipelinedefinitionforexecution) |

| `sagemaker` | [sagemaker:DescribePipelineExecution](../actions.md#sagemaker:describepipelineexecution) |

| `sagemaker` | [sagemaker:DescribeProcessingJob](../actions.md#sagemaker:describeprocessingjob) |

| `sagemaker` | [sagemaker:DescribeSpace](../actions.md#sagemaker:describespace) |

| `sagemaker` | [sagemaker:DescribeTrainingJob](../actions.md#sagemaker:describetrainingjob) |

| `sagemaker` | [sagemaker:DescribeTransformJob](../actions.md#sagemaker:describetransformjob) |

| `sagemaker` | [sagemaker:DescribeTrialComponent](../actions.md#sagemaker:describetrialcomponent) |

| `sagemaker` | [sagemaker:DescribeUserProfile](../actions.md#sagemaker:describeuserprofile) |

| `sagemaker` | [sagemaker:GetSearchSuggestions](../actions.md#sagemaker:getsearchsuggestions) |

| `sagemaker` | [sagemaker:InvokeEndpoint](../actions.md#sagemaker:invokeendpoint) |

| `sagemaker` | [sagemaker:InvokeEndpointAsync](../actions.md#sagemaker:invokeendpointasync) |

| `sagemaker` | [sagemaker:InvokeEndpointWithResponseStream](../actions.md#sagemaker:invokeendpointwithresponsestream) |

| `sagemaker` | [sagemaker:ListApps](../actions.md#sagemaker:listapps) |

| `sagemaker` | [sagemaker:ListArtifacts](../actions.md#sagemaker:listartifacts) |

| `sagemaker` | [sagemaker:ListAssociations](../actions.md#sagemaker:listassociations) |

| `sagemaker` | [sagemaker:ListAutoMLJobs](../actions.md#sagemaker:listautomljobs) |

| `sagemaker` | [sagemaker:ListCandidatesForAutoMLJob](../actions.md#sagemaker:listcandidatesforautomljob) |

| `sagemaker` | [sagemaker:ListContexts](../actions.md#sagemaker:listcontexts) |

| `sagemaker` | [sagemaker:ListDomains](../actions.md#sagemaker:listdomains) |

| `sagemaker` | [sagemaker:ListEndpointConfigs](../actions.md#sagemaker:listendpointconfigs) |

| `sagemaker` | [sagemaker:ListEndpoints](../actions.md#sagemaker:listendpoints) |

| `sagemaker` | [sagemaker:ListHubContents](../actions.md#sagemaker:listhubcontents) |

| `sagemaker` | [sagemaker:ListHubs](../actions.md#sagemaker:listhubs) |

| `sagemaker` | [sagemaker:ListHyperParameterTuningJobs](../actions.md#sagemaker:listhyperparametertuningjobs) |

| `sagemaker` | [sagemaker:ListImageVersions](../actions.md#sagemaker:listimageversions) |

| `sagemaker` | [sagemaker:ListInferenceComponents](../actions.md#sagemaker:listinferencecomponents) |

| `sagemaker` | [sagemaker:ListMlflowTrackingServers](../actions.md#sagemaker:listmlflowtrackingservers) |

| `sagemaker` | [sagemaker:ListModelMetadata](../actions.md#sagemaker:listmodelmetadata) |

| `sagemaker` | [sagemaker:ListModelPackageGroups](../actions.md#sagemaker:listmodelpackagegroups) |

| `sagemaker` | [sagemaker:ListModelPackages](../actions.md#sagemaker:listmodelpackages) |

| `sagemaker` | [sagemaker:ListModels](../actions.md#sagemaker:listmodels) |

| `sagemaker` | [sagemaker:ListPartnerApps](../actions.md#sagemaker:listpartnerapps) |

| `sagemaker` | [sagemaker:ListPipelineExecutionSteps](../actions.md#sagemaker:listpipelineexecutionsteps) |

| `sagemaker` | [sagemaker:ListPipelineExecutions](../actions.md#sagemaker:listpipelineexecutions) |

| `sagemaker` | [sagemaker:ListPipelineParametersForExecution](../actions.md#sagemaker:listpipelineparametersforexecution) |

| `sagemaker` | [sagemaker:ListPipelines](../actions.md#sagemaker:listpipelines) |

| `sagemaker` | [sagemaker:ListProcessingJobs](../actions.md#sagemaker:listprocessingjobs) |

| `sagemaker` | [sagemaker:ListSpaces](../actions.md#sagemaker:listspaces) |

| `sagemaker` | [sagemaker:ListTags](../actions.md#sagemaker:listtags) |

| `sagemaker` | [sagemaker:ListTrainingJobs](../actions.md#sagemaker:listtrainingjobs) |

| `sagemaker` | [sagemaker:ListTrainingJobsForHyperParameterTuningJob](../actions.md#sagemaker:listtrainingjobsforhyperparametertuningjob) |

| `sagemaker` | [sagemaker:ListTransformJobs](../actions.md#sagemaker:listtransformjobs) |

| `sagemaker` | [sagemaker:ListUserProfiles](../actions.md#sagemaker:listuserprofiles) |

| `sagemaker` | [sagemaker:QueryLineage](../actions.md#sagemaker:querylineage) |

| `sagemaker` | [sagemaker:RetryPipelineExecution](../actions.md#sagemaker:retrypipelineexecution) |

| `sagemaker` | [sagemaker:Search](../actions.md#sagemaker:search) |

| `sagemaker` | [sagemaker:SendPipelineExecutionStepFailure](../actions.md#sagemaker:sendpipelineexecutionstepfailure) |

| `sagemaker` | [sagemaker:SendPipelineExecutionStepSuccess](../actions.md#sagemaker:sendpipelineexecutionstepsuccess) |

| `sagemaker` | [sagemaker:StartMlflowTrackingServer](../actions.md#sagemaker:startmlflowtrackingserver) |

| `sagemaker` | [sagemaker:StartPipelineExecution](../actions.md#sagemaker:startpipelineexecution) |

| `sagemaker` | [sagemaker:StopAutoMLJob](../actions.md#sagemaker:stopautomljob) |

| `sagemaker` | [sagemaker:StopHyperParameterTuningJob](../actions.md#sagemaker:stophyperparametertuningjob) |

| `sagemaker` | [sagemaker:StopMlflowTrackingServer](../actions.md#sagemaker:stopmlflowtrackingserver) |

| `sagemaker` | [sagemaker:StopPipelineExecution](../actions.md#sagemaker:stoppipelineexecution) |

| `sagemaker` | [sagemaker:StopProcessingJob](../actions.md#sagemaker:stopprocessingjob) |

| `sagemaker` | [sagemaker:StopTrainingJob](../actions.md#sagemaker:stoptrainingjob) |

| `sagemaker` | [sagemaker:StopTransformJob](../actions.md#sagemaker:stoptransformjob) |

| `sagemaker` | [sagemaker:UpdateEndpoint](../actions.md#sagemaker:updateendpoint) |

| `sagemaker` | [sagemaker:UpdateEndpointWeightsAndCapacities](../actions.md#sagemaker:updateendpointweightsandcapacities) |

| `sagemaker` | [sagemaker:UpdateInferenceComponentRuntimeConfig](../actions.md#sagemaker:updateinferencecomponentruntimeconfig) |

| `sagemaker` | [sagemaker:UpdateMlflowTrackingServer](../actions.md#sagemaker:updatemlflowtrackingserver) |

| `sagemaker` | [sagemaker:UpdateModelPackage](../actions.md#sagemaker:updatemodelpackage) |

| `sagemaker` | [sagemaker:UpdatePipeline](../actions.md#sagemaker:updatepipeline) |

| `sagemaker` | [sagemaker:UpdatePipelineExecution](../actions.md#sagemaker:updatepipelineexecution) |

| `sagemaker` | [sagemaker:UpdateSpace](../actions.md#sagemaker:updatespace) |

| `sagemaker` | [sagemaker:UpdateTrainingJob](../actions.md#sagemaker:updatetrainingjob) |

| `sagemaker-mlflow` | [sagemaker-mlflow:AccessUI](../actions.md#sagemaker-mlflow:accessui) |

| `sagemaker-mlflow` | [sagemaker-mlflow:CreateExperiment](../actions.md#sagemaker-mlflow:createexperiment) |

| `sagemaker-mlflow` | [sagemaker-mlflow:CreateModelVersion](../actions.md#sagemaker-mlflow:createmodelversion) |

| `sagemaker-mlflow` | [sagemaker-mlflow:CreateRegisteredModel](../actions.md#sagemaker-mlflow:createregisteredmodel) |

| `sagemaker-mlflow` | [sagemaker-mlflow:CreateRun](../actions.md#sagemaker-mlflow:createrun) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteExperiment](../actions.md#sagemaker-mlflow:deleteexperiment) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteModelVersion](../actions.md#sagemaker-mlflow:deletemodelversion) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteModelVersionTag](../actions.md#sagemaker-mlflow:deletemodelversiontag) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteRegisteredModel](../actions.md#sagemaker-mlflow:deleteregisteredmodel) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteRegisteredModelAlias](../actions.md#sagemaker-mlflow:deleteregisteredmodelalias) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteRegisteredModelTag](../actions.md#sagemaker-mlflow:deleteregisteredmodeltag) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteRun](../actions.md#sagemaker-mlflow:deleterun) |

| `sagemaker-mlflow` | [sagemaker-mlflow:DeleteTag](../actions.md#sagemaker-mlflow:deletetag) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetDownloadURIForModelVersionArtifacts](../actions.md#sagemaker-mlflow:getdownloaduriformodelversionartifacts) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetExperiment](../actions.md#sagemaker-mlflow:getexperiment) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetExperimentByName](../actions.md#sagemaker-mlflow:getexperimentbyname) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetLatestModelVersions](../actions.md#sagemaker-mlflow:getlatestmodelversions) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetMetricHistory](../actions.md#sagemaker-mlflow:getmetrichistory) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetModelVersion](../actions.md#sagemaker-mlflow:getmodelversion) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetModelVersionByAlias](../actions.md#sagemaker-mlflow:getmodelversionbyalias) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetRegisteredModel](../actions.md#sagemaker-mlflow:getregisteredmodel) |

| `sagemaker-mlflow` | [sagemaker-mlflow:GetRun](../actions.md#sagemaker-mlflow:getrun) |

| `sagemaker-mlflow` | [sagemaker-mlflow:ListArtifacts](../actions.md#sagemaker-mlflow:listartifacts) |

| `sagemaker-mlflow` | [sagemaker-mlflow:LogBatch](../actions.md#sagemaker-mlflow:logbatch) |

| `sagemaker-mlflow` | [sagemaker-mlflow:LogInputs](../actions.md#sagemaker-mlflow:loginputs) |

| `sagemaker-mlflow` | [sagemaker-mlflow:LogMetric](../actions.md#sagemaker-mlflow:logmetric) |

| `sagemaker-mlflow` | [sagemaker-mlflow:LogModel](../actions.md#sagemaker-mlflow:logmodel) |

| `sagemaker-mlflow` | [sagemaker-mlflow:LogParam](../actions.md#sagemaker-mlflow:logparam) |

| `sagemaker-mlflow` | [sagemaker-mlflow:RenameRegisteredModel](../actions.md#sagemaker-mlflow:renameregisteredmodel) |

| `sagemaker-mlflow` | [sagemaker-mlflow:RestoreExperiment](../actions.md#sagemaker-mlflow:restoreexperiment) |

| `sagemaker-mlflow` | [sagemaker-mlflow:RestoreRun](../actions.md#sagemaker-mlflow:restorerun) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SearchExperiments](../actions.md#sagemaker-mlflow:searchexperiments) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SearchModelVersions](../actions.md#sagemaker-mlflow:searchmodelversions) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SearchRegisteredModels](../actions.md#sagemaker-mlflow:searchregisteredmodels) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SearchRuns](../actions.md#sagemaker-mlflow:searchruns) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SetExperimentTag](../actions.md#sagemaker-mlflow:setexperimenttag) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SetRegisteredModelAlias](../actions.md#sagemaker-mlflow:setregisteredmodelalias) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SetRegisteredModelTag](../actions.md#sagemaker-mlflow:setregisteredmodeltag) |

| `sagemaker-mlflow` | [sagemaker-mlflow:SetTag](../actions.md#sagemaker-mlflow:settag) |

| `sagemaker-mlflow` | [sagemaker-mlflow:TransitionModelVersionStage](../actions.md#sagemaker-mlflow:transitionmodelversionstage) |

| `sagemaker-mlflow` | [sagemaker-mlflow:UpdateExperiment](../actions.md#sagemaker-mlflow:updateexperiment) |

| `sagemaker-mlflow` | [sagemaker-mlflow:UpdateModelVersion](../actions.md#sagemaker-mlflow:updatemodelversion) |

| `sagemaker-mlflow` | [sagemaker-mlflow:UpdateRegisteredModel](../actions.md#sagemaker-mlflow:updateregisteredmodel) |

| `sagemaker-mlflow` | [sagemaker-mlflow:UpdateRun](../actions.md#sagemaker-mlflow:updaterun) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:ListSecrets](../actions.md#secretsmanager:listsecrets) |

| `secretsmanager` | [secretsmanager:PutSecretValue](../actions.md#secretsmanager:putsecretvalue) |

| `sqlworkbench` | [sqlworkbench:CreateConnection](../actions.md#sqlworkbench:createconnection) |

| `sqlworkbench` | [sqlworkbench:DeleteQCustomContext](../actions.md#sqlworkbench:deleteqcustomcontext) |

| `sqlworkbench` | [sqlworkbench:DeleteTab](../actions.md#sqlworkbench:deletetab) |

| `sqlworkbench` | [sqlworkbench:DriverExecute](../actions.md#sqlworkbench:driverexecute) |

| `sqlworkbench` | [sqlworkbench:GetAutocompletionMetadata](../actions.md#sqlworkbench:getautocompletionmetadata) |

| `sqlworkbench` | [sqlworkbench:GetAutocompletionResource](../actions.md#sqlworkbench:getautocompletionresource) |

| `sqlworkbench` | [sqlworkbench:GetQCustomContext](../actions.md#sqlworkbench:getqcustomcontext) |

| `sqlworkbench` | [sqlworkbench:GetQSqlPromptQuotas](../actions.md#sqlworkbench:getqsqlpromptquotas) |

| `sqlworkbench` | [sqlworkbench:GetQSqlRecommendations](../actions.md#sqlworkbench:getqsqlrecommendations) |

| `sqlworkbench` | [sqlworkbench:GetQueryExecutionHistory](../actions.md#sqlworkbench:getqueryexecutionhistory) |

| `sqlworkbench` | [sqlworkbench:GetUserInfo](../actions.md#sqlworkbench:getuserinfo) |

| `sqlworkbench` | [sqlworkbench:ListQueryExecutionHistory](../actions.md#sqlworkbench:listqueryexecutionhistory) |

| `sqlworkbench` | [sqlworkbench:ListTabs](../actions.md#sqlworkbench:listtabs) |

| `sqlworkbench` | [sqlworkbench:PassAccountSettings](../actions.md#sqlworkbench:passaccountsettings) |

| `sqlworkbench` | [sqlworkbench:PutQCustomContext](../actions.md#sqlworkbench:putqcustomcontext) |

| `sqlworkbench` | [sqlworkbench:PutTab](../actions.md#sqlworkbench:puttab) |

| `sqs` | [sqs:ChangeMessageVisibility](../actions.md#sqs:changemessagevisibility) |

| `sqs` | [sqs:DeleteMessage](../actions.md#sqs:deletemessage) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueUrl](../actions.md#sqs:getqueueurl) |

| `sqs` | [sqs:ReceiveMessage](../actions.md#sqs:receivemessage) |

| `sqs` | [sqs:SendMessage](../actions.md#sqs:sendmessage) |

| `ssm` | [ssm:GetParameter](../actions.md#ssm:getparameter) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `ssm` | [ssm:GetParametersByPath](../actions.md#ssm:getparametersbypath) |

| `sts` | [sts:AssumeRole](../actions.md#sts:assumerole) |

| `sts` | [sts:GetCallerIdentity](../actions.md#sts:getcalleridentity) |

| `sts` | [sts:SetSourceIdentity](../actions.md#sts:setsourceidentity) |

| `sts` | [sts:TagSession](../actions.md#sts:tagsession) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
