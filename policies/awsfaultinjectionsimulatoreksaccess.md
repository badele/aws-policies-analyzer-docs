# Policy: AWSFaultInjectionSimulatorEKSAccess

ARN: `arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorEKSAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| ec2 |
| tag |
| eks |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `eks` | [eks:DescribeCluster](../actions.md#eks:describecluster) |

| `eks` | [eks:DescribeNodegroup](../actions.md#eks:describenodegroup) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
