# Policy: AWSSSOReadOnly

ARN: `arn:aws:iam::aws:policy/AWSSSOReadOnly`

## Attached Roles

## Attached Services

| Service |
|---------|
| signin |
| sso-directory |
| sso |
| iam |
| organizations |
| ds |
| access-analyzer |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `access-analyzer` | [access-analyzer:ValidatePolicy](../actions.md#access-analyzer:validatepolicy) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `ds` | [ds:DescribeTrusts](../actions.md#ds:describetrusts) |

| `iam` | [iam:ListPolicies](../actions.md#iam:listpolicies) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAccounts](../actions.md#organizations:listaccounts) |

| `organizations` | [organizations:ListAccountsForParent](../actions.md#organizations:listaccountsforparent) |

| `organizations` | [organizations:ListChildren](../actions.md#organizations:listchildren) |

| `organizations` | [organizations:ListDelegatedAdministrators](../actions.md#organizations:listdelegatedadministrators) |

| `organizations` | [organizations:ListOrganizationalUnitsForParent](../actions.md#organizations:listorganizationalunitsforparent) |

| `organizations` | [organizations:ListParents](../actions.md#organizations:listparents) |

| `organizations` | [organizations:ListRoots](../actions.md#organizations:listroots) |

| `signin` | [signin:ListTrustedIdentityPropagationApplicationsForConsole](../actions.md#signin:listtrustedidentitypropagationapplicationsforconsole) |

| `sso` | [sso:Describe*](../actions.md#sso:describeall) |

| `sso` | [sso:Get*](../actions.md#sso:getall) |

| `sso` | [sso:List*](../actions.md#sso:listall) |

| `sso` | [sso:Search*](../actions.md#sso:searchall) |

| `sso-directory` | [sso-directory:DescribeDirectory](../actions.md#sso-directory:describedirectory) |
