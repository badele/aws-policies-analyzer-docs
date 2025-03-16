# Policy: ServiceQuotasFullAccess

ARN: `arn:aws:iam::aws:policy/ServiceQuotasFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| servicequotas |
| cloudformation |
| route53 |
| cloudwatch |
| kinesis |
| elasticloadbalancing |
| iam |
| organizations |
| rds |
| tag |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:DescribeAccountLimits](../actions.md#autoscaling:describeaccountlimits) |

| `cloudformation` | [cloudformation:DescribeAccountLimits](../actions.md#cloudformation:describeaccountlimits) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarmsForMetric](../actions.md#cloudwatch:describealarmsformetric) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `dynamodb` | [dynamodb:DescribeLimits](../actions.md#dynamodb:describelimits) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeAccountLimits](../actions.md#elasticloadbalancing:describeaccountlimits) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetAccountSummary](../actions.md#iam:getaccountsummary) |

| `kinesis` | [kinesis:DescribeLimits](../actions.md#kinesis:describelimits) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:EnableAWSServiceAccess](../actions.md#organizations:enableawsserviceaccess) |

| `organizations` | [organizations:ListAWSServiceAccessForOrganization](../actions.md#organizations:listawsserviceaccessfororganization) |

| `rds` | [rds:DescribeAccountAttributes](../actions.md#rds:describeaccountattributes) |

| `route53` | [route53:GetAccountLimit](../actions.md#route53:getaccountlimit) |

| `servicequotas` | [servicequotas:*](../actions.md#servicequotas:all) |

| `tag` | [tag:GetTagKeys](../actions.md#tag:gettagkeys) |

| `tag` | [tag:GetTagValues](../actions.md#tag:gettagvalues) |
