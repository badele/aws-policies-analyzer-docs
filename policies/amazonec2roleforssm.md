# Policy: AmazonEC2RoleforSSM

ARN: `arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| cloudwatch |
| logs |
| ssmmessages |
| ec2messages |
| ds |
| ec2 |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `ds` | [ds:CreateComputer](../actions.md#ds:createcomputer) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `ec2` | [ec2:DescribeInstanceStatus](../actions.md#ec2:describeinstancestatus) |

| `ec2messages` | [ec2messages:AcknowledgeMessage](../actions.md#ec2messages:acknowledgemessage) |

| `ec2messages` | [ec2messages:DeleteMessage](../actions.md#ec2messages:deletemessage) |

| `ec2messages` | [ec2messages:FailMessage](../actions.md#ec2messages:failmessage) |

| `ec2messages` | [ec2messages:GetEndpoint](../actions.md#ec2messages:getendpoint) |

| `ec2messages` | [ec2messages:GetMessages](../actions.md#ec2messages:getmessages) |

| `ec2messages` | [ec2messages:SendReply](../actions.md#ec2messages:sendreply) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetEncryptionConfiguration](../actions.md#s3:getencryptionconfiguration) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucketMultipartUploads](../actions.md#s3:listbucketmultipartuploads) |

| `s3` | [s3:ListMultipartUploadParts](../actions.md#s3:listmultipartuploadparts) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `ssm` | [ssm:DescribeAssociation](../actions.md#ssm:describeassociation) |

| `ssm` | [ssm:DescribeDocument](../actions.md#ssm:describedocument) |

| `ssm` | [ssm:GetDeployablePatchSnapshotForInstance](../actions.md#ssm:getdeployablepatchsnapshotforinstance) |

| `ssm` | [ssm:GetDocument](../actions.md#ssm:getdocument) |

| `ssm` | [ssm:GetManifest](../actions.md#ssm:getmanifest) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `ssm` | [ssm:ListAssociations](../actions.md#ssm:listassociations) |

| `ssm` | [ssm:ListInstanceAssociations](../actions.md#ssm:listinstanceassociations) |

| `ssm` | [ssm:PutComplianceItems](../actions.md#ssm:putcomplianceitems) |

| `ssm` | [ssm:PutConfigurePackageResult](../actions.md#ssm:putconfigurepackageresult) |

| `ssm` | [ssm:PutInventory](../actions.md#ssm:putinventory) |

| `ssm` | [ssm:UpdateAssociationStatus](../actions.md#ssm:updateassociationstatus) |

| `ssm` | [ssm:UpdateInstanceAssociationStatus](../actions.md#ssm:updateinstanceassociationstatus) |

| `ssm` | [ssm:UpdateInstanceInformation](../actions.md#ssm:updateinstanceinformation) |

| `ssmmessages` | [ssmmessages:CreateControlChannel](../actions.md#ssmmessages:createcontrolchannel) |

| `ssmmessages` | [ssmmessages:CreateDataChannel](../actions.md#ssmmessages:createdatachannel) |

| `ssmmessages` | [ssmmessages:OpenControlChannel](../actions.md#ssmmessages:opencontrolchannel) |

| `ssmmessages` | [ssmmessages:OpenDataChannel](../actions.md#ssmmessages:opendatachannel) |
