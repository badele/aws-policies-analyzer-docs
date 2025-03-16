# Policy: DatabaseAdministrator

ARN: `arn:aws:iam::aws:policy/job-function/DatabaseAdministrator`

## Attached Roles

## Attached Services

| Service |
|---------|
| lambda |
| cloudwatch |
| sns |
| logs |
| datapipeline |
| elasticache |
| iam |
| rds |
| redshift |
| ec2 |
| s3 |
| dynamodb |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:DisableAlarmActions](../actions.md#cloudwatch:disablealarmactions) |

| `cloudwatch` | [cloudwatch:EnableAlarmActions](../actions.md#cloudwatch:enablealarmactions) |

| `cloudwatch` | [cloudwatch:Get*](../actions.md#cloudwatch:getall) |

| `cloudwatch` | [cloudwatch:List*](../actions.md#cloudwatch:listall) |

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

| `dynamodb` | [dynamodb:*](../actions.md#dynamodb:all) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `elasticache` | [elasticache:*](../actions.md#elasticache:all) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:ListKeys](../actions.md#kms:listkeys) |

| `lambda` | [lambda:CreateEventSourceMapping](../actions.md#lambda:createeventsourcemapping) |

| `lambda` | [lambda:CreateFunction](../actions.md#lambda:createfunction) |

| `lambda` | [lambda:DeleteEventSourceMapping](../actions.md#lambda:deleteeventsourcemapping) |

| `lambda` | [lambda:DeleteFunction](../actions.md#lambda:deletefunction) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `logs` | [logs:Create*](../actions.md#logs:createall) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `logs` | [logs:PutMetricFilter](../actions.md#logs:putmetricfilter) |

| `rds` | [rds:*](../actions.md#rds:all) |

| `redshift` | [redshift:*](../actions.md#redshift:all) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteObject*](../actions.md#s3:deleteobjectall) |

| `s3` | [s3:Get*](../actions.md#s3:getall) |

| `s3` | [s3:List*](../actions.md#s3:listall) |

| `s3` | [s3:PutAccelerateConfiguration](../actions.md#s3:putaccelerateconfiguration) |

| `s3` | [s3:PutBucketTagging](../actions.md#s3:putbuckettagging) |

| `s3` | [s3:PutBucketVersioning](../actions.md#s3:putbucketversioning) |

| `s3` | [s3:PutBucketWebsite](../actions.md#s3:putbucketwebsite) |

| `s3` | [s3:PutLifecycleConfiguration](../actions.md#s3:putlifecycleconfiguration) |

| `s3` | [s3:PutObject*](../actions.md#s3:putobjectall) |

| `s3` | [s3:PutReplicationConfiguration](../actions.md#s3:putreplicationconfiguration) |

| `s3` | [s3:Replicate*](../actions.md#s3:replicateall) |

| `s3` | [s3:RestoreObject](../actions.md#s3:restoreobject) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:DeleteTopic](../actions.md#sns:deletetopic) |

| `sns` | [sns:Get*](../actions.md#sns:getall) |

| `sns` | [sns:List*](../actions.md#sns:listall) |

| `sns` | [sns:SetTopicAttributes](../actions.md#sns:settopicattributes) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `sns` | [sns:Unsubscribe](../actions.md#sns:unsubscribe) |
