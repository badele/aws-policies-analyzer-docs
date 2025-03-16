# Policy: AWSPanoramaFullAccess

ARN: `arn:aws:iam::aws:policy/AWSPanoramaFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| secretsmanager |
| cloudwatch |
| logs |
| panorama |
| iam |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `logs` | [logs:Describe*](../actions.md#logs:describeall) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:Get*](../actions.md#logs:getall) |

| `logs` | [logs:List*](../actions.md#logs:listall) |

| `logs` | [logs:StartQuery](../actions.md#logs:startquery) |

| `logs` | [logs:StopQuery](../actions.md#logs:stopquery) |

| `logs` | [logs:TestMetricFilter](../actions.md#logs:testmetricfilter) |

| `panorama` | [panorama:*](../actions.md#panorama:all) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:PutObjectAcl](../actions.md#s3:putobjectacl) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:ListSecretVersionIds](../actions.md#secretsmanager:listsecretversionids) |

| `secretsmanager` | [secretsmanager:PutSecretValue](../actions.md#secretsmanager:putsecretvalue) |

| `secretsmanager` | [secretsmanager:UpdateSecret](../actions.md#secretsmanager:updatesecret) |
