# Policy: AWSAppMeshFullAccess

ARN: `arn:aws:iam::aws:policy/AWSAppMeshFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudformation |
| acm |
| servicediscovery |
| iam |
| appmesh |
| acm-pca |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:DescribeCertificate](../actions.md#acm:describecertificate) |

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `acm-pca` | [acm-pca:DescribeCertificateAuthority](../actions.md#acm-pca:describecertificateauthority) |

| `acm-pca` | [acm-pca:ListCertificateAuthorities](../actions.md#acm-pca:listcertificateauthorities) |

| `appmesh` | [appmesh:*](../actions.md#appmesh:all) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudformation` | [cloudformation:DescribeStack*](../actions.md#cloudformation:describestackall) |

| `cloudformation` | [cloudformation:UpdateStack](../actions.md#cloudformation:updatestack) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `servicediscovery` | [servicediscovery:ListInstances](../actions.md#servicediscovery:listinstances) |

| `servicediscovery` | [servicediscovery:ListNamespaces](../actions.md#servicediscovery:listnamespaces) |

| `servicediscovery` | [servicediscovery:ListServices](../actions.md#servicediscovery:listservices) |
