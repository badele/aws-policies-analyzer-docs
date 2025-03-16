# Policy: AWSElasticBeanstalkReadOnly

ARN: `arn:aws:iam::aws:policy/AWSElasticBeanstalkReadOnly`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| elasticbeanstalk |
| cloudformation |
| cloudtrail |
| cloudwatch |
| acm |
| elasticloadbalancing |
| iam |
| sqs |
| rds |
| ec2 |
| s3 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `autoscaling` | [autoscaling:DescribeAccountLimits](../actions.md#autoscaling:describeaccountlimits) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `autoscaling` | [autoscaling:DescribeAutoScalingInstances](../actions.md#autoscaling:describeautoscalinginstances) |

| `autoscaling` | [autoscaling:DescribeLaunchConfigurations](../actions.md#autoscaling:describelaunchconfigurations) |

| `autoscaling` | [autoscaling:DescribeLoadBalancers](../actions.md#autoscaling:describeloadbalancers) |

| `autoscaling` | [autoscaling:DescribeNotificationConfigurations](../actions.md#autoscaling:describenotificationconfigurations) |

| `autoscaling` | [autoscaling:DescribePolicies](../actions.md#autoscaling:describepolicies) |

| `autoscaling` | [autoscaling:DescribeScalingActivities](../actions.md#autoscaling:describescalingactivities) |

| `autoscaling` | [autoscaling:DescribeScheduledActions](../actions.md#autoscaling:describescheduledactions) |

| `cloudformation` | [cloudformation:DescribeStackResource](../actions.md#cloudformation:describestackresource) |

| `cloudformation` | [cloudformation:DescribeStackResources](../actions.md#cloudformation:describestackresources) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:GetTemplate](../actions.md#cloudformation:gettemplate) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudformation` | [cloudformation:ValidateTemplate](../actions.md#cloudformation:validatetemplate) |

| `cloudtrail` | [cloudtrail:LookupEvents](../actions.md#cloudtrail:lookupevents) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeImages](../actions.md#ec2:describeimages) |

| `ec2` | [ec2:DescribeInstanceAttribute](../actions.md#ec2:describeinstanceattribute) |

| `ec2` | [ec2:DescribeInstanceStatus](../actions.md#ec2:describeinstancestatus) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeKeyPairs](../actions.md#ec2:describekeypairs) |

| `ec2` | [ec2:DescribeLaunchTemplateVersions](../actions.md#ec2:describelaunchtemplateversions) |

| `ec2` | [ec2:DescribeLaunchTemplates](../actions.md#ec2:describelaunchtemplates) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeSpotInstanceRequests](../actions.md#ec2:describespotinstancerequests) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `elasticbeanstalk` | [elasticbeanstalk:Check*](../actions.md#elasticbeanstalk:checkall) |

| `elasticbeanstalk` | [elasticbeanstalk:Describe*](../actions.md#elasticbeanstalk:describeall) |

| `elasticbeanstalk` | [elasticbeanstalk:List*](../actions.md#elasticbeanstalk:listall) |

| `elasticbeanstalk` | [elasticbeanstalk:RequestEnvironmentInfo](../actions.md#elasticbeanstalk:requestenvironmentinfo) |

| `elasticbeanstalk` | [elasticbeanstalk:RetrieveEnvironmentInfo](../actions.md#elasticbeanstalk:retrieveenvironmentinfo) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeInstanceHealth](../actions.md#elasticloadbalancing:describeinstancehealth) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeSSLPolicies](../actions.md#elasticloadbalancing:describesslpolicies) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetHealth](../actions.md#elasticloadbalancing:describetargethealth) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListInstanceProfiles](../actions.md#iam:listinstanceprofiles) |

| `iam` | [iam:ListRolePolicies](../actions.md#iam:listrolepolicies) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:ListServerCertificates](../actions.md#iam:listservercertificates) |

| `rds` | [rds:DescribeDBEngineVersions](../actions.md#rds:describedbengineversions) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `rds` | [rds:DescribeOrderableDBInstanceOptions](../actions.md#rds:describeorderabledbinstanceoptions) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectAcl](../actions.md#s3:getobjectacl) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `s3` | [s3:GetObjectVersionAcl](../actions.md#s3:getobjectversionacl) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |
