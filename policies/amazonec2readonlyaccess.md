# Policy: AmazonEC2ReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| elasticloadbalancing |
| cloudwatch |
| ec2 |
| autoscaling |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:GetSecurityGroupsForVpc](../actions.md#ec2:getsecuritygroupsforvpc) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |
