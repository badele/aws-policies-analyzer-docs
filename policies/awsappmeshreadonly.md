# Policy: AWSAppMeshReadOnly

ARN: `arn:aws:iam::aws:policy/AWSAppMeshReadOnly`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudformation |
| acm |
| servicediscovery |
| appmesh |
| acm-pca |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:DescribeCertificate](../actions.md#acm:describecertificate) |

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `acm-pca` | [acm-pca:DescribeCertificateAuthority](../actions.md#acm-pca:describecertificateauthority) |

| `acm-pca` | [acm-pca:ListCertificateAuthorities](../actions.md#acm-pca:listcertificateauthorities) |

| `appmesh` | [appmesh:Describe*](../actions.md#appmesh:describeall) |

| `appmesh` | [appmesh:List*](../actions.md#appmesh:listall) |

| `cloudformation` | [cloudformation:DescribeStack*](../actions.md#cloudformation:describestackall) |

| `servicediscovery` | [servicediscovery:ListInstances](../actions.md#servicediscovery:listinstances) |

| `servicediscovery` | [servicediscovery:ListNamespaces](../actions.md#servicediscovery:listnamespaces) |

| `servicediscovery` | [servicediscovery:ListServices](../actions.md#servicediscovery:listservices) |
