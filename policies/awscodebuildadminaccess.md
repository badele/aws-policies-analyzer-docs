# Policy: AWSCodeBuildAdminAccess

ARN: `arn:aws:iam::aws:policy/AWSCodeBuildAdminAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| events |
| ssm |
| codestar-notifications |
| codecommit |
| cloudwatch |
| logs |
| codestar-connections |
| sns |
| chatbot |
| s3 |
| codebuild |
| ecr |
| elasticfilesystem |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `chatbot` | [chatbot:DescribeSlackChannelConfigurations](../actions.md#chatbot:describeslackchannelconfigurations) |

| `chatbot` | [chatbot:ListMicrosoftTeamsChannelConfigurations](../actions.md#chatbot:listmicrosoftteamschannelconfigurations) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `codebuild` | [codebuild:*](../actions.md#codebuild:all) |

| `codecommit` | [codecommit:GetBranch](../actions.md#codecommit:getbranch) |

| `codecommit` | [codecommit:GetCommit](../actions.md#codecommit:getcommit) |

| `codecommit` | [codecommit:GetRepository](../actions.md#codecommit:getrepository) |

| `codecommit` | [codecommit:ListBranches](../actions.md#codecommit:listbranches) |

| `codecommit` | [codecommit:ListRepositories](../actions.md#codecommit:listrepositories) |

| `codestar-connections` | [codestar-connections:CreateConnection](../actions.md#codestar-connections:createconnection) |

| `codestar-connections` | [codestar-connections:DeleteConnection](../actions.md#codestar-connections:deleteconnection) |

| `codestar-connections` | [codestar-connections:GetConnection](../actions.md#codestar-connections:getconnection) |

| `codestar-connections` | [codestar-connections:GetIndividualAccessToken](../actions.md#codestar-connections:getindividualaccesstoken) |

| `codestar-connections` | [codestar-connections:GetInstallationUrl](../actions.md#codestar-connections:getinstallationurl) |

| `codestar-connections` | [codestar-connections:ListConnections](../actions.md#codestar-connections:listconnections) |

| `codestar-connections` | [codestar-connections:ListInstallationTargets](../actions.md#codestar-connections:listinstallationtargets) |

| `codestar-connections` | [codestar-connections:ListTagsForResource](../actions.md#codestar-connections:listtagsforresource) |

| `codestar-connections` | [codestar-connections:PassConnection](../actions.md#codestar-connections:passconnection) |

| `codestar-connections` | [codestar-connections:StartOAuthHandshake](../actions.md#codestar-connections:startoauthhandshake) |

| `codestar-connections` | [codestar-connections:TagResource](../actions.md#codestar-connections:tagresource) |

| `codestar-connections` | [codestar-connections:UntagResource](../actions.md#codestar-connections:untagresource) |

| `codestar-connections` | [codestar-connections:UpdateConnectionInstallation](../actions.md#codestar-connections:updateconnectioninstallation) |

| `codestar-connections` | [codestar-connections:UseConnection](../actions.md#codestar-connections:useconnection) |

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

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:DisableRule](../actions.md#events:disablerule) |

| `events` | [events:EnableRule](../actions.md#events:enablerule) |

| `events` | [events:ListRuleNamesByTarget](../actions.md#events:listrulenamesbytarget) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `logs` | [logs:DeleteLogGroup](../actions.md#logs:deleteloggroup) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:GetTopicAttributes](../actions.md#sns:gettopicattributes) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:SetTopicAttributes](../actions.md#sns:settopicattributes) |

| `ssm` | [ssm:PutParameter](../actions.md#ssm:putparameter) |

| `ssm` | [ssm:StartSession](../actions.md#ssm:startsession) |
