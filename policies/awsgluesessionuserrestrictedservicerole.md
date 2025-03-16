# Policy: AwsGlueSessionUserRestrictedServiceRole

ARN: `arn:aws:iam::aws:policy/service-role/AwsGlueSessionUserRestrictedServiceRole`

## Attached Roles

## Attached Services

| Service |
|---------|
| glue |
| logs |
| s3 |
| ec2 |
| tag |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `glue` | [glue:*](../actions.md#glue:all) |

| `glue` | [glue:CancelStatement](../actions.md#glue:cancelstatement) |

| `glue` | [glue:CreateSession](../actions.md#glue:createsession) |

| `glue` | [glue:DeleteSession](../actions.md#glue:deletesession) |

| `glue` | [glue:GetCompletion](../actions.md#glue:getcompletion) |

| `glue` | [glue:GetSession](../actions.md#glue:getsession) |

| `glue` | [glue:GetStatement](../actions.md#glue:getstatement) |

| `glue` | [glue:ListSessions](../actions.md#glue:listsessions) |

| `glue` | [glue:ListStatements](../actions.md#glue:liststatements) |

| `glue` | [glue:RunStatement](../actions.md#glue:runstatement) |

| `glue` | [glue:StartCompletion](../actions.md#glue:startcompletion) |

| `glue` | [glue:StopSession](../actions.md#glue:stopsession) |

| `glue` | [glue:TagResource](../actions.md#glue:tagresource) |

| `glue` | [glue:UntagResource](../actions.md#glue:untagresource) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `tag` | [tag:TagResources](../actions.md#tag:tagresources) |

| `tag` | [tag:UntagResources](../actions.md#tag:untagresources) |
