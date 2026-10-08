#!/usr/bin/env python3
"""R4 documentation-model validation only. No device/network access or control.

Checks declared data, not whether a PCS really implements it. True approval and
verification flags in SYNTHETIC fixtures are test inputs, not real approvals.
"""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OWNERS = {"PCS_DIRECT": "PCS_GRID_DOMAIN", "GW_MANAGED": "GW_GRID_DOMAIN"}
ELIGIBLE = {"ECHONET_LITE_PCS": ["PCS_DIRECT"], "RS485_PCS": ["GW_MANAGED"]}
FETCHERS = {"PCS_DIRECT": "PCS_GRID_CLIENT", "GW_MANAGED": "GW_GRID_CLIENT"}

def binding_errors(binding: dict) -> list[str]:
    """Return errors in a declared synthetic activation candidate, not its truth."""
    errors: list[str] = []
    if not isinstance(binding, dict):
        return ["BINDING_MUST_BE_OBJECT"]
    mode = binding.get("mode")
    cls = binding.get("normal_connection_class")
    if mode not in OWNERS:
        errors.append("UNKNOWN_MODE")
    if binding.get("device_kind") != "PCS":
        errors.append("PCS_REQUIRED")
    if mode not in ELIGIBLE.get(cls, []):
        errors.append("CONNECTION_MODE_NOT_ELIGIBLE")
    supported = binding.get("supported_modes")
    if not isinstance(supported, list) or mode not in supported:
        errors.append("MODE_NOT_SUPPORTED")
    elif set(supported) - set(ELIGIBLE.get(cls, [])):
        errors.append("SUPPORTED_MODES_EXCEED_R4_POLICY")
    if not binding.get("scope_id") or not binding.get("physical_device_id"):
        errors.append("PHYSICAL_SCOPE_REQUIRED")
    if binding.get("is_gw_virtual_echonet_object") is not False:
        errors.append("PHYSICAL_PCS_NOT_VIRTUAL_PROXY_REQUIRED")
    if binding.get("owner_domain") != OWNERS.get(mode):
        errors.append("WRONG_OWNER_DOMAIN")
    if binding.get("active_owners") != 1:
        errors.append("EXACTLY_ONE_ACTIVE_OWNER_REQUIRED")
    if binding.get("automatic_mode_fallback") is not False:
        errors.append("AUTOMATIC_MODE_FALLBACK_NOT_SUPPORTED")
    for key, err in [("device_profile_id", "DEVICE_PROFILE_REQUIRED"),
                     ("certification_profile_id", "CERTIFICATION_PROFILE_REQUIRED"),
                     ("router_profile_id", "ROUTER_PROFILE_REQUIRED"),
                     ("server_protocol_profile_id", "SERVER_PROTOCOL_PROFILE_REQUIRED")]:
        if not binding.get(key):
            errors.append(err)
    for key, err in [("approval_record_present", "APPROVAL_RECORD_REQUIRED"),
                     ("physical_application_verified", "PHYSICAL_CONFIRMATION_REQUIRED"),
                     ("r4_eligibility_checked", "R4_REVALIDATION_REQUIRED")]:
        if binding.get(key) is not True:
            errors.append(err)
    req = binding.get("request_path")
    res = binding.get("response_path")
    if not isinstance(req, list) or not isinstance(res, list):
        errors.append("ROUTE_LIST_REQUIRED")
    else:
        if "HOME_ROUTER" not in req or "HOME_ROUTER" not in res:
            errors.append("HOME_ROUTER_REQUIRED_BOTH_DIRECTIONS")
        if not req or req[0] != FETCHERS.get(mode) or req[-1] != "GRID_SERVER":
            errors.append("WRONG_REQUEST_ENDPOINTS")
        if res != list(reversed(req)):
            errors.append("RESPONSE_PATH_MUST_REVERSE_DECLARED_REQUEST")
        if mode == "PCS_DIRECT" and any(str(n).startswith("GW_") for n in req + res):
            errors.append("GW_IN_PCS_FETCH_PATH_PROHIBITED")
        if "GW_HEMS_PROXY" in req + res:
            errors.append("HEMS_PROXY_PROHIBITED")
    if binding.get("depends_on_hems") is not False:
        errors.append("HEMS_DEPENDENCY_PROHIBITED")
    if mode == "PCS_DIRECT":
        if binding.get("pcs_self_fetch_capability_confirmed") is not True:
            errors.append("PCS_FETCH_CAPABILITY_CONFIRMATION_REQUIRED")
        if binding.get("pcs_link_transport") != "ECHONET_LITE":
            errors.append("EL_NORMAL_LINK_REQUIRED")
    elif mode == "GW_MANAGED":
        if binding.get("pcs_link_transport") != "RS485":
            errors.append("RS485_REQUIRED")
        if not binding.get("pcs_link_fault_profile_id"):
            errors.append("REQUIRED_LINK_FAULT_PROFILE_REQUIRED")
    return errors

def main() -> int:
    registry = json.loads((ROOT / "data/grid_connection_profiles.json").read_text(encoding="utf-8"))
    routes = json.loads((ROOT / "data/grid_network_routes.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    if registry.get("schema") != "spkgw.grid-connection-profiles/v2":
        errors.append("SCHEMA_NOT_V2")
    if registry.get("default_mode") is not None or registry.get("router_required") is not True:
        errors.append("DEFAULT_OR_ROUTER_POLICY")
    declared = {x["normal_connection_class"]: x["allowed_modes"] for x in registry.get("eligibility_rules", [])}
    if declared != ELIGIBLE:
        errors.append("ELIGIBILITY_POLICY_MISMATCH")
    for profile in registry["profiles"]:
        mode = profile["mode"]
        if mode not in ELIGIBLE.get(profile.get("normal_connection_class"), []):
            errors.append("TEMPLATE_MODE_INELIGIBLE")
        if profile["schedule_owner_domain"] != OWNERS.get(mode):
            errors.append("TEMPLATE_OWNER")
        if profile["status"] != "TEMPLATE_NOT_DEPLOYABLE" or profile["validated_for_activation"] or profile["authority"]["active_mode"] is not None:
            errors.append("TEMPLATE_NOT_INACTIVE")
        network = profile["network"]
        if "HOME_ROUTER" not in network["request_path"] or network["response_path"] != list(reversed(network["request_path"])):
            errors.append("TEMPLATE_ROUTER_PATH")
        if mode == "PCS_DIRECT" and any(x.startswith("GW_") for x in network["request_path"]):
            errors.append("TEMPLATE_GW_BYPASS")
    for route in routes["routes"]:
        expected = [FETCHERS.get(route["mode"]), "HOME_ROUTER", "INTERNET", "GRID_SERVER"]
        if route["request_path"] != expected or route["response_path"] != list(reversed(expected)):
            errors.append("DESIGN_ROUTE_MISMATCH")
        if route["mode"] not in ELIGIBLE.get(route["normal_connection_class"], []):
            errors.append("DESIGN_ROUTE_CLASS")
    base = {
        "mode": "PCS_DIRECT", "normal_connection_class": "ECHONET_LITE_PCS", "device_kind": "PCS",
        "scope_id": "SYNTHETIC_SCOPE", "physical_device_id": "SYNTHETIC_PHYSICAL_PCS",
        "is_gw_virtual_echonet_object": False, "supported_modes": ["PCS_DIRECT"],
        "owner_domain": "PCS_GRID_DOMAIN", "active_owners": 1, "automatic_mode_fallback": False,
        "device_profile_id": "SYNTHETIC_DEVICE", "certification_profile_id": "SYNTHETIC_NOT_A_CERTIFICATE",
        "router_profile_id": "SYNTHETIC_ROUTER", "server_protocol_profile_id": "SYNTHETIC_UNSPECIFIED_PROTOCOL",
        "approval_record_present": True, "physical_application_verified": True, "r4_eligibility_checked": True,
        "depends_on_hems": False, "pcs_self_fetch_capability_confirmed": True,
        "pcs_link_fault_profile_id": "SYNTHETIC_FAULT", "pcs_link_transport": "ECHONET_LITE",
        "request_path": ["PCS_GRID_CLIENT", "HOME_ROUTER", "INTERNET", "GRID_SERVER"],
        "response_path": ["GRID_SERVER", "INTERNET", "HOME_ROUTER", "PCS_GRID_CLIENT"],
    }
    gw = deepcopy(base)
    gw.update(mode="GW_MANAGED", normal_connection_class="RS485_PCS", supported_modes=["GW_MANAGED"],
              owner_domain="GW_GRID_DOMAIN", pcs_self_fetch_capability_confirmed=False, pcs_link_transport="RS485",
              request_path=["GW_GRID_CLIENT", "HOME_ROUTER", "INTERNET", "GRID_SERVER"],
              response_path=["GRID_SERVER", "INTERNET", "HOME_ROUTER", "GW_GRID_CLIENT"])
    cases = [("valid_synthetic_el_shape", base, set()), ("valid_synthetic_rs_shape", gw, set())]
    negatives = [
        ("unknown_mode", base, {"mode": None}, "UNKNOWN_MODE"),
        ("rs_pcs_self_fetch", base, {"normal_connection_class": "RS485_PCS"}, "CONNECTION_MODE_NOT_ELIGIBLE"),
        ("el_pcs_gw_managed", gw, {"normal_connection_class": "ECHONET_LITE_PCS"}, "CONNECTION_MODE_NOT_ELIGIBLE"),
        ("non_pcs", base, {"device_kind": "AIR_CONDITIONER"}, "PCS_REQUIRED"),
        ("virtual_echonet_proxy", base, {"is_gw_virtual_echonet_object": True}, "PHYSICAL_PCS_NOT_VIRTUAL_PROXY_REQUIRED"),
        ("dual_modes_without_binding", base, {"supported_modes": ["PCS_DIRECT", "GW_MANAGED"]}, "SUPPORTED_MODES_EXCEED_R4_POLICY"),
        ("router_omitted", base, {"request_path": ["PCS_GRID_CLIENT", "GRID_SERVER"], "response_path": ["GRID_SERVER", "PCS_GRID_CLIENT"]}, "HOME_ROUTER_REQUIRED_BOTH_DIRECTIONS"),
        ("response_omits_router", base, {"response_path": ["GRID_SERVER", "PCS_GRID_CLIENT"]}, "HOME_ROUTER_REQUIRED_BOTH_DIRECTIONS"),
        ("gw_ip_forwarding", base, {"request_path": ["PCS_GRID_CLIENT", "GW_NAT", "HOME_ROUTER", "GRID_SERVER"], "response_path": ["GRID_SERVER", "HOME_ROUTER", "GW_NAT", "PCS_GRID_CLIENT"]}, "GW_IN_PCS_FETCH_PATH_PROHIBITED"),
        ("hems_proxy", gw, {"request_path": ["GW_GRID_CLIENT", "GW_HEMS_PROXY", "HOME_ROUTER", "GRID_SERVER"]}, "HEMS_PROXY_PROHIBITED"),
        ("no_independent_fetch_evidence", base, {"pcs_self_fetch_capability_confirmed": False}, "PCS_FETCH_CAPABILITY_CONFIRMATION_REQUIRED"),
        ("wrong_wire", gw, {"pcs_link_transport": "ECHONET_LITE"}, "RS485_REQUIRED"),
        ("unknown_scope", base, {"scope_id": None}, "PHYSICAL_SCOPE_REQUIRED"),
        ("two_owners", gw, {"active_owners": 2}, "EXACTLY_ONE_ACTIVE_OWNER_REQUIRED"),
        ("wrong_owner", gw, {"owner_domain": "HEMS"}, "WRONG_OWNER_DOMAIN"),
        ("auto_fallback", base, {"automatic_mode_fallback": True}, "AUTOMATIC_MODE_FALLBACK_NOT_SUPPORTED"),
        ("no_approval", base, {"approval_record_present": False}, "APPROVAL_RECORD_REQUIRED"),
        ("accepted_not_verified", gw, {"physical_application_verified": False}, "PHYSICAL_CONFIRMATION_REQUIRED"),
        ("hems_dependency", gw, {"depends_on_hems": True}, "HEMS_DEPENDENCY_PROHIBITED"),
        ("no_link_fault_contract", gw, {"pcs_link_fault_profile_id": None}, "REQUIRED_LINK_FAULT_PROFILE_REQUIRED"),
        ("legacy_without_revalidation", base, {"r4_eligibility_checked": False}, "R4_REVALIDATION_REQUIRED"),
        ("router_profile_missing", base, {"router_profile_id": None}, "ROUTER_PROFILE_REQUIRED"),
        ("server_contract_missing", base, {"server_protocol_profile_id": None}, "SERVER_PROTOCOL_PROFILE_REQUIRED"),
    ]
    for name, origin, patch, expected in negatives:
        fixture = deepcopy(origin); fixture.update(patch); cases.append((name, fixture, {expected}))
    results = []
    for name, fixture, expected in cases:
        actual = set(binding_errors(fixture))
        ok = not actual if not expected else expected.issubset(actual)
        results.append({"case": name, "passed": ok, "expected_error_codes": sorted(expected), "observed_errors": sorted(actual)})
        if not ok: errors.append("SELFTEST:" + name)
    report = {"status": "PASS" if not errors else "FAIL", "revision": "R4",
              "scope": "DOCUMENT_TEMPLATE_AND_SYNTHETIC_DATA_RULES_ONLY",
              "templates_checked": len(registry["profiles"]), "design_routes_checked": len(routes["routes"]),
              "synthetic_cases": len(cases), "results": results, "errors": errors,
              "no_device_operations": True, "network_access": False,
              "not_a_switch_or_certification_test": True, "does_not_verify_real_approval_or_capability": True}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
