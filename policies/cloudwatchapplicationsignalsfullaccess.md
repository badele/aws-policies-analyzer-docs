# Policy: CloudWatchApplicationSignalsFullAccess

ARN: `arn:aws:iam::aws:policy/CloudWatchApplicationSignalsFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudwatch |
| logs |
| application-signals |
| rum |
| iam |
| xray |
| synthetics |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `application-signals` | [application-signals:*](../actions.md#application-signals:all) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `logs` | [logs:GetQueryResults](../actions.md#logs:getqueryresults) |

| `logs` | [logs:StartQuery](../actions.md#logs:startquery) |

| `logs` | [logs:StopQuery](../actions.md#logs:stopquery) |

| `rum` | [rum:BatchCreateRumMetricDefinitions](../actions.md#rum:batchcreaterummetricdefinitions) |

| `rum` | [rum:BatchDeleteRumMetricDefinitions](../actions.md#rum:batchdeleterummetricdefinitions) |

| `rum` | [rum:BatchGetRumMetricDefinitions](../actions.md#rum:batchgetrummetricdefinitions) |

| `rum` | [rum:GetAppMonitor](../actions.md#rum:getappmonitor) |

| `rum` | [rum:GetAppMonitorData](../actions.md#rum:getappmonitordata) |

| `rum` | [rum:ListAppMonitors](../actions.md#rum:listappmonitors) |

| `rum` | [rum:PutRumMetricsDestination](../actions.md#rum:putrummetricsdestination) |

| `rum` | [rum:UpdateRumMetricDefinition](../actions.md#rum:updaterummetricdefinition) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `synthetics` | [synthetics:DescribeCanaries](../actions.md#synthetics:describecanaries) |

| `synthetics` | [synthetics:DescribeCanariesLastRun](../actions.md#synthetics:describecanarieslastrun) |

| `synthetics` | [synthetics:GetCanaryRuns](../actions.md#synthetics:getcanaryruns) |

| `xray` | [xray:GetTraceSummaries](../actions.md#xray:gettracesummaries) |
