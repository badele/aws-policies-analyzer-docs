# Policy: AmazonDynamoDBReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| lambda |
| cloudwatch |
| application-autoscaling |
| sns |
| resource-groups |
| datapipeline |
| kinesis |
| iam |
| dax |
| ec2 |
| tag |
| dynamodb |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingActivities](../actions.md#application-autoscaling:describescalingactivities) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `cloudwatch` | [cloudwatch:DescribeAlarmHistory](../actions.md#cloudwatch:describealarmhistory) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarmsForMetric](../actions.md#cloudwatch:describealarmsformetric) |

| `cloudwatch` | [cloudwatch:GetInsightRuleReport](../actions.md#cloudwatch:getinsightrulereport) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `datapipeline` | [datapipeline:DescribeObjects](../actions.md#datapipeline:describeobjects) |

| `datapipeline` | [datapipeline:DescribePipelines](../actions.md#datapipeline:describepipelines) |

| `datapipeline` | [datapipeline:GetPipelineDefinition](../actions.md#datapipeline:getpipelinedefinition) |

| `datapipeline` | [datapipeline:ListPipelines](../actions.md#datapipeline:listpipelines) |

| `datapipeline` | [datapipeline:QueryObjects](../actions.md#datapipeline:queryobjects) |

| `dax` | [dax:BatchGetItem](../actions.md#dax:batchgetitem) |

| `dax` | [dax:Describe*](../actions.md#dax:describeall) |

| `dax` | [dax:GetItem](../actions.md#dax:getitem) |

| `dax` | [dax:List*](../actions.md#dax:listall) |

| `dax` | [dax:Query](../actions.md#dax:query) |

| `dax` | [dax:Scan](../actions.md#dax:scan) |

| `dynamodb` | [dynamodb:BatchGetItem](../actions.md#dynamodb:batchgetitem) |

| `dynamodb` | [dynamodb:Describe*](../actions.md#dynamodb:describeall) |

| `dynamodb` | [dynamodb:GetAbacStatus](../actions.md#dynamodb:getabacstatus) |

| `dynamodb` | [dynamodb:GetItem](../actions.md#dynamodb:getitem) |

| `dynamodb` | [dynamodb:GetResourcePolicy](../actions.md#dynamodb:getresourcepolicy) |

| `dynamodb` | [dynamodb:List*](../actions.md#dynamodb:listall) |

| `dynamodb` | [dynamodb:PartiQLSelect](../actions.md#dynamodb:partiqlselect) |

| `dynamodb` | [dynamodb:Query](../actions.md#dynamodb:query) |

| `dynamodb` | [dynamodb:Scan](../actions.md#dynamodb:scan) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `kinesis` | [kinesis:DescribeStreamSummary](../actions.md#kinesis:describestreamsummary) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `resource-groups` | [resource-groups:GetGroup](../actions.md#resource-groups:getgroup) |

| `resource-groups` | [resource-groups:GetGroupQuery](../actions.md#resource-groups:getgroupquery) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `resource-groups` | [resource-groups:ListGroups](../actions.md#resource-groups:listgroups) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
