---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-MEETING
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.1.0
status: TEMPLATE
title: 会議・議題・決定・派生作業
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
trace_contract: spkgw.lifecycle-tags/v1
related_trace_ids: []
phase_ids: []
phase_scope: UNASSIGNED
activity_type: MEETING
related_ids: []
---

# 会議・議題・決定・派生作業

## 主題と対象
MTG ID、主Trace、関連Trace、TASK、phase_ids、日時、参加者、入力Baseline／成果版を記入する。

## 議題別記録
| 議題ID | 対象Trace／工程 | 入力成果ID・版 | 事実と議論 | 決定ID／保留 | 派生TASK／OQ | 担当・期限 |
|---|---|---|---|---|---|---|
| 未記入 | 未記入 | 未記入 | 未記入 | 未記入 | 未記入 | 未記入 |

## 追跡関係
MTG／AGENDA→対象はdiscusses、DEC→対象はdecides_on、派生TASK→DEC／MTGはaction_from。議論だけなら採用済みとしない。同じ会議録をTrace別に複製しない。

## 工数・機密
control.jsonの原票／TASKを参照し、議題数で全時間を重複計上しない。配布範囲を明記。

## Open Questions
未決事項・担当・期限をOQ又は議題の保留へ残す。
