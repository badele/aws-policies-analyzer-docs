# Policy: EC2InstanceProfileForImageBuilderECRContainerBuilds

ARN: `arn:aws:iam::aws:policy/EC2InstanceProfileForImageBuilderECRContainerBuilds`

## Attached Roles

## Attached Services

| Service |
|---------|
| imagebuilder |
| logs |
| ecr |
| s3 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ecr` | [ecr:BatchCheckLayerAvailability](../actions.md#ecr:batchchecklayeravailability) |

| `ecr` | [ecr:BatchGetImage](../actions.md#ecr:batchgetimage) |

| `ecr` | [ecr:CompleteLayerUpload](../actions.md#ecr:completelayerupload) |

| `ecr` | [ecr:GetAuthorizationToken](../actions.md#ecr:getauthorizationtoken) |

| `ecr` | [ecr:GetDownloadUrlForLayer](../actions.md#ecr:getdownloadurlforlayer) |

| `ecr` | [ecr:InitiateLayerUpload](../actions.md#ecr:initiatelayerupload) |

| `ecr` | [ecr:PutImage](../actions.md#ecr:putimage) |

| `ecr` | [ecr:UploadLayerPart](../actions.md#ecr:uploadlayerpart) |

| `imagebuilder` | [imagebuilder:GetComponent](../actions.md#imagebuilder:getcomponent) |

| `imagebuilder` | [imagebuilder:GetContainerRecipe](../actions.md#imagebuilder:getcontainerrecipe) |

| `kms` | [kms:Decrypt](../actions.md#kms:decrypt) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |
