# Policy: AWSBillingReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSBillingReadOnlyAccess`

## Attached Roles

| Role Name |
|-----------|
## Attached Services

| Service |
|---------|
| payments |
| freetier |
| tax |
| consolidatedbilling |
| ce |
| billing |
| budgets |
| cur |
| mapcredits |
| purchase-orders |
| account |
| sustainability |
| invoicing |
| aws-portal |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `account` | [account:GetAccountInformation](../actions.md#account:getaccountinformation) |

| `aws-portal` | [aws-portal:ViewBilling](../actions.md#aws-portal:viewbilling) |

| `billing` | [billing:GetBillingData](../actions.md#billing:getbillingdata) |

| `billing` | [billing:GetBillingDetails](../actions.md#billing:getbillingdetails) |

| `billing` | [billing:GetBillingNotifications](../actions.md#billing:getbillingnotifications) |

| `billing` | [billing:GetBillingPreferences](../actions.md#billing:getbillingpreferences) |

| `billing` | [billing:GetContractInformation](../actions.md#billing:getcontractinformation) |

| `billing` | [billing:GetCredits](../actions.md#billing:getcredits) |

| `billing` | [billing:GetIAMAccessPreference](../actions.md#billing:getiamaccesspreference) |

| `billing` | [billing:GetSellerOfRecord](../actions.md#billing:getsellerofrecord) |

| `billing` | [billing:ListBillingViews](../actions.md#billing:listbillingviews) |

| `budgets` | [budgets:DescribeBudgetAction](../actions.md#budgets:describebudgetaction) |

| `budgets` | [budgets:DescribeBudgetActionHistories](../actions.md#budgets:describebudgetactionhistories) |

| `budgets` | [budgets:DescribeBudgetActionsForAccount](../actions.md#budgets:describebudgetactionsforaccount) |

| `budgets` | [budgets:DescribeBudgetActionsForBudget](../actions.md#budgets:describebudgetactionsforbudget) |

| `budgets` | [budgets:ViewBudget](../actions.md#budgets:viewbudget) |

| `ce` | [ce:DescribeCostCategoryDefinition](../actions.md#ce:describecostcategorydefinition) |

| `ce` | [ce:GetCostAndUsage](../actions.md#ce:getcostandusage) |

| `ce` | [ce:GetDimensionValues](../actions.md#ce:getdimensionvalues) |

| `ce` | [ce:GetTags](../actions.md#ce:gettags) |

| `ce` | [ce:ListCostAllocationTagBackfillHistory](../actions.md#ce:listcostallocationtagbackfillhistory) |

| `ce` | [ce:ListCostAllocationTags](../actions.md#ce:listcostallocationtags) |

| `ce` | [ce:ListCostCategoryDefinitions](../actions.md#ce:listcostcategorydefinitions) |

| `ce` | [ce:ListTagsForResource](../actions.md#ce:listtagsforresource) |

| `consolidatedbilling` | [consolidatedbilling:GetAccountBillingRole](../actions.md#consolidatedbilling:getaccountbillingrole) |

| `consolidatedbilling` | [consolidatedbilling:ListLinkedAccounts](../actions.md#consolidatedbilling:listlinkedaccounts) |

| `cur` | [cur:DescribeReportDefinitions](../actions.md#cur:describereportdefinitions) |

| `cur` | [cur:GetClassicReport](../actions.md#cur:getclassicreport) |

| `cur` | [cur:GetClassicReportPreferences](../actions.md#cur:getclassicreportpreferences) |

| `cur` | [cur:GetUsageReport](../actions.md#cur:getusagereport) |

| `freetier` | [freetier:GetFreeTierAlertPreference](../actions.md#freetier:getfreetieralertpreference) |

| `freetier` | [freetier:GetFreeTierUsage](../actions.md#freetier:getfreetierusage) |

| `invoicing` | [invoicing:BatchGetInvoiceProfile](../actions.md#invoicing:batchgetinvoiceprofile) |

| `invoicing` | [invoicing:GetInvoiceEmailDeliveryPreferences](../actions.md#invoicing:getinvoiceemaildeliverypreferences) |

| `invoicing` | [invoicing:GetInvoicePDF](../actions.md#invoicing:getinvoicepdf) |

| `invoicing` | [invoicing:GetInvoiceUnit](../actions.md#invoicing:getinvoiceunit) |

| `invoicing` | [invoicing:ListInvoiceSummaries](../actions.md#invoicing:listinvoicesummaries) |

| `invoicing` | [invoicing:ListInvoiceUnits](../actions.md#invoicing:listinvoiceunits) |

| `invoicing` | [invoicing:ListTagsForResource](../actions.md#invoicing:listtagsforresource) |

| `mapcredits` | [mapcredits:ListAssociatedPrograms](../actions.md#mapcredits:listassociatedprograms) |

| `mapcredits` | [mapcredits:ListQuarterCredits](../actions.md#mapcredits:listquartercredits) |

| `mapcredits` | [mapcredits:ListQuarterSpend](../actions.md#mapcredits:listquarterspend) |

| `payments` | [payments:GetFinancingApplication](../actions.md#payments:getfinancingapplication) |

| `payments` | [payments:GetFinancingLine](../actions.md#payments:getfinancingline) |

| `payments` | [payments:GetFinancingLineWithdrawal](../actions.md#payments:getfinancinglinewithdrawal) |

| `payments` | [payments:GetFinancingOption](../actions.md#payments:getfinancingoption) |

| `payments` | [payments:GetPaymentInstrument](../actions.md#payments:getpaymentinstrument) |

| `payments` | [payments:GetPaymentStatus](../actions.md#payments:getpaymentstatus) |

| `payments` | [payments:ListFinancingApplications](../actions.md#payments:listfinancingapplications) |

| `payments` | [payments:ListFinancingLineWithdrawals](../actions.md#payments:listfinancinglinewithdrawals) |

| `payments` | [payments:ListFinancingLines](../actions.md#payments:listfinancinglines) |

| `payments` | [payments:ListPaymentInstruments](../actions.md#payments:listpaymentinstruments) |

| `payments` | [payments:ListPaymentPreferences](../actions.md#payments:listpaymentpreferences) |

| `payments` | [payments:ListPaymentProgramOptions](../actions.md#payments:listpaymentprogramoptions) |

| `payments` | [payments:ListPaymentProgramStatus](../actions.md#payments:listpaymentprogramstatus) |

| `payments` | [payments:ListTagsForResource](../actions.md#payments:listtagsforresource) |

| `purchase-orders` | [purchase-orders:GetPurchaseOrder](../actions.md#purchase-orders:getpurchaseorder) |

| `purchase-orders` | [purchase-orders:ListPurchaseOrderInvoices](../actions.md#purchase-orders:listpurchaseorderinvoices) |

| `purchase-orders` | [purchase-orders:ListPurchaseOrders](../actions.md#purchase-orders:listpurchaseorders) |

| `purchase-orders` | [purchase-orders:ListTagsForResource](../actions.md#purchase-orders:listtagsforresource) |

| `purchase-orders` | [purchase-orders:ViewPurchaseOrders](../actions.md#purchase-orders:viewpurchaseorders) |

| `sustainability` | [sustainability:GetCarbonFootprintSummary](../actions.md#sustainability:getcarbonfootprintsummary) |

| `tax` | [tax:GetTaxInheritance](../actions.md#tax:gettaxinheritance) |

| `tax` | [tax:GetTaxRegistrationDocument](../actions.md#tax:gettaxregistrationdocument) |

| `tax` | [tax:ListTaxRegistrations](../actions.md#tax:listtaxregistrations) |
