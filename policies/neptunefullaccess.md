# Policy: NeptuneFullAccess

ARN: `arn:aws:iam::aws:policy/NeptuneFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| neptune-db |
| cloudwatch |
| sns |
| logs |
| iam |
| rds |
| ec2 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcAttribute](../actions.md#ec2:describevpcattribute) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `kms` | [kms:ListKeyPolicies](../actions.md#kms:listkeypolicies) |

| `kms` | [kms:ListKeys](../actions.md#kms:listkeys) |

| `kms` | [kms:ListRetirableGrants](../actions.md#kms:listretirablegrants) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `neptune-db` | [neptune-db:*](../actions.md#neptune-db:all) |

| `rds` | [rds:AddRoleToDBCluster](../actions.md#rds:addroletodbcluster) |

| `rds` | [rds:AddSourceIdentifierToSubscription](../actions.md#rds:addsourceidentifiertosubscription) |

| `rds` | [rds:AddTagsToResource](../actions.md#rds:addtagstoresource) |

| `rds` | [rds:ApplyPendingMaintenanceAction](../actions.md#rds:applypendingmaintenanceaction) |

| `rds` | [rds:CopyDBClusterParameterGroup](../actions.md#rds:copydbclusterparametergroup) |

| `rds` | [rds:CopyDBClusterSnapshot](../actions.md#rds:copydbclustersnapshot) |

| `rds` | [rds:CopyDBParameterGroup](../actions.md#rds:copydbparametergroup) |

| `rds` | [rds:CreateDBCluster](../actions.md#rds:createdbcluster) |

| `rds` | [rds:CreateDBClusterEndpoint](../actions.md#rds:createdbclusterendpoint) |

| `rds` | [rds:CreateDBClusterParameterGroup](../actions.md#rds:createdbclusterparametergroup) |

| `rds` | [rds:CreateDBClusterSnapshot](../actions.md#rds:createdbclustersnapshot) |

| `rds` | [rds:CreateDBInstance](../actions.md#rds:createdbinstance) |

| `rds` | [rds:CreateDBParameterGroup](../actions.md#rds:createdbparametergroup) |

| `rds` | [rds:CreateDBSubnetGroup](../actions.md#rds:createdbsubnetgroup) |

| `rds` | [rds:CreateEventSubscription](../actions.md#rds:createeventsubscription) |

| `rds` | [rds:CreateGlobalCluster](../actions.md#rds:createglobalcluster) |

| `rds` | [rds:DeleteDBCluster](../actions.md#rds:deletedbcluster) |

| `rds` | [rds:DeleteDBClusterEndpoint](../actions.md#rds:deletedbclusterendpoint) |

| `rds` | [rds:DeleteDBClusterParameterGroup](../actions.md#rds:deletedbclusterparametergroup) |

| `rds` | [rds:DeleteDBClusterSnapshot](../actions.md#rds:deletedbclustersnapshot) |

| `rds` | [rds:DeleteDBInstance](../actions.md#rds:deletedbinstance) |

| `rds` | [rds:DeleteDBParameterGroup](../actions.md#rds:deletedbparametergroup) |

| `rds` | [rds:DeleteDBSubnetGroup](../actions.md#rds:deletedbsubnetgroup) |

| `rds` | [rds:DeleteEventSubscription](../actions.md#rds:deleteeventsubscription) |

| `rds` | [rds:DeleteGlobalCluster](../actions.md#rds:deleteglobalcluster) |

| `rds` | [rds:DescribeAccountAttributes](../actions.md#rds:describeaccountattributes) |

| `rds` | [rds:DescribeCertificates](../actions.md#rds:describecertificates) |

| `rds` | [rds:DescribeDBClusterEndpoints](../actions.md#rds:describedbclusterendpoints) |

| `rds` | [rds:DescribeDBClusterParameterGroups](../actions.md#rds:describedbclusterparametergroups) |

| `rds` | [rds:DescribeDBClusterParameters](../actions.md#rds:describedbclusterparameters) |

| `rds` | [rds:DescribeDBClusterSnapshotAttributes](../actions.md#rds:describedbclustersnapshotattributes) |

| `rds` | [rds:DescribeDBClusterSnapshots](../actions.md#rds:describedbclustersnapshots) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBEngineVersions](../actions.md#rds:describedbengineversions) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBLogFiles](../actions.md#rds:describedblogfiles) |

| `rds` | [rds:DescribeDBParameterGroups](../actions.md#rds:describedbparametergroups) |

| `rds` | [rds:DescribeDBParameters](../actions.md#rds:describedbparameters) |

| `rds` | [rds:DescribeDBSecurityGroups](../actions.md#rds:describedbsecuritygroups) |

| `rds` | [rds:DescribeDBSubnetGroups](../actions.md#rds:describedbsubnetgroups) |

| `rds` | [rds:DescribeEngineDefaultClusterParameters](../actions.md#rds:describeenginedefaultclusterparameters) |

| `rds` | [rds:DescribeEngineDefaultParameters](../actions.md#rds:describeenginedefaultparameters) |

| `rds` | [rds:DescribeEventCategories](../actions.md#rds:describeeventcategories) |

| `rds` | [rds:DescribeEventSubscriptions](../actions.md#rds:describeeventsubscriptions) |

| `rds` | [rds:DescribeEvents](../actions.md#rds:describeevents) |

| `rds` | [rds:DescribeGlobalClusters](../actions.md#rds:describeglobalclusters) |

| `rds` | [rds:DescribeOptionGroups](../actions.md#rds:describeoptiongroups) |

| `rds` | [rds:DescribeOrderableDBInstanceOptions](../actions.md#rds:describeorderabledbinstanceoptions) |

| `rds` | [rds:DescribePendingMaintenanceActions](../actions.md#rds:describependingmaintenanceactions) |

| `rds` | [rds:DescribeValidDBInstanceModifications](../actions.md#rds:describevaliddbinstancemodifications) |

| `rds` | [rds:DownloadDBLogFilePortion](../actions.md#rds:downloaddblogfileportion) |

| `rds` | [rds:FailoverDBCluster](../actions.md#rds:failoverdbcluster) |

| `rds` | [rds:FailoverGlobalCluster](../actions.md#rds:failoverglobalcluster) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `rds` | [rds:ModifyDBCluster](../actions.md#rds:modifydbcluster) |

| `rds` | [rds:ModifyDBClusterEndpoint](../actions.md#rds:modifydbclusterendpoint) |

| `rds` | [rds:ModifyDBClusterParameterGroup](../actions.md#rds:modifydbclusterparametergroup) |

| `rds` | [rds:ModifyDBClusterSnapshotAttribute](../actions.md#rds:modifydbclustersnapshotattribute) |

| `rds` | [rds:ModifyDBInstance](../actions.md#rds:modifydbinstance) |

| `rds` | [rds:ModifyDBParameterGroup](../actions.md#rds:modifydbparametergroup) |

| `rds` | [rds:ModifyDBSubnetGroup](../actions.md#rds:modifydbsubnetgroup) |

| `rds` | [rds:ModifyEventSubscription](../actions.md#rds:modifyeventsubscription) |

| `rds` | [rds:ModifyGlobalCluster](../actions.md#rds:modifyglobalcluster) |

| `rds` | [rds:PromoteReadReplicaDBCluster](../actions.md#rds:promotereadreplicadbcluster) |

| `rds` | [rds:RebootDBInstance](../actions.md#rds:rebootdbinstance) |

| `rds` | [rds:RemoveFromGlobalCluster](../actions.md#rds:removefromglobalcluster) |

| `rds` | [rds:RemoveRoleFromDBCluster](../actions.md#rds:removerolefromdbcluster) |

| `rds` | [rds:RemoveSourceIdentifierFromSubscription](../actions.md#rds:removesourceidentifierfromsubscription) |

| `rds` | [rds:RemoveTagsFromResource](../actions.md#rds:removetagsfromresource) |

| `rds` | [rds:ResetDBClusterParameterGroup](../actions.md#rds:resetdbclusterparametergroup) |

| `rds` | [rds:ResetDBParameterGroup](../actions.md#rds:resetdbparametergroup) |

| `rds` | [rds:RestoreDBClusterFromSnapshot](../actions.md#rds:restoredbclusterfromsnapshot) |

| `rds` | [rds:RestoreDBClusterToPointInTime](../actions.md#rds:restoredbclustertopointintime) |

| `rds` | [rds:StartDBCluster](../actions.md#rds:startdbcluster) |

| `rds` | [rds:StopDBCluster](../actions.md#rds:stopdbcluster) |

| `sns` | [sns:ListSubscriptions](../actions.md#sns:listsubscriptions) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |
