# Policy: CloudWatchAgentServerPolicy

ARN: `arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| cloudwatch |
| logs |
| xray |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `logs` | [logs:PutRetentionPolicy](../actions.md#logs:putretentionpolicy) |

| `ssm` | [ssm:GetParameter](../actions.md#ssm:getparameter) |

| `xray` | [xray:GetSamplingRules](../actions.md#xray:getsamplingrules) |

| `xray` | [xray:GetSamplingStatisticSummaries](../actions.md#xray:getsamplingstatisticsummaries) |

| `xray` | [xray:GetSamplingTargets](../actions.md#xray:getsamplingtargets) |

| `xray` | [xray:PutTelemetryRecords](../actions.md#xray:puttelemetryrecords) |

| `xray` | [xray:PutTraceSegments](../actions.md#xray:puttracesegments) |
