# Service: states

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/SecurityAudit` | [SecurityAudit](../policies.md#securityaudit) |
| `arn:aws:iam::aws:policy/job-function/ViewOnlyAccess` | [ViewOnlyAccess](../policies.md#viewonlyaccess) |
| `arn:aws:iam::aws:policy/service-role/AmazonSSMMaintenanceWindowRole` | [AmazonSSMMaintenanceWindowRole](../policies.md#amazonssmmaintenancewindowrole) |
| `arn:aws:iam::aws:policy/AWSStepFunctionsReadOnlyAccess` | [AWSStepFunctionsReadOnlyAccess](../policies.md#awsstepfunctionsreadonlyaccess) |
| `arn:aws:iam::aws:policy/AWSStepFunctionsFullAccess` | [AWSStepFunctionsFullAccess](../policies.md#awsstepfunctionsfullaccess) |
| `arn:aws:iam::aws:policy/AWSStepFunctionsConsoleFullAccess` | [AWSStepFunctionsConsoleFullAccess](../policies.md#awsstepfunctionsconsolefullaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AmazonSSMServiceRolePolicy` | [AmazonSSMServiceRolePolicy](../policies.md#amazonssmservicerolepolicy) |
| `arn:aws:iam::aws:policy/AmazonSageMakerFullAccess` | [AmazonSageMakerFullAccess](../policies.md#amazonsagemakerfullaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy` | [AWSConfigServiceRolePolicy](../policies.md#awsconfigservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/CloudwatchApplicationInsightsServiceLinkedRolePolicy` | [CloudwatchApplicationInsightsServiceLinkedRolePolicy](../policies.md#cloudwatchapplicationinsightsservicelinkedrolepolicy) |
| `arn:aws:iam::aws:policy/AWSCodePipeline_FullAccess` | [AWSCodePipeline_FullAccess](../policies.md#awscodepipeline_fullaccess) |
| `arn:aws:iam::aws:policy/service-role/AWS_ConfigRole` | [AWS_ConfigRole](../policies.md#aws_configrole) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSLambda_ReadOnlyAccess` | [AWSLambda_ReadOnlyAccess](../policies.md#awslambda_readonlyaccess) |
| `arn:aws:iam::aws:policy/AWSLambda_FullAccess` | [AWSLambda_FullAccess](../policies.md#awslambda_fullaccess) |
| `arn:aws:iam::aws:policy/CloudWatchApplicationInsightsFullAccess` | [CloudWatchApplicationInsightsFullAccess](../policies.md#cloudwatchapplicationinsightsfullaccess) |
| `arn:aws:iam::aws:policy/AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy` | [AmazonSageMakerAdmin-ServiceCatalogProductsServiceRolePolicy](../policies.md#amazonsagemakeradmin-servicecatalogproductsservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy` | [AWSResourceExplorerServiceRolePolicy](../policies.md#awsresourceexplorerservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSResilienceHubAsssessmentExecutionPolicy` | [AWSResilienceHubAsssessmentExecutionPolicy](../policies.md#awsresiliencehubasssessmentexecutionpolicy) |
| `arn:aws:iam::aws:policy/AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary` | [AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary](../policies.md#amazondatazonesagemakerenvironmentrolepermissionsboundary) |
| `arn:aws:iam::aws:policy/ResourceGroupsTaggingAPITagUntagSupportedResources` | [ResourceGroupsTaggingAPITagUntagSupportedResources](../policies.md#resourcegroupstaggingapitaguntagsupportedresources) |
| `arn:aws:iam::aws:policy/AIOpsAssistantPolicy` | [AIOpsAssistantPolicy](../policies.md#aiopsassistantpolicy) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [states:*](../actions.md#states:all) | states |
| [states:CreateStateMachine](../actions.md#states:createstatemachine) | states |
| [states:DeleteStateMachine](../actions.md#states:deletestatemachine) | states |
| [states:Describe*](../actions.md#states:describeall) | states |
| [states:DescribeActivity](../actions.md#states:describeactivity) | states |
| [states:DescribeExecution](../actions.md#states:describeexecution) | states |
| [states:DescribeMapRun](../actions.md#states:describemaprun) | states |
| [states:DescribeStateMachine](../actions.md#states:describestatemachine) | states |
| [states:DescribeStateMachineAlias](../actions.md#states:describestatemachinealias) | states |
| [states:DescribeStateMachineForExecution](../actions.md#states:describestatemachineforexecution) | states |
| [states:GetExecutionHistory](../actions.md#states:getexecutionhistory) | states |
| [states:List*](../actions.md#states:listall) | states |
| [states:ListActivities](../actions.md#states:listactivities) | states |
| [states:ListExecutions](../actions.md#states:listexecutions) | states |
| [states:ListMapRuns](../actions.md#states:listmapruns) | states |
| [states:ListStateMachineAliases](../actions.md#states:liststatemachinealiases) | states |
| [states:ListStateMachineVersions](../actions.md#states:liststatemachineversions) | states |
| [states:ListStateMachines](../actions.md#states:liststatemachines) | states |
| [states:ListTagsForResource](../actions.md#states:listtagsforresource) | states |
| [states:StartExecution](../actions.md#states:startexecution) | states |
| [states:StopExecution](../actions.md#states:stopexecution) | states |
| [states:TagResource](../actions.md#states:tagresource) | states |
| [states:UntagResource](../actions.md#states:untagresource) | states |
| [states:UpdateStateMachine](../actions.md#states:updatestatemachine) | states |
| [states:ValidateStateMachineDefinition](../actions.md#states:validatestatemachinedefinition) | states |
| [states:describeActivity](../actions.md#states:describeactivity) | states |
| [states:describeExecution](../actions.md#states:describeexecution) | states |
| [states:describeMapRun](../actions.md#states:describemaprun) | states |
| [states:describeStateMachine](../actions.md#states:describestatemachine) | states |
| [states:describeStateMachineAlias](../actions.md#states:describestatemachinealias) | states |
| [states:describeStateMachineForExecution](../actions.md#states:describestatemachineforexecution) | states |
| [states:getExecutionHistory](../actions.md#states:getexecutionhistory) | states |
| [states:listActivities](../actions.md#states:listactivities) | states |
| [states:listExecutions](../actions.md#states:listexecutions) | states |
| [states:listMapRuns](../actions.md#states:listmapruns) | states |
| [states:listStateMachineAliases](../actions.md#states:liststatemachinealiases) | states |
| [states:listStateMachineVersions](../actions.md#states:liststatemachineversions) | states |
| [states:listStateMachines](../actions.md#states:liststatemachines) | states |