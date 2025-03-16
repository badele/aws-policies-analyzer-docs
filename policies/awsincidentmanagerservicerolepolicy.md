# Policy: AWSIncidentManagerServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSIncidentManagerServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm-incidents |
| cloudwatch |
| ssm |
| ssm-contacts |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `ssm` | [ssm:AssociateOpsItemRelatedItem](../actions.md#ssm:associateopsitemrelateditem) |

| `ssm` | [ssm:CreateOpsItem](../actions.md#ssm:createopsitem) |

| `ssm-contacts` | [ssm-contacts:StartEngagement](../actions.md#ssm-contacts:startengagement) |

| `ssm-incidents` | [ssm-incidents:CreateTimelineEvent](../actions.md#ssm-incidents:createtimelineevent) |

| `ssm-incidents` | [ssm-incidents:ListIncidentRecords](../actions.md#ssm-incidents:listincidentrecords) |
