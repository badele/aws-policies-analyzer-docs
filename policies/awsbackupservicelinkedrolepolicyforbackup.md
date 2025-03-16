# Policy: AWSBackupServiceLinkedRolePolicyForBackup

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSBackupServiceLinkedRolePolicyForBackup`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm-sap |
| events |
| cloudformation |
| storagegateway |
| backup |
| redshift |
| s3 |
| elasticfilesystem |
| rds |
| fsx |
| backup-gateway |
| timestream |
| ec2 |
| tag |
| dynamodb |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `backup` | [backup:TagResource](../actions.md#backup:tagresource) |

| `backup-gateway` | [backup-gateway:ListTagsForResource](../actions.md#backup-gateway:listtagsforresource) |

| `backup-gateway` | [backup-gateway:ListVirtualMachines](../actions.md#backup-gateway:listvirtualmachines) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `dynamodb` | [dynamodb:DeleteBackup](../actions.md#dynamodb:deletebackup) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `dynamodb` | [dynamodb:ListTagsOfResource](../actions.md#dynamodb:listtagsofresource) |

| `ec2` | [ec2:CopyImage](../actions.md#ec2:copyimage) |

| `ec2` | [ec2:CopySnapshot](../actions.md#ec2:copysnapshot) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteSnapshot](../actions.md#ec2:deletesnapshot) |

| `ec2` | [ec2:DeregisterImage](../actions.md#ec2:deregisterimage) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSnapshotTierStatus](../actions.md#ec2:describesnapshottierstatus) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:ModifySnapshotTier](../actions.md#ec2:modifysnapshottier) |

| `elasticfilesystem` | [elasticfilesystem:Backup](../actions.md#elasticfilesystem:backup) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticfilesystem` | [elasticfilesystem:DescribeTags](../actions.md#elasticfilesystem:describetags) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:DisableRule](../actions.md#events:disablerule) |

| `events` | [events:EnableRule](../actions.md#events:enablerule) |

| `events` | [events:ListRules](../actions.md#events:listrules) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `fsx` | [fsx:CopyBackup](../actions.md#fsx:copybackup) |

| `fsx` | [fsx:DeleteBackup](../actions.md#fsx:deletebackup) |

| `fsx` | [fsx:DescribeBackups](../actions.md#fsx:describebackups) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `fsx` | [fsx:TagResource](../actions.md#fsx:tagresource) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:GenerateDataKeyWithoutPlaintext](../actions.md#kms:generatedatakeywithoutplaintext) |

| `kms` | [kms:ListGrants](../actions.md#kms:listgrants) |

| `kms` | [kms:ReEncryptFrom](../actions.md#kms:reencryptfrom) |

| `rds` | [rds:AddTagsToResource](../actions.md#rds:addtagstoresource) |

| `rds` | [rds:AddTagsToResource](../actions.md#rds:addtagstoresource) |

| `rds` | [rds:AddTagsToResource](../actions.md#rds:addtagstoresource) |

| `rds` | [rds:CopyDBClusterSnapshot](../actions.md#rds:copydbclustersnapshot) |

| `rds` | [rds:CopyDBSnapshot](../actions.md#rds:copydbsnapshot) |

| `rds` | [rds:DeleteDBClusterSnapshot](../actions.md#rds:deletedbclustersnapshot) |

| `rds` | [rds:DeleteDBInstanceAutomatedBackup](../actions.md#rds:deletedbinstanceautomatedbackup) |

| `rds` | [rds:DeleteDBSnapshot](../actions.md#rds:deletedbsnapshot) |

| `rds` | [rds:DescribeDBClusterSnapshots](../actions.md#rds:describedbclustersnapshots) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `redshift` | [redshift:DeleteClusterSnapshot](../actions.md#redshift:deleteclustersnapshot) |

| `redshift` | [redshift:DescribeClusterSnapshots](../actions.md#redshift:describeclustersnapshots) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeTags](../actions.md#redshift:describetags) |

| `s3` | [s3:GetBucketTagging](../actions.md#s3:getbuckettagging) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `ssm-sap` | [ssm-sap:GetOperation](../actions.md#ssm-sap:getoperation) |

| `ssm-sap` | [ssm-sap:UpdateHANABackupSettings](../actions.md#ssm-sap:updatehanabackupsettings) |

| `storagegateway` | [storagegateway:DescribeCachediSCSIVolumes](../actions.md#storagegateway:describecachediscsivolumes) |

| `storagegateway` | [storagegateway:DescribeStorediSCSIVolumes](../actions.md#storagegateway:describestorediscsivolumes) |

| `storagegateway` | [storagegateway:ListVolumes](../actions.md#storagegateway:listvolumes) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `timestream` | [timestream:DescribeDatabase](../actions.md#timestream:describedatabase) |

| `timestream` | [timestream:DescribeEndpoints](../actions.md#timestream:describeendpoints) |

| `timestream` | [timestream:DescribeTable](../actions.md#timestream:describetable) |

| `timestream` | [timestream:GetAwsBackupStatus](../actions.md#timestream:getawsbackupstatus) |

| `timestream` | [timestream:GetAwsRestoreStatus](../actions.md#timestream:getawsrestorestatus) |

| `timestream` | [timestream:ListDatabases](../actions.md#timestream:listdatabases) |

| `timestream` | [timestream:ListTables](../actions.md#timestream:listtables) |

| `timestream` | [timestream:ListTagsForResource](../actions.md#timestream:listtagsforresource) |
