# Policy: AWSLicenseManagerServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSLicenseManagerServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| license-manager |
| ssm |
| iam |
| organizations |
| ec2 |
| s3 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeHosts](../actions.md#ec2:describehosts) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `license-manager` | [license-manager:GetLicense*](../actions.md#license-manager:getlicenseall) |

| `license-manager` | [license-manager:GetServiceSettings](../actions.md#license-manager:getservicesettings) |

| `license-manager` | [license-manager:List*](../actions.md#license-manager:listall) |

| `license-manager` | [license-manager:UpdateLicenseSpecificationsForResource](../actions.md#license-manager:updatelicensespecificationsforresource) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAWSServiceAccessForOrganization](../actions.md#organizations:listawsserviceaccessfororganization) |

| `organizations` | [organizations:ListDelegatedAdministrators](../actions.md#organizations:listdelegatedadministrators) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |

| `ssm` | [ssm:CreateAssociation](../actions.md#ssm:createassociation) |

| `ssm` | [ssm:GetInventory](../actions.md#ssm:getinventory) |

| `ssm` | [ssm:ListInventoryEntries](../actions.md#ssm:listinventoryentries) |
