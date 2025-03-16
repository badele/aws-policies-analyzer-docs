# Policy: AmazonSecurityLakeAdministrator

ARN: `arn:aws:iam::aws:policy/AmazonSecurityLakeAdministrator`

## Attached Roles

## Attached Services

| Service |
|---------|
| events |
| glue |
| lambda |
| securitylake |
| secretsmanager |
| ram |
| organizations |
| iam |
| sqs |
| lakeformation |
| s3 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `events` | [events:CreateApiDestination](../actions.md#events:createapidestination) |

| `events` | [events:CreateConnection](../actions.md#events:createconnection) |

| `events` | [events:DeleteApiDestination](../actions.md#events:deleteapidestination) |

| `events` | [events:DeleteConnection](../actions.md#events:deleteconnection) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListApiDestinations](../actions.md#events:listapidestinations) |

| `events` | [events:ListConnections](../actions.md#events:listconnections) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `events` | [events:UpdateApiDestination](../actions.md#events:updateapidestination) |

| `events` | [events:UpdateConnection](../actions.md#events:updateconnection) |

| `glue` | [glue:CreateCrawler](../actions.md#glue:createcrawler) |

| `glue` | [glue:CreateDatabase](../actions.md#glue:createdatabase) |

| `glue` | [glue:CreateTable](../actions.md#glue:createtable) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetTable](../actions.md#glue:gettable) |

| `glue` | [glue:StopCrawlerSchedule](../actions.md#glue:stopcrawlerschedule) |

| `iam` | [iam:CreateRole](../actions.md#iam:createrole) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:DeleteRole](../actions.md#iam:deleterole) |

| `iam` | [iam:DeleteRolePolicy](../actions.md#iam:deleterolepolicy) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:GetRolePolicy](../actions.md#iam:getrolepolicy) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListRolePolicies](../actions.md#iam:listrolepolicies) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PutRolePolicy](../actions.md#iam:putrolepolicy) |

| `iam` | [iam:PutRolePolicy](../actions.md#iam:putrolepolicy) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `lakeformation` | [lakeformation:GetDatalakeSettings](../actions.md#lakeformation:getdatalakesettings) |

| `lakeformation` | [lakeformation:GrantPermissions](../actions.md#lakeformation:grantpermissions) |

| `lakeformation` | [lakeformation:ListPermissions](../actions.md#lakeformation:listpermissions) |

| `lakeformation` | [lakeformation:RegisterResource](../actions.md#lakeformation:registerresource) |

| `lakeformation` | [lakeformation:RevokePermissions](../actions.md#lakeformation:revokepermissions) |

| `lambda` | [lambda:AddPermission](../actions.md#lambda:addpermission) |

| `lambda` | [lambda:CreateEventSourceMapping](../actions.md#lambda:createeventsourcemapping) |

| `lambda` | [lambda:CreateFunction](../actions.md#lambda:createfunction) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAccounts](../actions.md#organizations:listaccounts) |

| `organizations` | [organizations:ListDelegatedServicesForAccount](../actions.md#organizations:listdelegatedservicesforaccount) |

| `ram` | [ram:AssociateResourceShare](../actions.md#ram:associateresourceshare) |

| `ram` | [ram:CreateResourceShare](../actions.md#ram:createresourceshare) |

| `ram` | [ram:DeleteResourceShare](../actions.md#ram:deleteresourceshare) |

| `ram` | [ram:DisassociateResourceShare](../actions.md#ram:disassociateresourceshare) |

| `ram` | [ram:GetResourceShareAssociations](../actions.md#ram:getresourceshareassociations) |

| `ram` | [ram:GetResourceShares](../actions.md#ram:getresourceshares) |

| `ram` | [ram:UpdateResourceShare](../actions.md#ram:updateresourceshare) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:Get*](../actions.md#s3:getall) |

| `s3` | [s3:GetAccountPublicAccessBlock](../actions.md#s3:getaccountpublicaccessblock) |

| `s3` | [s3:GetBucketNotification](../actions.md#s3:getbucketnotification) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `s3` | [s3:List*](../actions.md#s3:listall) |

| `s3` | [s3:ListAccessPoints](../actions.md#s3:listaccesspoints) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutBucketNotification](../actions.md#s3:putbucketnotification) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `s3` | [s3:PutBucketPublicAccessBlock](../actions.md#s3:putbucketpublicaccessblock) |

| `s3` | [s3:PutBucketTagging](../actions.md#s3:putbuckettagging) |

| `s3` | [s3:PutBucketVersioning](../actions.md#s3:putbucketversioning) |

| `s3` | [s3:PutEncryptionConfiguration](../actions.md#s3:putencryptionconfiguration) |

| `s3` | [s3:PutLifecycleConfiguration](../actions.md#s3:putlifecycleconfiguration) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:PutReplicationConfiguration](../actions.md#s3:putreplicationconfiguration) |

| `secretsmanager` | [secretsmanager:CreateSecret](../actions.md#secretsmanager:createsecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:PutSecretValue](../actions.md#secretsmanager:putsecretvalue) |

| `securitylake` | [securitylake:*](../actions.md#securitylake:all) |

| `sqs` | [sqs:AddPermission](../actions.md#sqs:addpermission) |

| `sqs` | [sqs:CreateQueue](../actions.md#sqs:createqueue) |

| `sqs` | [sqs:DeleteQueue](../actions.md#sqs:deletequeue) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueURL](../actions.md#sqs:getqueueurl) |

| `sqs` | [sqs:SetQueueAttributes](../actions.md#sqs:setqueueattributes) |
