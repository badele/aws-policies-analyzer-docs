# Policy: AmazonDynamoDBFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess`

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

| `application-autoscaling` | [application-autoscaling:DeleteScalingPolicy](../actions.md#application-autoscaling:deletescalingpolicy) |

| `application-autoscaling` | [application-autoscaling:DeregisterScalableTarget](../actions.md#application-autoscaling:deregisterscalabletarget) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingActivities](../actions.md#application-autoscaling:describescalingactivities) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `application-autoscaling` | [application-autoscaling:PutScalingPolicy](../actions.md#application-autoscaling:putscalingpolicy) |

| `application-autoscaling` | [application-autoscaling:RegisterScalableTarget](../actions.md#application-autoscaling:registerscalabletarget) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarmHistory](../actions.md#cloudwatch:describealarmhistory) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarmsForMetric](../actions.md#cloudwatch:describealarmsformetric) |

| `cloudwatch` | [cloudwatch:GetInsightRuleReport](../actions.md#cloudwatch:getinsightrulereport) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `datapipeline` | [datapipeline:ActivatePipeline](../actions.md#datapipeline:activatepipeline) |

| `datapipeline` | [datapipeline:CreatePipeline](../actions.md#datapipeline:createpipeline) |

| `datapipeline` | [datapipeline:DeletePipeline](../actions.md#datapipeline:deletepipeline) |

| `datapipeline` | [datapipeline:DescribeObjects](../actions.md#datapipeline:describeobjects) |

| `datapipeline` | [datapipeline:DescribePipelines](../actions.md#datapipeline:describepipelines) |

| `datapipeline` | [datapipeline:GetPipelineDefinition](../actions.md#datapipeline:getpipelinedefinition) |

| `datapipeline` | [datapipeline:ListPipelines](../actions.md#datapipeline:listpipelines) |

| `datapipeline` | [datapipeline:PutPipelineDefinition](../actions.md#datapipeline:putpipelinedefinition) |

| `datapipeline` | [datapipeline:QueryObjects](../actions.md#datapipeline:queryobjects) |

| `dax` | [dax:*](../actions.md#dax:all) |

| `dynamodb` | [dynamodb:*](../actions.md#dynamodb:all) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `kinesis` | [kinesis:DescribeStreamSummary](../actions.md#kinesis:describestreamsummary) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `lambda` | [lambda:CreateEventSourceMapping](../actions.md#lambda:createeventsourcemapping) |

| `lambda` | [lambda:CreateFunction](../actions.md#lambda:createfunction) |

| `lambda` | [lambda:DeleteEventSourceMapping](../actions.md#lambda:deleteeventsourcemapping) |

| `lambda` | [lambda:DeleteFunction](../actions.md#lambda:deletefunction) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `resource-groups` | [resource-groups:CreateGroup](../actions.md#resource-groups:creategroup) |

| `resource-groups` | [resource-groups:DeleteGroup](../actions.md#resource-groups:deletegroup) |

| `resource-groups` | [resource-groups:GetGroup](../actions.md#resource-groups:getgroup) |

| `resource-groups` | [resource-groups:GetGroupQuery](../actions.md#resource-groups:getgroupquery) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `resource-groups` | [resource-groups:ListGroups](../actions.md#resource-groups:listgroups) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:DeleteTopic](../actions.md#sns:deletetopic) |

| `sns` | [sns:ListSubscriptions](../actions.md#sns:listsubscriptions) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:SetTopicAttributes](../actions.md#sns:settopicattributes) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `sns` | [sns:Unsubscribe](../actions.md#sns:unsubscribe) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
