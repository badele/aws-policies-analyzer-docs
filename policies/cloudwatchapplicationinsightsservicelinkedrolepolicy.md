# Policy: CloudwatchApplicationInsightsServiceLinkedRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/CloudwatchApplicationInsightsServiceLinkedRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| application-autoscaling |
| elasticloadbalancing |
| states |
| rds |
| ecs |
| fsx |
| xray |
| cloudFormation |
| lambda |
| logs |
| sqs |
| ec2 |
| s3 |
| tag |
| autoscaling |
| events |
| route53 |
| apigateway |
| elasticfilesystem |
| sns |
| route53resolver |
| resource-groups |
| cloudwatch |
| eks |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `cloudFormation` | [cloudFormation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudFormation` | [cloudFormation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudFormation` | [cloudFormation:DescribeStackResources](../actions.md#cloudformation:describestackresources) |

| `cloudFormation` | [cloudFormation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudFormation` | [cloudFormation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudFormation` | [cloudFormation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudFormation` | [cloudFormation:UpdateStack](../actions.md#cloudformation:updatestack) |

| `cloudFormation` | [cloudFormation:UpdateTerminationProtection](../actions.md#cloudformation:updateterminationprotection) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DeleteAnomalyDetector](../actions.md#cloudwatch:deleteanomalydetector) |

| `cloudwatch` | [cloudwatch:DescribeAlarmHistory](../actions.md#cloudwatch:describealarmhistory) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAnomalyDetectors](../actions.md#cloudwatch:describeanomalydetectors) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `cloudwatch` | [cloudwatch:PutAnomalyDetector](../actions.md#cloudwatch:putanomalydetector) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `dynamodb` | [dynamodb:DescribeContributorInsights](../actions.md#dynamodb:describecontributorinsights) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:DescribeTimeToLive](../actions.md#dynamodb:describetimetolive) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeNatGateways](../actions.md#ec2:describenatgateways) |

| `ec2` | [ec2:DescribeVolumeStatus](../actions.md#ec2:describevolumestatus) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcAttribute](../actions.md#ec2:describevpcattribute) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ecs` | [ecs:DescribeClusters](../actions.md#ecs:describeclusters) |

| `ecs` | [ecs:DescribeContainerInstances](../actions.md#ecs:describecontainerinstances) |

| `ecs` | [ecs:DescribeServices](../actions.md#ecs:describeservices) |

| `ecs` | [ecs:DescribeTaskDefinition](../actions.md#ecs:describetaskdefinition) |

| `ecs` | [ecs:DescribeTaskSets](../actions.md#ecs:describetasksets) |

| `ecs` | [ecs:DescribeTasks](../actions.md#ecs:describetasks) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `ecs` | [ecs:ListContainerInstances](../actions.md#ecs:listcontainerinstances) |

| `ecs` | [ecs:ListServices](../actions.md#ecs:listservices) |

| `ecs` | [ecs:ListTasks](../actions.md#ecs:listtasks) |

| `ecs` | [ecs:UpdateClusterSettings](../actions.md#ecs:updateclustersettings) |

| `eks` | [eks:DescribeCluster](../actions.md#eks:describecluster) |

| `eks` | [eks:DescribeFargateProfile](../actions.md#eks:describefargateprofile) |

| `eks` | [eks:DescribeNodegroup](../actions.md#eks:describenodegroup) |

| `eks` | [eks:ListClusters](../actions.md#eks:listclusters) |

| `eks` | [eks:ListFargateProfiles](../actions.md#eks:listfargateprofiles) |

| `eks` | [eks:ListNodegroups](../actions.md#eks:listnodegroups) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetHealth](../actions.md#elasticloadbalancing:describetargethealth) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `logs` | [logs:DeleteSubscriptionFilter](../actions.md#logs:deletesubscriptionfilter) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `logs` | [logs:PutSubscriptionFilter](../actions.md#logs:putsubscriptionfilter) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `resource-groups` | [resource-groups:CreateGroup](../actions.md#resource-groups:creategroup) |

| `resource-groups` | [resource-groups:DeleteGroup](../actions.md#resource-groups:deletegroup) |

| `resource-groups` | [resource-groups:GetGroup](../actions.md#resource-groups:getgroup) |

| `resource-groups` | [resource-groups:GetGroupQuery](../actions.md#resource-groups:getgroupquery) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `route53` | [route53:GetHealthCheck](../actions.md#route53:gethealthcheck) |

| `route53` | [route53:GetHostedZone](../actions.md#route53:gethostedzone) |

| `route53` | [route53:ListHealthChecks](../actions.md#route53:listhealthchecks) |

| `route53` | [route53:ListHostedZones](../actions.md#route53:listhostedzones) |

| `route53` | [route53:ListQueryLoggingConfigs](../actions.md#route53:listqueryloggingconfigs) |

| `route53resolver` | [route53resolver:GetFirewallRuleGroup](../actions.md#route53resolver:getfirewallrulegroup) |

| `route53resolver` | [route53resolver:GetFirewallRuleGroupAssociation](../actions.md#route53resolver:getfirewallrulegroupassociation) |

| `route53resolver` | [route53resolver:GetResolverEndpoint](../actions.md#route53resolver:getresolverendpoint) |

| `route53resolver` | [route53resolver:GetResolverQueryLogConfig](../actions.md#route53resolver:getresolverquerylogconfig) |

| `route53resolver` | [route53resolver:ListFirewallRuleGroupAssociations](../actions.md#route53resolver:listfirewallrulegroupassociations) |

| `route53resolver` | [route53resolver:ListFirewallRuleGroups](../actions.md#route53resolver:listfirewallrulegroups) |

| `route53resolver` | [route53resolver:ListResolverEndpoints](../actions.md#route53resolver:listresolverendpoints) |

| `route53resolver` | [route53resolver:ListResolverQueryLogConfigAssociations](../actions.md#route53resolver:listresolverquerylogconfigassociations) |

| `route53resolver` | [route53resolver:ListResolverQueryLogConfigs](../actions.md#route53resolver:listresolverquerylogconfigs) |

| `s3` | [s3:GetMetricsConfiguration](../actions.md#s3:getmetricsconfiguration) |

| `s3` | [s3:GetReplicationConfiguration](../actions.md#s3:getreplicationconfiguration) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `sns` | [sns:GetSMSAttributes](../actions.md#sns:getsmsattributes) |

| `sns` | [sns:GetSubscriptionAttributes](../actions.md#sns:getsubscriptionattributes) |

| `sns` | [sns:GetTopicAttributes](../actions.md#sns:gettopicattributes) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `ssm` | [ssm:AddTagsToResource](../actions.md#ssm:addtagstoresource) |

| `ssm` | [ssm:AddTagsToResource](../actions.md#ssm:addtagstoresource) |

| `ssm` | [ssm:CreateAssociation](../actions.md#ssm:createassociation) |

| `ssm` | [ssm:CreateOpsItem](../actions.md#ssm:createopsitem) |

| `ssm` | [ssm:DeleteAssociation](../actions.md#ssm:deleteassociation) |

| `ssm` | [ssm:DeleteParameter](../actions.md#ssm:deleteparameter) |

| `ssm` | [ssm:DescribeAssociation](../actions.md#ssm:describeassociation) |

| `ssm` | [ssm:DescribeInstanceInformation](../actions.md#ssm:describeinstanceinformation) |

| `ssm` | [ssm:DescribeOpsItems](../actions.md#ssm:describeopsitems) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:GetOpsItem](../actions.md#ssm:getopsitem) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `ssm` | [ssm:ListCommandInvocations](../actions.md#ssm:listcommandinvocations) |

| `ssm` | [ssm:PutParameter](../actions.md#ssm:putparameter) |

| `ssm` | [ssm:RemoveTagsFromResource](../actions.md#ssm:removetagsfromresource) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:UpdateAssociation](../actions.md#ssm:updateassociation) |

| `ssm` | [ssm:UpdateOpsItem](../actions.md#ssm:updateopsitem) |

| `states` | [states:DescribeExecution](../actions.md#states:describeexecution) |

| `states` | [states:DescribeStateMachine](../actions.md#states:describestatemachine) |

| `states` | [states:GetExecutionHistory](../actions.md#states:getexecutionhistory) |

| `states` | [states:ListStateMachines](../actions.md#states:liststatemachines) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `xray` | [xray:GetServiceGraph](../actions.md#xray:getservicegraph) |

| `xray` | [xray:GetTimeSeriesServiceStatistics](../actions.md#xray:gettimeseriesservicestatistics) |

| `xray` | [xray:GetTraceGraph](../actions.md#xray:gettracegraph) |

| `xray` | [xray:GetTraceSummaries](../actions.md#xray:gettracesummaries) |
