# Policy: AWSServiceRoleForImageBuilder

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSServiceRoleForImageBuilder`

## Attached Roles

## Attached Services

| Service |
|---------|
| license-manager |
| events |
| ssm |
| logs |
| inspector2 |
| sts |
| iam |
| ecr |
| ec2 |
| sns |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:CancelExportTask](../actions.md#ec2:cancelexporttask) |

| `ec2` | [ec2:CopyImage](../actions.md#ec2:copyimage) |

| `ec2` | [ec2:CreateImage](../actions.md#ec2:createimage) |

| `ec2` | [ec2:CreateLaunchTemplate](../actions.md#ec2:createlaunchtemplate) |

| `ec2` | [ec2:CreateLaunchTemplateVersion](../actions.md#ec2:createlaunchtemplateversion) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeregisterImage](../actions.md#ec2:deregisterimage) |

| `ec2` | [ec2:DescribeExportImageTasks](../actions.md#ec2:describeexportimagetasks) |

| `ec2` | [ec2:DescribeHosts](../actions.md#ec2:describehosts) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeImportImageTasks](../actions.md#ec2:describeimportimagetasks) |

| `ec2` | [ec2:DescribeInstanceAttribute](../actions.md#ec2:describeinstanceattribute) |

| `ec2` | [ec2:DescribeInstanceStatus](../actions.md#ec2:describeinstancestatus) |

| `ec2` | [ec2:DescribeInstanceTypeOfferings](../actions.md#ec2:describeinstancetypeofferings) |

| `ec2` | [ec2:DescribeInstanceTypes](../actions.md#ec2:describeinstancetypes) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeLaunchTemplateVersions](../actions.md#ec2:describelaunchtemplateversions) |

| `ec2` | [ec2:DescribeLaunchTemplates](../actions.md#ec2:describelaunchtemplates) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `ec2` | [ec2:EnableFastLaunch](../actions.md#ec2:enablefastlaunch) |

| `ec2` | [ec2:ExportImage](../actions.md#ec2:exportimage) |

| `ec2` | [ec2:ExportImage](../actions.md#ec2:exportimage) |

| `ec2` | [ec2:ModifyImageAttribute](../actions.md#ec2:modifyimageattribute) |

| `ec2` | [ec2:ModifyLaunchTemplate](../actions.md#ec2:modifylaunchtemplate) |

| `ec2` | [ec2:ModifySnapshotAttribute](../actions.md#ec2:modifysnapshotattribute) |

| `ec2` | [ec2:RegisterImage](../actions.md#ec2:registerimage) |

| `ec2` | [ec2:RegisterImage](../actions.md#ec2:registerimage) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:StartInstances](../actions.md#ec2:startinstances) |

| `ec2` | [ec2:StopInstances](../actions.md#ec2:stopinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `ecr` | [ecr:BatchDeleteImage](../actions.md#ecr:batchdeleteimage) |

| `ecr` | [ecr:CreateRepository](../actions.md#ecr:createrepository) |

| `ecr` | [ecr:TagResource](../actions.md#ecr:tagresource) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `inspector2` | [inspector2:ListCoverage](../actions.md#inspector2:listcoverage) |

| `inspector2` | [inspector2:ListFindings](../actions.md#inspector2:listfindings) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:Encrypt](../actions.md#kms:encrypt) |

| `kms` | [kms:GenerateDataKeyWithoutPlaintext](../actions.md#kms:generatedatakeywithoutplaintext) |

| `kms` | [kms:ReEncryptFrom](../actions.md#kms:reencryptfrom) |

| `kms` | [kms:ReEncryptTo](../actions.md#kms:reencryptto) |

| `license-manager` | [license-manager:UpdateLicenseSpecificationsForResource](../actions.md#license-manager:updatelicensespecificationsforresource) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |

| `ssm` | [ssm:AddTagsToResource](../actions.md#ssm:addtagstoresource) |

| `ssm` | [ssm:CreateAssociation](../actions.md#ssm:createassociation) |

| `ssm` | [ssm:DeleteAssociation](../actions.md#ssm:deleteassociation) |

| `ssm` | [ssm:DescribeAssociationExecutions](../actions.md#ssm:describeassociationexecutions) |

| `ssm` | [ssm:DescribeInstanceAssociationsStatus](../actions.md#ssm:describeinstanceassociationsstatus) |

| `ssm` | [ssm:DescribeInstanceInformation](../actions.md#ssm:describeinstanceinformation) |

| `ssm` | [ssm:GetAutomationExecution](../actions.md#ssm:getautomationexecution) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:ListCommandInvocations](../actions.md#ssm:listcommandinvocations) |

| `ssm` | [ssm:ListCommands](../actions.md#ssm:listcommands) |

| `ssm` | [ssm:ListInventoryEntries](../actions.md#ssm:listinventoryentries) |

| `ssm` | [ssm:SendAutomationSignal](../actions.md#ssm:sendautomationsignal) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:StartAutomationExecution](../actions.md#ssm:startautomationexecution) |

| `ssm` | [ssm:StopAutomationExecution](../actions.md#ssm:stopautomationexecution) |

| `sts` | [sts:AssumeRole](../actions.md#sts:assumerole) |
