# Policy: AWSIoTDeviceTesterForGreengrassFullAccess

ARN: `arn:aws:iam::aws:policy/AWSIoTDeviceTesterForGreengrassFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| iot |
| iot-device-tester |
| greengrass |
| lambda |
| iam |
| execute-api |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `execute-api` | [execute-api:Invoke](../actions.md#execute-api:invoke) |

| `greengrass` | [greengrass:*](../actions.md#greengrass:all) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iot` | [iot:AttachPolicy](../actions.md#iot:attachpolicy) |

| `iot` | [iot:AttachThingPrincipal](../actions.md#iot:attachthingprincipal) |

| `iot` | [iot:CreateCertificateFromCsr](../actions.md#iot:createcertificatefromcsr) |

| `iot` | [iot:CreateJob](../actions.md#iot:createjob) |

| `iot` | [iot:CreateKeysAndCertificate](../actions.md#iot:createkeysandcertificate) |

| `iot` | [iot:CreatePolicy](../actions.md#iot:createpolicy) |

| `iot` | [iot:CreateThing](../actions.md#iot:creatething) |

| `iot` | [iot:DeleteCertificate](../actions.md#iot:deletecertificate) |

| `iot` | [iot:DeleteJob](../actions.md#iot:deletejob) |

| `iot` | [iot:DeletePolicy](../actions.md#iot:deletepolicy) |

| `iot` | [iot:DeleteThing](../actions.md#iot:deletething) |

| `iot` | [iot:DescribeEndpoint](../actions.md#iot:describeendpoint) |

| `iot` | [iot:DescribeJob](../actions.md#iot:describejob) |

| `iot` | [iot:DescribeJobExecution](../actions.md#iot:describejobexecution) |

| `iot` | [iot:DetachPolicy](../actions.md#iot:detachpolicy) |

| `iot` | [iot:DetachThingPrincipal](../actions.md#iot:detachthingprincipal) |

| `iot` | [iot:GetThingShadow](../actions.md#iot:getthingshadow) |

| `iot` | [iot:ListThings](../actions.md#iot:listthings) |

| `iot` | [iot:UpdateCertificate](../actions.md#iot:updatecertificate) |

| `iot` | [iot:UpdateThingShadow](../actions.md#iot:updatethingshadow) |

| `iot-device-tester` | [iot-device-tester:CheckVersion](../actions.md#iot-device-tester:checkversion) |

| `iot-device-tester` | [iot-device-tester:DownloadTestSuite](../actions.md#iot-device-tester:downloadtestsuite) |

| `iot-device-tester` | [iot-device-tester:LatestIdt](../actions.md#iot-device-tester:latestidt) |

| `iot-device-tester` | [iot-device-tester:SendMetrics](../actions.md#iot-device-tester:sendmetrics) |

| `iot-device-tester` | [iot-device-tester:SupportedVersion](../actions.md#iot-device-tester:supportedversion) |

| `lambda` | [lambda:CreateFunction](../actions.md#lambda:createfunction) |

| `lambda` | [lambda:DeleteFunction](../actions.md#lambda:deletefunction) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteBucket](../actions.md#s3:deletebucket) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:DeleteObjectVersion](../actions.md#s3:deleteobjectversion) |

| `s3` | [s3:ListBucketVersions](../actions.md#s3:listbucketversions) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |
