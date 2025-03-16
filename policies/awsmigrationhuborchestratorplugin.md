# Policy: AWSMigrationHubOrchestratorPlugin

ARN: `arn:aws:iam::aws:policy/AWSMigrationHubOrchestratorPlugin`

## Attached Roles

## Attached Services

| Service |
|---------|
| secretsmanager |
| migrationhub-orchestrator |
| execute-api |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `execute-api` | [execute-api:Invoke](../actions.md#execute-api:invoke) |

| `execute-api` | [execute-api:ManageConnections](../actions.md#execute-api:manageconnections) |

| `migrationhub-orchestrator` | [migrationhub-orchestrator:GetMessage](../actions.md#migrationhub-orchestrator:getmessage) |

| `migrationhub-orchestrator` | [migrationhub-orchestrator:RegisterPlugin](../actions.md#migrationhub-orchestrator:registerplugin) |

| `migrationhub-orchestrator` | [migrationhub-orchestrator:SendMessage](../actions.md#migrationhub-orchestrator:sendmessage) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:GetBucketAcl](../actions.md#s3:getbucketacl) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |
