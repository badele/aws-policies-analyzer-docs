# Policy: AWSBackupOperatorAccess

ARN: `arn:aws:iam::aws:policy/AWSBackupOperatorAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| backup |
| rds |
| fsx |
| backup-gateway |
| cloudformation |
| ds |
| ec2 |
| tag |
| s3 |
| storagegateway |
| iam |
| elasticfilesystem |
| timestream |
| ssm-sap |
| cloudwatch |
| ram |
| organizations |
| redshift |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `backup` | [backup:CreateBackupSelection](../actions.md#backup:createbackupselection) |

| `backup` | [backup:DeleteBackupSelection](../actions.md#backup:deletebackupselection) |

| `backup` | [backup:Describe*](../actions.md#backup:describeall) |

| `backup` | [backup:Get*](../actions.md#backup:getall) |

| `backup` | [backup:List*](../actions.md#backup:listall) |

| `backup` | [backup:StartBackupJob](../actions.md#backup:startbackupjob) |

| `backup` | [backup:StartCopyJob](../actions.md#backup:startcopyjob) |

| `backup` | [backup:StartRestoreJob](../actions.md#backup:startrestorejob) |

| `backup-gateway` | [backup-gateway:GetBandwidthRateLimitSchedule](../actions.md#backup-gateway:getbandwidthratelimitschedule) |

| `backup-gateway` | [backup-gateway:GetGateway](../actions.md#backup-gateway:getgateway) |

| `backup-gateway` | [backup-gateway:GetHypervisor](../actions.md#backup-gateway:gethypervisor) |

| `backup-gateway` | [backup-gateway:GetHypervisorPropertyMappings](../actions.md#backup-gateway:gethypervisorpropertymappings) |

| `backup-gateway` | [backup-gateway:GetVirtualMachine](../actions.md#backup-gateway:getvirtualmachine) |

| `backup-gateway` | [backup-gateway:ListGateways](../actions.md#backup-gateway:listgateways) |

| `backup-gateway` | [backup-gateway:ListHypervisors](../actions.md#backup-gateway:listhypervisors) |

| `backup-gateway` | [backup-gateway:ListTagsForResource](../actions.md#backup-gateway:listtagsforresource) |

| `backup-gateway` | [backup-gateway:ListVirtualMachines](../actions.md#backup-gateway:listvirtualmachines) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `dynamodb` | [dynamodb:ListBackups](../actions.md#dynamodb:listbackups) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstanceTypes](../actions.md#ec2:describeinstancetypes) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribePlacementGroups](../actions.md#ec2:describeplacementgroups) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:describeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFilesystems](../actions.md#elasticfilesystem:describefilesystems) |

| `fsx` | [fsx:DescribeBackups](../actions.md#fsx:describebackups) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeStorageVirtualMachines](../actions.md#fsx:describestoragevirtualmachines) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `ram` | [ram:GetResourceShareAssociations](../actions.md#ram:getresourceshareassociations) |

| `rds` | [rds:DescribeDBClusterAutomatedBackups](../actions.md#rds:describedbclusterautomatedbackups) |

| `rds` | [rds:DescribeDBClusterParameterGroups](../actions.md#rds:describedbclusterparametergroups) |

| `rds` | [rds:DescribeDBClusterSnapshots](../actions.md#rds:describedbclustersnapshots) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstanceAutomatedBackups](../actions.md#rds:describedbinstanceautomatedbackups) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBParameterGroups](../actions.md#rds:describedbparametergroups) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `rds` | [rds:describeDBEngineVersions](../actions.md#rds:describedbengineversions) |

| `rds` | [rds:describeDBSubnetGroups](../actions.md#rds:describedbsubnetgroups) |

| `rds` | [rds:describeOptionGroups](../actions.md#rds:describeoptiongroups) |

| `rds` | [rds:describeOrderableDBInstanceOptions](../actions.md#rds:describeorderabledbinstanceoptions) |

| `redshift` | [redshift:DescribeClusterParameterGroups](../actions.md#redshift:describeclusterparametergroups) |

| `redshift` | [redshift:DescribeClusterSnapshots](../actions.md#redshift:describeclustersnapshots) |

| `redshift` | [redshift:DescribeClusterSubnetGroups](../actions.md#redshift:describeclustersubnetgroups) |

| `redshift` | [redshift:DescribeClusterTracks](../actions.md#redshift:describeclustertracks) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeNodeConfigurationOptions](../actions.md#redshift:describenodeconfigurationoptions) |

| `redshift` | [redshift:DescribeOrderableClusterOptions](../actions.md#redshift:describeorderableclusteroptions) |

| `redshift` | [redshift:DescribeSnapshotSchedules](../actions.md#redshift:describesnapshotschedules) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `ssm` | [ssm:CancelCommand](../actions.md#ssm:cancelcommand) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm-sap` | [ssm-sap:GetDatabase](../actions.md#ssm-sap:getdatabase) |

| `ssm-sap` | [ssm-sap:GetOperation](../actions.md#ssm-sap:getoperation) |

| `ssm-sap` | [ssm-sap:ListDatabases](../actions.md#ssm-sap:listdatabases) |

| `ssm-sap` | [ssm-sap:ListTagsForResource](../actions.md#ssm-sap:listtagsforresource) |

| `storagegateway` | [storagegateway:DescribeCachediSCSIVolumes](../actions.md#storagegateway:describecachediscsivolumes) |

| `storagegateway` | [storagegateway:DescribeGatewayInformation](../actions.md#storagegateway:describegatewayinformation) |

| `storagegateway` | [storagegateway:DescribeStorediSCSIVolumes](../actions.md#storagegateway:describestorediscsivolumes) |

| `storagegateway` | [storagegateway:ListGateways](../actions.md#storagegateway:listgateways) |

| `storagegateway` | [storagegateway:ListLocalDisks](../actions.md#storagegateway:listlocaldisks) |

| `storagegateway` | [storagegateway:ListVolumes](../actions.md#storagegateway:listvolumes) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `tag` | [tag:GetTagKeys](../actions.md#tag:gettagkeys) |

| `tag` | [tag:GetTagValues](../actions.md#tag:gettagvalues) |

| `timestream` | [timestream:DescribeEndpoints](../actions.md#timestream:describeendpoints) |

| `timestream` | [timestream:ListDatabases](../actions.md#timestream:listdatabases) |

| `timestream` | [timestream:ListTables](../actions.md#timestream:listtables) |
