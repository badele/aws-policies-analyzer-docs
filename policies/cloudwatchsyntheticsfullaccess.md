# Policy: CloudWatchSyntheticsFullAccess

ARN: `arn:aws:iam::aws:policy/CloudWatchSyntheticsFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| apigateway |
| lambda |
| cloudwatch |
| logs |
| iam |
| xray |
| synthetics |
| ec2 |
| s3 |
| sns |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `lambda` | [lambda:AddPermission](../actions.md#lambda:addpermission) |

| `lambda` | [lambda:CreateFunction](../actions.md#lambda:createfunction) |

| `lambda` | [lambda:DeleteFunction](../actions.md#lambda:deletefunction) |

| `lambda` | [lambda:DeleteLayerVersion](../actions.md#lambda:deletelayerversion) |

| `lambda` | [lambda:GetFunction](../actions.md#lambda:getfunction) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:GetLayerVersion](../actions.md#lambda:getlayerversion) |

| `lambda` | [lambda:ListTags](../actions.md#lambda:listtags) |

| `lambda` | [lambda:PublishLayerVersion](../actions.md#lambda:publishlayerversion) |

| `lambda` | [lambda:PublishVersion](../actions.md#lambda:publishversion) |

| `lambda` | [lambda:TagResource](../actions.md#lambda:tagresource) |

| `lambda` | [lambda:UntagResource](../actions.md#lambda:untagresource) |

| `lambda` | [lambda:UpdateFunctionCode](../actions.md#lambda:updatefunctioncode) |

| `lambda` | [lambda:UpdateFunctionConfiguration](../actions.md#lambda:updatefunctionconfiguration) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `logs` | [logs:GetLogGroupFields](../actions.md#logs:getloggroupfields) |

| `logs` | [logs:GetLogRecord](../actions.md#logs:getlogrecord) |

| `logs` | [logs:StartQuery](../actions.md#logs:startquery) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutEncryptionConfiguration](../actions.md#s3:putencryptionconfiguration) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `synthetics` | [synthetics:*](../actions.md#synthetics:all) |

| `xray` | [xray:BatchGetTraces](../actions.md#xray:batchgettraces) |

| `xray` | [xray:GetTraceSummaries](../actions.md#xray:gettracesummaries) |
