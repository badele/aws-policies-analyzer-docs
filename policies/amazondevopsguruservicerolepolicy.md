# Policy: AmazonDevOpsGuruServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AmazonDevOpsGuruServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| application-autoscaling |
| elasticloadbalancing |
| rds |
| xray |
| cloudformation |
| lambda |
| logs |
| sqs |
| ec2 |
| tag |
| s3 |
| autoscaling |
| events |
| cloudtrail |
| pi |
| config |
| codedeploy |
| apigateway |
| servicequotas |
| cloudwatch |
| kinesis |
| organizations |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:ListImports](../actions.md#cloudformation:listimports) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudtrail` | [cloudtrail:LookupEvents](../actions.md#cloudtrail:lookupevents) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAnomalyDetectors](../actions.md#cloudwatch:describeanomalydetectors) |

| `cloudwatch` | [cloudwatch:GetDashboard](../actions.md#cloudwatch:getdashboard) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:ListDashboards](../actions.md#cloudwatch:listdashboards) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `codedeploy` | [codedeploy:BatchGetDeployments](../actions.md#codedeploy:batchgetdeployments) |

| `codedeploy` | [codedeploy:GetDeploymentGroup](../actions.md#codedeploy:getdeploymentgroup) |

| `codedeploy` | [codedeploy:ListDeployments](../actions.md#codedeploy:listdeployments) |

| `config` | [config:DescribeConfigurationRecorderStatus](../actions.md#config:describeconfigurationrecorderstatus) |

| `config` | [config:GetResourceConfigHistory](../actions.md#config:getresourceconfighistory) |

| `dynamodb` | [dynamodb:DescribeContinuousBackups](../actions.md#dynamodb:describecontinuousbackups) |

| `dynamodb` | [dynamodb:DescribeLimits](../actions.md#dynamodb:describelimits) |

| `dynamodb` | [dynamodb:DescribeStream](../actions.md#dynamodb:describestream) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:ListStreams](../actions.md#dynamodb:liststreams) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancerAttributes](../actions.md#elasticloadbalancing:describeloadbalancerattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:DisableRule](../actions.md#events:disablerule) |

| `events` | [events:EnableRule](../actions.md#events:enablerule) |

| `events` | [events:ListRuleNamesByTarget](../actions.md#events:listrulenamesbytarget) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `kinesis` | [kinesis:DescribeLimits](../actions.md#kinesis:describelimits) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `lambda` | [lambda:GetAccountSettings](../actions.md#lambda:getaccountsettings) |

| `lambda` | [lambda:GetFunction](../actions.md#lambda:getfunction) |

| `lambda` | [lambda:GetFunctionConcurrency](../actions.md#lambda:getfunctionconcurrency) |

| `lambda` | [lambda:GetPolicy](../actions.md#lambda:getpolicy) |

| `lambda` | [lambda:ListAliases](../actions.md#lambda:listaliases) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListProvisionedConcurrencyConfigs](../actions.md#lambda:listprovisionedconcurrencyconfigs) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `organizations` | [organizations:ListChildren](../actions.md#organizations:listchildren) |

| `organizations` | [organizations:ListDelegatedAdministrators](../actions.md#organizations:listdelegatedadministrators) |

| `organizations` | [organizations:ListRoots](../actions.md#organizations:listroots) |

| `pi` | [pi:GetResourceMetrics](../actions.md#pi:getresourcemetrics) |

| `rds` | [rds:DescribeAccountAttributes](../actions.md#rds:describeaccountattributes) |

| `rds` | [rds:DescribeDBClusterParameters](../actions.md#rds:describedbclusterparameters) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstanceAutomatedBackups](../actions.md#rds:describedbinstanceautomatedbackups) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeOptionGroups](../actions.md#rds:describeoptiongroups) |

| `s3` | [s3:GetBucketNotification](../actions.md#s3:getbucketnotification) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:GetBucketPublicAccessBlock](../actions.md#s3:getbucketpublicaccessblock) |

| `s3` | [s3:GetBucketTagging](../actions.md#s3:getbuckettagging) |

| `s3` | [s3:GetBucketWebsite](../actions.md#s3:getbucketwebsite) |

| `s3` | [s3:GetIntelligentTieringConfiguration](../actions.md#s3:getintelligenttieringconfiguration) |

| `s3` | [s3:GetLifecycleConfiguration](../actions.md#s3:getlifecycleconfiguration) |

| `s3` | [s3:GetReplicationConfiguration](../actions.md#s3:getreplicationconfiguration) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListStorageLensConfigurations](../actions.md#s3:liststoragelensconfigurations) |

| `servicequotas` | [servicequotas:GetServiceQuota](../actions.md#servicequotas:getservicequota) |

| `servicequotas` | [servicequotas:ListRequestedServiceQuotaChangeHistory](../actions.md#servicequotas:listrequestedservicequotachangehistory) |

| `servicequotas` | [servicequotas:ListServiceQuotas](../actions.md#servicequotas:listservicequotas) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `ssm` | [ssm:AddTagsToResource](../actions.md#ssm:addtagstoresource) |

| `ssm` | [ssm:CreateOpsItem](../actions.md#ssm:createopsitem) |

| `ssm` | [ssm:GetOpsItem](../actions.md#ssm:getopsitem) |

| `ssm` | [ssm:UpdateOpsItem](../actions.md#ssm:updateopsitem) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `xray` | [xray:GetServiceGraph](../actions.md#xray:getservicegraph) |
