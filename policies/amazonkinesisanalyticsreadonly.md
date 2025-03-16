# Policy: AmazonKinesisAnalyticsReadOnly

ARN: `arn:aws:iam::aws:policy/AmazonKinesisAnalyticsReadOnly`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudwatch |
| firehose |
| kinesis |
| logs |
| iam |
| kinesisanalytics |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `firehose` | [firehose:DescribeDeliveryStream](../actions.md#firehose:describedeliverystream) |

| `firehose` | [firehose:ListDeliveryStreams](../actions.md#firehose:listdeliverystreams) |

| `iam` | [iam:ListPolicyVersions](../actions.md#iam:listpolicyversions) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `kinesisanalytics` | [kinesisanalytics:Describe*](../actions.md#kinesisanalytics:describeall) |

| `kinesisanalytics` | [kinesisanalytics:Get*](../actions.md#kinesisanalytics:getall) |

| `kinesisanalytics` | [kinesisanalytics:List*](../actions.md#kinesisanalytics:listall) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |
