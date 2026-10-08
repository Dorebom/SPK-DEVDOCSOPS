#!/usr/bin/env python3
"""Rebuild R6 completion sections, per-note questions and navigation (stdlib only).

Authoritative additions: data/completion_items.json. Existing R5 SYS/test/TBD/
parameter/IF records remain unchanged. Does not access networks or equipment.
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEM_MARK = '<!-- R6:COMPLETION_ITEMS -->'
OQ_MARK = '<!-- R6:OPEN_QUESTIONS -->'


def readj(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def write(rel: str, text: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n', encoding='utf-8')


def relpath(target: str, source: str) -> str:
    return os.path.relpath(ROOT / target, (ROOT / source).parent).replace(os.sep, '/')


def strip_front(t: str) -> str:
    return re.sub(r'^---\n.*?\n---\n', '', t, count=1, flags=re.S).lstrip()


def main() -> None:
    index = readj('data/document_index.json')
    items = readj('data/completion_items.json')['items']
    policy = readj('data/completion_policy.json')
    gates = policy['gates_proposed']
    bindings = readj('data/note_question_bindings.json')['note_bindings']
    byq = {x['question_id']: x for x in items}
    if len(byq) != len(items):
        raise ValueError('Duplicate question IDs')
    for x in items:
        if x['decision_gate'] not in gates:
            raise ValueError('Unknown gate: ' + x['decision_gate'])
    chapter_by_num = {c['number']: c for c in index['chapters']}

    def qlink(q: str, src: str) -> str:
        x = byq[q]
        path = '' if src == x['note'] else relpath(x['note'], src)
        return f'[{q}]({path}#{q.lower()})'

    def list_questions(src: str, qs: list[str], own: bool = False) -> str:
        anchor = 'oq-list-' + re.sub(r'[^a-z0-9]+', '-', src.lower()).strip('-')
        out = [OQ_MARK, f'<a id="{anchor}"></a>', '## Open Questions — 本ノートを完成させるための未決事項', '']
        if own:
            out += ['以下は本章の具体的な未決事項。**担当者・回答期限の日付・採用値・承認結果は未確定**である。担当ロールと確定ゲートは提案。回答を得ただけでは閉じず、根拠確認・決定・本文と関連台帳への反映を行う。',
                    f'全体索引：[Open Question横断台帳]({relpath("appendices/Open_Question_Register.md", src)})。各質問の編集正本は[data/completion_items.json]({relpath("data/completion_items.json", src)})。', '']
            for q in qs:
                x = byq[q]
                owner = x.get('owner') or '未割当'
                due = x.get('due_date') or '未定'
                answer = x.get('answer') or '未記入'
                out += [f'<a id="{q.lower()}"></a>', f'### {q} — {x["title"]}', '',
                        f'**対象項：** [{x["section_number"]} {x["title"]}](#{x["id"].lower()})',
                        f'**質問：** {x["question"]}',
                        f'**必要資料・完了条件：** {x["closure"]}',
                        f'**決定担当：** {owner}（候補：{x["proposed_owner_role"]}）。承認者：{x.get("approver") or "未定"}。',
                        f'**確定時点：** {x["decision_gate"]}＝{gates[x["decision_gate"]]}（提案）。回答期限の日付：{due}。',
                        f'**未解決時の制約：** {x["impact"]}',
                        f'**既存ID：** {", ".join(x["related_ids"]) or "該当ID未付与。A1の補完指摘から追加した具体化項目"}。',
                        f'**状態：** {x["status"]}。**回答：** {answer}。**決定記録：** {x.get("decision_record") or "未記入"}。', '']
        else:
            out += ['本ノートに関係する質問を、下表の正本章で管理する。同じ質問を別IDで重複起票せず、回答・採用値・決定記録を参照元にも反映する。履歴本文は当時の状態であり、現在の未決事項が解消した証拠にはしない。', '',
                    '| Open Question・正本章 | 具体的に不足する判断 | 解消時に必要な成果物 |', '|---|---|---|']
            for q in qs:
                x = byq[q]
                out += [f'| {qlink(q, src)} | {x["question"]} | {x["closure"]} |']
            out += ['', '担当者・期限・状態はリンク先を正本とする。新たな数値や認証判断を本参照表だけで確定しない。', '']
        return re.sub(r'\n(\*\*(?:質問|必要資料・完了条件|決定担当|確定時点|未解決時の制約|既存ID|状態)：\*\*)', r'\n\n\1', '\n'.join(out))

    section_map = []
    for c in index['chapters']:
        src = 'chapters/' + c['file']
        t = (ROOT / src).read_text(encoding='utf-8').split(ITEM_MARK)[0].split(OQ_MARK)[0].rstrip()
        # All old section numbers remain. New subdivisions are appended after their max.
        oldnumbers = [int(m) for m in re.findall(rf'^## {c["number"]}\.(\d+)\b', t, re.M)]
        next_sec = max(oldnumbers, default=0) + 1
        selected = [x for x in items if x['chapter'] == c['number']]
        grouped: dict[str, list[dict]] = {}
        for x in selected:
            grouped.setdefault(x['group'], []).append(x)
        addition = [ITEM_MARK, '', '> **R6の補完範囲：** 以下はレビューA1から追加した章節項の記入枠であり、数値・機種・機能採否・個別規格適用を推定した確定仕様ではない。各項末のリンクから、本章末尾の具体的な質問・必要資料・確定時点を確認できる。', '']
        related_books = {
            1: ['Normative_References_Glossary.md','Product_Function_Matrix.md'],
            2: ['Interface_Contract_Detail.md','Device_Profile_Extended.md'],
            3: ['Interface_Contract_Detail.md','Deployment_Binding.md'],
            4: ['Product_Function_Matrix.md','Device_Profile_Extended.md'],
            5: ['Interface_Contract_Detail.md','Quality_Acceptance_Profiles.md'],
            6: ['Product_Function_Matrix.md','Quality_Acceptance_Profiles.md'],
            7: ['Interface_Contract_Detail.md','Device_Profile_Extended.md'],
            8: ['Product_Function_Matrix.md','Quality_Acceptance_Profiles.md'],
            9: ['Data_Dictionary.md','Parameter_Register.md'],
            10: ['Grid_Connection_Profile.md','Normative_References_Glossary.md'],
            11: ['Data_Dictionary.md','Quality_Acceptance_Profiles.md'],
            12: ['State_Permission_Matrix.md','Configuration_Register.md'],
            13: ['UI_Alarm_Register.md','Quality_Acceptance_Profiles.md'],
            14: ['Parameter_Register.md','Quality_Acceptance_Profiles.md'],
            15: ['Deployment_Binding.md','Release_Impact_Addendum.md'],
            16: ['Normative_References_Glossary.md','Release_Impact_Addendum.md'],
            17: ['Quality_Acceptance_Profiles.md','Traceability.md'],
            18: ['Product_Function_Matrix.md','Configuration_Register.md'],
            19: ['Open_Question_Register.md','Coverage_Completion_Map.md'],
            20: ['Interface_Contract_Detail.md','UI_Alarm_Register.md'],
            21: ['Grid_Connection_Profile.md','Device_Profile_Extended.md'],
            22: ['Normative_References_Glossary.md','Quality_Acceptance_Profiles.md'],
            23: ['Normative_References_Glossary.md','Quality_Acceptance_Profiles.md'],
            24: ['Quality_Acceptance_Profiles.md','UI_Alarm_Register.md'],
            25: ['Quality_Acceptance_Profiles.md','Parameter_Register.md'],
            26: ['State_Permission_Matrix.md','Configuration_Register.md'],
            27: ['Data_Dictionary.md','Interface_Contract_Detail.md']
        }
        book_titles = {a['file']:a['title'] for a in index['appendices']}
        addition += ['**記入先・関連する規範候補別冊：** ' + ' ／ '.join(
            f'[{book_titles[f]}](../appendices/{f})' for f in related_books[c['number']]), '']
        for si, (group, gg) in enumerate(grouped.items(), next_sec):
            addition += [f'## {c["number"]}.{si} {group}', '']
            for sub, x in enumerate(gg, 1):
                sn = f'{c["number"]}.{si}.{sub}'
                x['section_number'] = sn
                addition += [f'<a id="{x["id"].lower()}"></a>', f'### {sn} {x["title"]}', '',
                             f'**補完項目ID：** `{x["id"]}`。**対応観点：** {", ".join(x["coverage_ids"])}（[レビューA1](../sources/review/R5_Coverage_Review_A1.md)）。', '',
                             x['context'], '', '**本項に記載する仕様項目：**', '']
                addition += [f'- {field}。' for field in x['fields']]
                addition += ['', f'**本項の完成判定：** {x["closure"]}', '',
                             f'**具体的な不足：** {qlink(x["question_id"], src)}。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。', '']
                section_map.append({'id': x['id'], 'question_id': x['question_id'], 'note': src, 'section': sn, 'title': x['title'], 'coverage_ids': x['coverage_ids'], 'content_status': 'OPEN_NOT_PRODUCT_APPROVED'})
        body = t + '\n\n' + '\n'.join(addition)
        body += '\n' + list_questions(src, [x['question_id'] for x in selected], True)
        write(src, body)

    # Derive queryable views. completion_items.json remains the only writable addition source.
    oqrows = []
    for x in items:
        oqrows.append({k: v for k, v in x.items() if k not in ('fields', 'context', 'group')})
    write('data/open_questions_r6.json', json.dumps({'schema': 'spkgw.open-questions-view/v1', 'revision': 'R6', 'generated_from': 'data/completion_items.json', 'questions': oqrows}, ensure_ascii=False, indent=2))
    write('data/completion_section_map.json', json.dumps({'revision': 'R6', 'sections': section_map}, ensure_ascii=False, indent=2))

    # Coverage table: copy A1 rows verbatim for titles and old assessments.
    review = (ROOT / 'sources/review/R5_Coverage_Review_A1.md').read_text(encoding='utf-8')
    cr = []
    for line in review.splitlines():
        if re.match(r'^\| C\d{2} \|', line):
            cols = [z.strip() for z in line.strip().strip('|').split('|')]
            cr.append(dict(id=cols[0], title=cols[1], baseline_assessment=cols[2], baseline_location=cols[3], finding=cols[4]))
    if len(cr) != 34:
        raise ValueError('A1 coverage row count is not 34')
    src = 'appendices/Coverage_Completion_Map.md'
    cov = ['# 網羅性34観点とR6章節項・Open Questionの対応', '',
           '基準：[レビューA1](../sources/review/R5_Coverage_Review_A1.md)。34観点は同レビューのチェック観点で、ISO等の正式な条項数・指定目次ではない。', '',
           '**R6の判定は「項目配置済み・具体仕様はOPEN」**。見出しを追加したことを、数値確定・機能承認・適合確認・製品完成に読み替えない。主要項目がR5にある観点も、残る具体化質問を結び付けた。', '',
           '| 観点 | R5の評価 | R6の記載先（章節項） | 対応Open Question |', '|---|---|---|---|']
    for r in cr:
        linked = [x for x in items if r['id'] in x['coverage_ids']]
        r['completion_items'] = [x['id'] for x in linked]
        r['question_ids'] = [x['question_id'] for x in linked]
        r['r6_status'] = 'STRUCTURE_PRESENT_CONTENT_OPEN'
        # First two full locations then link to authoritative item mapping for the rest.
        locs = [f'[{x["section_number"]} {x["title"]}]({relpath(x["note"],src)}#{x["id"].lower()})' for x in linked]
        cov.append(f'| {r["id"]} {r["title"]} | {r["baseline_assessment"]} | {"<br/>".join(locs)} | {"<br/>".join(qlink(x["question_id"],src) for x in linked)} |')
    cov += ['', '## 完成とするために残ること', '',
            '適用/対象外と理由、製品・機器の実構成、値・範囲・既定値、規範資料の版、確認方法と合否、判断者と記録がそろい、対応OQの回答が本文・SYS/USDM・試験へ反映された時点で完成判定する。試験の未実施と、試験条件の未確定は別である。']
    write(src, '\n'.join(cov))
    write('data/coverage_completion_map.json', json.dumps({'revision': 'R6', 'coverage': cr}, ensure_ascii=False, indent=2))

    # Global question index with a mapping back to all existing TBD and PAR records.
    src = 'appendices/Open_Question_Register.md'
    out = ['# Open Question横断台帳・既存TBDとの対応', '',
           f'R6の具体化質問は**{len(items)}件**。初版作成時はすべて未回答・OPEN。個別の現在状態は正本章の質問カードで確認する。既存48件のTBDや50件のパラメータを削除・解消・改番したものではなく、章の完成に必要な問いへ分解・対応付けた管理ビューである。単純に48＋85件を独立課題の合計とは数えない。', '',
           '質問と項目の正本：[data/completion_items.json](../data/completion_items.json)。章末尾と本一覧は生成ビュー。回答欄・担当者・期限等を正本で更新し、`python tools/rebuild_views.py`で同期する。', '',
           '## 提案する確定ゲート', '', '| ゲート | 確定時点の案 |', '|---|---|']
    for k, v in gates.items():
        out.append(f'| {k} | {v} |')
    out += ['', 'G0〜G4は本改訂で提案した文書完成の判断時点であり、既存プロジェクトの承認済み日程や役職ではない。担当者名・実日付・承認者は未定。OQ-R6-19-02で正式な管理方法へ対応付ける。', '',
            '## 質問一覧', '', '| OQ・正本章 | 具体的な質問 | 担当候補／確定ゲート |', '|---|---|---|']
    for x in items:
        out.append(f'| {qlink(x["question_id"],src)}<br/>{x["section_number"]} {x["title"]} | {x["question"]} | {x["proposed_owner_role"]}<br/>{x["decision_gate"]}（提案） |')
    mapping = []
    for fn, key, title in [('open_issues.json','issues','既存TBD 48件との対応'),('parameters.json','parameters','既存パラメータ50件との対応')]:
        rows = readj('data/' + fn)[key]
        out += ['', '## ' + title, '', '| 既存ID | 既存の未決内容 | 具体化するR6 OQ |', '|---|---|---|']
        for r in rows:
            qs = [x['question_id'] for x in items if r['id'] in x['related_ids']]
            if not qs:
                raise ValueError('Existing undecided item not linked: ' + r['id'])
            out.append(f'| {r["id"]} | {r.get("subject", r.get("name", ""))} | {" / ".join(qlink(q,src) for q in qs)} |')
            mapping.append({'legacy_id':r['id'], 'source':'data/'+fn, 'question_ids':qs, 'legacy_status_unchanged':True})
    write(src, '\n'.join(out))
    write('data/legacy_question_crosswalk.json',json.dumps({'revision':'R6','crosswalk':mapping},ensure_ascii=False,indent=2))

    chg = readj('data/r6_document_changes.json')['changes'][0]
    write('appendices/R6_Change_Summary.md', f'''# R6改訂内容・保持範囲・未確定の扱い

## 入力と作業範囲

R5一式と[網羅性レビューA1](../sources/review/R5_Coverage_Review_A1.md)を基準に、[CTX-R6](../sources/USER_CONTEXT_R6.md)の不足項目・各ノート末尾の質問を具体化した。

## 追加・補強

本編は21章を維持・補強し、第22〜27章を新設した。34のレビュー観点を{len(items)}個の補完項目と{len(items)}件のOpen Questionへ対応付けた。物理・電気、環境、安全、品質、ライフサイクル、セキュリティは独立章、機能/状態/IF/データ/設定/UI/受入は既存章と規範候補別冊へ追補した。

## 既存文の明示補正（A1 AUD-12）

対象：第4.5節 NORMAL_OPERATION_ONLYの配置説明。

**変更前：** {chg['before']}

**変更後：** {chg['after']}

第15.4/15.7節で既に示された現行条件にそろえた。原典やR5の履歴を改ざんせず、新しいPCS_DIRECT対象を追加しない。これは文書内の補正であり、実装適合や正式な設計承認を意味しない。

## 保持するもの

124 SYS要求、69試験、48既存未決、50既存パラメータ、16外部IF、接続経路データ、R5のMermaid/SVG/PNGは変更しない。初版作成時の新しい質問はすべてOPENで、未確認値・担当者・日程・機器・認証判断を埋めていない。原典・旧版・A1原本はsources以下へ保存した。

## ノート末尾の適用範囲

現行の本編・別冊・README/MOC・編集案内・文書QA・図案内・統合版にOpen Questions節を設ける。本編には質問本文・解消条件・担当候補・確定時点・進行制限を置く。別冊等は同じ質問を正本章へ参照し、二重の回答正本を作らない。sources以下は不変の根拠資料のため、末尾を変更しない。

## 完了していないこと

具体的な数値・機種・機能採否・規範版の確定、正式SYS/USDM化、実装・実機・セキュリティ/安全評価、JET等の判断、全規格条項監査。追加見出しと質問の配置をもって製品仕様完成とはしない。
''')

    # Reading/editing guide.
    write('01_Completion_Guide.md', f'''# R6 — 仕様完成の進め方とOpen Questionの記入方法

## 1. 読む順序

[34観点の配置表](appendices/Coverage_Completion_Map.md)で不足の記載先を確認し、該当章の補完項目から末尾のOpen Questionへ進む。[横断台帳](appendices/Open_Question_Register.md)には全{len(items)}件と既存48 TBD/50パラメータの対応がある。

## 2. 項目と質問の関係

`Cxx（A1観点）→ SLOT-R6-章-項 → OQ-R6-章-項 → 決定・根拠 → 本文/規範別冊 → 必要なSYS/USDMと検証`で追跡する。SLOTは記入先であり、新しい承認済みシステム要求ではない。

## 3. 回答に含める内容

| 記入欄 | 内容 |
|---|---|
| OQ ID | 対象を一意に指定する |
| 回答 | 採用する内容、候補又は対象外の場合はその理由 |
| 適用条件 | 製品・HW/FW・機器・通信・状態・地域/契約等 |
| 根拠 | メーカー資料、既存仕様、設計判断、試験等のID・版・箇所 |
| 数値と確認 | 値・範囲・単位・測定条件・合否基準、又は確定する参照先 |
| 担当・期限 | 実担当者と回答日・判断予定日（未定ならそのまま） |
| 決定 | 承認者と判断記録。提案の回答を正式承認と同一視しない |
| 反映先 | 本文/別冊、既存TBD/PAR、SYS/USDM/設計/試験の更新箇所 |

## 4. 更新の正本

今回の追加本文と質問の編集正本は `data/completion_items.json`。`context`は分かっている前提、`fields`は記入項目、`question`/`closure`は問いと解消条件。回答時は `answer`、`owner`、`due_date`、`approver`、`decision_record`を更新する。具体仕様へ反映する際は本文・規範別冊及び必要な要求/試験を同時に改訂し、その改訂も記録する。

状態は自動で閉じない。採否と根拠を確認し、本文・関連データへの反映とレビューが完了してから判断する。既存 `data/open_issues.json` のOPENも、この生成処理で勝手にCLOSEDへ変えない。

## 5. 再生成・検査

```sh
python tools/rebuild_views.py
python tools/validate_el_routes.py
python tools/validate_grid_selection.py
python tools/validate_package.py --refresh-manifest
python tools/validate_package.py
```

文書QAが確認するのは、章節項とOQの配置、既存レコード/図/入力の保持、参照リンク、ID、生成の再現性等。実機・性能・安全・認証の試験にはならない。章番号は既存参照を壊さないよう21章まで保持し、新項はその章の既存最大節番号の後へ追加する。

## 6. 原典と対象外

sources内のアーキテクチャ・旧版・レビュー原本は不変とし、現行ノートの質問追加対象から除外する。古い参照本文や図を現行ルールより優先しない。基準はR5を維持したR6の本文。
''')

    # Add trailing reference questions to every non-chapter current note (except consolidated, built last).
    for src, qs in bindings.items():
        if src in ('README.md','00_MOC.md','DOCUMENT_QA.md','90_All_In_One.md'):
            continue
        p = ROOT/src
        if not p.exists():
            raise ValueError('Question target note missing: '+src)
        base = p.read_text(encoding='utf-8').split(OQ_MARK)[0].rstrip()
        write(src, base + '\n\n' + list_questions(src,qs))

    # Current MOC and package guide.
    info = readj('package_info.json')
    moc = ['# MOC — SPK-GW_HEMS システム仕様書 R6', '',
           'DRAFT_FOR_REVIEW。R5とA1の不足を章節項とOpen Questionへ展開した。機能採否・数値・認証判断は未確定。', '',
           '[R6改訂内容](appendices/R6_Change_Summary.md) ／ [34観点の配置](appendices/Coverage_Completion_Map.md) ／ [質問一覧](appendices/Open_Question_Register.md) ／ [記入方法](01_Completion_Guide.md) ／ [統合版](90_All_In_One.md)', '',
           '## 本編', '', '| 章 | ノート | R6補完項目・OQ |', '|---|---|---|']
    for c in index['chapters']:
        n = sum(x['chapter']==c['number'] for x in items)
        moc.append(f'| {c["number"]:02d} | [{c["title"]}](chapters/{c["file"]}) | {n}件 |')
    moc += ['', '## 別冊', '', '| ノート | 内容 |','|---|---|']
    for a in index['appendices']:
        moc.append(f'| [{a["file"]}](appendices/{a["file"]}) | {a["title"]} |')
    moc += ['', '## 原典・検査', '', '[R5入力ZIP](sources/baseline/R5.zip) ／ [レビューA1原本](sources/review/R5_Coverage_Review_A1.md) ／ [原典](sources/architecture/00_MOC.md) ／ [文書QA](DOCUMENT_QA.md)。sources内は不変の履歴・根拠。']
    write('00_MOC.md','\n'.join(moc)+'\n\n'+list_questions('00_MOC.md',bindings['00_MOC.md']))
    write('README.md', f'''# SPK-GW_HEMS システム仕様書 R6

2026-10-06／DRAFT_FOR_REVIEW。R5と網羅性レビューA1を基準に、不足を章節項へ記載し、各現行MDノート末尾にOpen Questionsを追加した。

[読む順序・記入方法](01_Completion_Guide.md) ／ [MOC](00_MOC.md) ／ [統合版](90_All_In_One.md) ／ [網羅性34観点の対応表](appendices/Coverage_Completion_Map.md) ／ [Open Question一覧](appendices/Open_Question_Register.md)

## 変更範囲

| 内容 | R6 |
|---|---|
| 本編 | {len(index['chapters'])}章。既存21章を保持・補強、6章新設 |
| 別冊 | {len(index['appendices'])}冊。機能/IF/データ/設定/状態/UI/受入等の記入項目と索引 |
| 補完項目・質問 | {len(items)}項・{len(items)}件。初版は全件OPEN、回答未記入。現在状態は質問カード |
| 既存管理データ | 124 SYS・69試験・48 TBD・50パラメータ・16 IFのレコードを不変保持 |
| 整合補正 | 第4.5節の旧RS-485/PCS_DIRECT例を現行条件へ明示補正 |
| 構成・図 | ルータ必須、EL PCS自律取得、RS-485 GW管理、H/G分離、R5通常EL図を保持 |

## 数値・根拠・承認

具体値、機種、規格適用、担当者、回答期限日、正式承認は補完していない。担当ロールとG0〜G4ゲートは提案。項目配置の網羅と、仕様内容の確定・製品適合は別。新設章の内容を承認済みの追加機能要求として扱わない。

## 正本・再生成

本編の既存部分はchapters、今回の追加項目と質問は[data/completion_items.json](data/completion_items.json)が編集正本。`python tools/rebuild_views.py`で追加節・章末OQ・別冊参照OQ・対応表・統合版を同期する。既存SYS/試験等は本改訂で変更しないため、R5からの管理データと本文ビューを維持した。

`python tools/validate_package.py`は文書QA。`--refresh-manifest`はレビュー済みの編集後にマニフェストを再作成する。詳細は[文書QA](DOCUMENT_QA.md)。旧版の検査結果とスクリプトはsources/historyに保存し、今回の検査に読み替えない。

## ノート末尾の対象

本編・別冊・README/MOC・編集案内・文書QA・図案内・統合版にOpen Questionsを設けた。原典/旧版/レビューを含むsources配下だけは不変保存のため除外。参照ノートの質問は正本章へ結び、独立した二重回答を求めない。

実装・実機・性能・安全・セキュリティ試験・JET判断は未実施。R5の2図はバイト不変で継承し、R6では再描画していない。

''' + list_questions('README.md',bindings['README.md']))

    # QA is written by validator; retain its base or create a factual placeholder.
    qa = ROOT/'DOCUMENT_QA.md'
    currentqa = qa.read_text(encoding='utf-8') if qa.exists() else ''
    if '# R6 文書QA' not in currentqa:
        currentqa = '# R6 文書QA\n\nR6の検査結果は`python tools/validate_package.py`で生成する。未生成の段階では合格を主張しない。\n'
    currentqa = currentqa.split(OQ_MARK)[0].rstrip()
    write('DOCUMENT_QA.md',currentqa+'\n\n'+list_questions('DOCUMENT_QA.md',bindings['DOCUMENT_QA.md']))

    # Consolidated view: section/question anchors are preserved, links are internalized.
    paths = [ROOT/'chapters'/c['file'] for c in index['chapters']]
    paths += [ROOT/'appendices'/a['file'] for a in index['appendices']]
    anchors = {(ROOT/'chapters'/c['file']).resolve():f'ch-{c["number"]:02d}' for c in index['chapters']}
    for a in index['appendices']:
        anchors[(ROOT/'appendices'/a['file']).resolve()]='ap-'+Path(a['file']).stem.lower().replace('_','-')
    def convert(t: str, src: Path) -> str:
        def rep(m: re.Match) -> str:
            label,target=m.groups()
            if target.startswith(('https:','http:','mailto:','#')):
                return m.group(0)
            base,sep,frag=target.partition('#')
            ab=(src.parent/base).resolve()
            if ab in anchors:
                return f'[{label}](#{frag if sep else anchors[ab]})'
            rp=os.path.relpath(ab,ROOT).replace(os.sep,'/')
            return f'[{label}]({rp}'+('#'+frag if sep else '')+')'
        return re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',rep,t)
    combined=['---','title: "SPK-GW_HEMS システム仕様書 R6 — 網羅性補完・Open Questions"','revision: "R6"','updated: 2026-10-06','status: DRAFT_FOR_REVIEW','source_baseline: "System_Spec_R5 + Coverage_Review_A1 + CTX-R6"','---','',
              '# SPK-GW_HEMS システム仕様書 R6','',
              f'R5の構成・制御契約を保持し、A1の34観点を補う{len(items)}項と{len(items)}件のOpen Questionを追加した。各章末尾に具体的な質問・資料・担当候補・確定時点を記載する。内容の決定・実装・試験・認証承認は未完了。', '',
              'このファイルは分割章・別冊からの生成ビュー。[編集案内](01_Completion_Guide.md)を参照。sourcesは変更しない根拠資料であり、現行方針を上書きしない。', '', '## 目次', '']
    for c in index['chapters']:
        combined.append(f'- [{c["number"]:02d}. {c["title"]}](#ch-{c["number"]:02d})')
    for a in index['appendices']:
        combined.append(f'- [別冊：{a["title"]}](#{anchors[(ROOT/"appendices"/a["file"]).resolve()]})')
    text='\n'.join(combined)+'\n'
    for p in paths:
        t=strip_front(p.read_text(encoding='utf-8'))
        an=anchors[p.resolve()]
        if f'<a id="{an}"></a>' not in t:
            t=f'<a id="{an}"></a>\n\n'+t
        text+='\n---\n\n'+convert(t,p)
    text+='\n---\n\n'+convert(list_questions('90_All_In_One.md',bindings['90_All_In_One.md']),ROOT/'90_All_In_One.md')
    write('90_All_In_One.md',text)
    print(f'R6 rebuilt: {len(index["chapters"])} chapters, {len(index["appendices"])} appendices, {len(items)} completion items/questions.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f'Rebuild failed: {exc}')
