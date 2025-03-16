# Policy: AWSBackupServiceRolePolicyForBackup

ARN: `arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm-sap |
| tag |
| ssm |
| cloudformation |
| storagegateway |
| backup |
| rds |
| fsx |
| backup-gateway |
| timestream |
| redshift |
| ec2 |
| elasticfilesystem |
| dynamodb |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `backup` | [backup:CopyFromBackupVault](../actions.md#backup:copyfrombackupvault) |

| `backup` | [backup:CopyIntoBackupVault](../actions.md#backup:copyintobackupvault) |

| `backup` | [backup:DescribeBackupVault](../actions.md#backup:describebackupvault) |

| `backup` | [backup:TagResource](../actions.md#backup:tagresource) |

| `backup-gateway` | [backup-gateway:Backup](../actions.md#backup-gateway:backup) |

| `backup-gateway` | [backup-gateway:ListTagsForResource](../actions.md#backup-gateway:listtagsforresource) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `dynamodb` | [dynamodb:CreateBackup](../actions.md#dynamodb:createbackup) |

| `dynamodb` | [dynamodb:DeleteBackup](../actions.md#dynamodb:deletebackup) |

| `dynamodb` | [dynamodb:DescribeBackup](../actions.md#dynamodb:describebackup) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:ListTagsOfResource](../actions.md#dynamodb:listtagsofresource) |

| `dynamodb` | [dynamodb:StartAwsBackupJob](../actions.md#dynamodb:startawsbackupjob) |

| `ec2` | [ec2:CopyImage](../actions.md#ec2:copyimage) |

| `ec2` | [ec2:CopySnapshot](../actions.md#ec2:copysnapshot) |

| `ec2` | [ec2:CreateImage](../actions.md#ec2:createimage) |

| `ec2` | [ec2:CreateSnapshot](../actions.md#ec2:createsnapshot) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteSnapshot](../actions.md#ec2:deletesnapshot) |

| `ec2` | [ec2:DeleteSnapshot](../actions.md#ec2:deletesnapshot) |

| `ec2` | [ec2:DeregisterImage](../actions.md#ec2:deregisterimage) |

| `ec2` | [ec2:DescribeElasticGpus](../actions.md#ec2:describeelasticgpus) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstanceAttribute](../actions.md#ec2:describeinstanceattribute) |

| `ec2` | [ec2:DescribeInstanceCreditSpecifications](../actions.md#ec2:describeinstancecreditspecifications) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeNetworkInterfaces](../actions.md#ec2:describenetworkinterfaces) |

| `ec2` | [ec2:DescribeSnapshotTierStatus](../actions.md#ec2:describesnapshottierstatus) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSpotInstanceRequests](../actions.md#ec2:describespotinstancerequests) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:ModifyImageAttribute](../actions.md#ec2:modifyimageattribute) |

| `ec2` | [ec2:ModifySnapshotAttribute](../actions.md#ec2:modifysnapshotattribute) |

| `ec2` | [ec2:ModifySnapshotTier](../actions.md#ec2:modifysnapshottier) |

| `elasticfilesystem` | [elasticfilesystem:Backup](../actions.md#elasticfilesystem:backup) |

| `elasticfilesystem` | [elasticfilesystem:DescribeTags](../actions.md#elasticfilesystem:describetags) |

| `fsx` | [fsx:CopyBackup](../actions.md#fsx:copybackup) |

| `fsx` | [fsx:CreateBackup](../actions.md#fsx:createbackup) |

| `fsx` | [fsx:DeleteBackup](../actions.md#fsx:deletebackup) |

| `fsx` | [fsx:DescribeBackups](../actions.md#fsx:describebackups) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `fsx` | [fsx:ListTagsForResource](../actions.md#fsx:listtagsforresource) |

| `fsx` | [fsx:ListTagsForResource](../actions.md#fsx:listtagsforresource) |

| `fsx` | [fsx:ManageBackupPrincipalAssociations](../actions.md#fsx:managebackupprincipalassociations) |

| `fsx` | [fsx:TagResource](../actions.md#fsx:tagresource) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKeyWithoutPlaintext](../actions.md#kms:generatedatakeywithoutplaintext) |

| `rds` | [rds:AddTagsToResource](../actions.md#rds:addtagstoresource) |

| `rds` | [rds:CopyDBClusterSnapshot](../actions.md#rds:copydbclustersnapshot) |

| `rds` | [rds:CopyDBSnapshot](../actions.md#rds:copydbsnapshot) |

| `rds` | [rds:CreateDBClusterSnapshot](../actions.md#rds:createdbclustersnapshot) |

| `rds` | [rds:CreateDBSnapshot](../actions.md#rds:createdbsnapshot) |

| `rds` | [rds:DeleteDBClusterAutomatedBackup](../actions.md#rds:deletedbclusterautomatedbackup) |

| `rds` | [rds:DeleteDBClusterSnapshot](../actions.md#rds:deletedbclustersnapshot) |

| `rds` | [rds:DeleteDBInstanceAutomatedBackup](../actions.md#rds:deletedbinstanceautomatedbackup) |

| `rds` | [rds:DeleteDBSnapshot](../actions.md#rds:deletedbsnapshot) |

| `rds` | [rds:DescribeDBClusterAutomatedBackups](../actions.md#rds:describedbclusterautomatedbackups) |

| `rds` | [rds:DescribeDBClusterSnapshots](../actions.md#rds:describedbclustersnapshots) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `rds` | [rds:ModifyDBCluster](../actions.md#rds:modifydbcluster) |

| `rds` | [rds:ModifyDBClusterSnapshotAttribute](../actions.md#rds:modifydbclustersnapshotattribute) |

| `rds` | [rds:ModifyDBInstance](../actions.md#rds:modifydbinstance) |

| `rds` | [rds:ModifyDBSnapshotAttribute](../actions.md#rds:modifydbsnapshotattribute) |

| `redshift` | [redshift:CreateClusterSnapshot](../actions.md#redshift:createclustersnapshot) |

| `redshift` | [redshift:CreateTags](../actions.md#redshift:createtags) |

| `redshift` | [redshift:DeleteClusterSnapshot](../actions.md#redshift:deleteclustersnapshot) |

| `redshift` | [redshift:DescribeClusterSnapshots](../actions.md#redshift:describeclustersnapshots) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeTags](../actions.md#redshift:describetags) |

| `ssm` | [ssm:CancelCommand](../actions.md#ssm:cancelcommand) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm-sap` | [ssm-sap:BackupDatabase](../actions.md#ssm-sap:backupdatabase) |

| `ssm-sap` | [ssm-sap:GetDatabase](../actions.md#ssm-sap:getdatabase) |

| `ssm-sap` | [ssm-sap:GetOperation](../actions.md#ssm-sap:getoperation) |

| `ssm-sap` | [ssm-sap:ListDatabases](../actions.md#ssm-sap:listdatabases) |

| `ssm-sap` | [ssm-sap:ListTagsForResource](../actions.md#ssm-sap:listtagsforresource) |

| `ssm-sap` | [ssm-sap:UpdateHanaBackupSettings](../actions.md#ssm-sap:updatehanabackupsettings) |

| `storagegateway` | [storagegateway:CreateSnapshot](../actions.md#storagegateway:createsnapshot) |

| `storagegateway` | [storagegateway:ListTagsForResource](../actions.md#storagegateway:listtagsforresource) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `timestream` | [timestream:DescribeDatabase](../actions.md#timestream:describedatabase) |

| `timestream` | [timestream:DescribeEndpoints](../actions.md#timestream:describeendpoints) |

| `timestream` | [timestream:DescribeTable](../actions.md#timestream:describetable) |

| `timestream` | [timestream:GetAwsBackupStatus](../actions.md#timestream:getawsbackupstatus) |

| `timestream` | [timestream:ListDatabases](../actions.md#timestream:listdatabases) |

| `timestream` | [timestream:ListTables](../actions.md#timestream:listtables) |

| `timestream` | [timestream:ListTagsForResource](../actions.md#timestream:listtagsforresource) |

| `timestream` | [timestream:StartAwsBackupJob](../actions.md#timestream:startawsbackupjob) |
