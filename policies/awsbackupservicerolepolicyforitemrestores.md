# Policy: AWSBackupServiceRolePolicyForItemRestores

ARN: `arn:aws:iam::aws:policy/AWSBackupServiceRolePolicyForItemRestores`

## Attached Roles

## Attached Services

| Service |
|---------|
| s3 |
| ec2 |
| ebs |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ebs` | [ebs:GetSnapshotBlock](../actions.md#ebs:getsnapshotblock) |

| `ebs` | [ebs:ListSnapshotBlocks](../actions.md#ebs:listsnapshotblocks) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListMultipartUploadParts](../actions.md#s3:listmultipartuploadparts) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |
