# Policy: AWSBatchServiceRole

ARN: `arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| logs |
| iam |
| ecs |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:CreateAutoScalingGroup](../actions.md#autoscaling:createautoscalinggroup) |

| `autoscaling` | [autoscaling:CreateLaunchConfiguration](../actions.md#autoscaling:createlaunchconfiguration) |

| `autoscaling` | [autoscaling:CreateOrUpdateTags](../actions.md#autoscaling:createorupdatetags) |

| `autoscaling` | [autoscaling:DeleteAutoScalingGroup](../actions.md#autoscaling:deleteautoscalinggroup) |

| `autoscaling` | [autoscaling:DeleteLaunchConfiguration](../actions.md#autoscaling:deletelaunchconfiguration) |

| `autoscaling` | [autoscaling:DescribeAccountLimits](../actions.md#autoscaling:describeaccountlimits) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `autoscaling` | [autoscaling:DescribeAutoScalingInstances](../actions.md#autoscaling:describeautoscalinginstances) |

| `autoscaling` | [autoscaling:DescribeLaunchConfigurations](../actions.md#autoscaling:describelaunchconfigurations) |

| `autoscaling` | [autoscaling:DescribeScalingActivities](../actions.md#autoscaling:describescalingactivities) |

| `autoscaling` | [autoscaling:PutNotificationConfiguration](../actions.md#autoscaling:putnotificationconfiguration) |

| `autoscaling` | [autoscaling:SetDesiredCapacity](../actions.md#autoscaling:setdesiredcapacity) |

| `autoscaling` | [autoscaling:SuspendProcesses](../actions.md#autoscaling:suspendprocesses) |

| `autoscaling` | [autoscaling:TerminateInstanceInAutoScalingGroup](../actions.md#autoscaling:terminateinstanceinautoscalinggroup) |

| `autoscaling` | [autoscaling:UpdateAutoScalingGroup](../actions.md#autoscaling:updateautoscalinggroup) |

| `ec2` | [ec2:CancelSpotFleetRequests](../actions.md#ec2:cancelspotfleetrequests) |

| `ec2` | [ec2:CreateLaunchTemplate](../actions.md#ec2:createlaunchtemplate) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteLaunchTemplate](../actions.md#ec2:deletelaunchtemplate) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeImageAttribute](../actions.md#ec2:describeimageattribute) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstanceAttribute](../actions.md#ec2:describeinstanceattribute) |

| `ec2` | [ec2:DescribeInstanceStatus](../actions.md#ec2:describeinstancestatus) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeKeyPairs](../actions.md#ec2:describekeypairs) |

| `ec2` | [ec2:DescribeLaunchTemplateVersions](../actions.md#ec2:describelaunchtemplateversions) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSpotFleetInstances](../actions.md#ec2:describespotfleetinstances) |

| `ec2` | [ec2:DescribeSpotFleetRequestHistory](../actions.md#ec2:describespotfleetrequesthistory) |

| `ec2` | [ec2:DescribeSpotFleetRequests](../actions.md#ec2:describespotfleetrequests) |

| `ec2` | [ec2:DescribeSpotInstanceRequests](../actions.md#ec2:describespotinstancerequests) |

| `ec2` | [ec2:DescribeSpotPriceHistory](../actions.md#ec2:describespotpricehistory) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcClassicLink](../actions.md#ec2:describevpcclassiclink) |

| `ec2` | [ec2:ModifySpotFleetRequest](../actions.md#ec2:modifyspotfleetrequest) |

| `ec2` | [ec2:RequestSpotFleet](../actions.md#ec2:requestspotfleet) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `ecs` | [ecs:CreateCluster](../actions.md#ecs:createcluster) |

| `ecs` | [ecs:DeleteCluster](../actions.md#ecs:deletecluster) |

| `ecs` | [ecs:DeregisterContainerInstance](../actions.md#ecs:deregistercontainerinstance) |

| `ecs` | [ecs:DeregisterTaskDefinition](../actions.md#ecs:deregistertaskdefinition) |

| `ecs` | [ecs:DescribeClusters](../actions.md#ecs:describeclusters) |

| `ecs` | [ecs:DescribeContainerInstances](../actions.md#ecs:describecontainerinstances) |

| `ecs` | [ecs:DescribeTaskDefinition](../actions.md#ecs:describetaskdefinition) |

| `ecs` | [ecs:DescribeTasks](../actions.md#ecs:describetasks) |

| `ecs` | [ecs:ListAccountSettings](../actions.md#ecs:listaccountsettings) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `ecs` | [ecs:ListContainerInstances](../actions.md#ecs:listcontainerinstances) |

| `ecs` | [ecs:ListTaskDefinitionFamilies](../actions.md#ecs:listtaskdefinitionfamilies) |

| `ecs` | [ecs:ListTaskDefinitions](../actions.md#ecs:listtaskdefinitions) |

| `ecs` | [ecs:ListTasks](../actions.md#ecs:listtasks) |

| `ecs` | [ecs:RegisterTaskDefinition](../actions.md#ecs:registertaskdefinition) |

| `ecs` | [ecs:RunTask](../actions.md#ecs:runtask) |

| `ecs` | [ecs:StartTask](../actions.md#ecs:starttask) |

| `ecs` | [ecs:StopTask](../actions.md#ecs:stoptask) |

| `ecs` | [ecs:TagResource](../actions.md#ecs:tagresource) |

| `ecs` | [ecs:UpdateContainerAgent](../actions.md#ecs:updatecontaineragent) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetInstanceProfile](../actions.md#iam:getinstanceprofile) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |
