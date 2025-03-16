# Policy: ElasticLoadBalancingReadOnly

ARN: `arn:aws:iam::aws:policy/ElasticLoadBalancingReadOnly`

## Attached Roles

## Attached Services

| Service |
|---------|
| elasticloadbalancing |
| ec2 |
| arc-zonal-shift |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `arc-zonal-shift` | [arc-zonal-shift:GetManagedResource](../actions.md#arc-zonal-shift:getmanagedresource) |

| `arc-zonal-shift` | [arc-zonal-shift:ListManagedResources](../actions.md#arc-zonal-shift:listmanagedresources) |

| `arc-zonal-shift` | [arc-zonal-shift:ListZonalShifts](../actions.md#arc-zonal-shift:listzonalshifts) |

| `ec2` | [ec2:DescribeClassicLinkInstances](../actions.md#ec2:describeclassiclinkinstances) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:Get*](../actions.md#elasticloadbalancing:getall) |
