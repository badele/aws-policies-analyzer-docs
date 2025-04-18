#!/usr/bin/env python3

import argparse
import os
from typing import Any, Dict, List

from aws_policies_analyzer_sdk import (
    build_cross_reference_table,
    extract_service_from_action,
    is_policy_managed_by_aws,
    is_role_managed_by_aws,
    slugify,
)

NB_COLUMNS = 3


def generate_roles_markdown(
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for roles index page.

    Args:
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    content = """---
search:
  exclude: true
---

"""
    content += "# AWS IAM Roles\n\n"
    content += "This document lists all IAM roles. Click on a role name to view its details.\n\n"

    content += "| Role Name | # Policies | # Services | # Actions |\n"
    content += "|-----------|------------|------------|-----------|\n"

    # Generate list of roles with links to individual pages
    for role_arn in sorted(cross_ref["roles"].keys()):
        role_data = cross_ref["roles"][role_arn]
        role_name = role_data["name"]
        role_filename = slugify(role_name)

        nb_policies = (
            str(len(role_data["policies"])) if len(role_data["policies"]) > 0 else ""
        )
        nb_services = (
            str(len(role_data["services"])) if len(role_data["services"]) > 0 else ""
        )
        nb_actions = (
            str(len(role_data["actions"])) if len(role_data["actions"]) > 0 else ""
        )

        content += f"| [{role_name}]({role_filename}.md) | {nb_policies} | {nb_services} | {nb_actions}\n"

    return content


def generate_single_role_markdown(
    role_arn: str,
    role_data: Dict[str, Any],
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for a single role.

    Args:
        role_name: Name of the role
        role_data: Data for this role
        cross_ref: Cross-reference table

    Returns:
        Markdown content for the role
    """
    role_name = role_data["name"]
    if only_managed_by_aws and not is_role_managed_by_aws(role_arn):
        print(f"Skipping managed role: {role_arn}")
        return ""

    content = f"# Role: {role_name}\n\n"
    content += f"ARN: `{role_arn}`\n\n"

    # Policies section
    content += "## Attached Policies\n\n"
    if role_data["policies"]:
        content += "| Policy ARN | Policy Name | # Services| # Actions|\n"
        content += "|------------|-------------|\n"
        for policy_arn in role_data["policies"]:
            if policy_arn in cross_ref["policies"]:
                policy_name = cross_ref["policies"][policy_arn]["name"]
                policy_link = (
                    f"[{policy_name}](../../policies/{slugify(policy_name.lower())})"
                )

                nb_services = len(cross_ref["policies"][policy_arn]["services"])
                nb_actions = len(cross_ref["policies"][policy_arn]["actions"])

                content += f"| `{policy_arn}` | {policy_link} | {nb_services} | {nb_actions} |\n"
        content += "\n"

    # Actions section
    content += "\n## Allowed Actions\n\n"
    if role_data["actions"]:
        content += "| Actions | Services |\n"
        content += "|---------|:--------:|\n"

        # Group actions by service
        actions_by_service = {}
        for action in sorted(role_data["actions"]):
            service = "all"
            if ":" in action:
                service, action_name = action.split(":", 1)
            if service not in actions_by_service:
                actions_by_service[service] = []
            actions_by_service[service].append(action)

        # List actions by service
        for service in sorted(actions_by_service.keys()):
            for action in sorted(actions_by_service[service]):
                service_link = f"[{service}](../../services/{slugify(service)})"
                action_link = f"[{action}](../../actions/{slugify(action)})"
                content += f"| {action_link} | {service_link} |\n"
        content += "\n"

    return content


def generate_policies_markdown(
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for policies index page.

    Args:
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    content = """---
search:
  exclude: true
---

"""
    content += "# AWS IAM Policies\n\n"
    content += "This document lists all IAM policies. Click on a policy name to view its details.\n\n"

    content += "| Policy Name | # By roles | # Services | # Actions |\n"
    content += "|-------------|---------|------------|-----------|\n"

    # Generate list of policies with links to individual pages
    for policy_arn in sorted(cross_ref["policies"].keys()):
        policy_data = cross_ref["policies"][policy_arn]
        policy_name = policy_data["name"]
        policy_filename = slugify(policy_name)

        nb_roles = (
            str(len(policy_data["roles"]))
            if len(policy_data["roles"]) > 0 and not only_managed_by_aws
            else ""
        )
        nb_services = (
            str(len(policy_data["services"]))
            if len(policy_data["services"]) > 0
            else ""
        )
        nb_actions = (
            str(len(policy_data["actions"])) if len(policy_data["actions"]) > 0 else ""
        )

        content += f"| [{policy_name}]({policy_filename}) | {nb_roles} | {nb_services} | {nb_actions}\n"

    return content


def generate_single_policy_markdown(
    policy_arn: str,
    policy_data: Dict[str, Any],
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for a single policy.

    Args:
        policy_arn: ARN of the policy
        policy_data: Data for this policy
        cross_ref: Cross-reference table

    Returns:
        Markdown content for the policy
    """
    policy_name = policy_data["name"]
    if only_managed_by_aws and not is_policy_managed_by_aws(policy_arn):
        print(f"Skipping managed policy: {policy_arn}")
        return ""

    content = f"# Policy: {policy_name}\n\n"
    content += f"ARN: `{policy_arn}`\n\n"

    # Roles section
    if not only_managed_by_aws:
        content += "## Roles use this policy\n\n"
        if policy_data["roles"]:
            content += "| Role Name |\n"
            content += "|-----------|\n"
            for role_arn in policy_data["roles"]:
                if role_arn in cross_ref["roles"]:
                    role_name = cross_ref["roles"][role_arn]["name"]
                    role_link = (
                        f"[{role_name}](../../roles/{slugify(role_name.lower())})"
                    )
                    content += f"| {role_link} |\n"
            content += "\n"

    # Actions section
    content += "\n## Allowed Actions\n\n"
    if policy_data["actions"]:
        content += "| Actions | Services |\n"
        content += "|---------|:--------:|\n"

        # Group actions by service
        actions_by_service = {}
        for action in sorted(policy_data["actions"]):
            service = "all"
            if ":" in action:
                service, action_name = action.split(":", 1)
            if service not in actions_by_service:
                actions_by_service[service] = []
            actions_by_service[service].append(action)

        # List actions by service
        for service in sorted(actions_by_service.keys()):
            for action in sorted(actions_by_service[service]):
                service_link = f"[{service}](../../services/{slugify(service)})"
                action_link = f"[{action}](../../actions/{slugify(action)})"
                content += f"| {action_link} | {service_link} |\n"
        content += "\n"

    return content


def generate_services_markdown(
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for services index page.

    Args:
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    content = """---
search:
  exclude: true
---

"""
    content += "# AWS Services\n\n"
    content += "This document lists all AWS services. Click on a service name to view its details.\n\n"

    content += "| Service Name | # Roles | # Policies | # Actions |\n"
    content += "|--------------|---------|------------|-----------|\n"

    # Generate list of services with links to individual pages
    for service_name in sorted(cross_ref["services"].keys()):
        service_data = cross_ref["services"][service_name]
        service_filename = slugify(service_name)

        nb_roles = (
            str(len(service_data["roles"]))
            if len(service_data["roles"]) > 0 and not only_managed_by_aws
            else ""
        )
        nb_policies = (
            str(len(service_data["policies"]))
            if len(service_data["policies"]) > 0
            else ""
        )
        nb_actions = (
            str(len(service_data["actions"]))
            if len(service_data["actions"]) > 0
            else ""
        )

        content += f"| [{service_name}]({service_filename}.md) | {nb_roles} | {nb_policies} | {nb_actions}\n"

    return content


def generate_actions_markdown(
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for actions index page.

    Args:
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    content = """---
search:
  exclude: true
---

"""
    content += "# AWS IAM Actions\n\n"
    content += "This document lists all IAM actions. Click on an action name to view its details.\n\n"

    content += "| Action Name | # Roles | # Policies |\n"
    content += "|-------------|---------|------------|\n"

    # Generate list of actions with links to individual pages
    for action_name in sorted(cross_ref["actions"].keys()):
        action_data = cross_ref["actions"][action_name]
        action_filename = slugify(action_name)

        nb_roles = (
            str(len(action_data["roles"]))
            if "roles" in action_data
            and len(action_data["roles"]) > 0
            and not only_managed_by_aws
            else ""
        )
        nb_policies = (
            str(len(action_data["policies"]))
            if "policies" in action_data and len(action_data["policies"]) > 0
            else ""
        )

        content += (
            f"| [{action_name}]({action_filename}) | {nb_roles} | {nb_policies}\n"
        )

    return content


def generate_single_service_markdown(
    service: str,
    service_data: Dict[str, List[str]],
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for a single service.

    Args:
        service: Name of the service
        service_data: Dictionary of actions grouped by service
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    roles = service_data.get("roles", [])
    policies = service_data.get("policies", [])
    actions = service_data.get("actions", [])

    content = f"# Service: {service}\n\n"

    if not only_managed_by_aws:
        content += "## Roles use this service\n\n"
        if roles:
            content += "| Policy ARN | Policy Name |\n"
            content += "|------------|-------------|\n"
            for role_arn in roles:
                if only_managed_by_aws and not is_role_managed_by_aws(role_arn):
                    continue

                role_name = cross_ref["roles"][role_arn]["name"]
                role_link = f"[{role_name}](../../roles/{slugify(role_name.lower())})"
                content += f"| `{role_arn}` | {role_link} |\n"
            content += "\n"

    # Policies section
    content += "## Attached Policies\n\n"
    if policies:
        content += "| Policy ARN | Policy Name |\n"
        content += "|------------|-------------|\n"
        for policy_arn in service_data["policies"]:
            if only_managed_by_aws and not is_policy_managed_by_aws(policy_arn):
                continue

            policy_name = cross_ref["policies"][policy_arn]["name"]
            policy_link = (
                f"[{policy_name}](../../policies/{slugify(policy_name.lower())})"
            )
            content += f"| `{policy_arn}` | {policy_link} |\n"
        content += "\n"

    # Actions section
    content += "\n## Allowed Actions\n\n"
    if actions:
        content += "| Action | Service |\n"
        content += "|--------|---------|"

        # Group actions by service
        actions_by_service = {}
        for action in sorted(service_data["actions"]):
            service = "all"
            if ":" in action:
                service, action_name = action.split(":", 1)
            if service not in actions_by_service:
                actions_by_service[service] = []
            actions_by_service[service].append(action)

        # List actions by service
        for service in sorted(actions_by_service.keys()):
            for action in sorted(actions_by_service[service]):
                action_link = f"[{action}](../../actions/{slugify(action)})"
                content += f"\n| {action_link} | {service} |"
        content += "\n"

    return content


def generate_single_action_markdown(
    action: str,
    action_data: Dict[str, List[str]],
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for a single action.

    Args:
        action: Name of the action
        action_data: Dictionary of roles, policies, and services associated with the action
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    roles = action_data.get("roles", [])
    policies = action_data.get("policies", [])

    content = f"# Action: {action}\n\n"

    # Roles section
    if not only_managed_by_aws:
        content += "## Roles use this action\n\n"
        if roles:
            content += "| Role ARN | Role Name |\n"
            content += "|----------|-----------|\n"
            for role_arn in roles:
                if only_managed_by_aws and not is_role_managed_by_aws(role_arn):
                    continue

                role_name = cross_ref["roles"][role_arn]["name"]
                role_link = f"[{role_name}](../../roles/{slugify(role_name.lower())})"
                content += f"| `{role_arn}` | {role_link} |\n"

    # Policies section
    content += "## Attached Policies\n\n"
    if policies:
        content += "| Policy ARN | Policy Name |\n"
        content += "|------------|-------------|\n"
        for policy_arn in policies:
            if only_managed_by_aws and not is_policy_managed_by_aws(policy_arn):
                continue

            policy_name = cross_ref["policies"][policy_arn]["name"]
            policy_link = (
                f"[{policy_name}](../../policies/{slugify(policy_name.lower())})"
            )
            content += f"| `{policy_arn}` | {policy_link} |\n"

    # Services section
    content += "\n## Associated Services\n\n"

    service = extract_service_from_action(action)
    content += f"[{service}](../../services/{service})"

    return content


def generate_summary_markdown(
    cross_ref: Dict[str, Dict[str, Any]],
    only_managed_by_aws: bool = False,
) -> str:
    """
    Generate markdown content for the summary documentation.

    Args:
        cross_ref: Cross-reference table from aws_policies_analyzer

    Returns:
        Markdown content as a string
    """
    content = "# AWS IAM Summary\n\n"
    content += "This document provides a summary of the AWS IAM roles, policies, actions, and services.\n\n"
    content += "## Summary Statistics\n\n"

    # Count resources
    roles_count = len(cross_ref["roles"])
    policies_count = len(cross_ref["policies"])
    actions_count = len(cross_ref["actions"])

    # Count unique services
    services = set()
    for action in cross_ref["actions"]:
        if ":" in action:
            service, _ = action.split(":", 1)
            services.add(service)
        else:
            services.add("all")
    services_count = len(services)

    # Create table with embedded links
    content += "| Resource Type | Count | Documentation |\n"
    content += "|--------------|-------|---------------|\n"

    if roles_count > 0:
        content += f"| Roles | {roles_count} | [View Details](./roles) |\n"

    if policies_count > 0:
        content += f"| Policies | {policies_count} | [View Details](./policies) |\n"

    if actions_count > 0:
        content += f"| Actions | {actions_count} | [View Details](./actions) |\n"

    if services_count > 0:
        content += f"| Services | {services_count} | [View Details](./services) |\n"

    return content


def main() -> None:
    """
    Main function to generate documentation.
    """
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Generate AWS IAM documentation")
    parser.add_argument(
        "--only-managed-by-aws",
        action="store_true",
        help="Only include roles and policies managed by AWS",
    )
    args = parser.parse_args()

    print("Generating AWS IAM documentation...")

    # Create docs directory if it doesn't exist
    docs_dir = "docs"
    roles_dir = os.path.join(docs_dir, "roles")
    policies_dir = os.path.join(docs_dir, "policies")
    services_dir = os.path.join(docs_dir, "services")
    actions_dir = os.path.join(docs_dir, "actions")

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # Get cross-reference data
    print("Building cross-reference table...")
    cross_ref = build_cross_reference_table(
        only_managed_by_aws=args.only_managed_by_aws
    )

    # Create dirs
    if not os.path.exists(actions_dir):
        os.makedirs(actions_dir)

    if not os.path.exists(services_dir):
        os.makedirs(services_dir)

    if not os.path.exists(policies_dir):
        os.makedirs(policies_dir)

    if not args.only_managed_by_aws:
        # Create roles directory
        if not os.path.exists(roles_dir):
            os.makedirs(roles_dir)

        # Generate roles index file
        print("Generating roles.md...")
        roles_md = generate_roles_markdown(cross_ref, args.only_managed_by_aws)
        with open(os.path.join(docs_dir, "roles/README.md"), "w") as f:
            f.write(roles_md)

        # Generate individual role files
        print("Generating individual role files...")
        for role_arn, role_data in sorted(cross_ref["roles"].items()):
            role_name = role_data["name"]
            role_filename = slugify(role_name.lower())
            role_md = generate_single_role_markdown(
                role_arn, role_data, cross_ref, args.only_managed_by_aws
            )
            if not role_md:
                continue

            with open(os.path.join(roles_dir, f"{role_filename}.md"), "w") as f:
                f.write(role_md)

    # Generate services index file
    print("Generating services.md...")
    services_md = generate_services_markdown(cross_ref, args.only_managed_by_aws)
    with open(os.path.join(docs_dir, "services/README.md"), "w") as f:
        f.write(services_md)

    # Generate individual service files
    print("Generating individual service files...")
    for service, service_data in sorted(cross_ref["services"].items()):
        service_filename = slugify(service.lower())
        service_md = generate_single_service_markdown(
            service, service_data, cross_ref, args.only_managed_by_aws
        )
        if not service_md:
            continue

        with open(os.path.join(services_dir, f"{service_filename}.md"), "w") as f:
            f.write(service_md)

    # Generate other markdown files (unchanged)
    print("Generating policies.md...")
    policies_md = generate_policies_markdown(cross_ref, args.only_managed_by_aws)
    with open(os.path.join(docs_dir, "policies/README.md"), "w") as f:
        f.write(policies_md)

    print("Generating individual policy files...")
    for policy_arn, policy_data in sorted(cross_ref["policies"].items()):
        policy_name = policy_data["name"]
        policy_filename = slugify(policy_name.lower())
        policy_md = generate_single_policy_markdown(
            policy_arn, policy_data, cross_ref, args.only_managed_by_aws
        )
        if not policy_md:
            continue

        with open(os.path.join(policies_dir, f"{policy_filename}.md"), "w") as f:
            f.write(policy_md)

    print("Generating actions.md...")
    actions_md = generate_actions_markdown(cross_ref, args.only_managed_by_aws)
    with open(os.path.join(docs_dir, "actions/README.md"), "w") as f:
        f.write(actions_md)

    # Generate individual action files
    print("Generating individual action files...")
    for action, action_data in sorted(cross_ref["actions"].items()):
        action_filename = slugify(action.lower())
        action_md = generate_single_action_markdown(
            action, action_data, cross_ref, args.only_managed_by_aws
        )
        if not action_md:
            continue

        with open(os.path.join(actions_dir, f"{action_filename}.md"), "w") as f:
            f.write(action_md)

    print("Generating summary.md...")
    summary_md = generate_summary_markdown(cross_ref, args.only_managed_by_aws)
    with open(os.path.join(docs_dir, "README.md"), "w") as f:
        f.write(summary_md)

    print(f"Documentation generated in the '{docs_dir}' directory.")
    print("Files created:")
    print(f"  - {os.path.join(docs_dir, 'roles/README.md')}")
    print(f"  - Multiple role files in {roles_dir}/")
    print(f"  - {os.path.join(docs_dir, 'policies/README.me')}")
    print(f"  - {os.path.join(docs_dir, 'actions/README.md')}")
    print(f"  - {os.path.join(docs_dir, 'services/README.md')}")
    print(f"  - Multiple service files in {services_dir}/")
    print(f"  - {os.path.join(docs_dir, 'README.md')}")


if __name__ == "__main__":
    main()
