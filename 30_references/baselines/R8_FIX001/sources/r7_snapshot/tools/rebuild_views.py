#!/usr/bin/env python3
"""Rebuild R7 navigation and derived function/role/configuration views.

Python 3.11+, standard library only. No network or device operations.
Existing R6 completion generator is reused with its original index; R7 data do
not replace SYS requirements, test results or approved device profiles.
"""
from __future__ import annotations
import json, os, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def write(p,t):
 q=ROOT/p; q.parent.mkdir(parents=True,exist_ok=True); q.write_text(t.rstrip()+'\n',encoding='utf-8')
def dump(p,d): write(p,json.dumps(d,ensure_ascii=False,indent=2))
def rel(target,src): return os.path.relpath(ROOT/target,(ROOT/src).parent).replace(os.sep,'/')
def link(label,target,src,anchor=''): return f'[{label}]({rel(target,src)}'+('#'+anchor if anchor else '')+')'
def table(headers,rows):
 def c(v):return str(v).replace('|','&#124;').replace('\n','<br/>')
 return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(c(x) for x in r)+' |' for r in rows])
PARTS=[
 ('I','I_System_Specification.md','システム全体仕様',[1,2,4,6,10,11,21]),
 ('II','II_GW_Product_Specification.md','SPK-GW製品仕様',[3,5,7,8,9,12,13,20]),
 ('III','III_Boundary_Interfaces.md','境界インターフェース仕様',[2,3,7,15,20,21,22]),
 ('IV','IV_Quality_Constraints.md','横断品質・制約仕様',[10,11,14,15,22,23,24,25,27]),
 ('V','V_Lifecycle_Verification.md','ライフサイクル・適合・検証',[16,17,18,19,26])]
NEW_AP=[('Functional_Allocation.md','二段機能・既存要求・R6棚卸しの対応'),('Role_Function_Access.md','4利用者の機能・操作権限（規範別冊候補）'),('Configuration_Patterns.md','機器構成パターン・対応条件（規範別冊候補）'),('R7_Change_Summary.md','R7変更内容・確認結果・正本の分担')]

def main():
 original=load('data/r6_document_index.json')
 old_qa = (ROOT/'DOCUMENT_QA.md').read_text(encoding='utf-8') if (ROOT/'DOCUMENT_QA.md').exists() else ''
 dump('data/document_index.json',original)
 subprocess.run([sys.executable,str(ROOT/'tools/r6_rebuild_core.py')],check=True)
 if old_qa.startswith('# R7 文書QA'):
  write('DOCUMENT_QA.md',old_qa)
 catalog=load('data/function_catalog_r7.json'); S=catalog['system_functions']; G=catalog['gw_functions']
 roles=load('data/role_access_r7.json'); patterns=load('data/configuration_patterns_r7.json')['patterns']
 reqs=load('data/requirements.json')['requirements']; rmap={r['id']:r for r in reqs}
 items=load('data/completion_items.json')['items']; qm={q['question_id']:q for q in items}
 chapter={c['number']:c for c in original['chapters']}
 def qlink(q,src):return link(q,qm[q]['note'],src,q.lower())
 def fnlink(f,src):
  dest='parts/II_GW_Product_Specification.md' if f.startswith('GW-') else 'parts/I_System_Specification.md'
  return link(f,dest,src,f.lower())
 def source_links(r,src):
  return '<br/>'.join(link(Path(p).stem,p,src) for p in r['source_notes'])
 def qtail(src,ids):
  ids=list(dict.fromkeys(ids))
  rows=[]
  for q in ids:
   x=qm[q]; note=''
   if q=='OQ-R6-01-01':note='【一部回答済み】4分類の名称は今回確定。権限・委譲・環境等は未決。 '
   rows.append([qlink(q,src),note+x['question'],x['closure']])
  return '\n\n## Open Questions — 本ノートの完成に必要な確認\n\n既存OQの正本は `data/completion_items.json`。本一覧は参照で、別の回答正本を作らない。4利用者の確定事項は `data/known_answers_r7.json` を併読する。承認・数値・適合を未確認で補完しない。\n\n'+table(['OQ・正本章','具体的な質問／未回答部分','必要資料・完了条件'],rows)
 def chrefs(nums,src):return table(['既存章','扱う内容'],[[link(f'{n:02d}. {chapter[n]["title"]}','chapters/'+chapter[n]['file'],src),chapter[n]['title']] for n in nums])
 def role_summary(src):return table(['利用者分類（確定）','役割範囲の案（権限は未承認）'],[[r['name'],r['responsibility_proposal']] for r in roles['human_roles']])
 def pattern_summary(src):return table(['構成ID／代表型','出力制御スケジュールの取得・適用主体','通常操作・観測','適合状態'],[[link(p['id']+' '+p['name'],'appendices/Configuration_Patterns.md',src,p['id'].lower()),p['grid_fetch_owner'],p['pcs_route'],'型式・版・台数・共存条件は未確認'] for p in patterns])
 def definitions(rows,src,system):
  out=[]
  for r in rows:
   out.extend([f'<a id="{r["id"].lower()}"></a>',f'### {r["id"]} — {r["name"]}',r['behavior'],f'**適用条件：** {r["applicability"]}',f'**実現責任：** {r.get("allocation",r.get("realization_owners"))}',f'**根拠状態：** `{r["basis"]}`。採用リリース・実装確認・正式USDM対応は未確定。'])
   refs=r.get('gw_function_ids') if system else r['parent_system_function_ids']
   out.append(('**関係するGW機能（実装責任は別途確認）：** ' if system else '**上位の全体機能：** ')+ ' ／ '.join(fnlink(x,src) for x in refs))
   out.append('**関連SYS要求：** '+'、'.join(link(x,'appendices/Requirements_Catalog.md',src) for x in r['requirement_ids']))
   out.append('**根拠本文：** '+source_links(r,src))
   out.append('**残る確認：** '+' ／ '.join(qlink(x,src) for x in r['open_question_ids']))
   out.append('')
  return '\n\n'.join(out)
 base_note='**文書状態：DRAFT_FOR_REVIEW。** 機能の一覧化・配賦整理であり、実装・機能採用・権限付与・対応機器の承認ではない。R6の27詳細章・124 SYS要求・69試験・85 OQは維持する。'

 src='parts/I_System_Specification.md'
 summary=table(['全体機能ID','機能（要求の要約）','実現する要素','関係するGW機能'],[[fnlink(r['id'],src),r['name']+'：'+r['behavior'],r['realization_owners'],'、'.join(fnlink(x,src) for x in r['gw_function_ids'])] for r in S])
 t=f'''<a id="part-i"></a>
# I. システム全体仕様

{base_note}

## I.1 対象と読み方

住宅設備・GW・クラウド・端末・宅内ネットワークを含め、全体として何ができるかと誰が実現するかを記載する。GWに実装しないPCSの自律取得・系統保護、スマートフォン／クラウドの役割も全体機能に含める。

システム全体の一覧とGW一覧は二重記載ではなく、上位機能から各要素への配賦関係である。`S-FN-*`／`GW-FN-*`は本一覧の識別子で、既存`SYS-*`要求の改番や承認済みUSDMの新設ではない。

## I.2 システム全体の機能（要件）一覧

**21機能群。既存R6から抽出した設計・候補の一覧であり、既存実装の全機能棚卸し完了を意味しない。** 各行の詳細カードに適用条件・要求・OQを載せる。

{summary}

## I.3 システム利用者と機能範囲

{role_summary(src)}

4つは利用者の種類であり、権限の上下4段階ではない。メーカー又は開発者を全機能の管理者にしない。1人の複数役割、役割切替、兼任可否、委任対象・期限は未確定。施工者・運用者等のR6表現を新たな第5ロールとせず、4分類への対応を確認する。

本編はロールの定義、利用場面、機能群ごとの概要、通常APIからの禁止事項を保持する。詳細は[利用者別機能・操作権限別冊](../appendices/Role_Function_Access.md)を文書ID・版で規範参照する。手順書や画面非表示だけを認可の正本にしない。自動EMS、上位サービス、配信サービス等の機械主体は人の4分類とは別に識別する。

## I.4 機器構成パターン

{pattern_summary(src)}

本編に責務・経路が異なる代表パターンを残す。メーカー・型式・FW・台数・配線・プロパティ差の全組合せは[構成パターン別冊](../appendices/Configuration_Patterns.md)に展開する。構成別の対応機能は「あり／なし」だけでなく、条件付き・非対応・未確認を分ける。

すべての出力制御サーバ通信は宅内ルータ経由。EL接続PCSだけがGW非経由で取得し、RS-485接続PCSはGW G側が取得・管理・指示する。これを単なる選択メニューで入替えない。

## I.5 既存詳細章との対応

{chrefs(PARTS[0][3],src)}

## I.6 全体機能の適用条件・根拠カード

{definitions(S,src,True)}
'''
 write(src,t+qtail(src,['OQ-R6-04-01','OQ-R6-01-01','OQ-R6-04-02','OQ-R6-08-01','OQ-R6-21-01','OQ-R6-11-02']))
 src='parts/II_GW_Product_Specification.md'
 summary=table(['GW機能ID','GWが提供する機能','GW内の担当責務','上位全体機能'],[[fnlink(r['id'],src),r['name'],r['allocation'],'、'.join(fnlink(x,src) for x in r['parent_system_function_ids'])] for r in G])
 t=f'''<a id="part-ii"></a>
# II. SPK-GW製品仕様

{base_note}

## II.1 GW単体の保証範囲

本部はSPK-GW製品に配賦された振る舞いを列挙する。構成に応じたH/G双方を含む。論理機能を独立プロセス又は別CPUと断定しない。スマートフォンアプリの画面、PCS内の系統連系保護、EL接続PCSのサーバ取得はGW機能に移さない。

## II.2 SPK-GW製品の機能（要件）一覧

**32機能群。** 全体機能からGWへ割り当てる要求と支援・観測だけの関係を区別する。詳細操作・採用リリース・機器能力・数値・USDM確定は既存OQで継続する。

{summary}

## II.3 機能要件と非機能要求のつなぎ方

IVに横断品質・制約をまとめるが、認証する・拒否する・記録する・復旧する等の必要な機構は本機能一覧にも現れる。例えば「認可機能」は本部の機能、「権限を持たない主体から保護する」という品質目標はIV、「許可操作・期限・対象・エラー」はIIIの契約に対応付ける。

非機能要求をIVへ隔離して関係を切らない。機能ごとに適用する性能、セキュリティ、安全、可用性等の要求IDを関連付ける。機能件数と要求件数は一致させない。

## II.4 利用者からの操作と自律機能

ユーザ／メンテナンス／メーカー／開発者に同じ機能の全操作を一括付与しない。監視、運転、設定、診断、更新適用、配布承認、系統保守を操作単位に分割する。

認可の判定と実行可能性は別である。提案する実行許可条件は、本人・機械主体の認証、役割の操作権限、対象住宅／機器のscope、環境・チャネル、機能採用、現在状態・Capability、期限と制御権の成立を組み合わせる。ルータ経由か直接Webかだけで権限を変えない。UIだけでなくGWの境界で拒否する。

詳細は[4利用者の機能・操作権限](../appendices/Role_Function_Access.md)。G側通常APIの禁止操作はどの利用者名でも解除できない。認可された専用保守は別契約として残す。

## II.5 既存詳細章との対応

{chrefs(PARTS[1][3],src)}

## II.6 GW機能の適用条件・根拠カード

{definitions(G,src,False)}
'''
 write(src,t+qtail(src,['OQ-R6-04-01','OQ-R6-05-01','OQ-R6-07-01','OQ-R6-07-02','OQ-R6-20-01','OQ-R6-01-01','OQ-R6-19-01']))

 src='parts/III_Boundary_Interfaces.md'
 ifaces=load('data/external_interfaces.json')['interfaces']
 t=f'''<a id="part-iii"></a>
# III. 境界インターフェース仕様

{base_note}

## III.1 IF一覧と責務

新しいIF-IDへ改番せず、R6の16契約を参照する。複数段のアプリ→クラウド→GWを一つの通信セッションとみなさない。人の役割とサーバ接続の資格も分ける。

{table(['既存ID','契約','両端・主体','主な情報'],[[link(x['id'],'appendices/External_Interface_Register.md',src),x['name'],x['actor']+' → '+x['peer'],x['information']] for x in ifaces])}

## III.2 規範別冊の粒度

[IF台帳](../appendices/External_Interface_Register.md)と[具体化項目](../appendices/Interface_Contract_Detail.md)を正本候補とする。主体、開始側、経路、形式、必須項目、認証認可、設定世代、期限・再送・冪等性、エラー、版、負荷上限、監査、試験条件を定義する。

通信IFだけでなく、H/G間の論理操作境界、観測の正本と参照、電源・信号・配線の物理境界も対応付ける。詳細実装のIPC方式・構造体までは本部で決めない。

## III.3 4利用者と操作権限

各操作に [Role_Function_Access](../appendices/Role_Function_Access.md) のポリシーIDを関連付ける。受信経路が信頼できることと、依頼者が対象操作を許可されることは別。クラウドの接続認証を、すべての依頼者の無制限権限へ変換しない。

## III.4 既存詳細章との対応

{chrefs(PARTS[2][3],src)}
'''
 write(src,t+qtail(src,['OQ-R6-03-02','OQ-R6-07-01','OQ-R6-07-02','OQ-R6-20-01','OQ-R6-27-03']))
 src='parts/IV_Quality_Constraints.md'
 t=f'''<a id="part-iv"></a>
# IV. 横断品質・制約仕様

{base_note}

## IV.1 適用範囲

性能、時間、容量、精度、信頼性、可用性、保守性、耐久性、安全、セキュリティ、プライバシー、物理・電気・設置・環境の要求を横断管理する。各要求にシステム全体／GW／PCS／IF／共有資源の適用対象を付ける。

## IV.2 機能と非機能要求の関係

I/IIの機能に対して品質・制約要求を関連付ける。同じログ記録でも、記録操作は機能、保持期間・改ざん耐性・容量は制約である。認可・失効・更新検証などの具体機構を、非機能という理由で機能一覧から除外しない。

役割名や文書の置き場所は試験免除の条件ではない。ソフト変更時には機能・IFの構文だけでなく、要求頻度、資源、設定、依存先、故障時の振る舞いへの影響を確認する。実際の認証変更判断は未実施。

## IV.3 既存詳細章との対応

{chrefs(PARTS[3][3],src)}

[パラメータ台帳](../appendices/Parameter_Register.md)の既存50件を保持し、値を創作しない。[品質受入別冊](../appendices/Quality_Acceptance_Profiles.md)で対象構成・測定方法・合否を確定する。
'''
 write(src,t+qtail(src,['OQ-R6-14-01','OQ-R6-15-02','OQ-R6-25-01','OQ-R6-24-01','OQ-R6-27-01']))
 src='parts/V_Lifecycle_Verification.md'
 t=f'''<a id="part-v"></a>
# V. ライフサイクル・適合・検証

{base_note}

## V.1 機能を採用・検証する条件

システム全体の目的とGW配賦を区別し、各構成・役割・操作・状態について、要求への適合と利用目的の成立を確認する。機能一覧掲載だけで初回採用、実装済み、認証済みとしない。

## V.2 必要な対応関係

`USDM／製品要求 → S-FN → GW-FN及び外部要素への配賦 → SYS要求・境界IF → 構成条件・権限条件 → 試験／レビュー／解析 → 判定・証拠`を管理する。

既存124 SYS要求の正式USDM対応と採用内容は未確定のまま。すべてを機能要件へ分類し直すものではない。機能に紐付かない管理・品質・適合要求は [配賦別冊](../appendices/Functional_Allocation.md)で明示して後続レビューする。

## V.3 構成別・役割別の確認案

同じ機能について、許可／不許可ロール、他住宅、期限切れ委任、運転中、保守中、量産／開発環境、直接Web／上位／再送を組み合わせて確認する。IFの入り口だけでなくGW・対象機器での実際の処置を観測する。

代表構成ごとに取得主体、通常通信、保護責任、障害位置、HW/H/G/PCS版、対応機能を確認する。これは試験追加の提案であり、既存69試験の実施結果を変更しない。

## V.4 既存詳細章との対応

{chrefs(PARTS[4][3],src)}
'''
 write(src,t+qtail(src,['OQ-R6-17-01','OQ-R6-17-02','OQ-R6-19-01','OQ-R6-19-02','OQ-R6-26-07']))

 # Mapping between levels and actual legacy requirements.
 src='appendices/Functional_Allocation.md'
 groups={r['id']:[g['id'] for g in G if r['id'] in g['requirement_ids']] for r in reqs}
 # System-only technical conditions remain on system functions rather than invented GW implementations.
 extra={'S-FN-013':['SYS-GRID-001','SYS-GNET-002'],'S-FN-014':['SYS-GRID-002']}
 rows=[]
 for r in reqs:
  sy=[s['id'] for s in S if r['id'] in s['requirement_ids'] or r['id'] in extra.get(s['id'],[])]
  rows.append(dict(requirement_id=r['id'],system_function_ids=sy,gw_function_ids=groups[r['id']],classification='FUNCTION_RELATED_CANDIDATE_MAPPING' if sy or groups[r['id']] else 'CROSS_CUTTING_OR_ALLOCATION_REVIEW',verification_ids=r['verification_ids'],review=r.get('verification_review')))
 dump('data/requirements_function_crosswalk_r7.json',dict(schema='spkgw.function-requirement-crosswalk/v1',rows=rows))
 alloc=table(['全体機能','関係するGW機能','外部要素の責任／誤ってGWへ配賦しない条件'],[[fnlink(s['id'],src)+' '+s['name'],'、'.join(fnlink(g,src) for g in s['gw_function_ids']),s['realization_owners']+'。'+s['applicability']] for s in S])
 cross=load('data/function_lineage_r7.json')['rows']
 t=f'''# 二段の機能一覧・既存SYS要求・R6棚卸しの対応

**規範候補・配賦案。** 本表は上位の目的・機能と、GWの実行責任を対応付ける。自動生成ビューで、編集正本は [function_catalog_r7.json](../data/function_catalog_r7.json)。既存SYS要求と試験を新しい件数に置き換えない。

## 1. 全体機能からGW・外部要素への配賦

{alloc}

S-FN-013に対するGW-FN-016は状態参照だけ、GW-FN-028は非迂回の境界支援だけであり、GWがPCSのスケジュールを取得・適用するという意味ではない。S-FN-014の保護成立責任もPCS等に残る。クラウドの認証・アプリの画面はGWへ転記しない。

## 2. R6の21棚卸し行との対応

R6のFN-DRAFTは調査開始行であり、採用済み要件ではない。本表は内容を捨てずに二段の一覧へ展開した対応である。

{table(['R6開始行','R7の関係するGW機能'],[[x['r6_inventory_id'],'、'.join(fnlink(g,src) for g in x['gw_function_ids'])] for x in cross])}

## 3. 既存124 SYS要求との対応

「機能関連なし」は要求削除ではない。品質・構成・証拠・管理要求等への配賦又は対応見直しが必要な行として保持する。関連SYS要求に含めたことは正式な要求分解承認ではない。試験IDはR6の値から転記し、未実施を合格にしない。

{table(['SYS要求','全体機能','GW機能','R6検証参照／分類'],[[link(x['requirement_id'],'appendices/Requirements_Catalog.md',src),'、'.join(fnlink(g,src) for g in x['system_function_ids']) or '横断要求等・要配賦レビュー','、'.join(fnlink(g,src) for g in x['gw_function_ids']) or 'GW機能への直接配賦なし','、'.join(x['verification_ids']) or x.get('review') or x['classification']] for x in rows])}

## 4. 単一正本と完成条件

同じ詳細規定をI・II・IF・ロール表へ複製しない。機能の意味は機能ID、操作の通信契約はIF-ID、権限はポリシーID、対応機器は構成ID・版で参照する。採用、変更区分、必須／任意／将来／対象外、正式USDM、受入条件を確定して初めて対応機能とする。
'''
 write(src,t+qtail(src,['OQ-R6-04-01','OQ-R6-19-01','OQ-R6-17-01']))

 src='appendices/Role_Function_Access.md'
 perm=table(['操作ID／操作','関連GW機能','ユーザ','メンテナンス','メーカー','開発者'],[[x['id']+' '+x['operation'],'、'.join(fnlink(g,src) for g in x['gw_function_ids'])]+[x['proposed_permissions'][r['id']] for r in roles['human_roles']] for x in roles['permissions']])
 cond=table(['操作ID','追加条件・境界','環境'],[[x['id'],x['condition'],x['environment']] for x in roles['permissions']])
 t=f'''# 利用者別機能・操作権限仕様（規範別冊候補）

文書ID：`SPKGW-ANNEX-ACCESS`。版：`R7-DRAFT`。**4利用者の名称はユーザー確定。以下の権限マトリクスは提案であり、実行認可として使用しない。** 正本候補は [role_access_r7.json](../data/role_access_r7.json)。承認済み権限欄はすべてnullのまま。

## 1. 本編と別冊に何を書くか

本編Iには4分類・目的・利用場面・機能群別概要、本編IIにはGWが実施する認可・拒否・状態検査、本編IIIにはIFの認証・認可文脈、本編IVには最小権限・環境分離・監査等を記載する。この別冊が操作単位の詳細表を所有する。利用者マニュアル・施工保守手順・開発手順には具体操作を展開し、権限の新設は手順書側で行わない。

版・適用製品・承認・変更影響を持つ規範別冊として本体仕様の一部にする。単なる参考添付にしない。秘匿性の高い保守の具体手順は配布先を限定してよいが、禁止操作・認可境界まで本体から消さない。

## 2. 4利用者

{role_summary(src)}

ロールをユーザ＜メンテナンス＜メーカー＜開発者という単純な包含関係にしない。「メーカー」は全住宅への恒久アクセス、「開発者」は量産機の自由な操作を意味しない。製造・施工・運用の担当がどのロールを取るかは職務と委任で確定する。人の兼任・ロール切替、同一セッションでの併用、職務分離は未決。

## 3. 操作単位の権限マトリクス案

全セルは**レビュー案**。既存仕様の通常API非迂回原則を除き、新しい許可・禁止の採用を確定していない。空欄／nullは許可ではない。

{perm}

## 4. 条件付き権限

{cond}

判定は「誰」「何の操作」「どの住宅・GW・機器」「どのチャネル」「どの製品状態」「本番・製造・開発のどの環境」「いつまで」「誰の承認・委任か」を含める。GW操作の許可と実行順序・機器制御権の調停は分ける。

通常API経由の保護・出力制御の迂回は4ロールとも許可しない。専用のG側保守はIF-MAINT-01／IF-GRID-03の独立認可・対象・手続きを維持し、通常ロールの文字列だけで有効化しない。

## 5. 完成させる台帳フィールド

`policy_id / function_id / operation_id / target_scope / role / environment / channel / product_state / feature_profile / allowed_or_denied / value_range / delegation / expiry / additional_approval / audit / error_response / verification_id / applicable_document_revision`。

サーバやアプリに表示しないだけでなく、GWのAPI・公開IF・最終操作境界でも強制する。受信時と実行時に古い認可・期限・対象所属を再確認する。機械主体と人の代理権を別々に表現する。

## 6. 既存Open Questionの一部回答

OQ-R6-01-01の「誰が利用するか」のうち4分類の名称は今回の入力で回答済み。具体的権限、本人確認、委譲、兼任、対象範囲、承認者が残るため、質問全体はOPENを維持する。更新根拠は [CTX-R7](../sources/USER_CONTEXT_R7.md) と [部分回答記録](../data/known_answers_r7.json)。
'''
 write(src,t+qtail(src,['OQ-R6-01-01','OQ-R6-20-01','OQ-R6-27-02','OQ-R6-27-04','OQ-R6-27-06','OQ-R6-26-01']))

 src='appendices/Configuration_Patterns.md'
 cards=[]
 for p in patterns:
  cards+=[f'<a id="{p["id"].lower()}"></a>',f'### {p["id"]} — {p["name"]}',table(['項目','構成条件'],[[k,p[v]] for k,v in [('RS-485接続PCS','rs485_pcs'),('EL接続PCS','el_pcs'),('空調・給湯・計測器','other_el'),('取得・適用主体','grid_fetch_owner'),('サーバ通信経路','grid_route'),('機器への経路','pcs_route'),('方式','grid_mode'),('注意','important')]]),'**対応可否：** `TBD_NOT_APPROVED`。具体型式・版・台数・電力トポロジー・認証根拠は未確認。\n']
 t=f'''# 構成パターン・機能適用仕様（規範別冊候補）

文書ID：`SPKGW-ANNEX-CONFIG`。版：`R7-DRAFT`。既存の二方式・混在の記述を、3代表構成として整理した。**構成の説明と、当該機器組合せの対応承認は別。** 正本候補は [configuration_patterns_r7.json](../data/configuration_patterns_r7.json)。

## 1. 本編と別冊の分担

本編Iは、機器構成で機能分担が変わる代表図・代表表、選択の規則、共通不変条件を記載する。別冊は型式、HW/H/G/PCS/クラウド/アプリ版、台数、計測点、能力、IF、制限、試験結果、認証範囲を管理する。施工手順は選択・登録・検査の手順であり、製品が対応する構成そのものを変更しない。

各設置サイトには承認された構成プロファイルの版と、実際に据え付けた個体・配線・設定を関連付ける。代表例の存在だけで任意メーカー・台数・混在を許可しない。

## 2. 責務が異なる代表3構成

{chr(10).join(cards)}

## 3. 構成と主な機能の対応

以下の「対象」はアーキテクチャ上の対象であって、実機動作・製品採用の承認ではない。空調・給湯・計測器は各構成で必要能力に従う。

{table(['機能／責務','CFG-RS','CFG-EL','CFG-MIX'],[
 ['RS-485 PCS通常制御','対象','対象外','RS-485対象のみ'],
 ['EL PCS通常制御','対象外','対象','EL対象のみ'],
 ['GW G側の取得・管理・指示','RS-485対象','PCS向け適用なし','RS-485対象のみ'],
 ['PCS自身のサーバ取得','RS-485 PCSは対象外','各EL PCSが担当','各EL PCSが担当'],
 ['空調・給湯・計測器の通常EL接続','必要機器があれば対象','必要機器があれば対象','必要機器があれば対象'],
 ['高度エネマネ戦略','必要能力と採用戦略次第','必要能力と採用戦略次第','必要能力・全体制約次第'],
 ['宅内Web・上位・アプリ・FW','接続・採用条件による','接続・採用条件による','接続・採用条件による'],
 ['系統連系保護','PCS等の責任','PCS等の責任','各保護領域で確認']])}

## 4. 組合せを増やす軸と、増やさない軸

PVのみ／蓄電池のみ／双方／Hybrid PCS、RS-485／EL／混在、単台／複数、空調・給湯・計測の能力、上位サービス採否を独立した構成属性にする。Hybrid PCSの複数ELオブジェクトを複数物理PCSと数えない。

全パターンを掛け合わせて図を増やす必要はない。責務・制御経路・保証条件が変わる分類だけを本編へ、機種差・台数差・プロパティ差は別冊の表へ置く。WAN断等の一時的な故障状態は原則として新しい販売構成ではなく、既存構成の運用状態として扱う。

PCSなし構成は今回新たな対応範囲へ追加していない。必要なら別途機能採否・制御対象なし時のUI・製品価値を確認する。

## 5. 全構成で維持する条件

出力制御サーバとの通信はすべて宅内ルータ経由。EL接続PCSだけがGW非経由で取得し、RS-485 PCSはGW G側が取得・管理・指示する。通常EL通信とサーバ取得を混同しない。空調・給湯・計測器へ出力制御クライアントを一般化しない。

同一制御scopeに二つの能動適用主体を置かない。混在構成で連系点全体に制約がある場合、独立PCSの上限を設定しただけでは全体適合の確認にならない。対応する統括構成・配分又は対象外判断を必要とする。未確認の自動方式切替や代理取得を追加しない。

## 6. 正式な構成プロファイルに必要な項目

`configuration_id / revision / product_model / HW_version / H_FW / G_FW / device_model_FW / device_count / physical_device_id / resource_group / measurement_point / power_topology / router_profile / normal_route / grid_fetch_owner / grid_scope / feature_ids / function_status / supported_operations / limits / interface_versions / verification_evidence / certification_basis / approval_record`。

機能状態は対応／条件付き／非対応／未確認を区別する。TBDを「非対応」又は「対応」に黙って置換しない。機器プロファイル、構成一覧、機能一覧、役割表、試験をIDで対応させる。
'''
 write(src,t+qtail(src,['OQ-R6-04-02','OQ-R6-21-01','OQ-R6-11-02','OQ-R6-07-02','OQ-R6-15-01','OQ-R6-26-03']))

 src='appendices/R7_Change_Summary.md'
 t='''# R7 — 機能の二段一覧・4利用者・機器構成の文書分担

## 1. 確認結果

R6には第4.10節の記入枠と、Product_Function_Matrixの21棚卸し行が存在した。全体とGWを区別したI/IIそれぞれの一覧は未作成だった。前回の5部構成は回答中の提案であり、R6の27章が既に5部へ物理再編されていたわけではない。

## 2. 今回実施したこと

5部の入口ノートを作り、Iへ全体21機能群、IIへGW32機能群を明示した。両者の配賦、既存124 SYS要求、R6の21棚卸し行、OQの関係を生成表へ展開した。

利用者名はユーザ／メンテナンス／メーカー／開発者の4種類に固定した。権限表13操作群は提案で、承認欄は未記入。機器構成はRS-485主体／EL PCS主体／混在の3代表型を示すが、機種・版・台数の対応承認は未実施。

## 3. 保持したもの

既存27詳細章は番号・ファイル・内容を維持し、既存29別冊の本文も維持した。85 OQ、124 SYS要求、69試験、48既存TBD、50パラメータ、16 IF、R5図資産、現行ルータ／取得主体ルールを変更しない。

既存OQ-R6-01-01は4分類の名称部分が回答済みであることを部分回答台帳に記録した。権限・委任等が未決のため、原質問全体をCLOSEDにしない。

## 4. 再編の範囲

今回は5部で読める入口・一覧と規範候補別冊を追加する改訂であり、27詳細章をすべて切り分けて新章番号へ移動する作業は行っていない。旧章が複数Partに関係する場合は参照でつなぐ。既存リンク・IDの大規模改番を避ける。

## 5. 出典と提案の区別

主たる根拠はR6実ファイルと今回のユーザー指示。一般的な分解・配賦、役割と権限、規範IF・構成管理の文書分担を考える補助として下記公開一次資料を2026-10-07に確認した。これらをSPK-GWの正式採用規格や認証条件として追加したものではない。

- NASA, [4.3 Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/): 上位機能を要素へ分解・配賦する考え方。
- NASA, [6.3 Interface Management](https://www.nasa.gov/reference/6-3-interface-management/): 境界の定義・相手との合意・変更管理。
- NASA, [6.5 Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/): 構成の識別・基準化・変更管理。
- NIST, [RBAC FAQs](https://csrc.nist.gov/projects/role-based-access-control/faqs): 人への役割割当と役割への権限割当を区別する考え方。4種類の具体名称・権限内容はこの資料の規定ではない。

## 6. 未完了のこと

既存実装の全機能監査、機能採否、正式USDM化、具体的権限の承認、機種・構成対応の承認、性能・安全・認証評価、実機試験は未実施。機能一覧の件数は製品完成度ではない。新規図の作成・描画は行っていない。
'''
 write(src,t+qtail(src,['OQ-R6-04-01','OQ-R6-01-01','OQ-R6-04-02','OQ-R6-19-01']))

 # Current package navigation. Retain original detailed notes, not duplicate normative copies.
 index=dict(original);index['parts']=[dict(part=p,file=f,title=title,related_chapters=cs) for p,f,title,cs in PARTS]
 index['appendices']=original['appendices']+[dict(file=f,title=title) for f,title in NEW_AP]
 dump('data/document_index.json',index)
 src='00_MOC.md'
 t='''# MOC — SPK-GW_HEMS システム仕様書 R7

2026-10-07／DRAFT_FOR_REVIEW。I/IIに二段の機能一覧を追加した。5部の入口から既存27詳細章を読む構成で、全章の物理移動・改番ではない。4利用者名は確定、権限・対応構成の詳細は提案／未確定。

## 5部の入口

'''+table(['Part','本編入口','主な内容'],[[p,link(title,'parts/'+f,src),'全体21機能群' if p=='I' else 'GW32機能群' if p=='II' else '境界・品質・ライフサイクルの索引'] for p,f,title,cs in PARTS])+'''

## 今回追加の規範候補別冊

'''+table(['別冊','内容'],[[link(title,'appendices/'+f,src),title] for f,title in NEW_AP])+'''

## 既存詳細章（番号・内容を維持）

'''+chrefs(list(range(1,28)),src)+'''

## 既存別冊

'''+table(['別冊','内容'],[[link(a['file'],'appendices/'+a['file'],src),a['title']] for a in original['appendices']])+'''

[統合版](90_All_In_One.md) ／ [編集・完成ガイド](01_Completion_Guide.md) ／ [文書QA](DOCUMENT_QA.md)
'''
 write(src,t+qtail(src,['OQ-R6-04-01','OQ-R6-01-01','OQ-R6-04-02']))
 src='README.md'
 t='''# SPK-GW_HEMS システム仕様書 R7

2026-10-07／DRAFT_FOR_REVIEW。R6を基準に、5部の入口と二段の機能一覧を追加した。既存27詳細章は改番・移動せず保持する。

[I. システム全体機能21群](parts/I_System_Specification.md) ／ [II. GW機能32群](parts/II_GW_Product_Specification.md) ／ [MOC](00_MOC.md) ／ [統合版](90_All_In_One.md)

## 追加内容

[機能配賦・要求対応](appendices/Functional_Allocation.md)、[4利用者の機能・操作権限](appendices/Role_Function_Access.md)、[3代表構成と適用条件](appendices/Configuration_Patterns.md)、[変更内容](appendices/R7_Change_Summary.md)を追加した。

権限表は13操作群の提案。4利用者名以外の権限を承認したものではない。構成型は責務の代表例であり、実機のサポート認定ではない。機能一覧はR6の既知内容から抽出し、既存実装の全機能調査を完了してはいない。

## 維持条件

全出力制御サーバ通信は宅内ルータ経由。EL接続PCSのみGW非経由で自律取得し、RS-485接続PCSはGW G側が取得・管理・指示する。通常EL接続・上位・Web・アプリ・FW配信とH/G分離を維持する。124 SYS要求・69試験・85 OQを改番・承認・実行しない。

## 編集と検査

[編集・完成ガイド](01_Completion_Guide.md)の正本で編集し、`python tools/rebuild_views.py`、`python tools/validate_package.py --refresh-manifest`、`python tools/validate_package.py`の順で再生成・検査する。文書QAは実機・安全・性能・認証の検証ではない。
'''
 write(src,t+qtail(src,['OQ-R6-04-01','OQ-R6-01-01','OQ-R6-04-02']))
 src='01_Completion_Guide.md'
 t='''# R7 — 仕様完成と正本・別冊の更新方法

## 1. 確定事項と提案

今回確定した入力は、人の利用者分類がユーザ／メンテナンス／メーカー／開発者の4種類であること。具体機能の採否・権限・構成適合・数値は未承認のまま。過去の一般的な利用者表現より今回の4分類を優先するが、過去の職務項目は4分類への対応確認対象として残す。

## 2. 編集する正本

| 内容 | 正本 | 生成先 |
|---|---|---|
| R6の85補完項・OQ | data/completion_items.json | 各章末、既存横断台帳 |
| 2段の機能名・振る舞い・配賦 | data/function_catalog_r7.json | Part I/II、配賦別冊 |
| R6棚卸しからの対応 | data/function_lineage_r7.json | 配賦別冊 |
| 4利用者名・権限提案／承認欄 | data/role_access_r7.json | 権限別冊、Part I概要 |
| 代表構成・対応状態 | data/configuration_patterns_r7.json | 構成別冊、Part I概要 |
| R6 OQへの追加の部分回答 | data/known_answers_r7.json | 質問の残りを示す補助記録 |
| 既存要求・試験・IF | 各既存dataと本文 | 今回は変更しない。将来変更時はレビュー・差分記録を別途行う |

`S-FN`／`GW-FN`は機能索引で、SYS要求を置き換えない。正式USDM、採用リリース、既存／追加等の変更区分、受入条件はOQの回答とレビューで確定する。

## 3. 質問の閉じ方

4種類の名称が分かっただけでは、OQ-R6-01-01の認可・委譲・責任等は未回答。部分回答記録を参照し、残りだけを質問する。回答・根拠・承認者・適用条件を本文と規範別冊へ反映してから閉じる。

既存の記入説明は [R6ガイド原本](sources/history/R6_Completion_Guide.md)に保存した。現行R7では本ガイドと新しい生成スクリプトを使用する。

## 4. 再生成と検査

```sh
python tools/rebuild_views.py
python tools/validate_package.py --refresh-manifest
python tools/validate_package.py
```

生成ツールは最初にR6の補完項・OQを同期し、その後5部入口・新別冊・統合版を生成する。R6の旧スクリプトを単独実行してR7の入口を上書きしない。

本文は27詳細章、入口は5Partのまま維持する。本体を完全に再配置する場合でも、機能ID・要求ID・OQ IDは章番号だけに依存させず、移設の対応表を作る。

## 5. 別冊の採用管理

本編には代表例と原則を置き、別冊の文書ID・版・適用製品・承認状態を明示する。詳細権限や機種対応の正本を本編へ複製しない。手順書は操作手順であり、権限や対応範囲を独自に拡大できない。
'''
 write(src,t+qtail(src,['OQ-R6-19-01','OQ-R6-19-02','OQ-R6-01-01']))

 # Do not carry old QA forward as a new result.
 qa=ROOT/'DOCUMENT_QA.md'
 if not qa.exists() or not qa.read_text(encoding='utf-8').startswith('# R7 文書QA'):
  write('DOCUMENT_QA.md','# R7 文書QA\n\n今回の検査結果は未生成。`python tools/validate_package.py --refresh-manifest`で検査後に更新する。'+qtail('DOCUMENT_QA.md',['OQ-R6-17-01']))

 # Metadata: R6 fields retained as historic record, current summaries explicit.
 info=load('package_info.json')
 info.update(package_id='SPK-GW_HEMS_System_Spec_20261007_R7',revision='R7',updated='2026-10-07',reference_baseline='SPK-GW_HEMS_System_Spec_20261006_R6',parts=5,chapters=27,appendices=len(index['appendices']),system_function_groups=len(S),gw_function_groups=len(G),human_role_names_confirmed=4,role_operation_groups_proposed=len(roles['permissions']),representative_configurations=len(patterns),r7_change_scope='PART_ENTRY_VIEWS_AND_TWO_LEVEL_FUNCTION_INDEX_ROLE_CONFIG_PROPOSALS',r7_detailed_chapters_moved_or_renumbered=False,r7_runtime_contracts_changed=False,r7_new_product_requirements=0,r7_diagrams_changed=False,r7_diagrams_rerendered=False,document_completeness='FUNCTION_INVENTORY_AND_VIEWS_ADDED_CONTENT_ADOPTION_OPEN')
 dump('package_info.json',info)

 # Consolidate new parts + existing detailed notes + appendices, one anchor per source.
 paths=[ROOT/'parts'/f for _,f,_,_ in PARTS]+[ROOT/'chapters'/c['file'] for c in original['chapters']]+[ROOT/'appendices'/a['file'] for a in index['appendices']]
 anchors={}
 for p in paths:
  txt=p.read_text(encoding='utf-8'); found=re.search(r'<a id="([^"]+)"',txt)
  if p.parent.name=='parts':an='part-'+next(x[0].lower() for x in PARTS if x[1]==p.name)
  elif p.parent.name=='chapters':an='ch-'+p.name[:2]
  else:an='ap-'+p.stem.lower().replace('_','-')
  anchors[p.resolve()]=an
 def convert(txt,p):
  def replace(m):
   lab,target=m.groups()
   if target.startswith(('http:','https:','mailto:','#','data:')):return m.group(0)
   base,sep,frag=target.partition('#'); full=(p.parent/base).resolve()
   if full in anchors:return f'[{lab}](#{frag if sep else anchors[full]})'
   return f'[{lab}]({os.path.relpath(full,ROOT).replace(os.sep,"/")}'+('#'+frag if sep else '')+')'
  return re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',replace,txt)
 allone=['---','title: "SPK-GW_HEMS システム仕様書 R7 — 5部入口・二段機能一覧"','revision: "R7"','updated: 2026-10-07','status: DRAFT_FOR_REVIEW','---','','# SPK-GW_HEMS システム仕様書 R7','','5部の入口と全体21／GW32機能群を追加。既存27詳細章・124 SYS要求・69試験・85 OQを保持。機能採否・権限・構成適合は未承認。前回の5部構成案を入口として実ファイル化したが、詳細章は物理移動・改番していない。','','[編集ガイド](01_Completion_Guide.md) ／ [MOC](00_MOC.md)','','## 目次','']
 for p in paths:allone.append(f'- [{p.stem}](#{anchors[p.resolve()]})')
 for p in paths:
  txt=re.sub(r'^---\n.*?\n---\n','',p.read_text(encoding='utf-8'),count=1,flags=re.S)
  an=anchors[p.resolve()]
  if f'<a id="{an}"></a>' not in txt:txt=f'<a id="{an}"></a>\n\n'+txt
  allone+=['','---','',convert(txt,p)]
 allone+=['','---',convert(qtail('90_All_In_One.md',['OQ-R6-04-01','OQ-R6-01-01','OQ-R6-04-02']),ROOT/'90_All_In_One.md')]
 write('90_All_In_One.md','\n'.join(allone))
 print(f'R7 rebuilt: {len(S)} system / {len(G)} GW functions, 5 Part entries, 27 detailed chapters, {len(index["appendices"])} appendices.')

if __name__=='__main__':
 try:main()
 except (OSError,ValueError,KeyError,json.JSONDecodeError,subprocess.CalledProcessError) as exc: raise SystemExit(f'Rebuild failed: {exc}')
