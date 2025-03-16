# Policy: AdministratorAccess-AWSElasticBeanstalk

ARN: `arn:aws:iam::aws:policy/AdministratorAccess-AWSElasticBeanstalk`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| elasticbeanstalk |
| cloudformation |
| cloudtrail |
| cloudwatch |
| acm |
| codecommit |
| logs |
| elasticloadbalancing |
| iam |
| sqs |
| dynamodb |
| ecs |
| rds |
| codebuild |
| ec2 |
| s3 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:Describe*](../actions.md#acm:describeall) |

| `acm` | [acm:List*](../actions.md#acm:listall) |

| `autoscaling` | [autoscaling:*](../actions.md#autoscaling:all) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `cloudformation` | [cloudformation:CancelUpdateStack](../actions.md#cloudformation:cancelupdatestack) |

| `cloudformation` | [cloudformation:ContinueUpdateRollback](../actions.md#cloudformation:continueupdaterollback) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudformation` | [cloudformation:Describe*](../actions.md#cloudformation:describeall) |

| `cloudformation` | [cloudformation:Estimate*](../actions.md#cloudformation:estimateall) |

| `cloudformation` | [cloudformation:Get*](../actions.md#cloudformation:getall) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:List*](../actions.md#cloudformation:listall) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:SignalResource](../actions.md#cloudformation:signalresource) |

| `cloudformation` | [cloudformation:TagResource](../actions.md#cloudformation:tagresource) |

| `cloudformation` | [cloudformation:UntagResource](../actions.md#cloudformation:untagresource) |

| `cloudformation` | [cloudformation:UpdateStack](../actions.md#cloudformation:updatestack) |

| `cloudformation` | [cloudformation:Validate*](../actions.md#cloudformation:validateall) |

| `cloudtrail` | [cloudtrail:LookupEvents](../actions.md#cloudtrail:lookupevents) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `codebuild` | [codebuild:BatchGetBuilds](../actions.md#codebuild:batchgetbuilds) |

| `codebuild` | [codebuild:CreateProject](../actions.md#codebuild:createproject) |

| `codebuild` | [codebuild:DeleteProject](../actions.md#codebuild:deleteproject) |

| `codebuild` | [codebuild:StartBuild](../actions.md#codebuild:startbuild) |

| `codecommit` | [codecommit:Get*](../actions.md#codecommit:getall) |

| `codecommit` | [codecommit:UploadArchive](../actions.md#codecommit:uploadarchive) |

| `dynamodb` | [dynamodb:CreateTable](../actions.md#dynamodb:createtable) |

| `dynamodb` | [dynamodb:DeleteTable](../actions.md#dynamodb:deletetable) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:TagResource](../actions.md#dynamodb:tagresource) |

| `ec2` | [ec2:AllocateAddress](../actions.md#ec2:allocateaddress) |

| `ec2` | [ec2:AssociateAddress](../actions.md#ec2:associateaddress) |

| `ec2` | [ec2:AuthorizeSecurityGroup*](../actions.md#ec2:authorizesecuritygroupall) |

| `ec2` | [ec2:CreateLaunchTemplate*](../actions.md#ec2:createlaunchtemplateall) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteLaunchTemplate*](../actions.md#ec2:deletelaunchtemplateall) |

| `ec2` | [ec2:DeleteSecurityGroup](../actions.md#ec2:deletesecuritygroup) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DisassociateAddress](../actions.md#ec2:disassociateaddress) |

| `ec2` | [ec2:RebootInstances](../actions.md#ec2:rebootinstances) |

| `ec2` | [ec2:ReleaseAddress](../actions.md#ec2:releaseaddress) |

| `ec2` | [ec2:RevokeSecurityGroup*](../actions.md#ec2:revokesecuritygroupall) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `ecs` | [ecs:CreateCluster](../actions.md#ecs:createcluster) |

| `ecs` | [ecs:DeRegisterTaskDefinition](../actions.md#ecs:deregistertaskdefinition) |

| `ecs` | [ecs:DeleteCluster](../actions.md#ecs:deletecluster) |

| `ecs` | [ecs:Describe*](../actions.md#ecs:describeall) |

| `ecs` | [ecs:List*](../actions.md#ecs:listall) |

| `ecs` | [ecs:RegisterTaskDefinition](../actions.md#ecs:registertaskdefinition) |

| `ecs` | [ecs:TagResource](../actions.md#ecs:tagresource) |

| `elasticbeanstalk` | [elasticbeanstalk:*](../actions.md#elasticbeanstalk:all) |

| `elasticloadbalancing` | [elasticloadbalancing:*](../actions.md#elasticloadbalancing:all) |

| `elasticloadbalancing` | [elasticloadbalancing:*Rule](../actions.md#elasticloadbalancing:allrule) |

| `elasticloadbalancing` | [elasticloadbalancing:*Tags](../actions.md#elasticloadbalancing:alltags) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:SetRulePriorities](../actions.md#elasticloadbalancing:setrulepriorities) |

| `elasticloadbalancing` | [elasticloadbalancing:SetSecurityGroups](../actions.md#elasticloadbalancing:setsecuritygroups) |

| `iam` | [iam:AddRoleToInstanceProfile](../actions.md#iam:addroletoinstanceprofile) |

| `iam` | [iam:AttachRolePolicy](../actions.md#iam:attachrolepolicy) |

| `iam` | [iam:CreateInstanceProfile](../actions.md#iam:createinstanceprofile) |

| `iam` | [iam:CreateRole](../actions.md#iam:createrole) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListInstanceProfiles](../actions.md#iam:listinstanceprofiles) |

| `iam` | [iam:ListRolePolicies](../actions.md#iam:listrolepolicies) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:ListServerCertificates](../actions.md#iam:listservercertificates) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:DeleteLogGroup](../actions.md#logs:deleteloggroup) |

| `logs` | [logs:Describe*](../actions.md#logs:describeall) |

| `logs` | [logs:PutRetentionPolicy](../actions.md#logs:putretentionpolicy) |

| `rds` | [rds:*DBSubnetGroup](../actions.md#rds:alldbsubnetgroup) |

| `rds` | [rds:AuthorizeDBSecurityGroupIngress](../actions.md#rds:authorizedbsecuritygroupingress) |

| `rds` | [rds:CreateDBInstance](../actions.md#rds:createdbinstance) |

| `rds` | [rds:CreateDBSecurityGroup](../actions.md#rds:createdbsecuritygroup) |

| `rds` | [rds:DeleteDBInstance](../actions.md#rds:deletedbinstance) |

| `rds` | [rds:DeleteDBSecurityGroup](../actions.md#rds:deletedbsecuritygroup) |

| `rds` | [rds:Describe*](../actions.md#rds:describeall) |

| `rds` | [rds:ModifyDBInstance](../actions.md#rds:modifydbinstance) |

| `rds` | [rds:RestoreDBInstanceFromDBSnapshot](../actions.md#rds:restoredbinstancefromdbsnapshot) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:Delete*](../actions.md#s3:deleteall) |

| `s3` | [s3:Get*](../actions.md#s3:getall) |

| `s3` | [s3:GetBucket*](../actions.md#s3:getbucketall) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:Put*](../actions.md#s3:putall) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:DeleteTopic](../actions.md#sns:deletetopic) |

| `sns` | [sns:GetTopicAttributes](../actions.md#sns:gettopicattributes) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |

| `sns` | [sns:SetTopicAttributes](../actions.md#sns:settopicattributes) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `sns` | [sns:Unsubscribe](../actions.md#sns:unsubscribe) |

| `sqs` | [sqs:*QueueAttributes](../actions.md#sqs:allqueueattributes) |

| `sqs` | [sqs:CreateQueue](../actions.md#sqs:createqueue) |

| `sqs` | [sqs:DeleteQueue](../actions.md#sqs:deletequeue) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `sqs` | [sqs:SendMessage](../actions.md#sqs:sendmessage) |

| `sqs` | [sqs:TagQueue](../actions.md#sqs:tagqueue) |
