# Policy: VPCLatticeFullAccess

ARN: `arn:aws:iam::aws:policy/VPCLatticeFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| lambda |
| cloudwatch |
| acm |
| vpc-lattice |
| firehose |
| logs |
| elasticloadbalancing |
| iam |
| rds |
| ec2 |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:DescribeCertificate](../actions.md#acm:describecertificate) |

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcAttribute](../actions.md#ec2:describevpcattribute) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `firehose` | [firehose:DescribeDeliveryStream](../actions.md#firehose:describedeliverystream) |

| `firehose` | [firehose:ListDeliveryStreams](../actions.md#firehose:listdeliverystreams) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:DeleteServiceLinkedRole](../actions.md#iam:deleteservicelinkedrole) |

| `iam` | [iam:GetServiceLinkedRoleDeletionStatus](../actions.md#iam:getservicelinkedroledeletionstatus) |

| `lambda` | [lambda:ListAliases](../actions.md#lambda:listaliases) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `lambda` | [lambda:ListVersionsByFunction](../actions.md#lambda:listversionsbyfunction) |

| `logs` | [logs:CreateLogDelivery](../actions.md#logs:createlogdelivery) |

| `logs` | [logs:DeleteLogDelivery](../actions.md#logs:deletelogdelivery) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeResourcePolicies](../actions.md#logs:describeresourcepolicies) |

| `logs` | [logs:GetLogDelivery](../actions.md#logs:getlogdelivery) |

| `logs` | [logs:ListLogDeliveries](../actions.md#logs:listlogdeliveries) |

| `logs` | [logs:UpdateLogDelivery](../actions.md#logs:updatelogdelivery) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `vpc-lattice` | [vpc-lattice:*](../actions.md#vpc-lattice:all) |
