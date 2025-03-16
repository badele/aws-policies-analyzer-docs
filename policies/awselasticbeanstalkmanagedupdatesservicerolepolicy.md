# Policy: AWSElasticBeanstalkManagedUpdatesServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSElasticBeanstalkManagedUpdatesServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| elasticbeanstalk |
| autoscaling |
| cloudformation |
| logs |
| elasticloadbalancing |
| iam |
| ecs |
| rds |
| ec2 |
| s3 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:AttachInstances](../actions.md#autoscaling:attachinstances) |

| `autoscaling` | [autoscaling:CreateAutoScalingGroup](../actions.md#autoscaling:createautoscalinggroup) |

| `autoscaling` | [autoscaling:CreateLaunchConfiguration](../actions.md#autoscaling:createlaunchconfiguration) |

| `autoscaling` | [autoscaling:CreateOrUpdateTags](../actions.md#autoscaling:createorupdatetags) |

| `autoscaling` | [autoscaling:DeleteAutoScalingGroup](../actions.md#autoscaling:deleteautoscalinggroup) |

| `autoscaling` | [autoscaling:DeleteLaunchConfiguration](../actions.md#autoscaling:deletelaunchconfiguration) |

| `autoscaling` | [autoscaling:DeleteScheduledAction](../actions.md#autoscaling:deletescheduledaction) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `autoscaling` | [autoscaling:DetachInstances](../actions.md#autoscaling:detachinstances) |

| `autoscaling` | [autoscaling:PutNotificationConfiguration](../actions.md#autoscaling:putnotificationconfiguration) |

| `autoscaling` | [autoscaling:PutScalingPolicy](../actions.md#autoscaling:putscalingpolicy) |

| `autoscaling` | [autoscaling:PutScheduledUpdateGroupAction](../actions.md#autoscaling:putscheduledupdategroupaction) |

| `autoscaling` | [autoscaling:ResumeProcesses](../actions.md#autoscaling:resumeprocesses) |

| `autoscaling` | [autoscaling:SuspendProcesses](../actions.md#autoscaling:suspendprocesses) |

| `autoscaling` | [autoscaling:TerminateInstanceInAutoScalingGroup](../actions.md#autoscaling:terminateinstanceinautoscalinggroup) |

| `autoscaling` | [autoscaling:UpdateAutoScalingGroup](../actions.md#autoscaling:updateautoscalinggroup) |

| `cloudformation` | [cloudformation:CancelUpdateStack](../actions.md#cloudformation:cancelupdatestack) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudformation` | [cloudformation:Describe*](../actions.md#cloudformation:describeall) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:List*](../actions.md#cloudformation:listall) |

| `cloudformation` | [cloudformation:TagResource](../actions.md#cloudformation:tagresource) |

| `cloudformation` | [cloudformation:UntagResource](../actions.md#cloudformation:untagresource) |

| `cloudformation` | [cloudformation:UpdateStack](../actions.md#cloudformation:updatestack) |

| `ec2` | [ec2:AssociateAddress](../actions.md#ec2:associateaddress) |

| `ec2` | [ec2:CreateLaunchTemplate](../actions.md#ec2:createlaunchtemplate) |

| `ec2` | [ec2:CreateLaunchTemplateVersion](../actions.md#ec2:createlaunchtemplateversion) |

| `ec2` | [ec2:DeleteLaunchTemplate](../actions.md#ec2:deletelaunchtemplate) |

| `ec2` | [ec2:DeleteLaunchTemplateVersions](../actions.md#ec2:deletelaunchtemplateversions) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DisassociateAddress](../actions.md#ec2:disassociateaddress) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `ec2` | [ec2:allocateAddress](../actions.md#ec2:allocateaddress) |

| `ec2` | [ec2:releaseAddress](../actions.md#ec2:releaseaddress) |

| `ecs` | [ecs:DeRegisterTaskDefinition](../actions.md#ecs:deregistertaskdefinition) |

| `ecs` | [ecs:Describe*](../actions.md#ecs:describeall) |

| `ecs` | [ecs:List*](../actions.md#ecs:listall) |

| `ecs` | [ecs:RegisterTaskDefinition](../actions.md#ecs:registertaskdefinition) |

| `ecs` | [ecs:TagResource](../actions.md#ecs:tagresource) |

| `elasticbeanstalk` | [elasticbeanstalk:*](../actions.md#elasticbeanstalk:all) |

| `elasticloadbalancing` | [elasticloadbalancing:DeRegisterTargets](../actions.md#elasticloadbalancing:deregistertargets) |

| `elasticloadbalancing` | [elasticloadbalancing:DeregisterInstancesFromLoadBalancer](../actions.md#elasticloadbalancing:deregisterinstancesfromloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterInstancesWithLoadBalancer](../actions.md#elasticloadbalancing:registerinstanceswithloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterTargets](../actions.md#elasticloadbalancing:registertargets) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:DeleteLogGroup](../actions.md#logs:deleteloggroup) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:PutRetentionPolicy](../actions.md#logs:putretentionpolicy) |

| `rds` | [rds:DescribeDBEngineVersions](../actions.md#rds:describedbengineversions) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectAcl](../actions.md#s3:getobjectacl) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `s3` | [s3:GetObjectVersionAcl](../actions.md#s3:getobjectversionacl) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:PutObjectAcl](../actions.md#s3:putobjectacl) |

| `s3` | [s3:PutObjectVersionAcl](../actions.md#s3:putobjectversionacl) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:GetTopicAttributes](../actions.md#sns:gettopicattributes) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |
