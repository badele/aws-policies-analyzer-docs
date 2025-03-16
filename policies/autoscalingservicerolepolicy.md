# Policy: AutoScalingServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AutoScalingServiceRolePolicy`

## Attached Roles

| Role Name |
|-----------|
## Attached Services

| Service |
|---------|
| events |
| ssm |
| resource-groups |
| cloudwatch |
| vpc-lattice |
| elasticloadbalancing |
| iam |
| ec2 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ec2` | [ec2:AttachClassicLinkVpc](../actions.md#ec2:attachclassiclinkvpc) |

| `ec2` | [ec2:CancelSpotInstanceRequests](../actions.md#ec2:cancelspotinstancerequests) |

| `ec2` | [ec2:CreateFleet](../actions.md#ec2:createfleet) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DetachClassicLinkVpc](../actions.md#ec2:detachclassiclinkvpc) |

| `ec2` | [ec2:GetInstanceTypesFromInstanceRequirements](../actions.md#ec2:getinstancetypesfrominstancerequirements) |

| `ec2` | [ec2:GetSecurityGroupsForVpc](../actions.md#ec2:getsecuritygroupsforvpc) |

| `ec2` | [ec2:ModifyInstanceAttribute](../actions.md#ec2:modifyinstanceattribute) |

| `ec2` | [ec2:RequestSpotInstances](../actions.md#ec2:requestspotinstances) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:StartInstances](../actions.md#ec2:startinstances) |

| `ec2` | [ec2:StopInstances](../actions.md#ec2:stopinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `elasticloadbalancing` | [elasticloadbalancing:Deregister*](../actions.md#elasticloadbalancing:deregisterall) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:Register*](../actions.md#elasticloadbalancing:registerall) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `vpc-lattice` | [vpc-lattice:DeregisterTargets](../actions.md#vpc-lattice:deregistertargets) |

| `vpc-lattice` | [vpc-lattice:GetTargetGroup](../actions.md#vpc-lattice:gettargetgroup) |

| `vpc-lattice` | [vpc-lattice:ListTargetGroups](../actions.md#vpc-lattice:listtargetgroups) |

| `vpc-lattice` | [vpc-lattice:ListTargets](../actions.md#vpc-lattice:listtargets) |

| `vpc-lattice` | [vpc-lattice:RegisterTargets](../actions.md#vpc-lattice:registertargets) |
