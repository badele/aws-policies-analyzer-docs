# Policy: AmazonSecurityLakeMetastoreManager

ARN: `arn:aws:iam::aws:policy/service-role/AmazonSecurityLakeMetastoreManager`

## Attached Roles

## Attached Services

| Service |
|---------|
| sqs |
| logs |
| glue |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `glue` | [glue:BatchCreatePartition](../actions.md#glue:batchcreatepartition) |

| `glue` | [glue:CreatePartition](../actions.md#glue:createpartition) |

| `glue` | [glue:GetTable](../actions.md#glue:gettable) |

| `glue` | [glue:UpdateTable](../actions.md#glue:updatetable) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `sqs` | [sqs:DeleteMessage](../actions.md#sqs:deletemessage) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:ReceiveMessage](../actions.md#sqs:receivemessage) |
