# Policy: AmazonRedshiftFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonRedshiftFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| secretsmanager |
| cloudwatch |
| redshift-data |
| redshift-serverless |
| iam |
| redshift |
| ec2 |
| tag |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:DisableAlarmActions](../actions.md#cloudwatch:disablealarmactions) |

| `cloudwatch` | [cloudwatch:EnableAlarmActions](../actions.md#cloudwatch:enablealarmactions) |

| `cloudwatch` | [cloudwatch:Get*](../actions.md#cloudwatch:getall) |

| `cloudwatch` | [cloudwatch:List*](../actions.md#cloudwatch:listall) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `redshift` | [redshift:*](../actions.md#redshift:all) |

| `redshift-data` | [redshift-data:CancelStatement](../actions.md#redshift-data:cancelstatement) |

| `redshift-data` | [redshift-data:DescribeStatement](../actions.md#redshift-data:describestatement) |

| `redshift-data` | [redshift-data:DescribeTable](../actions.md#redshift-data:describetable) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:GetStatementResult](../actions.md#redshift-data:getstatementresult) |

| `redshift-data` | [redshift-data:ListDatabases](../actions.md#redshift-data:listdatabases) |

| `redshift-data` | [redshift-data:ListSchemas](../actions.md#redshift-data:listschemas) |

| `redshift-data` | [redshift-data:ListStatements](../actions.md#redshift-data:liststatements) |

| `redshift-data` | [redshift-data:ListTables](../actions.md#redshift-data:listtables) |

| `redshift-serverless` | [redshift-serverless:*](../actions.md#redshift-serverless:all) |

| `secretsmanager` | [secretsmanager:CreateSecret](../actions.md#secretsmanager:createsecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:ListSecrets](../actions.md#secretsmanager:listsecrets) |

| `secretsmanager` | [secretsmanager:TagResource](../actions.md#secretsmanager:tagresource) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:Get*](../actions.md#sns:getall) |

| `sns` | [sns:List*](../actions.md#sns:listall) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `tag` | [tag:GetTagKeys](../actions.md#tag:gettagkeys) |

| `tag` | [tag:GetTagValues](../actions.md#tag:gettagvalues) |

| `tag` | [tag:TagResources](../actions.md#tag:tagresources) |

| `tag` | [tag:UntagResources](../actions.md#tag:untagresources) |
