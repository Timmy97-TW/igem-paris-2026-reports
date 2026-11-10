---
layout: doc
title: Pre-trip triage
eyebrow: Before we fly
section: Triage
description: Every accepted 2026 team, read from its published abstract and ranked against the four themes.
title_alt: 行前分類
eyebrow_alt: 出發之前
section_alt: 分類
description_alt: 每一支獲准參賽的 2026 隊伍，都讀過公開摘要，並依四個主題排序。
---

<div data-l="en" markdown="1">

Built before leaving, from the published abstracts of all **452 accepted** teams. Nothing here is an
observation — it is a reading list, so the floor time in Paris is deliberate.

Start with the [floor plan]({{ '/floor-plan.html' | relative_url }}): the {{ site.data.targets | size }} targets these four
documents produced, split between the three of us.

</div>
<div data-l="zh" data-tr markdown="1">

出發前根據全部 **452 支獲准參賽**隊伍的公開摘要整理而成。這裡沒有任何實地觀察——這是一份閱讀清單，讓我們在巴黎會場的時間用得有目的。

從[會場平面圖]({{ '/floor-plan.html' | relative_url }})開始看：這四份文件產生的 {{ site.data.targets | size }} 個目標，由我們三個人分工。

</div>
<div data-l="en" markdown="1">

## The four slices

| Slice | Villages | Teams |
|---|---|---|
| [A]({{ '/research/triage_A_agri_env_food.html' | relative_url }}) | Agriculture, bioremediation, conservation, food | 146 |
| [B]({{ '/research/triage_B_mfg_foundational_sw_space.html' | relative_url }}) | Biomanufacturing, foundational advance, software &amp; AI, space | 135 |
| [C]({{ '/research/triage_C_health.html' | relative_url }}) | Therapeutics, oncology, infectious diseases | 98 |
| [D]({{ '/research/triage_D_dx_fashion_other.html' | relative_url }}) | Diagnostics, fashion &amp; cosmetics | 73 |

Every accepted team appears in exactly one of them. Teams with no published abstract are marked `?`
and need their wiki opened, or a look at the board on the day.

</div>
<div data-l="zh" data-tr markdown="1">

## 四個分區 {#the-four-slices}

| 分區 | Village | 隊伍數 |
|---|---|---|
| [A]({{ '/research/triage_A_agri_env_food.html' | relative_url }}) | 農業、生物復育、保育、食品 | 146 |
| [B]({{ '/research/triage_B_mfg_foundational_sw_space.html' | relative_url }}) | 生物製造、基礎研究進展、軟體與 AI、太空 | 135 |
| [C]({{ '/research/triage_C_health.html' | relative_url }}) | 治療、腫瘤、傳染病 | 98 |
| [D]({{ '/research/triage_D_dx_fashion_other.html' | relative_url }}) | 診斷、時尚與美妝 | 73 |

每一支獲准參賽的隊伍都只出現在其中一份。沒有公開摘要的隊伍標記為 `?`，需要打開他們的 wiki，或當天去看他們的展板。

</div>
<div data-l="en" markdown="1">

## What came out of it

Four things worth knowing before the floor:

- **ACC deaminase is not ours alone.** Three other teams use it, and TUS-Japan surface-displays it on
  *Bacillus subtilis* via Tat secretion with a LysM anchor — our exact enzyme, our exact chassis, and
  our exact unsolved problem.
- **Our secretion blocker has precedents.** *B. subtilis* secretion appears in at least six teams.
  Hongwen School is the only one quoting a yield; Texas and Stony Brook both document secretion
  *failures*, which are worth more to us than the successes.
- **The closest hardware analogue is Taiwanese.** NTHU Taiwan built a self-built three-tank
  instrumented reactor with three biosafety layers.
- **Another team is also called ReLeaf** — WLSA-ShanghaiAcademy, lignocellulose to bioethanol. Worth
  knowing before someone congratulates the wrong booth.

</div>
<div data-l="zh" data-tr markdown="1">

## 整理出來的結果 {#what-came-out-of-it}

進會場前值得先知道的四件事：

- **ACC deaminase 不是只有我們在用。**另外三支隊伍也用它，而 TUS-Japan 透過 Tat 分泌搭配 LysM 錨定，把它表現在 *Bacillus subtilis* 表面——跟我們一模一樣的酵素、一模一樣的底盤菌，以及一模一樣尚未解決的問題。
- **我們卡住的分泌問題有前例。**至少六支隊伍做 *B. subtilis* 分泌。Hongwen School 是唯一提出產量數字的隊伍；Texas 和 Stony Brook 都記錄了分泌*失敗*，這對我們來說比成功案例更有價值。
- **最接近的硬體對照是台灣隊伍。**NTHU Taiwan 自己做了一台三槽、配有感測儀器的反應器，有三層生物安全防護。
- **另一支隊伍也叫 ReLeaf**——WLSA-ShanghaiAcademy，做木質纖維素轉生質乙醇。先知道這件事，免得有人恭喜錯攤位。

</div>
<div data-l="en" markdown="1">

## How to read it

These are abstracts the teams wrote to sell their projects, read by a language model, not by us. A
ranking is a reason to walk over, never a finding about the work. Where a claim looked unsupported
the triage says so — those are the questions to open with.

The inputs can be rebuilt: `tools/fetch_teams.py` re-pulls the team list from the iGEM API,
`tools/make_slices.py` splits it, and `tools/build_site_data.py` regenerates what this site renders.

</div>
<div data-l="zh" data-tr markdown="1">

## 怎麼讀 {#how-to-read-it}

這些是各隊為了推銷自己專案而寫的摘要，由語言模型閱讀，不是我們讀的。排名只是走過去看的理由，絕不是對他們研究成果的判斷。看起來缺乏根據的說法，分類裡都有註明——那些就是開場要問的問題。

輸入資料可以重建：`tools/fetch_teams.py` 從 iGEM API 重新抓取隊伍清單，`tools/make_slices.py` 把它分區，`tools/build_site_data.py` 重新產生這個網站呈現的內容。

</div>
