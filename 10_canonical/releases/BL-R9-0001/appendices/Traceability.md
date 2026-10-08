# 要求・機能・試験の双方向対応

生成正本：requirements.json、function_catalog.json、test_catalog.json。版固定の原典表は30_referencesのR8原本に保持。

| SYS要求 | 原典ARCH | 全体機能 | GW機能 | 検証 |
|---|---|---|---|---|
| [SYS-RESP-001](Requirements_Catalog.md#sys-resp-001) | ARCH-001 | S-FN-004, S-FN-006, S-FN-007, S-FN-015 | GW-FN-004 | 責務・依存図レビュー |
| [SYS-GRID-001](Requirements_Catalog.md#sys-grid-001) | ARCH-002 | S-FN-012, S-FN-013 | GW-FN-014 | T01, T02 |
| [SYS-GRID-002](Requirements_Catalog.md#sys-grid-002) | ARCH-003 | S-FN-014 |  | T03 |
| [SYS-BOUND-001](Requirements_Catalog.md#sys-bound-001) | ARCH-004 | S-FN-012, S-FN-013, S-FN-014, S-FN-019 | GW-FN-028 | T04, T05 |
| [SYS-GRID-003](Requirements_Catalog.md#sys-grid-003) | ARCH-005 | S-FN-012 | GW-FN-014 | T01, T06 |
| [SYS-AUTH-001](Requirements_Catalog.md#sys-auth-001) | ARCH-006 | S-FN-004, S-FN-005, S-FN-006, S-FN-015 | GW-FN-002 | T07, T08 |
| [SYS-AUTH-002](Requirements_Catalog.md#sys-auth-002) | ARCH-007 | S-FN-004, S-FN-005, S-FN-006, S-FN-015 | GW-FN-002 | T07 |
| [SYS-ORCH-001](Requirements_Catalog.md#sys-orch-001) | ARCH-008 | S-FN-004, S-FN-005, S-FN-006, S-FN-007, S-FN-015 | GW-FN-003 | T09 |
| [SYS-ADAPT-001](Requirements_Catalog.md#sys-adapt-001) | ARCH-009 |  |  | T07 |
| [SYS-CAP-001](Requirements_Catalog.md#sys-cap-001) | ARCH-010 | S-FN-001, S-FN-004, S-FN-005, S-FN-008, S-FN-020, S-FN-021 | GW-FN-010, GW-FN-012, GW-FN-031 | T10, T11 |
| [SYS-RESULT-001](Requirements_Catalog.md#sys-result-001) | ARCH-011 | S-FN-004, S-FN-006, S-FN-007, S-FN-015 | GW-FN-004 | T12 |
| [SYS-TOPO-001](Requirements_Catalog.md#sys-topo-001) | ARCH-012 |  |  | T08, T13 |
| [SYS-CONST-001](Requirements_Catalog.md#sys-const-001) | ARCH-013 | S-FN-006, S-FN-007, S-FN-015 | GW-FN-006, GW-FN-007 | T06, T14 |
| [SYS-CONST-002](Requirements_Catalog.md#sys-const-002) | ARCH-014 |  |  | T13 |
| [SYS-ISO-001](Requirements_Catalog.md#sys-iso-001) | ARCH-015 |  |  | T15 |
| [SYS-OTA-001](Requirements_Catalog.md#sys-ota-001) | ARCH-016 | S-FN-011, S-FN-012, S-FN-013, S-FN-014, S-FN-015, S-FN-019 | GW-FN-024, GW-FN-028 | T04, T16 |
| [SYS-OTA-002](Requirements_Catalog.md#sys-ota-002) | ARCH-017 | S-FN-011, S-FN-015, S-FN-020 | GW-FN-024, GW-FN-032 | T16, T17 |
| [SYS-EXPIRY-001](Requirements_Catalog.md#sys-expiry-001) | ARCH-018 | S-FN-007, S-FN-015, S-FN-021 | GW-FN-026 | T17 |
| [SYS-COEX-001](Requirements_Catalog.md#sys-coex-001) | ARCH-019 | S-FN-004, S-FN-005, S-FN-006, S-FN-015 | GW-FN-002 | T18 |
| [SYS-CERT-001](Requirements_Catalog.md#sys-cert-001) | ARCH-020 |  |  | T19 |
| [SYS-ISO-002](Requirements_Catalog.md#sys-iso-002) | ARCH-021 |  |  | T15, T16 |
| [SYS-CHG-001](Requirements_Catalog.md#sys-chg-001) | ARCH-022 |  |  | T19 |
| [SYS-TIME-001](Requirements_Catalog.md#sys-time-001) | ARCH-023 |  |  | T02, T03, T13 |
| [SYS-LOG-001](Requirements_Catalog.md#sys-log-001) | ARCH-024 | S-FN-016, S-FN-019, S-FN-020 | GW-FN-025 | T12, T19 |
| [SYS-SCOPE-001](Requirements_Catalog.md#sys-scope-001) |  |  |  | 仕様・契約レビュー |
| [SYS-DEPLOY-001](Requirements_Catalog.md#sys-deploy-001) |  |  |  | T01, SYS-T05 |
| [SYS-REQ-001](Requirements_Catalog.md#sys-req-001) |  | S-FN-002, S-FN-003, S-FN-004, S-FN-005, S-FN-009, S-FN-010, S-FN-019 | GW-FN-001 | SYS-T10 |
| [SYS-RS-001](Requirements_Catalog.md#sys-rs-001) |  | S-FN-004, S-FN-008, S-FN-012 | GW-FN-011 | SYS-T01 |
| [SYS-RS-002](Requirements_Catalog.md#sys-rs-002) |  | S-FN-004, S-FN-008, S-FN-012 | GW-FN-011 | SYS-T01, SYS-T02 |
| [SYS-RS-003](Requirements_Catalog.md#sys-rs-003) |  | S-FN-004, S-FN-008, S-FN-012 | GW-FN-011 | SYS-T05 |
| [SYS-RS-004](Requirements_Catalog.md#sys-rs-004) |  |  |  | T01, SYS-T05 |
| [SYS-RS-005](Requirements_Catalog.md#sys-rs-005) |  | S-FN-004, S-FN-008, S-FN-012 | GW-FN-011 | SYS-T01, T04, T07 |
| [SYS-RS-006](Requirements_Catalog.md#sys-rs-006) |  | S-FN-004, S-FN-008, S-FN-012 | GW-FN-011 | SYS-T04, SYS-T05, T15 |
| [SYS-SEM-001](Requirements_Catalog.md#sys-sem-001) |  | S-FN-004, S-FN-006, S-FN-007, S-FN-015 | GW-FN-004 | SYS-T02 |
| [SYS-EL-001](Requirements_Catalog.md#sys-el-001) |  | S-FN-001, S-FN-004, S-FN-005, S-FN-008, S-FN-018 | GW-FN-012, GW-FN-013 | SYS-T03 |
| [SYS-EL-002](Requirements_Catalog.md#sys-el-002) |  | S-FN-018 | GW-FN-013 | SYS-T03, T12 |
| [SYS-ROUTE-001](Requirements_Catalog.md#sys-route-001) |  | S-FN-004, S-FN-005, S-FN-008, S-FN-020 | GW-FN-010 | SYS-T07, T17 |
| [SYS-CAP-002](Requirements_Catalog.md#sys-cap-002) |  | S-FN-004, S-FN-005, S-FN-008, S-FN-015, S-FN-020 | GW-FN-010, GW-FN-032 | T10, T14 |
| [SYS-RESULT-002](Requirements_Catalog.md#sys-result-002) |  | S-FN-004, S-FN-006, S-FN-007, S-FN-015 | GW-FN-004, GW-FN-007 | T12, T18 |
| [SYS-RESULT-003](Requirements_Catalog.md#sys-result-003) |  | S-FN-004, S-FN-006, S-FN-007, S-FN-015 | GW-FN-004 | SYS-T02, T12 |
| [SYS-RETRY-001](Requirements_Catalog.md#sys-retry-001) |  | S-FN-004, S-FN-005, S-FN-006, S-FN-007, S-FN-015, S-FN-021 | GW-FN-003, GW-FN-026 | T09, T12 |
| [SYS-LOAD-001](Requirements_Catalog.md#sys-load-001) |  | S-FN-005, S-FN-006, S-FN-007 | GW-FN-005 | SYS-T10, T13 |
| [SYS-EMS-001](Requirements_Catalog.md#sys-ems-001) |  | S-FN-006, S-FN-007, S-FN-015 | GW-FN-006, GW-FN-007 | SYS-T10, T10, T14 |
| [SYS-MEAS-001](Requirements_Catalog.md#sys-meas-001) |  | S-FN-001, S-FN-007, S-FN-016, S-FN-017 | GW-FN-008 | T06, T12, SYS-T08 |
| [SYS-MEAS-002](Requirements_Catalog.md#sys-meas-002) |  | S-FN-001, S-FN-007, S-FN-016, S-FN-017 | GW-FN-008 | T08, SYS-T04, SYS-T08 |
| [SYS-DATA-001](Requirements_Catalog.md#sys-data-001) |  | S-FN-001, S-FN-003, S-FN-016, S-FN-017 | GW-FN-009 | SYS-T08 |
| [SYS-DATA-002](Requirements_Catalog.md#sys-data-002) |  | S-FN-001, S-FN-003, S-FN-016, S-FN-017 | GW-FN-009 | SYS-T08 |
| [SYS-CFG-001](Requirements_Catalog.md#sys-cfg-001) |  | S-FN-009, S-FN-015, S-FN-020 | GW-FN-020 | SYS-T06 |
| [SYS-CFG-002](Requirements_Catalog.md#sys-cfg-002) |  | S-FN-009, S-FN-015, S-FN-020 | GW-FN-020 | SYS-T06, T04 |
| [SYS-CFG-003](Requirements_Catalog.md#sys-cfg-003) |  | S-FN-009, S-FN-019, S-FN-020 | GW-FN-030 | SYS-T06, T16 |
| [SYS-PERF-001](Requirements_Catalog.md#sys-perf-001) |  |  |  | T11, SYS-T04 |
| [SYS-PERF-002](Requirements_Catalog.md#sys-perf-002) |  |  |  | T05, T11, T15 |
| [SYS-SEC-001](Requirements_Catalog.md#sys-sec-001) |  | S-FN-008, S-FN-019, S-FN-020, S-FN-021 | GW-FN-027, GW-FN-031 | SYS-T09, T04 |
| [SYS-SEC-002](Requirements_Catalog.md#sys-sec-002) |  |  |  | 仕様・契約レビュー |
| [SYS-FAULT-001](Requirements_Catalog.md#sys-fault-001) |  | S-FN-007, S-FN-015, S-FN-021 | GW-FN-026 | SYS-T05, T02, T06 |
| [SYS-CERT-002](Requirements_Catalog.md#sys-cert-002) |  |  |  | 仕様・契約レビュー |
| [SYS-MIG-001](Requirements_Catalog.md#sys-mig-001) |  |  |  | SYS-T01, T07 |
| [SYS-MIG-002](Requirements_Catalog.md#sys-mig-002) |  | S-FN-008, S-FN-021 | GW-FN-031 | 仕様・契約レビュー |
| [SYS-BASE-001](Requirements_Catalog.md#sys-base-001) |  |  |  | 仕様・契約レビュー |
| [SYS-VERIFY-001](Requirements_Catalog.md#sys-verify-001) |  |  |  | T19 |
| [SYS-CTX-001](Requirements_Catalog.md#sys-ctx-001) |  |  |  | SYS-T11 |
| [SYS-CTX-002](Requirements_Catalog.md#sys-ctx-002) |  |  |  | SYS-T11, SYS-T13 |
| [SYS-NORTH-001](Requirements_Catalog.md#sys-north-001) |  | S-FN-002, S-FN-003, S-FN-004, S-FN-005, S-FN-009, S-FN-010, S-FN-016, S-FN-019 | GW-FN-001, GW-FN-017 | SYS-T11, SYS-T17 |
| [SYS-NORTH-002](Requirements_Catalog.md#sys-north-002) |  | S-FN-002, S-FN-003, S-FN-004, S-FN-005, S-FN-009, S-FN-010, S-FN-016, S-FN-019, S-FN-020 | GW-FN-001, GW-FN-017, GW-FN-027 | SYS-T14, SYS-T16 |
| [SYS-NORTH-003](Requirements_Catalog.md#sys-north-003) |  | S-FN-003, S-FN-009, S-FN-010, S-FN-016, S-FN-019 | GW-FN-017 | SYS-T16, SYS-T24 |
| [SYS-NORTH-004](Requirements_Catalog.md#sys-north-004) |  | S-FN-003, S-FN-009, S-FN-010, S-FN-016, S-FN-019 | GW-FN-017 | SYS-T16, SYS-T21 |
| [SYS-NORTH-005](Requirements_Catalog.md#sys-north-005) |  | S-FN-003, S-FN-009, S-FN-010, S-FN-016, S-FN-019, S-FN-020 | GW-FN-017, GW-FN-025 | SYS-T18, SYS-T25 |
| [SYS-NORTH-006](Requirements_Catalog.md#sys-north-006) |  | S-FN-001, S-FN-003, S-FN-016, S-FN-017 | GW-FN-009, GW-FN-019 | SYS-T21, SYS-T28 |
| [SYS-NORTH-007](Requirements_Catalog.md#sys-north-007) |  | S-FN-002, S-FN-003, S-FN-004, S-FN-005, S-FN-009, S-FN-010, S-FN-019, S-FN-020 | GW-FN-001, GW-FN-027 | SYS-T14, SYS-T15, SYS-T21 |
| [SYS-CFG-004](Requirements_Catalog.md#sys-cfg-004) |  | S-FN-009, S-FN-015, S-FN-020 | GW-FN-020 | SYS-T15 |
| [SYS-CFG-005](Requirements_Catalog.md#sys-cfg-005) |  | S-FN-009, S-FN-015, S-FN-020 | GW-FN-020 | SYS-T15, SYS-T28 |
| [SYS-CFG-006](Requirements_Catalog.md#sys-cfg-006) |  | S-FN-009, S-FN-021 | GW-FN-021 | SYS-T13, SYS-T22 |
| [SYS-GWOP-001](Requirements_Catalog.md#sys-gwop-001) |  | S-FN-003, S-FN-009, S-FN-010, S-FN-015, S-FN-016, S-FN-019, S-FN-020 | GW-FN-017, GW-FN-022 | SYS-T17, SYS-T23 |
| [SYS-GWOP-002](Requirements_Catalog.md#sys-gwop-002) |  | S-FN-010, S-FN-015, S-FN-016, S-FN-020 | GW-FN-022 | SYS-T17, SYS-T20, SYS-T22 |
| [SYS-UI-001](Requirements_Catalog.md#sys-ui-001) |  | S-FN-002 | GW-FN-018 | SYS-T12 |
| [SYS-UI-002](Requirements_Catalog.md#sys-ui-002) |  | S-FN-002 | GW-FN-018 | SYS-T13 |
| [SYS-UI-003](Requirements_Catalog.md#sys-ui-003) |  | S-FN-002 | GW-FN-018 | SYS-T12, SYS-T13, SYS-T22 |
| [SYS-UI-004](Requirements_Catalog.md#sys-ui-004) |  | S-FN-002 | GW-FN-018 | SYS-T12, SYS-T23, SYS-T24 |
| [SYS-UI-005](Requirements_Catalog.md#sys-ui-005) |  | S-FN-002 | GW-FN-018 | SYS-T23, SYS-T27 |
| [SYS-APP-001](Requirements_Catalog.md#sys-app-001) |  | S-FN-003, S-FN-016 | GW-FN-019 | SYS-T14, SYS-T24 |
| [SYS-APP-002](Requirements_Catalog.md#sys-app-002) |  | S-FN-003, S-FN-016 | GW-FN-019 | SYS-T21, SYS-T24 |
| [SYS-APP-003](Requirements_Catalog.md#sys-app-003) |  | S-FN-009, S-FN-019, S-FN-020 | GW-FN-027, GW-FN-030 | SYS-T14, SYS-T26 |
| [SYS-FW-001](Requirements_Catalog.md#sys-fw-001) |  | S-FN-011 | GW-FN-023 | SYS-T11, SYS-T19, SYS-T20 |
| [SYS-FW-002](Requirements_Catalog.md#sys-fw-002) |  | S-FN-011 | GW-FN-023 | SYS-T19 |
| [SYS-FW-003](Requirements_Catalog.md#sys-fw-003) |  | S-FN-011, S-FN-015 | GW-FN-024 | SYS-T19, SYS-T20 |
| [SYS-FW-004](Requirements_Catalog.md#sys-fw-004) |  | S-FN-011, S-FN-015 | GW-FN-024 | SYS-T20, SYS-T21 |
| [SYS-FW-005](Requirements_Catalog.md#sys-fw-005) |  | S-FN-011 | GW-FN-023 | SYS-T18, SYS-T25 |
| [SYS-STATE-001](Requirements_Catalog.md#sys-state-001) |  | S-FN-001, S-FN-003, S-FN-007, S-FN-009, S-FN-010, S-FN-016, S-FN-017, S-FN-019, S-FN-020 | GW-FN-008, GW-FN-017, GW-FN-025 | SYS-T18, SYS-T23 |
| [SYS-STATE-002](Requirements_Catalog.md#sys-state-002) |  | S-FN-001, S-FN-003, S-FN-007, S-FN-016, S-FN-017 | GW-FN-008, GW-FN-019 | SYS-T21, SYS-T28 |
| [SYS-SVC-001](Requirements_Catalog.md#sys-svc-001) |  | S-FN-008, S-FN-020 | GW-FN-029 | SYS-T27 |
| [SYS-ISO-003](Requirements_Catalog.md#sys-iso-003) |  |  |  | SYS-T18, SYS-T22, SYS-T25 |
| [SYS-CHG-002](Requirements_Catalog.md#sys-chg-002) |  |  |  | SYS-T27 |
| [SYS-GSEL-001](Requirements_Catalog.md#sys-gsel-001) |  | S-FN-012 | GW-FN-014 | SYS-T29, SYS-T30 |
| [SYS-GSEL-002](Requirements_Catalog.md#sys-gsel-002) |  |  |  | SYS-T31 |
| [SYS-GSEL-003](Requirements_Catalog.md#sys-gsel-003) |  |  |  | SYS-T32, SYS-T41 |
| [SYS-GSEL-004](Requirements_Catalog.md#sys-gsel-004) |  | S-FN-012, S-FN-013, S-FN-014, S-FN-015, S-FN-019 | GW-FN-015, GW-FN-028 | SYS-T29, SYS-T30, SYS-T39 |
| [SYS-GSEL-005](Requirements_Catalog.md#sys-gsel-005) |  | S-FN-012, S-FN-015 | GW-FN-014, GW-FN-015 | SYS-T30, SYS-T35, SYS-T39 |
| [SYS-GSEL-006](Requirements_Catalog.md#sys-gsel-006) |  | S-FN-012, S-FN-013, S-FN-014, S-FN-019 | GW-FN-014, GW-FN-028 | SYS-T29, SYS-T30, SYS-T37, SYS-T38 |
| [SYS-GSEL-007](Requirements_Catalog.md#sys-gsel-007) |  |  |  | SYS-T31, SYS-T33, SYS-T40 |
| [SYS-GSEL-008](Requirements_Catalog.md#sys-gsel-008) |  |  |  | SYS-T33, SYS-T34 |
| [SYS-GSEL-009](Requirements_Catalog.md#sys-gsel-009) |  |  |  | SYS-T32, SYS-T34, SYS-T42 |
| [SYS-GSEL-010](Requirements_Catalog.md#sys-gsel-010) |  |  |  | SYS-T36 |
| [SYS-GSEL-011](Requirements_Catalog.md#sys-gsel-011) |  | S-FN-012, S-FN-015, S-FN-020 | GW-FN-015, GW-FN-032 | SYS-T35, SYS-T36 |
| [SYS-GSEL-012](Requirements_Catalog.md#sys-gsel-012) |  | S-FN-012, S-FN-015 | GW-FN-015 | SYS-T39 |
| [SYS-GSEL-013](Requirements_Catalog.md#sys-gsel-013) |  | S-FN-001, S-FN-013, S-FN-014, S-FN-016 | GW-FN-016 | SYS-T38 |
| [SYS-GSEL-014](Requirements_Catalog.md#sys-gsel-014) |  | S-FN-001, S-FN-013, S-FN-014, S-FN-016 | GW-FN-016 | SYS-T38 |
| [SYS-GSEL-015](Requirements_Catalog.md#sys-gsel-015) |  |  |  | SYS-T37, SYS-T40 |
| [SYS-GSEL-016](Requirements_Catalog.md#sys-gsel-016) |  |  |  | SYS-T40 |
| [SYS-GSEL-017](Requirements_Catalog.md#sys-gsel-017) |  |  |  | SYS-T41 |
| [SYS-GSEL-018](Requirements_Catalog.md#sys-gsel-018) |  |  |  | SYS-T34, SYS-T42 |
| [SYS-GSEL-019](Requirements_Catalog.md#sys-gsel-019) |  | S-FN-008, S-FN-009, S-FN-019, S-FN-020 | GW-FN-029, GW-FN-030 | SYS-T31, SYS-T42 |
| [SYS-GSEL-020](Requirements_Catalog.md#sys-gsel-020) |  |  |  | SYS-T33, SYS-T38, SYS-T40, SYS-T42 |
| [SYS-GNET-001](Requirements_Catalog.md#sys-gnet-001) |  | S-FN-012 | GW-FN-014 | SYS-T43, SYS-T44 |
| [SYS-GNET-002](Requirements_Catalog.md#sys-gnet-002) |  | S-FN-013 |  | SYS-T43, SYS-T45, SYS-T50 |
| [SYS-GNET-003](Requirements_Catalog.md#sys-gnet-003) |  | S-FN-012, S-FN-015 | GW-FN-014, GW-FN-015 | SYS-T44, SYS-T48 |
| [SYS-GNET-004](Requirements_Catalog.md#sys-gnet-004) |  | S-FN-001, S-FN-004, S-FN-005, S-FN-008, S-FN-013, S-FN-014, S-FN-016 | GW-FN-012, GW-FN-016 | SYS-T43, SYS-T45, SYS-T49 |
| [SYS-GNET-005](Requirements_Catalog.md#sys-gnet-005) |  | S-FN-007, S-FN-015, S-FN-021 | GW-FN-026 | SYS-T46, SYS-T48 |
| [SYS-GNET-006](Requirements_Catalog.md#sys-gnet-006) |  | S-FN-009, S-FN-021 | GW-FN-021 | SYS-T47, SYS-T48 |
| [SYS-GNET-007](Requirements_Catalog.md#sys-gnet-007) |  | S-FN-001, S-FN-013, S-FN-014, S-FN-016 | GW-FN-016 | SYS-T49 |
| [SYS-GNET-008](Requirements_Catalog.md#sys-gnet-008) |  |  |  | SYS-T45, SYS-T50 |
| [SYS-GNET-009](Requirements_Catalog.md#sys-gnet-009) |  |  |  | SYS-T43, SYS-T44, SYS-T46 |
| [SYS-GNET-010](Requirements_Catalog.md#sys-gnet-010) |  | S-FN-002 | GW-FN-018 | SYS-T47 |
| [SYS-GNET-011](Requirements_Catalog.md#sys-gnet-011) |  |  |  | SYS-T47, SYS-T48 |
| [SYS-GNET-012](Requirements_Catalog.md#sys-gnet-012) |  | S-FN-004, S-FN-005, S-FN-008, S-FN-018, S-FN-020 | GW-FN-010, GW-FN-013 | SYS-T45, SYS-T50 |

## 試験から要求への逆引き

| 試験 | 対応SYS | 状態 |
|---|---|---|
| T01 | SYS-GRID-001, SYS-GRID-003, SYS-DEPLOY-001, SYS-RS-004 | NOT_RUN |
| T02 | SYS-GRID-001, SYS-TIME-001, SYS-FAULT-001 | NOT_RUN |
| T03 | SYS-GRID-002, SYS-TIME-001 | NOT_RUN |
| T04 | SYS-BOUND-001, SYS-OTA-001, SYS-RS-005, SYS-CFG-002, SYS-SEC-001 | NOT_RUN |
| T05 | SYS-BOUND-001, SYS-PERF-002 | NOT_RUN |
| T06 | SYS-GRID-003, SYS-CONST-001, SYS-MEAS-001, SYS-FAULT-001 | NOT_RUN |
| T07 | SYS-AUTH-001, SYS-AUTH-002, SYS-ADAPT-001, SYS-RS-005, SYS-MIG-001 | NOT_RUN |
| T08 | SYS-AUTH-001, SYS-TOPO-001, SYS-MEAS-002 | NOT_RUN |
| T09 | SYS-ORCH-001, SYS-RETRY-001 | NOT_RUN |
| T10 | SYS-CAP-001, SYS-CAP-002, SYS-EMS-001 | NOT_RUN |
| T11 | SYS-CAP-001, SYS-PERF-001, SYS-PERF-002 | NOT_RUN |
| T12 | SYS-RESULT-001, SYS-LOG-001, SYS-EL-002, SYS-RESULT-002, SYS-RESULT-003, SYS-RETRY-001, SYS-MEAS-001 | NOT_RUN |
| T13 | SYS-TOPO-001, SYS-CONST-002, SYS-TIME-001, SYS-LOAD-001 | NOT_RUN |
| T14 | SYS-CONST-001, SYS-CAP-002, SYS-EMS-001 | NOT_RUN |
| T15 | SYS-ISO-001, SYS-ISO-002, SYS-RS-006, SYS-PERF-002 | NOT_RUN |
| T16 | SYS-OTA-001, SYS-OTA-002, SYS-ISO-002, SYS-CFG-003 | NOT_RUN |
| T17 | SYS-OTA-002, SYS-EXPIRY-001, SYS-ROUTE-001 | NOT_RUN |
| T18 | SYS-COEX-001, SYS-RESULT-002 | NOT_RUN |
| T19 | SYS-CERT-001, SYS-CHG-001, SYS-LOG-001, SYS-VERIFY-001 | NOT_RUN |
| SYS-T01 | SYS-RS-001, SYS-RS-002, SYS-RS-005, SYS-MIG-001 | NOT_RUN |
| SYS-T02 | SYS-RS-002, SYS-SEM-001, SYS-RESULT-003 | NOT_RUN |
| SYS-T03 | SYS-EL-001, SYS-EL-002 | NOT_RUN |
| SYS-T04 | SYS-RS-006, SYS-MEAS-002, SYS-PERF-001 | NOT_RUN |
| SYS-T05 | SYS-DEPLOY-001, SYS-RS-003, SYS-RS-004, SYS-RS-006, SYS-FAULT-001 | NOT_RUN |
| SYS-T06 | SYS-CFG-001, SYS-CFG-002, SYS-CFG-003 | NOT_RUN |
| SYS-T07 | SYS-ROUTE-001 | NOT_RUN |
| SYS-T08 | SYS-MEAS-001, SYS-MEAS-002, SYS-DATA-001, SYS-DATA-002 | NOT_RUN |
| SYS-T09 | SYS-SEC-001 | NOT_RUN |
| SYS-T10 | SYS-REQ-001, SYS-LOAD-001, SYS-EMS-001 | NOT_RUN |
| SYS-T11 | SYS-CTX-001, SYS-CTX-002, SYS-NORTH-001, SYS-FW-001 | NOT_RUN |
| SYS-T12 | SYS-UI-001, SYS-UI-003, SYS-UI-004 | NOT_RUN |
| SYS-T13 | SYS-CTX-002, SYS-CFG-006, SYS-UI-002, SYS-UI-003 | NOT_RUN |
| SYS-T14 | SYS-NORTH-002, SYS-NORTH-007, SYS-APP-001, SYS-APP-003 | NOT_RUN |
| SYS-T15 | SYS-NORTH-007, SYS-CFG-004, SYS-CFG-005 | NOT_RUN |
| SYS-T16 | SYS-NORTH-002, SYS-NORTH-003, SYS-NORTH-004 | NOT_RUN |
| SYS-T17 | SYS-NORTH-001, SYS-GWOP-001, SYS-GWOP-002 | NOT_RUN |
| SYS-T18 | SYS-NORTH-005, SYS-FW-005, SYS-STATE-001, SYS-ISO-003 | NOT_RUN |
| SYS-T19 | SYS-FW-001, SYS-FW-002, SYS-FW-003 | NOT_RUN |
| SYS-T20 | SYS-GWOP-002, SYS-FW-001, SYS-FW-003, SYS-FW-004 | NOT_RUN |
| SYS-T21 | SYS-NORTH-004, SYS-NORTH-006, SYS-NORTH-007, SYS-APP-002, SYS-FW-004, SYS-STATE-002 | NOT_RUN |
| SYS-T22 | SYS-CFG-006, SYS-GWOP-002, SYS-UI-003, SYS-ISO-003 | NOT_RUN |
| SYS-T23 | SYS-GWOP-001, SYS-UI-004, SYS-UI-005, SYS-STATE-001 | NOT_RUN |
| SYS-T24 | SYS-NORTH-003, SYS-UI-004, SYS-APP-001, SYS-APP-002 | NOT_RUN |
| SYS-T25 | SYS-NORTH-005, SYS-FW-005, SYS-ISO-003 | NOT_RUN |
| SYS-T26 | SYS-APP-003 | NOT_RUN |
| SYS-T27 | SYS-UI-005, SYS-SVC-001, SYS-CHG-002 | NOT_RUN |
| SYS-T28 | SYS-NORTH-006, SYS-CFG-005, SYS-STATE-002 | NOT_RUN |
| SYS-T29 | SYS-GSEL-001, SYS-GSEL-004, SYS-GSEL-006 | NOT_RUN |
| SYS-T30 | SYS-GSEL-001, SYS-GSEL-004, SYS-GSEL-005, SYS-GSEL-006 | NOT_RUN |
| SYS-T31 | SYS-GSEL-002, SYS-GSEL-007, SYS-GSEL-019 | NOT_RUN |
| SYS-T32 | SYS-GSEL-003, SYS-GSEL-009 | NOT_RUN |
| SYS-T33 | SYS-GSEL-007, SYS-GSEL-008, SYS-GSEL-020 | NOT_RUN |
| SYS-T34 | SYS-GSEL-008, SYS-GSEL-009, SYS-GSEL-018 | NOT_RUN |
| SYS-T35 | SYS-GSEL-005, SYS-GSEL-011 | NOT_RUN |
| SYS-T36 | SYS-GSEL-010, SYS-GSEL-011 | NOT_RUN |
| SYS-T37 | SYS-GSEL-006, SYS-GSEL-015 | NOT_RUN |
| SYS-T38 | SYS-GSEL-006, SYS-GSEL-013, SYS-GSEL-014, SYS-GSEL-020 | NOT_RUN |
| SYS-T39 | SYS-GSEL-004, SYS-GSEL-005, SYS-GSEL-012 | NOT_RUN |
| SYS-T40 | SYS-GSEL-007, SYS-GSEL-015, SYS-GSEL-016, SYS-GSEL-020 | NOT_RUN |
| SYS-T41 | SYS-GSEL-003, SYS-GSEL-017 | NOT_RUN |
| SYS-T42 | SYS-GSEL-009, SYS-GSEL-018, SYS-GSEL-019, SYS-GSEL-020 | NOT_RUN |
| SYS-T43 | SYS-GNET-001, SYS-GNET-002, SYS-GNET-004, SYS-GNET-009 | NOT_RUN |
| SYS-T44 | SYS-GNET-001, SYS-GNET-003, SYS-GNET-009 | NOT_RUN |
| SYS-T45 | SYS-GNET-002, SYS-GNET-004, SYS-GNET-008, SYS-GNET-012 | NOT_RUN |
| SYS-T46 | SYS-GNET-005, SYS-GNET-009 | NOT_RUN |
| SYS-T47 | SYS-GNET-006, SYS-GNET-010, SYS-GNET-011 | NOT_RUN |
| SYS-T48 | SYS-GNET-003, SYS-GNET-005, SYS-GNET-006, SYS-GNET-011 | NOT_RUN |
| SYS-T49 | SYS-GNET-004, SYS-GNET-007 | NOT_RUN |
| SYS-T50 | SYS-GNET-002, SYS-GNET-008, SYS-GNET-012 | NOT_RUN |

## Open Questions — 本ビューの完成

[OQ-R6-19-01](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-01)：正式USDM・要求対応。[OQ-R6-17-01](../chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-01)：受入条件。
