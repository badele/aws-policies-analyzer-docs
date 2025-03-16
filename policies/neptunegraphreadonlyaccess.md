# Policy: NeptuneGraphReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/NeptuneGraphReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudwatch |
| logs |
| neptune-graph |
| ec2 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcAttribute](../actions.md#ec2:describevpcattribute) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `kms` | [kms:ListKeys](../actions.md#kms:listkeys) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `neptune-graph` | [neptune-graph:Get*](../actions.md#neptune-graph:getall) |

| `neptune-graph` | [neptune-graph:List*](../actions.md#neptune-graph:listall) |

| `neptune-graph` | [neptune-graph:Read*](../actions.md#neptune-graph:readall) |
