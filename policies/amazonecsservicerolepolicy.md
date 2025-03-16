# Policy: AmazonECSServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AmazonECSServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| events |
| ssm |
| route53 |
| cloudwatch |
| servicediscovery |
| logs |
| autoscaling-plans |
| elasticloadbalancing |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:CompleteLifecycleAction](../actions.md#autoscaling:completelifecycleaction) |

| `autoscaling` | [autoscaling:DeleteLifecycleHook](../actions.md#autoscaling:deletelifecyclehook) |

| `autoscaling` | [autoscaling:DeletePolicy](../actions.md#autoscaling:deletepolicy) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `autoscaling` | [autoscaling:PutLifecycleHook](../actions.md#autoscaling:putlifecyclehook) |

| `autoscaling` | [autoscaling:PutScalingPolicy](../actions.md#autoscaling:putscalingpolicy) |

| `autoscaling` | [autoscaling:RecordLifecycleActionHeartbeat](../actions.md#autoscaling:recordlifecycleactionheartbeat) |

| `autoscaling` | [autoscaling:SetInstanceProtection](../actions.md#autoscaling:setinstanceprotection) |

| `autoscaling` | [autoscaling:UpdateAutoScalingGroup](../actions.md#autoscaling:updateautoscalinggroup) |

| `autoscaling-plans` | [autoscaling-plans:CreateScalingPlan](../actions.md#autoscaling-plans:createscalingplan) |

| `autoscaling-plans` | [autoscaling-plans:DeleteScalingPlan](../actions.md#autoscaling-plans:deletescalingplan) |

| `autoscaling-plans` | [autoscaling-plans:DescribeScalingPlanResources](../actions.md#autoscaling-plans:describescalingplanresources) |

| `autoscaling-plans` | [autoscaling-plans:DescribeScalingPlans](../actions.md#autoscaling-plans:describescalingplans) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ec2` | [ec2:AttachNetworkInterface](../actions.md#ec2:attachnetworkinterface) |

| `ec2` | [ec2:CreateNetworkInterface](../actions.md#ec2:createnetworkinterface) |

| `ec2` | [ec2:CreateNetworkInterfacePermission](../actions.md#ec2:createnetworkinterfacepermission) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteNetworkInterface](../actions.md#ec2:deletenetworkinterface) |

| `ec2` | [ec2:DeleteNetworkInterfacePermission](../actions.md#ec2:deletenetworkinterfacepermission) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DetachNetworkInterface](../actions.md#ec2:detachnetworkinterface) |

| `elasticloadbalancing` | [elasticloadbalancing:DeregisterInstancesFromLoadBalancer](../actions.md#elasticloadbalancing:deregisterinstancesfromloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:DeregisterTargets](../actions.md#elasticloadbalancing:deregistertargets) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterInstancesWithLoadBalancer](../actions.md#elasticloadbalancing:registerinstanceswithloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterTargets](../actions.md#elasticloadbalancing:registertargets) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `logs` | [logs:PutRetentionPolicy](../actions.md#logs:putretentionpolicy) |

| `route53` | [route53:ChangeResourceRecordSets](../actions.md#route53:changeresourcerecordsets) |

| `route53` | [route53:CreateHealthCheck](../actions.md#route53:createhealthcheck) |

| `route53` | [route53:DeleteHealthCheck](../actions.md#route53:deletehealthcheck) |

| `route53` | [route53:Get*](../actions.md#route53:getall) |

| `route53` | [route53:List*](../actions.md#route53:listall) |

| `route53` | [route53:UpdateHealthCheck](../actions.md#route53:updatehealthcheck) |

| `servicediscovery` | [servicediscovery:CreateHttpNamespace](../actions.md#servicediscovery:createhttpnamespace) |

| `servicediscovery` | [servicediscovery:CreateService](../actions.md#servicediscovery:createservice) |

| `servicediscovery` | [servicediscovery:DeleteService](../actions.md#servicediscovery:deleteservice) |

| `servicediscovery` | [servicediscovery:DeregisterInstance](../actions.md#servicediscovery:deregisterinstance) |

| `servicediscovery` | [servicediscovery:DiscoverInstances](../actions.md#servicediscovery:discoverinstances) |

| `servicediscovery` | [servicediscovery:DiscoverInstancesRevision](../actions.md#servicediscovery:discoverinstancesrevision) |

| `servicediscovery` | [servicediscovery:Get*](../actions.md#servicediscovery:getall) |

| `servicediscovery` | [servicediscovery:List*](../actions.md#servicediscovery:listall) |

| `servicediscovery` | [servicediscovery:RegisterInstance](../actions.md#servicediscovery:registerinstance) |

| `servicediscovery` | [servicediscovery:TagResource](../actions.md#servicediscovery:tagresource) |

| `servicediscovery` | [servicediscovery:UpdateInstanceCustomHealthStatus](../actions.md#servicediscovery:updateinstancecustomhealthstatus) |

| `ssm` | [ssm:DescribeSessions](../actions.md#ssm:describesessions) |

| `ssm` | [ssm:StartSession](../actions.md#ssm:startsession) |
