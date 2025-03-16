# Policy: AIOpsReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AIOpsReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| aiops |
| sso |
| sso-directory |
| identitystore |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `aiops` | [aiops:Get*](../actions.md#aiops:getall) |

| `aiops` | [aiops:List*](../actions.md#aiops:listall) |

| `identitystore` | [identitystore:DescribeUser](../actions.md#identitystore:describeuser) |

| `sso` | [sso:DescribeInstance](../actions.md#sso:describeinstance) |

| `sso-directory` | [sso-directory:DescribeUsers](../actions.md#sso-directory:describeusers) |
