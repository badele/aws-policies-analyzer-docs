# Policy: AmazonBedrockStudioPermissionsBoundary

ARN: `arn:aws:iam::aws:policy/AmazonBedrockStudioPermissionsBoundary`

## Attached Roles

## Attached Services

| Service |
|---------|
| bedrock |
| lambda |
| secretsmanager |
| logs |
| aoss |
| s3 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `aoss` | [aoss:APIAccessAll](../actions.md#aoss:apiaccessall) |

| `bedrock` | [bedrock:ApplyGuardrail](../actions.md#bedrock:applyguardrail) |

| `bedrock` | [bedrock:CreatePrompt](../actions.md#bedrock:createprompt) |

| `bedrock` | [bedrock:CreatePromptVersion](../actions.md#bedrock:createpromptversion) |

| `bedrock` | [bedrock:DeletePrompt](../actions.md#bedrock:deleteprompt) |

| `bedrock` | [bedrock:GetIngestionJob](../actions.md#bedrock:getingestionjob) |

| `bedrock` | [bedrock:GetPrompt](../actions.md#bedrock:getprompt) |

| `bedrock` | [bedrock:InvokeAgent](../actions.md#bedrock:invokeagent) |

| `bedrock` | [bedrock:InvokeFlow](../actions.md#bedrock:invokeflow) |

| `bedrock` | [bedrock:InvokeModel](../actions.md#bedrock:invokemodel) |

| `bedrock` | [bedrock:InvokeModelWithResponseStream](../actions.md#bedrock:invokemodelwithresponsestream) |

| `bedrock` | [bedrock:ListIngestionJobs](../actions.md#bedrock:listingestionjobs) |

| `bedrock` | [bedrock:ListPrompts](../actions.md#bedrock:listprompts) |

| `bedrock` | [bedrock:ListTagsForResource](../actions.md#bedrock:listtagsforresource) |

| `bedrock` | [bedrock:Retrieve](../actions.md#bedrock:retrieve) |

| `bedrock` | [bedrock:RetrieveAndGenerate](../actions.md#bedrock:retrieveandgenerate) |

| `bedrock` | [bedrock:StartIngestionJob](../actions.md#bedrock:startingestionjob) |

| `bedrock` | [bedrock:TagResource](../actions.md#bedrock:tagresource) |

| `bedrock` | [bedrock:UntagResource](../actions.md#bedrock:untagresource) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `kms` | [kms:GenerateDataKey](../actions.md#kms:generatedatakey) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:DeleteObjectVersion](../actions.md#s3:deleteobjectversion) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucketVersions](../actions.md#s3:listbucketversions) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:PutSecretValue](../actions.md#secretsmanager:putsecretvalue) |
