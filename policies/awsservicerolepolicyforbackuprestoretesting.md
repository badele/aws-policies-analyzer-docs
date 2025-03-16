# Policy: AWSServiceRolePolicyForBackupRestoreTesting

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupRestoreTesting`

## Attached Roles

## Attached Services

| Service |
|---------|
| backup |
| iam |
| s3 |
| rds |
| fsx |
| redshift |
| ec2 |
| elasticfilesystem |
| dynamodb |
| timestream |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `backup` | [backup:DescribeProtectedResource](../actions.md#backup:describeprotectedresource) |

| `backup` | [backup:DescribeRecoveryPoint](../actions.md#backup:describerecoverypoint) |

| `backup` | [backup:DescribeRestoreJob](../actions.md#backup:describerestorejob) |

| `backup` | [backup:GetRecoveryPointRestoreMetadata](../actions.md#backup:getrecoverypointrestoremetadata) |

| `backup` | [backup:ListBackupVaults](../actions.md#backup:listbackupvaults) |

| `backup` | [backup:ListProtectedResources](../actions.md#backup:listprotectedresources) |

| `backup` | [backup:ListProtectedResourcesByBackupVault](../actions.md#backup:listprotectedresourcesbybackupvault) |

| `backup` | [backup:ListRecoveryPointsByBackupVault](../actions.md#backup:listrecoverypointsbybackupvault) |

| `backup` | [backup:ListRecoveryPointsByResource](../actions.md#backup:listrecoverypointsbyresource) |

| `backup` | [backup:ListTags](../actions.md#backup:listtags) |

| `backup` | [backup:StartRestoreJob](../actions.md#backup:startrestorejob) |

| `dynamodb` | [dynamodb:DeleteTable](../actions.md#dynamodb:deletetable) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `ec2` | [ec2:DeleteVolume](../actions.md#ec2:deletevolume) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSnapshotTierStatus](../actions.md#ec2:describesnapshottierstatus) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `elasticfilesystem` | [elasticfilesystem:DeleteFilesystem](../actions.md#elasticfilesystem:deletefilesystem) |

| `elasticfilesystem` | [elasticfilesystem:DeleteMountTarget](../actions.md#elasticfilesystem:deletemounttarget) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticfilesystem` | [elasticfilesystem:DescribeMountTargets](../actions.md#elasticfilesystem:describemounttargets) |

| `fsx` | [fsx:DeleteFileSystem](../actions.md#fsx:deletefilesystem) |

| `fsx` | [fsx:DeleteVolume](../actions.md#fsx:deletevolume) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `fsx` | [fsx:ListTagsForResource](../actions.md#fsx:listtagsforresource) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `rds` | [rds:DeleteDBCluster](../actions.md#rds:deletedbcluster) |

| `rds` | [rds:DeleteDBInstance](../actions.md#rds:deletedbinstance) |

| `rds` | [rds:DescribeDBClusterAutomatedBackups](../actions.md#rds:describedbclusterautomatedbackups) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstanceAutomatedBackups](../actions.md#rds:describedbinstanceautomatedbackups) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `redshift` | [redshift:DeleteCluster](../actions.md#redshift:deletecluster) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `s3` | [s3:DeleteBucket](../actions.md#s3:deletebucket) |

| `s3` | [s3:GetLifecycleConfiguration](../actions.md#s3:getlifecycleconfiguration) |

| `s3` | [s3:PutLifecycleConfiguration](../actions.md#s3:putlifecycleconfiguration) |

| `timestream` | [timestream:DeleteTable](../actions.md#timestream:deletetable) |
