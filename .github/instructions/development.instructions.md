---
description: "SPK-GWの開発変更・対象環境・検証境界"
applyTo: "**/*.c,**/*.h,**/*.cpp,**/*.hpp,**/*.py,**/*.bb,**/*.bbappend,**/*.conf,**/CMakeLists.txt,**/Makefile"
---

# 開発変更の確認
[設計STD](../../00_governance/STD_15_Design_Decisions.md)と[実装STD](../../00_governance/STD_16_Implementation_C_Yocto.md)を、実際の対象・言語に適用する。

認可されたTASKの範囲内で最小の差分にする。要求/ITR、入力commit・未commit差分、影響するAPI/状態/保存/競合を確認する。Cでは所有権・寿命・長さ・整数変換・異常解放・同期を調べる。Yocto対象ならMACHINE/DISTRO/layer/recipe/patchを版付きで示す。ホストでの成功を対象機や実機の合格にしない。

既存ユーザー変更を消さず、未実施試験をNOT_RUNとして理由を残す。テストのskip・判定閾値・警告無視を変えて合格を演出しない。生成コードを独立レビュー済みと表示しない。
