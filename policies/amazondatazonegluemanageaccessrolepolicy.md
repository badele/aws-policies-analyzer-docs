# Policy: AmazonDataZoneGlueManageAccessRolePolicy

ARN: `arn:aws:iam::aws:policy/service-role/AmazonDataZoneGlueManageAccessRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| glue |
| ram |
| organizations |
| iam |
| lakeformation |
| ec2 |
| s3 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `glue` | [glue:CreateCatalog](../actions.md#glue:createcatalog) |

| `glue` | [glue:CreateDatabase](../actions.md#glue:createdatabase) |

| `glue` | [glue:CreateTable](../actions.md#glue:createtable) |

| `glue` | [glue:DeleteCatalog](../actions.md#glue:deletecatalog) |

| `glue` | [glue:DeleteDatabase](../actions.md#glue:deletedatabase) |

| `glue` | [glue:DeleteResourcePolicy](../actions.md#glue:deleteresourcepolicy) |

| `glue` | [glue:DeleteTable](../actions.md#glue:deletetable) |

| `glue` | [glue:GetCatalog](../actions.md#glue:getcatalog) |

| `glue` | [glue:GetDataQualityResult](../actions.md#glue:getdataqualityresult) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetDatabases](../actions.md#glue:getdatabases) |

| `glue` | [glue:GetTable](../actions.md#glue:gettable) |

| `glue` | [glue:GetTables](../actions.md#glue:gettables) |

| `glue` | [glue:GetTags](../actions.md#glue:gettags) |

| `glue` | [glue:ListCrawls](../actions.md#glue:listcrawls) |

| `glue` | [glue:ListDataQualityResults](../actions.md#glue:listdataqualityresults) |

| `glue` | [glue:PutResourcePolicy](../actions.md#glue:putresourcepolicy) |

| `glue` | [glue:SearchTables](../actions.md#glue:searchtables) |

| `glue` | [glue:TagResource](../actions.md#glue:tagresource) |

| `glue` | [glue:UntagResource](../actions.md#glue:untagresource) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `lakeformation` | [lakeformation:BatchGrantPermissions](../actions.md#lakeformation:batchgrantpermissions) |

| `lakeformation` | [lakeformation:BatchRevokePermissions](../actions.md#lakeformation:batchrevokepermissions) |

| `lakeformation` | [lakeformation:CreateDataCellsFilter](../actions.md#lakeformation:createdatacellsfilter) |

| `lakeformation` | [lakeformation:CreateLakeFormationOptIn](../actions.md#lakeformation:createlakeformationoptin) |

| `lakeformation` | [lakeformation:DeleteDataCellsFilter](../actions.md#lakeformation:deletedatacellsfilter) |

| `lakeformation` | [lakeformation:DeleteLakeFormationOptIn](../actions.md#lakeformation:deletelakeformationoptin) |

| `lakeformation` | [lakeformation:GetDataAccess](../actions.md#lakeformation:getdataaccess) |

| `lakeformation` | [lakeformation:GetDataCellsFilter](../actions.md#lakeformation:getdatacellsfilter) |

| `lakeformation` | [lakeformation:GetResourceLFTags](../actions.md#lakeformation:getresourcelftags) |

| `lakeformation` | [lakeformation:GrantPermissions](../actions.md#lakeformation:grantpermissions) |

| `lakeformation` | [lakeformation:ListDataCellsFilter](../actions.md#lakeformation:listdatacellsfilter) |

| `lakeformation` | [lakeformation:ListLakeFormationOptIns](../actions.md#lakeformation:listlakeformationoptins) |

| `lakeformation` | [lakeformation:ListPermissions](../actions.md#lakeformation:listpermissions) |

| `lakeformation` | [lakeformation:RegisterResource](../actions.md#lakeformation:registerresource) |

| `lakeformation` | [lakeformation:RevokePermissions](../actions.md#lakeformation:revokepermissions) |

| `lakeformation` | [lakeformation:UpdateDataCellsFilter](../actions.md#lakeformation:updatedatacellsfilter) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `ram` | [ram:AcceptResourceShareInvitation](../actions.md#ram:acceptresourceshareinvitation) |

| `ram` | [ram:AssociateResourceShare](../actions.md#ram:associateresourceshare) |

| `ram` | [ram:AssociateResourceSharePermission](../actions.md#ram:associateresourcesharepermission) |

| `ram` | [ram:CreateResourceShare](../actions.md#ram:createresourceshare) |

| `ram` | [ram:DeleteResourceShare](../actions.md#ram:deleteresourceshare) |

| `ram` | [ram:DisassociateResourceShare](../actions.md#ram:disassociateresourceshare) |

| `ram` | [ram:GetResourceShareInvitations](../actions.md#ram:getresourceshareinvitations) |

| `ram` | [ram:GetResourceShares](../actions.md#ram:getresourceshares) |

| `ram` | [ram:ListResourceSharePermissions](../actions.md#ram:listresourcesharepermissions) |

| `ram` | [ram:ListResources](../actions.md#ram:listresources) |

| `ram` | [ram:UpdateResourceShare](../actions.md#ram:updateresourceshare) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteBucket](../actions.md#s3:deletebucket) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `s3` | [s3:PutBucketTagging](../actions.md#s3:putbuckettagging) |

| `s3` | [s3:PutBucketVersioning](../actions.md#s3:putbucketversioning) |

| `s3` | [s3:PutEncryptionConfiguration](../actions.md#s3:putencryptionconfiguration) |

| `s3` | [s3:PutLifecycleConfiguration](../actions.md#s3:putlifecycleconfiguration) |
