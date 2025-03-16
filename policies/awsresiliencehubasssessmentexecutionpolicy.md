# Policy: AWSResilienceHubAsssessmentExecutionPolicy

ARN: `arn:aws:iam::aws:policy/AWSResilienceHubAsssessmentExecutionPolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| docdb-elastic |
| backup |
| application-autoscaling |
| elasticloadbalancing |
| states |
| ecs |
| fsx |
| rds |
| fis |
| servicecatalog |
| cloudformation |
| datasync |
| lambda |
| sqs |
| ds |
| route53-recovery-control-config |
| ec2 |
| s3 |
| tag |
| autoscaling |
| route53-recovery-readiness |
| route53 |
| drs |
| apigateway |
| ecr |
| elasticfilesystem |
| sns |
| route53resolver |
| resource-groups |
| cloudwatch |
| devops-guru |
| elasticache |
| eks |
| dlm |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `backup` | [backup:DescribeBackupVault](../actions.md#backup:describebackupvault) |

| `backup` | [backup:GetBackupPlan](../actions.md#backup:getbackupplan) |

| `backup` | [backup:GetBackupSelection](../actions.md#backup:getbackupselection) |

| `backup` | [backup:ListBackupPlans](../actions.md#backup:listbackupplans) |

| `backup` | [backup:ListBackupSelections](../actions.md#backup:listbackupselections) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:ValidateTemplate](../actions.md#cloudformation:validatetemplate) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `datasync` | [datasync:DescribeTask](../actions.md#datasync:describetask) |

| `datasync` | [datasync:ListLocations](../actions.md#datasync:listlocations) |

| `datasync` | [datasync:ListTasks](../actions.md#datasync:listtasks) |

| `devops-guru` | [devops-guru:ListMonitoredResources](../actions.md#devops-guru:listmonitoredresources) |

| `dlm` | [dlm:GetLifecyclePolicies](../actions.md#dlm:getlifecyclepolicies) |

| `dlm` | [dlm:GetLifecyclePolicy](../actions.md#dlm:getlifecyclepolicy) |

| `docdb-elastic` | [docdb-elastic:GetCluster](../actions.md#docdb-elastic:getcluster) |

| `docdb-elastic` | [docdb-elastic:GetClusterSnapshot](../actions.md#docdb-elastic:getclustersnapshot) |

| `docdb-elastic` | [docdb-elastic:ListClusterSnapshots](../actions.md#docdb-elastic:listclustersnapshots) |

| `docdb-elastic` | [docdb-elastic:ListTagsForResource](../actions.md#docdb-elastic:listtagsforresource) |

| `drs` | [drs:DescribeJobs](../actions.md#drs:describejobs) |

| `drs` | [drs:DescribeSourceServers](../actions.md#drs:describesourceservers) |

| `drs` | [drs:GetReplicationConfiguration](../actions.md#drs:getreplicationconfiguration) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `dynamodb` | [dynamodb:DescribeContinuousBackups](../actions.md#dynamodb:describecontinuousbackups) |

| `dynamodb` | [dynamodb:DescribeGlobalTable](../actions.md#dynamodb:describeglobaltable) |

| `dynamodb` | [dynamodb:DescribeLimits](../actions.md#dynamodb:describelimits) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:ListGlobalTables](../actions.md#dynamodb:listglobaltables) |

| `dynamodb` | [dynamodb:ListTagsOfResource](../actions.md#dynamodb:listtagsofresource) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeFastSnapshotRestores](../actions.md#ec2:describefastsnapshotrestores) |

| `ec2` | [ec2:DescribeFleets](../actions.md#ec2:describefleets) |

| `ec2` | [ec2:DescribeHosts](../actions.md#ec2:describehosts) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeNatGateways](../actions.md#ec2:describenatgateways) |

| `ec2` | [ec2:DescribePlacementGroups](../actions.md#ec2:describeplacementgroups) |

| `ec2` | [ec2:DescribeRegions](../actions.md#ec2:describeregions) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ecr` | [ecr:DescribeRegistry](../actions.md#ecr:describeregistry) |

| `ecs` | [ecs:DescribeCapacityProviders](../actions.md#ecs:describecapacityproviders) |

| `ecs` | [ecs:DescribeClusters](../actions.md#ecs:describeclusters) |

| `ecs` | [ecs:DescribeContainerInstances](../actions.md#ecs:describecontainerinstances) |

| `ecs` | [ecs:DescribeServices](../actions.md#ecs:describeservices) |

| `ecs` | [ecs:DescribeTaskDefinition](../actions.md#ecs:describetaskdefinition) |

| `ecs` | [ecs:ListContainerInstances](../actions.md#ecs:listcontainerinstances) |

| `ecs` | [ecs:ListServices](../actions.md#ecs:listservices) |

| `eks` | [eks:DescribeCluster](../actions.md#eks:describecluster) |

| `eks` | [eks:DescribeFargateProfile](../actions.md#eks:describefargateprofile) |

| `eks` | [eks:DescribeNodegroup](../actions.md#eks:describenodegroup) |

| `eks` | [eks:ListFargateProfiles](../actions.md#eks:listfargateprofiles) |

| `eks` | [eks:ListNodegroups](../actions.md#eks:listnodegroups) |

| `elasticache` | [elasticache:DescribeCacheClusters](../actions.md#elasticache:describecacheclusters) |

| `elasticache` | [elasticache:DescribeGlobalReplicationGroups](../actions.md#elasticache:describeglobalreplicationgroups) |

| `elasticache` | [elasticache:DescribeReplicationGroups](../actions.md#elasticache:describereplicationgroups) |

| `elasticache` | [elasticache:DescribeServerlessCacheSnapshots](../actions.md#elasticache:describeserverlesscachesnapshots) |

| `elasticache` | [elasticache:DescribeServerlessCaches](../actions.md#elasticache:describeserverlesscaches) |

| `elasticache` | [elasticache:DescribeSnapshots](../actions.md#elasticache:describesnapshots) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticfilesystem` | [elasticfilesystem:DescribeLifecycleConfiguration](../actions.md#elasticfilesystem:describelifecycleconfiguration) |

| `elasticfilesystem` | [elasticfilesystem:DescribeMountTargets](../actions.md#elasticfilesystem:describemounttargets) |

| `elasticfilesystem` | [elasticfilesystem:DescribeReplicationConfigurations](../actions.md#elasticfilesystem:describereplicationconfigurations) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeListeners](../actions.md#elasticloadbalancing:describelisteners) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetHealth](../actions.md#elasticloadbalancing:describetargethealth) |

| `fis` | [fis:GetExperiment](../actions.md#fis:getexperiment) |

| `fis` | [fis:GetExperimentTemplate](../actions.md#fis:getexperimenttemplate) |

| `fis` | [fis:ListExperimentResolvedTargets](../actions.md#fis:listexperimentresolvedtargets) |

| `fis` | [fis:ListExperimentTemplates](../actions.md#fis:listexperimenttemplates) |

| `fis` | [fis:ListExperiments](../actions.md#fis:listexperiments) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `lambda` | [lambda:GetFunctionConcurrency](../actions.md#lambda:getfunctionconcurrency) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:ListAliases](../actions.md#lambda:listaliases) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListFunctionEventInvokeConfigs](../actions.md#lambda:listfunctioneventinvokeconfigs) |

| `lambda` | [lambda:ListVersionsByFunction](../actions.md#lambda:listversionsbyfunction) |

| `rds` | [rds:DescribeDBClusterSnapshots](../actions.md#rds:describedbclustersnapshots) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstanceAutomatedBackups](../actions.md#rds:describedbinstanceautomatedbackups) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBProxies](../actions.md#rds:describedbproxies) |

| `rds` | [rds:DescribeDBProxyTargets](../actions.md#rds:describedbproxytargets) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `rds` | [rds:DescribeGlobalClusters](../actions.md#rds:describeglobalclusters) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `resource-groups` | [resource-groups:GetGroup](../actions.md#resource-groups:getgroup) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `route53` | [route53:GetHealthCheck](../actions.md#route53:gethealthcheck) |

| `route53` | [route53:ListHealthChecks](../actions.md#route53:listhealthchecks) |

| `route53` | [route53:ListHostedZones](../actions.md#route53:listhostedzones) |

| `route53` | [route53:ListResourceRecordSets](../actions.md#route53:listresourcerecordsets) |

| `route53-recovery-control-config` | [route53-recovery-control-config:ListClusters](../actions.md#route53-recovery-control-config:listclusters) |

| `route53-recovery-control-config` | [route53-recovery-control-config:ListControlPanels](../actions.md#route53-recovery-control-config:listcontrolpanels) |

| `route53-recovery-control-config` | [route53-recovery-control-config:ListRoutingControls](../actions.md#route53-recovery-control-config:listroutingcontrols) |

| `route53-recovery-readiness` | [route53-recovery-readiness:GetReadinessCheckStatus](../actions.md#route53-recovery-readiness:getreadinesscheckstatus) |

| `route53-recovery-readiness` | [route53-recovery-readiness:GetResourceSet](../actions.md#route53-recovery-readiness:getresourceset) |

| `route53-recovery-readiness` | [route53-recovery-readiness:ListReadinessChecks](../actions.md#route53-recovery-readiness:listreadinesschecks) |

| `route53resolver` | [route53resolver:ListResolverEndpointIpAddresses](../actions.md#route53resolver:listresolverendpointipaddresses) |

| `route53resolver` | [route53resolver:ListResolverEndpoints](../actions.md#route53resolver:listresolverendpoints) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetBucketLogging](../actions.md#s3:getbucketlogging) |

| `s3` | [s3:GetBucketObjectLockConfiguration](../actions.md#s3:getbucketobjectlockconfiguration) |

| `s3` | [s3:GetBucketPolicyStatus](../actions.md#s3:getbucketpolicystatus) |

| `s3` | [s3:GetBucketTagging](../actions.md#s3:getbuckettagging) |

| `s3` | [s3:GetBucketVersioning](../actions.md#s3:getbucketversioning) |

| `s3` | [s3:GetMultiRegionAccessPointRoutes](../actions.md#s3:getmultiregionaccesspointroutes) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetReplicationConfiguration](../actions.md#s3:getreplicationconfiguration) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListMultiRegionAccessPoints](../actions.md#s3:listmultiregionaccesspoints) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `servicecatalog` | [servicecatalog:GetApplication](../actions.md#servicecatalog:getapplication) |

| `servicecatalog` | [servicecatalog:ListAssociatedResources](../actions.md#servicecatalog:listassociatedresources) |

| `sns` | [sns:GetSubscriptionAttributes](../actions.md#sns:getsubscriptionattributes) |

| `sns` | [sns:GetTopicAttributes](../actions.md#sns:gettopicattributes) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueUrl](../actions.md#sqs:getqueueurl) |

| `ssm` | [ssm:DescribeAutomationExecutions](../actions.md#ssm:describeautomationexecutions) |

| `ssm` | [ssm:GetParametersByPath](../actions.md#ssm:getparametersbypath) |

| `states` | [states:DescribeStateMachine](../actions.md#states:describestatemachine) |

| `states` | [states:ListStateMachineAliases](../actions.md#states:liststatemachinealiases) |

| `states` | [states:ListStateMachineVersions](../actions.md#states:liststatemachineversions) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
