# Policy: AWSCodeStarServiceRole

ARN: `arn:aws:iam::aws:policy/service-role/AWSCodeStarServiceRole`

## Attached Roles

## Attached Services

| Service |
|---------|
| elasticloadbalancing |
| cloud9 |
| cloudformation |
| logs |
| codestar-connections |
| ec2 |
| s3 |
| autoscaling |
| elasticbeanstalk |
| events |
| config |
| codecommit |
| iam |
| codestar |
| codedeploy |
| codebuild |
| sns |
| cloudwatch |
| codepipeline |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:*](../actions.md#autoscaling:all) |

| `cloud9` | [cloud9:CreateEnvironmentEC2](../actions.md#cloud9:createenvironmentec2) |

| `cloud9` | [cloud9:DeleteEnvironment](../actions.md#cloud9:deleteenvironment) |

| `cloud9` | [cloud9:DescribeEnvironment*](../actions.md#cloud9:describeenvironmentall) |

| `cloud9` | [cloud9:ListEnvironments](../actions.md#cloud9:listenvironments) |

| `cloudformation` | [cloudformation:*Stack*](../actions.md#cloudformation:allstackall) |

| `cloudformation` | [cloudformation:CreateChangeSet](../actions.md#cloudformation:createchangeset) |

| `cloudformation` | [cloudformation:DeleteChangeSet](../actions.md#cloudformation:deletechangeset) |

| `cloudformation` | [cloudformation:DescribeChangeSet](../actions.md#cloudformation:describechangeset) |

| `cloudformation` | [cloudformation:ExecuteChangeSet](../actions.md#cloudformation:executechangeset) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:GetTemplateSummary](../actions.md#cloudformation:gettemplatesummary) |

| `cloudwatch` | [cloudwatch:Put*](../actions.md#cloudwatch:putall) |

| `codebuild` | [codebuild:*](../actions.md#codebuild:all) |

| `codecommit` | [codecommit:*](../actions.md#codecommit:all) |

| `codedeploy` | [codedeploy:*](../actions.md#codedeploy:all) |

| `codepipeline` | [codepipeline:*](../actions.md#codepipeline:all) |

| `codestar` | [codestar:*](../actions.md#codestar:all) |

| `codestar-connections` | [codestar-connections:GetConnection](../actions.md#codestar-connections:getconnection) |

| `codestar-connections` | [codestar-connections:PassConnection](../actions.md#codestar-connections:passconnection) |

| `codestar-connections` | [codestar-connections:UseConnection](../actions.md#codestar-connections:useconnection) |

| `config` | [config:DescribeConfigRules](../actions.md#config:describeconfigrules) |

| `ec2` | [ec2:*](../actions.md#ec2:all) |

| `elasticbeanstalk` | [elasticbeanstalk:*](../actions.md#elasticbeanstalk:all) |

| `elasticloadbalancing` | [elasticloadbalancing:*](../actions.md#elasticloadbalancing:all) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `iam` | [iam:AddRoleToInstanceProfile](../actions.md#iam:addroletoinstanceprofile) |

| `iam` | [iam:AttachRolePolicy](../actions.md#iam:attachrolepolicy) |

| `iam` | [iam:AttachUserPolicy](../actions.md#iam:attachuserpolicy) |

| `iam` | [iam:CreateInstanceProfile](../actions.md#iam:createinstanceprofile) |

| `iam` | [iam:CreatePolicy](../actions.md#iam:createpolicy) |

| `iam` | [iam:CreatePolicy](../actions.md#iam:createpolicy) |

| `iam` | [iam:CreatePolicyVersion](../actions.md#iam:createpolicyversion) |

| `iam` | [iam:CreateRole](../actions.md#iam:createrole) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:DeleteInstanceProfile](../actions.md#iam:deleteinstanceprofile) |

| `iam` | [iam:DeletePolicy](../actions.md#iam:deletepolicy) |

| `iam` | [iam:DeletePolicy](../actions.md#iam:deletepolicy) |

| `iam` | [iam:DeletePolicyVersion](../actions.md#iam:deletepolicyversion) |

| `iam` | [iam:DeleteRole](../actions.md#iam:deleterole) |

| `iam` | [iam:DeleteRolePolicy](../actions.md#iam:deleterolepolicy) |

| `iam` | [iam:DetachRolePolicy](../actions.md#iam:detachrolepolicy) |

| `iam` | [iam:DetachUserPolicy](../actions.md#iam:detachuserpolicy) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:GetRolePolicy](../actions.md#iam:getrolepolicy) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListEntitiesForPolicy](../actions.md#iam:listentitiesforpolicy) |

| `iam` | [iam:ListPolicyVersions](../actions.md#iam:listpolicyversions) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PutRolePolicy](../actions.md#iam:putrolepolicy) |

| `iam` | [iam:RemoveRoleFromInstanceProfile](../actions.md#iam:removerolefrominstanceprofile) |

| `iam` | [iam:SetDefaultPolicyVersion](../actions.md#iam:setdefaultpolicyversion) |

| `logs` | [logs:*](../actions.md#logs:all) |

| `s3` | [s3:*](../actions.md#s3:all) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `sns` | [sns:*](../actions.md#sns:all) |
