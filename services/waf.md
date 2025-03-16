# Service: waf

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/CloudFrontFullAccess` | [CloudFrontFullAccess](../policies.md#cloudfrontfullaccess) |
| `arn:aws:iam::aws:policy/CloudFrontReadOnlyAccess` | [CloudFrontReadOnlyAccess](../policies.md#cloudfrontreadonlyaccess) |
| `arn:aws:iam::aws:policy/SecurityAudit` | [SecurityAudit](../policies.md#securityaudit) |
| `arn:aws:iam::aws:policy/AWSWAFReadOnlyAccess` | [AWSWAFReadOnlyAccess](../policies.md#awswafreadonlyaccess) |
| `arn:aws:iam::aws:policy/AWSWAFFullAccess` | [AWSWAFFullAccess](../policies.md#awswaffullaccess) |
| `arn:aws:iam::aws:policy/job-function/ViewOnlyAccess` | [ViewOnlyAccess](../policies.md#viewonlyaccess) |
| `arn:aws:iam::aws:policy/job-function/SupportUser` | [SupportUser](../policies.md#supportuser) |
| `arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy` | [FMSServiceRolePolicy](../policies.md#fmsservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSFMAdminFullAccess` | [AWSFMAdminFullAccess](../policies.md#awsfmadminfullaccess) |
| `arn:aws:iam::aws:policy/AWSFMAdminReadOnlyAccess` | [AWSFMAdminReadOnlyAccess](../policies.md#awsfmadminreadonlyaccess) |
| `arn:aws:iam::aws:policy/AWSFMMemberReadOnlyAccess` | [AWSFMMemberReadOnlyAccess](../policies.md#awsfmmemberreadonlyaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy` | [AWSConfigServiceRolePolicy](../policies.md#awsconfigservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy` | [AWSShieldDRTAccessPolicy](../policies.md#awsshielddrtaccesspolicy) |
| `arn:aws:iam::aws:policy/AWSWAFConsoleFullAccess` | [AWSWAFConsoleFullAccess](../policies.md#awswafconsolefullaccess) |
| `arn:aws:iam::aws:policy/AWSWAFConsoleReadOnlyAccess` | [AWSWAFConsoleReadOnlyAccess](../policies.md#awswafconsolereadonlyaccess) |
| `arn:aws:iam::aws:policy/service-role/AWS_ConfigRole` | [AWS_ConfigRole](../policies.md#aws_configrole) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSAuditManagerServiceRolePolicy` | [AWSAuditManagerServiceRolePolicy](../policies.md#awsauditmanagerservicerolepolicy) |
| `arn:aws:iam::aws:policy/ResourceGroupsTaggingAPITagUntagSupportedResources` | [ResourceGroupsTaggingAPITagUntagSupportedResources](../policies.md#resourcegroupstaggingapitaguntagsupportedresources) |
| `arn:aws:iam::aws:policy/AWSPartnerLedSupportReadOnlyAccess` | [AWSPartnerLedSupportReadOnlyAccess](../policies.md#awspartnerledsupportreadonlyaccess) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [waf:*](../actions.md#waf:all) | waf |
| [waf:CreateWebACL](../actions.md#waf:createwebacl) | waf |
| [waf:DeletePermissionPolicy](../actions.md#waf:deletepermissionpolicy) | waf |
| [waf:DeleteWebACL](../actions.md#waf:deletewebacl) | waf |
| [waf:Get*](../actions.md#waf:getall) | waf |
| [waf:GetChangeToken](../actions.md#waf:getchangetoken) | waf |
| [waf:GetLoggingConfiguration](../actions.md#waf:getloggingconfiguration) | waf |
| [waf:GetPermissionPolicy](../actions.md#waf:getpermissionpolicy) | waf |
| [waf:GetRule](../actions.md#waf:getrule) | waf |
| [waf:GetRuleGroup](../actions.md#waf:getrulegroup) | waf |
| [waf:GetWebACL](../actions.md#waf:getwebacl) | waf |
| [waf:List*](../actions.md#waf:listall) | waf |
| [waf:ListActivatedRulesInRuleGroup](../actions.md#waf:listactivatedrulesinrulegroup) | waf |
| [waf:ListRuleGroups](../actions.md#waf:listrulegroups) | waf |
| [waf:ListRules](../actions.md#waf:listrules) | waf |
| [waf:ListSubscribedRuleGroups](../actions.md#waf:listsubscribedrulegroups) | waf |
| [waf:ListTagsForResource](../actions.md#waf:listtagsforresource) | waf |
| [waf:ListWebACLs](../actions.md#waf:listwebacls) | waf |
| [waf:ListWebAcls](../actions.md#waf:listwebacls) | waf |
| [waf:PutPermissionPolicy](../actions.md#waf:putpermissionpolicy) | waf |
| [waf:TagResource](../actions.md#waf:tagresource) | waf |
| [waf:UntagResource](../actions.md#waf:untagresource) | waf |
| [waf:UpdateWebACL](../actions.md#waf:updatewebacl) | waf |
| [waf:getByteMatchSet](../actions.md#waf:getbytematchset) | waf |
| [waf:getChangeTokenStatus](../actions.md#waf:getchangetokenstatus) | waf |
| [waf:getGeoMatchSet](../actions.md#waf:getgeomatchset) | waf |
| [waf:getIPSet](../actions.md#waf:getipset) | waf |
| [waf:getLoggingConfiguration](../actions.md#waf:getloggingconfiguration) | waf |
| [waf:getRateBasedRule](../actions.md#waf:getratebasedrule) | waf |
| [waf:getRegexMatchSet](../actions.md#waf:getregexmatchset) | waf |
| [waf:getRegexPatternSet](../actions.md#waf:getregexpatternset) | waf |
| [waf:getRule](../actions.md#waf:getrule) | waf |
| [waf:getRuleGroup](../actions.md#waf:getrulegroup) | waf |
| [waf:getSampledRequests](../actions.md#waf:getsampledrequests) | waf |
| [waf:getSizeConstraintSet](../actions.md#waf:getsizeconstraintset) | waf |
| [waf:getSqlInjectionMatchSet](../actions.md#waf:getsqlinjectionmatchset) | waf |
| [waf:getWebACL](../actions.md#waf:getwebacl) | waf |
| [waf:getXssMatchSet](../actions.md#waf:getxssmatchset) | waf |
| [waf:listActivatedRulesInRuleGroup](../actions.md#waf:listactivatedrulesinrulegroup) | waf |
| [waf:listByteMatchSets](../actions.md#waf:listbytematchsets) | waf |
| [waf:listGeoMatchSets](../actions.md#waf:listgeomatchsets) | waf |
| [waf:listIPSets](../actions.md#waf:listipsets) | waf |
| [waf:listLoggingConfigurations](../actions.md#waf:listloggingconfigurations) | waf |
| [waf:listRateBasedRules](../actions.md#waf:listratebasedrules) | waf |
| [waf:listRegexMatchSets](../actions.md#waf:listregexmatchsets) | waf |
| [waf:listRegexPatternSets](../actions.md#waf:listregexpatternsets) | waf |
| [waf:listRuleGroups](../actions.md#waf:listrulegroups) | waf |
| [waf:listRules](../actions.md#waf:listrules) | waf |
| [waf:listSizeConstraintSets](../actions.md#waf:listsizeconstraintsets) | waf |
| [waf:listSqlInjectionMatchSets](../actions.md#waf:listsqlinjectionmatchsets) | waf |
| [waf:listWebACLs](../actions.md#waf:listwebacls) | waf |
| [waf:listXssMatchSets](../actions.md#waf:listxssmatchsets) | waf |