# Policy: AWSMigrationHubOrchestratorServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSMigrationHubOrchestratorServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| events |
| ssm |
| discovery |
| mgh |
| mgn |
| launchwizard |
| ec2 |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `discovery` | [discovery:DescribeConfigurations](../actions.md#discovery:describeconfigurations) |

| `discovery` | [discovery:ListConfigurations](../actions.md#discovery:listconfigurations) |

| `ec2` | [ec2:CreateLaunchTemplateVersion](../actions.md#ec2:createlaunchtemplateversion) |

| `ec2` | [ec2:DescribeImportImageTasks](../actions.md#ec2:describeimportimagetasks) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeLaunchTemplates](../actions.md#ec2:describelaunchtemplates) |

| `ec2` | [ec2:ModifyLaunchTemplate](../actions.md#ec2:modifylaunchtemplate) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `launchwizard` | [launchwizard:DescribeProvisionedApp](../actions.md#launchwizard:describeprovisionedapp) |

| `launchwizard` | [launchwizard:GetDeployment](../actions.md#launchwizard:getdeployment) |

| `launchwizard` | [launchwizard:ListDeployments](../actions.md#launchwizard:listdeployments) |

| `launchwizard` | [launchwizard:ListProvisionedApps](../actions.md#launchwizard:listprovisionedapps) |

| `mgh` | [mgh:GetHomeRegion](../actions.md#mgh:gethomeregion) |

| `mgn` | [mgn:ChangeServerLifeCycleState](../actions.md#mgn:changeserverlifecyclestate) |

| `mgn` | [mgn:DescribeSourceServers](../actions.md#mgn:describesourceservers) |

| `mgn` | [mgn:FinalizeCutover](../actions.md#mgn:finalizecutover) |

| `mgn` | [mgn:GetLaunchConfiguration](../actions.md#mgn:getlaunchconfiguration) |

| `mgn` | [mgn:GetReplicationConfiguration](../actions.md#mgn:getreplicationconfiguration) |

| `mgn` | [mgn:MarkAsArchived](../actions.md#mgn:markasarchived) |

| `mgn` | [mgn:StartCutover](../actions.md#mgn:startcutover) |

| `mgn` | [mgn:StartTest](../actions.md#mgn:starttest) |

| `mgn` | [mgn:UpdateReplicationConfiguration](../actions.md#mgn:updatereplicationconfiguration) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `ssm` | [ssm:CancelCommand](../actions.md#ssm:cancelcommand) |

| `ssm` | [ssm:DescribeInstanceInformation](../actions.md#ssm:describeinstanceinformation) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |
