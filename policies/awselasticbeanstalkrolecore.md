# Policy: AWSElasticBeanstalkRoleCore

ARN: `arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkRoleCore`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| cloudformation |
| cloudwatch |
| acm |
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

| `acm` | [acm:Describe*](../actions.md#acm:describeall) |

| `acm` | [acm:List*](../actions.md#acm:listall) |

| `autoscaling` | [autoscaling:*AutoScalingGroup](../actions.md#autoscaling:allautoscalinggroup) |

| `autoscaling` | [autoscaling:*LaunchConfiguration](../actions.md#autoscaling:alllaunchconfiguration) |

| `autoscaling` | [autoscaling:*LoadBalancer*](../actions.md#autoscaling:allloadbalancerall) |

| `autoscaling` | [autoscaling:*Tags](../actions.md#autoscaling:alltags) |

| `autoscaling` | [autoscaling:AttachInstances](../actions.md#autoscaling:attachinstances) |

| `autoscaling` | [autoscaling:DeletePolicy](../actions.md#autoscaling:deletepolicy) |

| `autoscaling` | [autoscaling:DeleteScheduledAction](../actions.md#autoscaling:deletescheduledaction) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `autoscaling` | [autoscaling:DetachInstances](../actions.md#autoscaling:detachinstances) |

| `autoscaling` | [autoscaling:PutNotificationConfiguration](../actions.md#autoscaling:putnotificationconfiguration) |

| `autoscaling` | [autoscaling:PutScalingPolicy](../actions.md#autoscaling:putscalingpolicy) |

| `autoscaling` | [autoscaling:PutScheduledUpdateGroupAction](../actions.md#autoscaling:putscheduledupdategroupaction) |

| `autoscaling` | [autoscaling:ResumeProcesses](../actions.md#autoscaling:resumeprocesses) |

| `autoscaling` | [autoscaling:SuspendProcesses](../actions.md#autoscaling:suspendprocesses) |

| `cloudformation` | [cloudformation:CancelUpdateStack](../actions.md#cloudformation:cancelupdatestack) |

| `cloudformation` | [cloudformation:ContinueUpdateRollback](../actions.md#cloudformation:continueupdaterollback) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudformation` | [cloudformation:Describe*](../actions.md#cloudformation:describeall) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:TagResource](../actions.md#cloudformation:tagresource) |

| `cloudformation` | [cloudformation:UntagResource](../actions.md#cloudformation:untagresource) |

| `cloudformation` | [cloudformation:UpdateStack](../actions.md#cloudformation:updatestack) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ec2` | [ec2:AllocateAddress](../actions.md#ec2:allocateaddress) |

| `ec2` | [ec2:AssociateAddress](../actions.md#ec2:associateaddress) |

| `ec2` | [ec2:AuthorizeSecurityGroup*](../actions.md#ec2:authorizesecuritygroupall) |

| `ec2` | [ec2:CreateLaunchTemplate*](../actions.md#ec2:createlaunchtemplateall) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteLaunchTemplate*](../actions.md#ec2:deletelaunchtemplateall) |

| `ec2` | [ec2:DeleteSecurityGroup](../actions.md#ec2:deletesecuritygroup) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DisassociateAddress](../actions.md#ec2:disassociateaddress) |

| `ec2` | [ec2:ReleaseAddress](../actions.md#ec2:releaseaddress) |

| `ec2` | [ec2:RevokeSecurityGroup*](../actions.md#ec2:revokesecuritygroupall) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `ecs` | [ecs:Describe*](../actions.md#ecs:describeall) |

| `ecs` | [ecs:List*](../actions.md#ecs:listall) |

| `elasticloadbalancing` | [elasticloadbalancing:*Tags](../actions.md#elasticloadbalancing:alltags) |

| `elasticloadbalancing` | [elasticloadbalancing:ConfigureHealthCheck](../actions.md#elasticloadbalancing:configurehealthcheck) |

| `elasticloadbalancing` | [elasticloadbalancing:Create*](../actions.md#elasticloadbalancing:createall) |

| `elasticloadbalancing` | [elasticloadbalancing:DeRegisterTargets](../actions.md#elasticloadbalancing:deregistertargets) |

| `elasticloadbalancing` | [elasticloadbalancing:Delete*](../actions.md#elasticloadbalancing:deleteall) |

| `elasticloadbalancing` | [elasticloadbalancing:DeregisterInstancesFromLoadBalancer](../actions.md#elasticloadbalancing:deregisterinstancesfromloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:Modify*](../actions.md#elasticloadbalancing:modifyall) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterInstancesWithLoadBalancer](../actions.md#elasticloadbalancing:registerinstanceswithloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterTargets](../actions.md#elasticloadbalancing:registertargets) |

| `elasticloadbalancing` | [elasticloadbalancing:SetLoadBalancerPoliciesOfListener](../actions.md#elasticloadbalancing:setloadbalancerpoliciesoflistener) |

| `elasticloadbalancing` | [elasticloadbalancing:SetRulePriorities](../actions.md#elasticloadbalancing:setrulepriorities) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:List*](../actions.md#iam:listall) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `logs` | [logs:Describe*](../actions.md#logs:describeall) |

| `rds` | [rds:Describe*](../actions.md#rds:describeall) |

| `s3` | [s3:Delete*](../actions.md#s3:deleteall) |

| `s3` | [s3:Get*](../actions.md#s3:getall) |

| `s3` | [s3:GetBucket*](../actions.md#s3:getbucketall) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:Put*](../actions.md#s3:putall) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `sns` | [sns:List*](../actions.md#sns:listall) |
