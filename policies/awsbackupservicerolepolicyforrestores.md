# Policy: AWSBackupServiceRolePolicyForRestores

ARN: `arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForRestores`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudformation |
| storagegateway |
| ebs |
| rds |
| fsx |
| ds |
| backup-gateway |
| redshift |
| timestream |
| ec2 |
| elasticfilesystem |
| dynamodb |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `backup-gateway` | [backup-gateway:Restore](../actions.md#backup-gateway:restore) |

| `cloudformation` | [cloudformation:CreateChangeSet](../actions.md#cloudformation:createchangeset) |

| `cloudformation` | [cloudformation:DescribeChangeSet](../actions.md#cloudformation:describechangeset) |

| `cloudformation` | [cloudformation:TagResource](../actions.md#cloudformation:tagresource) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `dynamodb` | [dynamodb:BatchWriteItem](../actions.md#dynamodb:batchwriteitem) |

| `dynamodb` | [dynamodb:DeleteItem](../actions.md#dynamodb:deleteitem) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:GetItem](../actions.md#dynamodb:getitem) |

| `dynamodb` | [dynamodb:PutItem](../actions.md#dynamodb:putitem) |

| `dynamodb` | [dynamodb:Query](../actions.md#dynamodb:query) |

| `dynamodb` | [dynamodb:RestoreTableFromAwsBackup](../actions.md#dynamodb:restoretablefromawsbackup) |

| `dynamodb` | [dynamodb:RestoreTableFromBackup](../actions.md#dynamodb:restoretablefrombackup) |

| `dynamodb` | [dynamodb:Scan](../actions.md#dynamodb:scan) |

| `dynamodb` | [dynamodb:UpdateItem](../actions.md#dynamodb:updateitem) |

| `ebs` | [ebs:CompleteSnapshot](../actions.md#ebs:completesnapshot) |

| `ebs` | [ebs:PutSnapshotBlock](../actions.md#ebs:putsnapshotblock) |

| `ebs` | [ebs:StartSnapshot](../actions.md#ebs:startsnapshot) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateVolume](../actions.md#ec2:createvolume) |

| `ec2` | [ec2:DeleteSnapshot](../actions.md#ec2:deletesnapshot) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:DeleteVolume](../actions.md#ec2:deletevolume) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSnapshotTierStatus](../actions.md#ec2:describesnapshottierstatus) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:RestoreSnapshotTier](../actions.md#ec2:restoresnapshottier) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `elasticfilesystem` | [elasticfilesystem:CreateFilesystem](../actions.md#elasticfilesystem:createfilesystem) |

| `elasticfilesystem` | [elasticfilesystem:DeleteFilesystem](../actions.md#elasticfilesystem:deletefilesystem) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFilesystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticfilesystem` | [elasticfilesystem:Restore](../actions.md#elasticfilesystem:restore) |

| `elasticfilesystem` | [elasticfilesystem:TagResource](../actions.md#elasticfilesystem:tagresource) |

| `fsx` | [fsx:CreateFileSystemFromBackup](../actions.md#fsx:createfilesystemfrombackup) |

| `fsx` | [fsx:CreateVolumeFromBackup](../actions.md#fsx:createvolumefrombackup) |

| `fsx` | [fsx:CreateVolumeFromBackup](../actions.md#fsx:createvolumefrombackup) |

| `fsx` | [fsx:DeleteFileSystem](../actions.md#fsx:deletefilesystem) |

| `fsx` | [fsx:DeleteVolume](../actions.md#fsx:deletevolume) |

| `fsx` | [fsx:DescribeBackups](../actions.md#fsx:describebackups) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `fsx` | [fsx:TagResource](../actions.md#fsx:tagresource) |

| `fsx` | [fsx:TagResource](../actions.md#fsx:tagresource) |

| `fsx` | [fsx:TagResource](../actions.md#fsx:tagresource) |

| `fsx` | [fsx:UntagResource](../actions.md#fsx:untagresource) |

| `fsx` | [fsx:UntagResource](../actions.md#fsx:untagresource) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:Encrypt](../actions.md#kms:encrypt) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKeyWithoutPlaintext](../actions.md#kms:generatedatakeywithoutplaintext) |

| `kms` | [kms:ReEncryptFrom](../actions.md#kms:reencryptfrom) |

| `kms` | [kms:ReEncryptTo](../actions.md#kms:reencryptto) |

| `rds` | [rds:AddTagsToResource](../actions.md#rds:addtagstoresource) |

| `rds` | [rds:CreateDBInstance](../actions.md#rds:createdbinstance) |

| `rds` | [rds:CreateTenantDatabase](../actions.md#rds:createtenantdatabase) |

| `rds` | [rds:DeleteDBCluster](../actions.md#rds:deletedbcluster) |

| `rds` | [rds:DeleteDBInstance](../actions.md#rds:deletedbinstance) |

| `rds` | [rds:DeleteTenantDatabase](../actions.md#rds:deletetenantdatabase) |

| `rds` | [rds:DescribeDBClusterSnapshots](../actions.md#rds:describedbclustersnapshots) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `rds` | [rds:RestoreDBClusterFromSnapshot](../actions.md#rds:restoredbclusterfromsnapshot) |

| `rds` | [rds:RestoreDBClusterToPointInTime](../actions.md#rds:restoredbclustertopointintime) |

| `rds` | [rds:RestoreDBInstanceFromDBSnapshot](../actions.md#rds:restoredbinstancefromdbsnapshot) |

| `rds` | [rds:RestoreDBInstanceToPointInTime](../actions.md#rds:restoredbinstancetopointintime) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeTableRestoreStatus](../actions.md#redshift:describetablerestorestatus) |

| `redshift` | [redshift:RestoreFromClusterSnapshot](../actions.md#redshift:restorefromclustersnapshot) |

| `redshift` | [redshift:RestoreTableFromClusterSnapshot](../actions.md#redshift:restoretablefromclustersnapshot) |

| `storagegateway` | [storagegateway:AddTagsToResource](../actions.md#storagegateway:addtagstoresource) |

| `storagegateway` | [storagegateway:CreateCachediSCSIVolume](../actions.md#storagegateway:createcachediscsivolume) |

| `storagegateway` | [storagegateway:CreateStorediSCSIVolume](../actions.md#storagegateway:createstorediscsivolume) |

| `storagegateway` | [storagegateway:DeleteVolume](../actions.md#storagegateway:deletevolume) |

| `storagegateway` | [storagegateway:DescribeCachediSCSIVolumes](../actions.md#storagegateway:describecachediscsivolumes) |

| `storagegateway` | [storagegateway:DescribeGatewayInformation](../actions.md#storagegateway:describegatewayinformation) |

| `storagegateway` | [storagegateway:DescribeStorediSCSIVolumes](../actions.md#storagegateway:describestorediscsivolumes) |

| `storagegateway` | [storagegateway:ListVolumes](../actions.md#storagegateway:listvolumes) |

| `timestream` | [timestream:DescribeDatabase](../actions.md#timestream:describedatabase) |

| `timestream` | [timestream:DescribeEndpoints](../actions.md#timestream:describeendpoints) |

| `timestream` | [timestream:DescribeTable](../actions.md#timestream:describetable) |

| `timestream` | [timestream:GetAwsRestoreStatus](../actions.md#timestream:getawsrestorestatus) |

| `timestream` | [timestream:ListDatabases](../actions.md#timestream:listdatabases) |

| `timestream` | [timestream:ListTables](../actions.md#timestream:listtables) |

| `timestream` | [timestream:ListTagsForResource](../actions.md#timestream:listtagsforresource) |

| `timestream` | [timestream:StartAwsRestoreJob](../actions.md#timestream:startawsrestorejob) |
