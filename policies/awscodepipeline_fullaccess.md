# Policy: AWSCodePipeline_FullAccess

ARN: `arn:aws:iam::aws:policy/AWSCodePipeline_FullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| chatbot |
| states |
| ecs |
| codestar-notifications |
| cloudformation |
| lambda |
| ec2 |
| s3 |
| elasticbeanstalk |
| events |
| cloudtrail |
| codecommit |
| iam |
| codedeploy |
| codebuild |
| ecr |
| sns |
| opsworks |
| codepipeline |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `chatbot` | [chatbot:DescribeSlackChannelConfigurations](../actions.md#chatbot:describeslackchannelconfigurations) |

| `chatbot` | [chatbot:ListMicrosoftTeamsChannelConfigurations](../actions.md#chatbot:listmicrosoftteamschannelconfigurations) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:ListChangeSets](../actions.md#cloudformation:listchangesets) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudtrail` | [cloudtrail:CreateTrail](../actions.md#cloudtrail:createtrail) |

| `cloudtrail` | [cloudtrail:DescribeTrails](../actions.md#cloudtrail:describetrails) |

| `cloudtrail` | [cloudtrail:GetEventSelectors](../actions.md#cloudtrail:geteventselectors) |

| `cloudtrail` | [cloudtrail:PutEventSelectors](../actions.md#cloudtrail:puteventselectors) |

| `cloudtrail` | [cloudtrail:StartLogging](../actions.md#cloudtrail:startlogging) |

| `codebuild` | [codebuild:BatchGetProjects](../actions.md#codebuild:batchgetprojects) |

| `codebuild` | [codebuild:CreateProject](../actions.md#codebuild:createproject) |

| `codebuild` | [codebuild:ListCuratedEnvironmentImages](../actions.md#codebuild:listcuratedenvironmentimages) |

| `codebuild` | [codebuild:ListProjects](../actions.md#codebuild:listprojects) |

| `codecommit` | [codecommit:GetReferences](../actions.md#codecommit:getreferences) |

| `codecommit` | [codecommit:ListBranches](../actions.md#codecommit:listbranches) |

| `codecommit` | [codecommit:ListRepositories](../actions.md#codecommit:listrepositories) |

| `codedeploy` | [codedeploy:BatchGetDeploymentGroups](../actions.md#codedeploy:batchgetdeploymentgroups) |

| `codedeploy` | [codedeploy:ListApplications](../actions.md#codedeploy:listapplications) |

| `codedeploy` | [codedeploy:ListDeploymentGroups](../actions.md#codedeploy:listdeploymentgroups) |

| `codepipeline` | [codepipeline:*](../actions.md#codepipeline:all) |

| `codestar-notifications` | [codestar-notifications:CreateNotificationRule](../actions.md#codestar-notifications:createnotificationrule) |

| `codestar-notifications` | [codestar-notifications:DeleteNotificationRule](../actions.md#codestar-notifications:deletenotificationrule) |

| `codestar-notifications` | [codestar-notifications:DescribeNotificationRule](../actions.md#codestar-notifications:describenotificationrule) |

| `codestar-notifications` | [codestar-notifications:ListEventTypes](../actions.md#codestar-notifications:listeventtypes) |

| `codestar-notifications` | [codestar-notifications:ListNotificationRules](../actions.md#codestar-notifications:listnotificationrules) |

| `codestar-notifications` | [codestar-notifications:ListTagsforResource](../actions.md#codestar-notifications:listtagsforresource) |

| `codestar-notifications` | [codestar-notifications:ListTargets](../actions.md#codestar-notifications:listtargets) |

| `codestar-notifications` | [codestar-notifications:Subscribe](../actions.md#codestar-notifications:subscribe) |

| `codestar-notifications` | [codestar-notifications:Unsubscribe](../actions.md#codestar-notifications:unsubscribe) |

| `codestar-notifications` | [codestar-notifications:UpdateNotificationRule](../actions.md#codestar-notifications:updatenotificationrule) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ecr` | [ecr:DescribeRepositories](../actions.md#ecr:describerepositories) |

| `ecr` | [ecr:ListImages](../actions.md#ecr:listimages) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `ecs` | [ecs:ListServices](../actions.md#ecs:listservices) |

| `elasticbeanstalk` | [elasticbeanstalk:DescribeApplications](../actions.md#elasticbeanstalk:describeapplications) |

| `elasticbeanstalk` | [elasticbeanstalk:DescribeEnvironments](../actions.md#elasticbeanstalk:describeenvironments) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:DisableRule](../actions.md#events:disablerule) |

| `events` | [events:ListRules](../actions.md#events:listrules) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `opsworks` | [opsworks:DescribeApps](../actions.md#opsworks:describeapps) |

| `opsworks` | [opsworks:DescribeLayers](../actions.md#opsworks:describelayers) |

| `opsworks` | [opsworks:DescribeStacks](../actions.md#opsworks:describestacks) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:GetBucketVersioning](../actions.md#s3:getbucketversioning) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:SetTopicAttributes](../actions.md#sns:settopicattributes) |

| `states` | [states:ListStateMachines](../actions.md#states:liststatemachines) |
