# Policy: AmazonRedshiftDataFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonRedshiftDataFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| secretsmanager |
| redshift-data |
| redshift-serverless |
| iam |
| redshift |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `redshift` | [redshift:CreateClusterUser](../actions.md#redshift:createclusteruser) |

| `redshift` | [redshift:GetClusterCredentials](../actions.md#redshift:getclustercredentials) |

| `redshift` | [redshift:GetClusterCredentialsWithIAM](../actions.md#redshift:getclustercredentialswithiam) |

| `redshift-data` | [redshift-data:BatchExecuteStatement](../actions.md#redshift-data:batchexecutestatement) |

| `redshift-data` | [redshift-data:CancelStatement](../actions.md#redshift-data:cancelstatement) |

| `redshift-data` | [redshift-data:DescribeStatement](../actions.md#redshift-data:describestatement) |

| `redshift-data` | [redshift-data:DescribeTable](../actions.md#redshift-data:describetable) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:GetStatementResult](../actions.md#redshift-data:getstatementresult) |

| `redshift-data` | [redshift-data:ListDatabases](../actions.md#redshift-data:listdatabases) |

| `redshift-data` | [redshift-data:ListSchemas](../actions.md#redshift-data:listschemas) |

| `redshift-data` | [redshift-data:ListStatements](../actions.md#redshift-data:liststatements) |

| `redshift-data` | [redshift-data:ListTables](../actions.md#redshift-data:listtables) |

| `redshift-serverless` | [redshift-serverless:GetCredentials](../actions.md#redshift-serverless:getcredentials) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |
