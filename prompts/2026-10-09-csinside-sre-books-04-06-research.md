---
doc_type: prompt-log
id: 2026-10-09-csinside-sre-books-04-06-research
author: "@csinside"
date: 2026-10-09
platform: Claude Code (desktop app)
model: "Claude Opus 5.5 (claude-opus-5-5)"
phase: exploration
role: research
significant: true
significant_reason: "Produced the topic 04, 05 and 06 claims that report sections 6, 7 and 8 rely on."
purpose: Plan and research the topic 04, 05 and 06 claims (OS, hardware, architecture) from the Google SRE books and official Google sources
pr: null
claims: [04-01, 04-02, 04-03, 04-04, 04-05, 04-06, 04-07, 04-08, 04-09, 04-10, 04-11, 04-12, 04-13, 04-14, 04-15, 04-16, 04-17, 04-18, 04-19, 04-20, 04-21, 04-22, 04-23, 04-24, 04-25, 04-26, 04-27, 04-28, 04-29, 04-30, 04-31, 04-32, 04-33, 04-34, 04-35, 04-36, 04-37, 04-38, 04-39, 04-40, 04-41, 04-42, 04-43, 04-44, 04-45, 04-46, 04-47, 04-48, 04-49, 04-50, 04-51, 04-52, 04-53, 04-54, 04-55, 04-56, 04-57, 05-01, 05-02, 05-03, 05-04, 05-05, 05-06, 05-07, 05-08, 05-09, 05-10, 05-11, 05-12, 05-13, 05-14, 05-15, 05-16, 05-17, 05-18, 05-19, 05-20, 05-21, 05-22, 05-23, 05-24, 05-25, 05-26, 05-27, 05-28, 05-29, 05-30, 05-31, 05-32, 05-33, 05-34, 05-35, 06-01, 06-02, 06-03, 06-04, 06-05, 06-06, 06-07, 06-08, 06-09, 06-10, 06-11, 06-12, 06-13, 06-14, 06-15, 06-16, 06-17, 06-18, 06-19, 06-20, 06-21, 06-22, 06-23, 06-24, 06-25, 06-26, 06-27, 06-28]
redactions: 22
supporting_docs:
  - docs/FinalAssignment_204341_1_69_AIAssignProject-1.pdf
  - https://sre.google/books/
---

## Turn 1 — user
@"[REDACTED:path]"
ยังไม่ต้องเขียนอะไร just plan สรุปมาอย่างง่ายว่าทำอะไรบ้าง หัวของที่เราได้เน้นทำคือ 
04-operating-systems
05-hardware-requirements
06-system-architecture-infrastructure
หัวข้องอื่นจะเป็นของเพื่อน
เอกสารอ้างอิงหลักคือ https://sre.google/books/
อยากให้หาว่าควรไปเน้นอ่านที่ส่วนไหน วางแผนการจัดสรรเนื้อหา

## Turn 1 — assistant
Downloaded all 3 books into scratchpad. Now keyword-scanning chapters to rank which ones matter for OS / hardware / architecture.

นี่คือแผนครับ ยังไม่ได้เขียนไฟล์อะไรใน repo ผมโหลดหนังสือทั้ง 3 เล่มบน sre.google/books มาค้นคำทุกบท เพื่อหาว่าบทไหนพูดถึง OS, hardware และ architecture จริง

## สิ่งที่เจอ

1. **SRE book บทที่ 2 คือแกนของทั้ง 3 หัวข้อ** ([Production Environment](https://sre.google/sre-book/production-environment/)) มีเครื่อง → rack → cluster → datacenter, Borg ที่หนังสือเรียกว่า "cluster operating system", Colossus, Jupiter/B4 และเส้นทางของ request หนึ่งตัว
2. **SRE book ทั้งเล่มไม่มีคำว่า "Linux" เลย** หลักฐานว่า Google ใช้ Linux อยู่ในเล่ม *Building Secure & Reliable Systems* (BSRS) บทที่ 9, 14, 15, 16 และใน Workbook บทที่ 7
3. **หนังสือไม่พูดถึง OS ของเครื่องที่วิศวกรใช้ทำงาน และไม่พูดถึงฮาร์ดแวร์สำหรับฝึกเอง** ส่วนนี้ต้องหาแหล่งอื่น หรือเขียนเป็น `type: assumption`

## Tier 1: อ่านละเอียด (4 บท)

| บท | ส่วนที่อ่าน | ใช้กับหัวข้อ |
|---|---|---|
| SRE บทที่ 2 Production Environment | ทั้งบท (~3.4k คำ) | 04, 05, 06 |
| BSRS บทที่ 9 Design for Recovery | "Know Your Intended State": Host management, Device firmware และ "Rolling back firmware" | 04, 05 (Linux distribution ภายในของ Google, BIOS/NIC firmware, CPU แบบ Arm และ x86, UEFI) |
| BSRS บทที่ 16 Disaster Planning | "Google Examples" (ช่องโหว่ Linux kernel ปี 2018) | 04 (ประโยคที่ดีที่สุดที่ยืนยันว่า Linux kernel เป็นฐานของ production, ksplice, การ rollout kernel ทั้ง fleet) |
| Workbook บทที่ 12 NALSD | One Machine, Multidatacenter | 05, 06 (คำนวณ CPU, RAM, จำนวน disk และ bandwidth แบบมีตัวเลข) |

## Tier 2: อ่านเฉพาะส่วน แยกตามหัวข้อ

**04 Operating systems**
- BSRS บทที่ 15: ตัวอย่างดีบัก dentry cache ของ kernel ใน container และส่วน "Operating system logs" / "Host agents"
- BSRS บทที่ 8: "Google App Engine Analysis" (attack surface ของ Linux kernel, ptrace sandbox)
- BSRS บทที่ 14: Borg alloc ซึ่งคือ Linux process ที่รันใน container
- Workbook บทที่ 7 Simplicity: Borg รัน Linux container จำนวนมหาศาล
- SRE บทที่ 22: "Resource Exhaustion" (CPU, memory, threads, file descriptors)
- SRE บทที่ 7 และ 13: reboot เพื่อ upgrade kernel, เหตุการณ์ Diskerase (BIOS, TFTP, ติดตั้ง kernel ใหม่)

**05 Hardware requirements**
- Workbook บทที่ 6: Case Study 1 "Reducing Toil in the Datacenter"
- Workbook บทที่ 10: satellite racks ใน colo (edge)
- SRE บทที่ 20: "Machine diversity"
- SRE บทที่ 23: failure domains (เครื่อง, rack, power supply)

**06 System architecture**
- SRE บทที่ 19–20: load balancing ทั้งฝั่ง frontend และใน datacenter
- Workbook บทที่ 11: GCLB, Anycast, Maglev, autoscaling
- SRE บทที่ 23: Paxos และ Chubby
- SRE บทที่ 26 Data Integrity: backup เทียบกับ archive, replication, GTape (ครอบคลุม backup และ DR)
- BSRS บทที่ 8: "Controlling the Blast Radius"
- Workbook บทที่ 9: case study ของ GKE

**ข้ามได้ เพราะเป็นของเพื่อน:** SLO (SRE บทที่ 3–4), on-call และ postmortem (03, 09), release และ canary (08), monitoring (09), management (Part IV)

## แหล่งเสริมเพื่อปิดช่องที่หนังสือไม่มี

- **04:** Borg paper (EuroSys 2015, research.google) อธิบายว่า Borg ใช้ container บน Linux, บล็อกของ Google เรื่อง gLinux (OS ของเครื่องวิศวกร), ประกาศงาน SRE ของ Google ที่ขอความรู้ Linux
- **05:** *The Datacenter as a Computer* ซึ่ง SRE บทที่ 2 อ้างไว้เป็น [Bar13], เอกสาร machine families ของ Google Cloud (x86 และ Arm), Google infrastructure security overview (ชิป Titan, secure boot)
- **06:** บทความ "Borg, Omega, and Kubernetes" (ACM Queue 2016) ส่วน paper ของ Maglev และ Jupiter ใช้ถ้าเหลือเวลา

หมายเหตุ: หนังสือพิมพ์ปี 2016–2020 claim จากหนังสือให้เขียนว่า "ตามที่หนังสือบรรยายไว้ ณ ปีที่พิมพ์" claim ที่เกี่ยวกับ Google ต้องเป็น `org-fact` และมี archive link

## การจัดเนื้อหาในรายงาน (ประมาณ 3 หน้า)

ประเมินว่าได้ประมาณนี้ เพราะ appendix ที่เก็บ prompt ก็นับรวมใน 15 หน้า

| หัวข้อในรายงาน | หน้า | เนื้อหาหลัก |
|---|---|---|
| §6 OS (04) | ~1 | ① server ใช้ Linux พร้อมหลักฐาน ② Borg เป็น "cluster OS" ที่วางอยู่บน Linux ของแต่ละเครื่อง ซึ่งเชื่อมกับวิชา OS ได้ดี ③ วิธีดูแล: rollout kernel, live patch, จัดการ firmware, sandbox ④ OS ของเครื่องทำงานเทียบกับ server ⑤ distro ที่แนะนำให้ฝึก (assumption) |
| §7 Hardware (05) | ~0.75 | ① เครื่องที่เหมือนกันทั้ง fleet, rack, cluster, datacenter ② ฮาร์ดแวร์เสียเป็นเรื่องปกติ เลยต้อง automation ③ storage (HDD เทียบ flash, IOPS) และ network (Jupiter, B4, edge) ④ firmware และสถาปัตยกรรม CPU ⑤ ฮาร์ดแวร์สำหรับฝึกเอง (assumption) |
| §8 Architecture (06) | ~1.25 + diagram | จับคู่รายการใน Appendix E ของโจทย์กับตัวอย่างของ Google: request เดินทางผ่าน GSLB → GFE → frontend → backend → Bigtable, load balancing, Borg และ Kubernetes, VM, Chubby/Spanner/Colossus, backup และ DR, failure domain |

## เส้นแบ่งกับเพื่อน (ควรคุยตกลงกันก่อน)

- **11 (@TonCS05):** หัวข้อ 04 ตอบว่าใช้ OS อะไร ทำไม และ config อย่างไร ส่วน 11 เอาเรื่องนั้นไปโยงกับแนวคิด OS ในวิชา ข้อมูลจาก SRE บทที่ 22 ส่งให้ 11 ใช้ต่อได้
- **12 (@Bximai):** 12 ก็มี "Computing infrastructure" ใน scope เสนอว่ารายละเอียดเชิงเทคนิค (Borg, Colossus, Jupiter) อยู่ที่ 06 แล้วให้ 12 ลิงก์มา
- **08, 09, 10:** หัวข้อ 06 อธิบาย Kubernetes, Borgmon และ Bigtable แค่ในระดับ architecture รายละเอียดของเครื่องมือเป็นของเพื่อน

## ลำดับงาน

1. อ่าน Tier 1 แล้วเขียน claim ของ 04 ก่อน เพราะหลักฐานแน่นที่สุด ตามด้วย 05 แล้วจึง 06 แต่ละหัวข้อแยก branch และ PR
2. ถ้าจะใช้ NotebookLM เป็น GenAI ตัวที่สอง ให้ใส่ Tier 1 เป็น source ซึ่งตรงกับที่โจทย์แนะนำไว้ ทุกครั้งต้องบันทึก prompt ลง `prompts/`
3. เป้าคือ PR ทั้ง 3 ผ่านการ review ก่อนเหลือเวลาประมาณ 3–4 วันก่อน deadline 18 ต.ค. เพื่อให้มีเวลา draft รายงาน

ถ้าโอเค บอกได้ครับว่าอยากให้เริ่ม 04 เลย หรือให้บันทึกแผนนี้ลงไฟล์ก่อน

---
เรื่องอื่นสองข้อ: ปลั๊กอิน Figma ต้องกดอนุญาตผ่าน `/mcp` ก่อนถึงจะใช้ได้ (งานนี้ไม่ได้ใช้) และ caveman statusline ยังไม่ได้ตั้งค่า ถ้าอยากเปิดผมเพิ่มให้ใน settings ได้

## Turn 2 — user
writing clam 04 05 06 in 2 languages, Thai and English, separate file
Don't push Thai language file to git hub
But now don't push anything

## Turn 2 — assistant
Main had 4 new commits (new rules, scripts, teammate's 07 claims). Switched to main, pulled. Reading updated rules + research skill before writing claims.

Mining exact sentences from the books for 04 now. 05/06 next, then add claims through `add_claim.py` (it checks each quote live + finds archive snapshot).

Still collecting exact source sentences (load balancing, storage, backup now). Then claims get added through the repo script.

Spec of 67 claims written. Now verifying every quote verbatim against local page text + word count before touching repo.

All 15 source pages have a Wayback snapshot holding every quote. Now adding the 70 claims via `scripts/add_claim.py` (live re-check of each quote), 3 topics in parallel.

Claims going in steadily (04 at 04-15, no failures now). While it runs I'll draft the Thai companion files.

All 70 claims added (0 failures). Now verifying IDs match plan, then writing note summaries + index, lint.

Now updating the storage note text for 06-25, adding "Not found yet" sections to the three index files, then lint.

Lint passes (0 errors; the 6 warnings are a teammate's topic 07 files). `.local/` confirmed git-ignored. Writing Thai files for 05 and 06.

ผมเขียน claim ของหัวข้อ 04, 05, 06 เสร็จแล้วครับ มีทั้งฉบับภาษาอังกฤษและภาษาไทยแยกไฟล์กัน ยังไม่ได้ commit และไม่ได้ push อะไรเลย ไฟล์ภาษาไทยอยู่ใน `.local/th/` ซึ่ง repo ตั้ง ignore ไว้แล้ว เลยจะไม่ถูก push ขึ้น GitHub แน่นอน

## ผลลัพธ์

ได้ทั้งหมด 71 claims ทุกตัวสถานะ `unverified` lint ผ่านโดยไม่มี error (warning 6 ตัวมาจากไฟล์หัวข้อ 07 ของเพื่อน)

| หัวข้อ | Claims | ไฟล์ภาษาอังกฤษ |
|---|---|---|
| 04 OS | 25 (04-01 ถึง 04-25) | [linux-in-google-production](knowledge-base/04-operating-systems/linux-in-google-production.md), [kernel-updates-and-os-logs](knowledge-base/04-operating-systems/kernel-updates-and-os-logs.md), [isolation-and-resource-limits](knowledge-base/04-operating-systems/isolation-and-resource-limits.md), [workstations-and-servers](knowledge-base/04-operating-systems/workstations-and-servers.md) |
| 05 Hardware | 21 (05-01 ถึง 05-21) | [datacenter-hardware](knowledge-base/05-hardware-requirements/datacenter-hardware.md), [firmware-and-cpu-platforms](knowledge-base/05-hardware-requirements/firmware-and-cpu-platforms.md), [sizing-and-practice-hardware](knowledge-base/05-hardware-requirements/sizing-and-practice-hardware.md) |
| 06 Architecture | 25 (06-01 ถึง 06-25) | [request-path-and-load-balancing](knowledge-base/06-system-architecture-infrastructure/request-path-and-load-balancing.md), [cluster-management-containers-vms](knowledge-base/06-system-architecture-infrastructure/cluster-management-containers-vms.md), [storage-consensus-and-recovery](knowledge-base/06-system-architecture-infrastructure/storage-consensus-and-recovery.md) |

- **ฉบับภาษาไทย:** มี 10 ไฟล์ จับคู่กับฉบับอังกฤษครบทุก ID ดูสารบัญได้ที่ [.local/th/README.md](.local/th/README.md) ฉบับไทยไม่ได้ใส่ quote ซ้ำ หลักฐานอยู่ในไฟล์ภาษาอังกฤษ
- **วิธีเพิ่ม claim:** ทุกตัวเพิ่มผ่าน `scripts/add_claim.py` ซึ่งเช็คว่า quote ตรงกับหน้าเว็บคำต่อคำ claim ที่เกี่ยวกับ Google มีลิงก์ Wayback ที่มี quote นั้นอยู่จริงทุกตัว
- **index.md ทั้ง 3 หัวข้อ:** อัปเดตรายการ note แล้ว และเพิ่มส่วน "Not found yet" สำหรับสิ่งที่หนังสือไม่ได้บอก
- **ใช้แค่หนังสือ 3 เล่มบน sre.google/books** เหมือนรอบแรกของเพื่อนหัวข้อ 07

## เรื่องที่ควรรู้

- **ผมเปลี่ยน branch แล้ว:** branch เดิมถูก merge ไปแล้ว และ main มี commit ใหม่ 4 ตัว (กฎใหม่, scripts, `.local/`) ผมเลย pull main แล้วสร้าง branch `04-operating-systems/sre-books-claims` ไฟล์ของ 05 และ 06 อยู่ใน working tree เดียวกัน ตอน commit ต้องแยกไปไว้คนละ branch และคนละ PR
- **quote สั้นกว่า 15 คำ และหลายตัวเป็นแค่ท่อนหนึ่งของประโยค:** ผมตั้งใจทำแบบนี้เพราะเรื่องลิขสิทธิ์ แต่กฎใน AGENTS.md เขียนว่า "a sentence copied verbatim" reviewer อาจทักได้
- **หนังสือสองบทขัดกันเอง:** SRE book บทที่ 2 บอกว่า hardware ใน datacenter เหมือนกันหมด (05-02) แต่บทที่ 20 บอกว่าไม่จำเป็นต้องเหมือนกัน (05-03) ในรายงานไม่ควรเขียนว่าทุกเครื่องเหมือนกัน
- **หนังสือไม่ได้บอกเรื่องเหล่านี้:**
  - workstation ของวิศวกร Google ใช้ OS อะไร
  - ชื่อ distro ภายใน และ kernel feature ที่ Borg ใช้ทำ container เช่น cgroups
  - GPU/TPU
  - hypervisor ที่ Google ใช้

  ส่วนนี้ต้องหาแหล่งอื่นในรอบหน้า ตอนนี้มี assumption ที่เขียนเป็นข้อแนะนำไว้ 2 ตัว คือ 04-25 และ 05-21
- **ยังไม่ได้ทำ prompt log:** `scripts/make_prompt_log.py` ต้องใช้ transcript ของ session นี้ที่รวมคำตอบนี้แล้ว จึงต้องทำหลังจบ turn นี้ log จะมีข้อความภาษาไทยของ prompt อยู่ตามจริง เพราะกฎห้ามแก้คำ

## ขั้นต่อไป เลือกได้

1. รัน blind author check (skill `agent-fact-check`) จะใช้ subagent 10 ตัว ตัวละ note ถ้าผ่านสถานะจะเป็น `ai-checked`
2. สร้าง prompt log ของ session นี้
3. commit แยก 3 branch แต่จะยังไม่ push จนกว่าจะสั่ง

## Turn 3 — user
04 Are there any points where the information is unclear and requires external research?

## Turn 3 — assistant
Checking candidate outside sources. Borg paper PDF downloaded but no PDF reader here, trying quick text extraction.

มีครับ หัวข้อ 04 มีจุดที่ข้อมูลไม่ชัดอยู่ 2 แบบ แบบแรกคือ claim ที่เขียนไปแล้วแต่อ่านแล้วเข้าใจผิดได้ แบบที่สองคือ scope ที่หนังสือไม่ได้พูดถึงเลย ผมยังไม่ได้แก้ไฟล์อะไร แหล่งภายนอกด้านล่างผมเปิดดูแล้วว่ามีอยู่จริง แต่ยังไม่ได้ทำเป็น claim

## A. claim ที่มีอยู่แล้วแต่ยังไม่ชัด

| Claim | ปัญหา | ควรทำอะไร |
|---|---|---|
| 04-01 | ต้นฉบับเขียนว่า "much of" production คือส่วนใหญ่ ไม่ใช่ทั้งหมด และไม่บอกว่าส่วนที่เหลือรันอะไร หน้าเว็บ BSRS ก็ไม่มีวันที่ | ในรายงานใช้คำว่า "ส่วนใหญ่" ห้ามเขียนว่า "ทั้งหมด" |
| 04-02 ถึง 04-04 | ไม่มีชื่อ distro และต้นฉบับใช้คำว่า "until recently" โดยไม่บอกว่าเมื่อไร | ใช้ paper LISA'13 ด้านล่างเพื่อเติมไทม์ไลน์ |
| 04-05 | "cluster operating system" เป็นคำเปรียบเทียบ Borg ไม่ใช่ kernel แต่ทำงานอยู่บน Linux ของแต่ละเครื่อง | ในรายงานต้องแยก OS ของเครื่องกับ cluster OS ให้ชัด |
| 04-06, 04-07 | บอกแค่ "Linux containers" ไม่บอกว่าใช้ kernel feature ตัวไหน | ต้องใช้ Borg paper |
| 04-08 | นิยาม node ว่าเป็น "running kernel ... or container" แต่ในทางวิชา OS container ใช้ kernel ร่วมกับ host ซึ่งตรงกับ 04-21 | ใช้คำนิยามนี้อย่างระวัง และแจ้งเจ้าของหัวข้อ 11 |
| 04-11, 04-12 | "ksplice" อาจหมายถึงผลิตภัณฑ์ Ksplice ของ Oracle หรือคำทั่วไปก็ได้ หนังสือไม่บอก | ห้ามเขียนว่า Google ใช้ Oracle Ksplice |
| 04-11 กับ 04-13 | ดูเหมือนขัดกัน แต่จริงๆ ใช้คู่กัน: live patch ใช้แก้บางเคส ส่วนการ upgrade kernel ปกติยังต้อง reboot | อธิบายในรายงานว่าใช้ร่วมกัน |
| 04-14 | เป็นข้อความทั่วไป ไม่ได้บอกว่า Google ใช้ syslog หรือ auditd | ห้ามเขียนว่า Google ใช้สองตัวนี้ |
| 04-15 | "เกิน limit แล้วโดน kill" น่าจะเป็นคำอธิบายแบบย่อ | ต้องเปิด Borg paper ดูว่าแยก CPU (throttle) กับ memory (kill) หรือเปล่า ตรงนี้ผมยังไม่ได้ยืนยัน |
| 04-16 | ปกติ OOM killer จะ kill แค่ process เดียว การ kill ทุก process ตรงกับ `memory.oom.group` ของ cgroup v2 (ยืนยันจาก docs.kernel.org แล้ว) | BSRS ไม่ได้บอกกลไก จึงอ้าง kernel docs ได้เป็น fact ทั่วไปเท่านั้น ห้ามเขียนเป็นข้อเท็จจริงของ Google |
| 04-19, 04-20 | sandbox ของ App Engine (NaCl + ptrace) เป็นเรื่องเก่า ตอนนี้ Google มี gVisor | ดูแหล่ง gVisor ด้านล่าง |
| ทั้งหัวข้อ | หนังสือพิมพ์ปี 2016–2020 ไม่มีหลักฐานว่าตอนนี้ยังเป็นอย่างนั้นอยู่ | ใช้ประกาศงาน (topic 01/02) ยืนยันว่าตอนนี้ยังต้องใช้ทักษะ Linux |

## B. scope ที่หนังสือไม่มี และแหล่งที่เช็คแล้วว่ามีจริง

1. **workstation ใช้ OS อะไร:** Google Cloud Blog "How Google got to rolling Linux releases for Desktops" (13 ก.ค. 2022)
   - gLinux Rodete เป็น Debian testing แบบ rolling release มาแทน Goobuntu ที่ใช้ฐาน Ubuntu LTS
   - fleet มี "hundreds of thousands of devices"
   - ใช้ยกระดับ 04-25 จาก assumption เป็น org-fact ได้บางส่วน
   - ยังไม่ชัดว่าวิศวกรทุกคนใช้ Linux หรือมี Mac/ChromeOS ด้วย
2. **ประวัติ distro ของ production:** USENIX LISA '13 โดย Marc Merlin (Google)
   - อัปเกรดแบบ live จาก image ที่ใช้ Red Hat 7.1 ไปเป็น distro ที่สร้างจาก Debian testing
   - เป็น paper ของ USENIX ไม่ใช่หน้าเว็บของ Google เอง ทีมต้องตัดสินใจว่ายอมรับเป็นหลักฐานสำหรับ org-fact หรือไม่
3. **kernel feature ที่ใช้ทำ container:** Borg paper (EuroSys 2015, research.google)
   - คาดว่ามีเรื่อง cgroups, chroot และ compressible resource แต่ผมยังไม่ได้ยืนยัน
   - เครื่องนี้ไม่มีโปรแกรมแปลง PDF เป็นข้อความ ผมเลยอ่าน PDF ไม่ได้ ส่วน abstract บอกแค่ "process-level performance isolation"
   - ถ้าจะให้ผมอ่านเอง ต้องติดตั้ง `brew install poppler` ก่อน (คุณต้องติดตั้งเอง) หรือคุณเปิดอ่านเองก็ได้
4. **ฝั่ง Google Cloud:** Container-Optimized OS เป็น image ที่ Google ดูแล สร้างบน Chromium OS และเป็น node OS ค่าเริ่มต้นของ GKE (เช็คแล้ว)
5. **sandbox สมัยใหม่:** gvisor.dev
   - gVisor เป็น application kernel เขียนด้วย Go รันใน userspace
   - หน้าเว็บมี badge "Powered by gVisor" ที่ลิงก์ไป Cloud Run แต่ไม่ได้พูดถึง App Engine
6. **เหตุผลที่เลือก Linux:** ไม่มีแหล่งไหนบอกตรงๆ ใช้ได้แค่ประกาศงาน (ประสานกับเจ้าของ topic 01/02) หรือเขียนเป็น assumption พร้อมเหตุผล
7. **การ config OS** เช่น sysctl, ulimit, pid_max: หนังสือไม่มี ใช้ docs ของ kernel.org และ man pages ได้ แต่จะเป็น fact ทั่วไป ไม่ใช่เรื่องของ Google

## ลำดับที่แนะนำสำหรับรอบ 2

ข้อ 1 (workstation) → ข้อ 3 (Borg paper) → ข้อ 2 → ข้อ 5 → ข้อ 4 → kernel docs สำหรับ 04-16

ถ้าเริ่มรอบ 2 ผมจะเพิ่ม claim ใหม่ผ่าน `add_claim.py` และอัปเดตไฟล์ภาษาไทยไปพร้อมกัน

## Turn 4 — user
Have you already looked for the additional information in the documents?

## Turn 4 — assistant
ทำไปแล้วบางส่วนครับ แยกเป็นในหนังสือ 3 เล่ม กับแหล่งภายนอก

## 1. ในหนังสือ 3 เล่ม: ค้นครบแล้ว

ผมค้นทั้ง 79 หน้า (SRE book, Workbook, BSRS) สองรอบ รอบแรกค้นตอนเขียน claim รอบสองเพิ่งค้นเพิ่มเมื่อกี้ด้วยคำที่ตรงกับจุดที่ยังไม่ชัด

**ไม่มีในหนังสือเลย:**
- ชื่อ distro ของ production (ไม่มีคำว่า Ubuntu, Red Hat, gLinux, Goobuntu)
- cgroups และ namespaces
- การแยก CPU กับ memory แบบ compressible/non-compressible ของ Borg
- systemd และ journald
- Oracle Ksplice
- gVisor และ Container-Optimized OS
- hypervisor
- OS ของ workstation

แปลว่าจุดที่ไม่ชัดในรอบที่แล้ว ปิดด้วยหนังสือ 3 เล่มไม่ได้แล้ว ต้องใช้แหล่งภายนอกเท่านั้น

**เจอเพิ่มเล็กน้อย แต่ยังไม่ได้ทำเป็น claim:**
- BSRS ch.15 บอกว่า Google เจอ OOM เยอะทุกวัน และมี OOM metric ของ Borg task ใช้เสริม 04-16 ได้
- BSRS ch.8 บอกว่า Python runtime ของ App Engine ถูก compile เป็น Native Client (NaCl) ใช้เสริม 04-19 และ 04-20 ได้
- BSRS ch.9 บอกว่า hook ของระบบ package (`post_install` กับ `pre_rm`) ยืมแนวคิดมาจาก Debian เป็นแค่เบาะแส ไม่ได้บอกว่า distro ของ Google ใช้ฐาน Debian

## 2. แหล่งภายนอก: แค่เช็คว่ามีอยู่จริง ยังไม่ได้ค้นจริง

- ผมเปิดหน้าเว็บผ่าน WebFetch ซึ่งได้แค่บทสรุปที่ model ตัวเล็กเขียนให้ ไม่ใช่ข้อความต้นฉบับ จึงยังใช้เป็น quote ไม่ได้
- ยังไม่ได้ส่งผ่าน `add_claim.py` ยังไม่มี claim และยังไม่มีลิงก์ archive
- Borg paper อ่านไม่ได้ เพราะเครื่องนี้ไม่มีโปรแกรมแปลง PDF เป็นข้อความ เรื่อง cgroups, chroot และ compressible resource จึงยังไม่ได้ยืนยัน
- รายละเอียดอย่าง "gLinux เป็น Debian testing แบบ rolling release" หรือ "LISA'13 อัปเกรดจาก Red Hat 7.1" ตอนนี้ยังเป็นแค่ข้อมูลเบื้องต้น ห้ามใช้ในรายงานจนกว่าจะเช็ค quote

## ถ้าจะทำต่อ (รอบ 2 ของหัวข้อ 04)

1. เพิ่ม claim จาก 3 ข้อที่เจอเพิ่มในหนังสือ
2. ทำ claim จากแหล่งภายนอก โดยเลือกประโยคจากหน้าจริงและให้ script เช็ค quote และ archive ได้แก่ gLinux blog, LISA'13, gVisor, Container-Optimized OS docs และ kernel docs (`memory.oom.group`)
3. Borg paper: คุณติดตั้ง `brew install poppler` ให้ผมอ่าน PDF ได้ หรือเปิดอ่านเองแล้วส่งข้อความมาก็ได้
4. อัปเดตไฟล์ภาษาไทยตาม

จะให้เริ่มเลยไหมครับ

## Turn 5 — user
Discard the Thai-language files and continue the research; all information used for the write-up must be clear and factually verifiable.
[Request interrupted by user]
Discard the Thai-language files and continue the research; all information used for the write-up must be clear and factually verifiable.

## Turn 5 — assistant
Moving Thai files to Trash (recoverable, not hard-deleted), then round 2 research for 04.

Round-2 spec ready (30 new claims for 04: gLinux, LISA'13, Google container pages, kernel docs, gVisor, GKE Sandbox, COS). Checking quotes locally first.

Wayback lookup slow (4 of 8 sources done). Waiting on GKE, COS, gLinux, BSRS ch.8 snapshots.

Wayback slow. Waiting on 4 sources (BSRS ch.8, GKE Sandbox, gLinux blog, COS docs); will continue as soon as monitor reports.

Still waiting on 3 sources (GKE Sandbox, gLinux blog, COS docs) to finish the Wayback check.

All 8 sources now have snapshots holding quotes (GKE quotes swapped to wording present in both live page and archive). Adding 30 round-2 claims now.

Round-2 claims are being added. The Wayback archive is slow, so it is retrying fetches with backoff. I'll get a notification when it finishes or if it fails.

All 30 added. Verifying IDs, then updating summaries, 04-25 assumption, index, lint.

ผมย้ายไฟล์ภาษาไทยไปไว้ในถังขยะแล้ว และทำ research รอบสองของหัวข้อ 04 เสร็จแล้วครับ ยังไม่ได้ commit หรือ push

ไฟล์ภาษาไทยอยู่ใน `~/.Trash/th-claims-04-06-…` ยังกู้คืนได้ ถ้าจะลบถาวรให้กดล้างถังขยะเองนะครับ

## ผลลัพธ์

ตอนนี้หัวข้อ 04 มี 55 claims (เพิ่มขึ้น 30 ตัวจากรอบนี้) แบ่งเป็น 5 note รวม [google-cloud-container-os.md](knowledge-base/04-operating-systems/google-cloud-container-os.md) ที่สร้างใหม่

- **ตรวจซ้ำแล้ว:** quote ทั้ง 54 ตัว (ทุกตัวยกเว้น assumption 04-25) เจอคำต่อคำในหน้าเว็บจริงวันนี้ จาก 20 หน้า
- **ลิงก์ archive:** claim ที่เกี่ยวกับ Google ทั้ง 41 ตัวมีลิงก์ Wayback ที่มี quote นั้นอยู่จริง
- **lint:** ผ่าน ไม่มี error

## จุดที่เคยไม่ชัด และตอนนี้มีหลักฐานแล้ว

| จุดที่ไม่ชัด | ตอนนี้ได้คำตอบว่า | Claims |
|---|---|---|
| workstation ใช้ OS อะไร | Google มี OS ให้เลือกหลายแบบ หนึ่งในนั้นคือ Linux ชื่อ gLinux Rodete ซึ่งเป็น Debian testing แบบ rolling (เดิมชื่อ Goobuntu ใช้ฐาน Ubuntu LTS) ย้ายเสร็จปี 2018 และเลือก Debian เพราะย้ายระบบแบบ in-place ได้ราบรื่น | 04-44 ถึง 04-51 |
| ประวัติ distro ฝั่ง server | ปี 2013 อัปเกรดแบบ live จาก image ที่ใช้ Red Hat 7.1 ไปเป็น distro ที่ใช้ฐาน Debian Testing และ build จาก source โดยแยก partition ของ application ออกจาก OS | 04-26 ถึง 04-29 |
| container กับ cgroups | ทุกอย่างใน Google รันใน container มาตั้งแต่ต้นยุค 2000 และ Google เป็นผู้ contribute cgroups ให้ Linux kernel | 04-30 ถึง 04-32 |
| นิยาม "node" ใน 04-08 ที่ขัดกับวิชา OS | container ใช้ OS kernel ร่วมกับ host ใน note มีคำแนะนำว่าในรายงานควรนิยาม node อย่างไร | 04-33 |
| kill ทุก process ใน container (04-16) | กลไกของ Linux คือ `memory.max` ที่เรียก OOM killer และ `memory.oom.group` ที่ kill ทั้งกลุ่ม ส่วน Google เจอ OOM ทุกวัน | 04-35 ถึง 04-37 |
| ksplice | อธิบายด้วยเอกสาร livepatch ของ kernel ได้ แต่ห้ามบอกว่าเป็นผลิตภัณฑ์ Oracle Ksplice | 04-43 |
| sandbox ปัจจุบัน | GKE Sandbox ใช้ gVisor ซึ่งเขียน Linux kernel API ใหม่ให้รันใน userspace ส่วน App Engine เดิมใช้ NaCl ร่วมกับ ptrace | 04-38 ถึง 04-42 |
| ฝั่ง Google Cloud | Container-Optimized OS: Google ดูแล, ใช้ฐาน Chromium OS, เป็น OS เริ่มต้นของ node ใน GKE, อัปเดตทุกสัปดาห์, kernel ถูกล็อก | 04-52 ถึง 04-55 |

ทุก note มีส่วน "Notes for the write-up" บอกว่าข้อมูลไหนห้ามเขียนในรายงาน เช่น
- ห้ามเขียนว่า Borg ใช้ cgroups เพราะไม่มีแหล่งไหนเชื่อมสองเรื่องนี้เข้าหากัน
- gLinux เป็น distro ของ desktop ไม่ใช่ของ server
- ห้ามเขียนว่าวิศวกร Google ทุกคนใช้ Linux

## ยังไม่มีหลักฐาน (ห้ามใช้เป็น fact)

รายการนี้อยู่ในส่วน "Not found yet" ของ [index.md](knowledge-base/04-operating-systems/index.md)

- SRE ใช้ OS อะไรบน workstation ของตัวเอง ตอนนี้ 04-25 ยังเป็น assumption แต่ปรับข้อความตามหลักฐานใหม่แล้ว
- ชื่อและเวอร์ชันของ distro ฝั่ง server ในปัจจุบัน
- Borg ใช้ kernel feature ตัวไหน
  - Borg paper เป็นไฟล์ PDF ที่ script ตรวจ quote อ่านไม่ได้
  - บทความ ACM Queue ปฏิเสธการเข้าถึงจาก script (HTTP 403)
- เหตุผลที่ Google เลือก Linux สำหรับ server
- ตอนนี้ App Engine ใช้ gVisor หรือไม่

## ต้องให้ทีมตัดสินใจ

paper USENIX LISA '13 (04-26 ถึง 04-29) เขียนโดยวิศวกรของ Google แต่ไม่ได้เผยแพร่บนเว็บของ Google เอง ทีมต้องตกลงกันว่าจะรับเป็นหลักฐานสำหรับ org-fact หรือไม่

## สถานะ

ทุก claim ยังเป็น `unverified` ขั้นต่อไปคือ blind author check และยังไม่ได้ทำ prompt log หัวข้อ 05 และ 06 ยังเป็นข้อมูลจากรอบแรกอยู่ ถ้าอยากให้ทำรอบสองแบบเดียวกันบอกได้เลยครับ

You've hit your session limit · resets 11:30pm (Asia/Bangkok)

## Turn 6 — user
I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.

## Turn 6 — assistant
20 new claims specced (05: custom servers, Titan, Axion/x86 CPUs, TPU/GPU, practice minimums; 06: GFE, Maglev, KVM hypervisor; 04: Google's own gVisor use). Checking quotes, then Wayback.

3 of 7 snapshots found (security overview, data center site, CPU platforms). Waiting on TPU, GPU, load balancer docs, KVM blog.

TPU snapshot found (4 of 7). Waiting on GPU, load balancer docs, KVM blog.

GPU snapshot found (5 of 7). Waiting on the load balancer docs and KVM blog.

6 of 7 sources have snapshots. Next: the network load balancer docs and the KVM blog post.

Network LB page has no archive holding the Maglev sentence, so I'm dropping that one claim. Maglev is already covered by 06-07 from the Workbook. Fixing IDs in the text, then adding claims.

Adding the 19 claims now. The monitor will report when it finishes, and after that I'll apply the summaries, index updates and lint.

ทำต่อจนเสร็จแล้วครับ ตอนที่ติดลิมิต หัวข้อ 04 รอบสองเสร็จไปแล้ว ผมเลยทำหัวข้อ 05 และ 06 ต่อด้วยมาตรฐานเดียวกัน และเพิ่ม claim ให้ 04 อีก 2 ตัว ยังไม่ได้ commit หรือ push

## ภาพรวม

| หัวข้อ | Claims | เพิ่มในรอบนี้ |
|---|---|---|
| 04 OS | 57 | 2 |
| 05 Hardware | 35 | 14 (มี note ใหม่ [google-cloud-instance-hardware.md](knowledge-base/05-hardware-requirements/google-cloud-instance-hardware.md)) |
| 06 Architecture | 28 | 3 |

เช็คซ้ำครบแล้วทั้งสามหัวข้อ:
- quote ทุกตัวเจอคำต่อคำในหน้าเว็บจริงวันนี้ (38 หน้า)
- claim ที่เกี่ยวกับ Google ทุกตัวมีลิงก์ Wayback ที่มี quote นั้นอยู่จริง
- เลข claim ที่อ้างถึงในเนื้อหา note มีอยู่จริงทุกตัว
- lint ผ่าน ไม่มี error

## จุดที่เคยไม่ชัด และตอนนี้มีหลักฐานแล้ว

**05 Hardware**
- **hardware ของ Google:** Google ออกแบบ server board และอุปกรณ์เครือข่ายเอง และประกอบ server เองสำหรับ data center ของตัวเองโดยเฉพาะ (05-22, 05-23)
- **ชิปความปลอดภัย:** Google ออกแบบชิป Titan ใช้เป็น hardware root of trust และ server ตรวจว่า boot ชุด software ที่ตั้งใจไว้จริง (05-24 ถึง 05-26)
- **CPU บน Google Cloud:**
  - มี Google Axion ซึ่งเป็น CPU แบบ Arm
  - บน x86 ส่วนใหญ่ 1 vCPU เท่ากับ 1 hardware thread แต่บน Arm 1 vCPU เท่ากับ 1 physical core
  - ใช้คำสั่ง `lscpu` ใน guest OS ดูได้ว่าเครื่องรันบน CPU แบบไหน
  - (05-27 ถึง 05-31)
- **TPU และ GPU:** TPU เป็น ASIC ที่ Google ออกแบบเอง และมี NVIDIA GPU ให้ใช้ (05-32, 05-33)
- **hardware สำหรับฝึก:** มีตัวเลขขั้นต่ำที่ตรวจสอบได้แล้ว
  - Debian แบบไม่มี desktop แนะนำ RAM 1GB และดิสก์ 4GB (05-34)
  - minikube ต้องใช้ 2 CPU, RAM ว่าง 2GB และดิสก์ว่าง 20GB (05-35)
  - assumption 05-21 จึงปรับเป็น "RAM ประมาณ 8 GB พอ ถ้า 16 GB รันได้ทั้งสองอย่างพร้อมกัน" และระบุชัดว่าเป็นตัวเลขที่ผมประเมินเอง

**06 Architecture**
- **hypervisor:** Google Cloud ใช้ KVM ที่ Google ปรับให้แน่นหนาขึ้น และเขียน VMM ของตัวเองแทน QEMU ข้อมูลนี้มาจากโพสต์ปี 2017 จึงต้องเขียนในรายงานว่า "ณ ปี 2017" (06-27, 06-28)
- **GFE:** เอกสารปัจจุบันยืนยันว่า Application Load Balancer ยังใช้ GFE อยู่ (06-26)

**04 OS**
- Google ระบุว่า infrastructure ของตัวเองใช้ Linux user separation และ application kernel อย่าง gVisor แยก service ที่อยู่บนเครื่องเดียวกัน (04-56, 04-57)

## สิ่งที่ตัดออก และสิ่งที่ยังหาไม่เจอ

- **ตัดออก:** claim ที่ยืนยันว่าเอกสารปัจจุบันยังใช้ Maglev หน้าเอกสาร Network Load Balancer ยังไม่มี snapshot บน Wayback ที่มีประโยคนี้ เรื่อง Maglev ยังมี 06-07 จาก Workbook อยู่ ถ้าอยากให้ขอ snapshot ใหม่บน Wayback ต้องให้คุณอนุญาตก่อน
- **ยังหาไม่เจอ (อยู่ใน "Not found yet" ของแต่ละ index):**
  - CPU, RAM และดิสก์ของเครื่อง production ภายใน Google (เอกสาร Cloud พูดถึงแค่เครื่องที่ลูกค้าเช่า)
  - hardware ในแต่ละ datacenter เหมือนกันหมดหรือไม่ (05-02 กับ 05-03 ยังขัดกัน)
  - hardware ของ workstation วิศวกร
  - hypervisor ที่ใช้ในปัจจุบัน
  - IoT และ edge computing

## ขั้นต่อไป

ทุก claim ยังเป็น `unverified` ขั้นต่อไปคือ blind author check และสร้าง prompt log ส่วน paper LISA '13 ยังต้องให้ทีมตัดสินว่าจะรับเป็นหลักฐานหรือไม่

## Tool-call ledger
- Bash List repo layout and topic index files
- ToolSearch select:WebFetch
- Bash Read assignment summary and relevant topic index files
- WebFetch https://sre.google/books/
- WebFetch https://sre.google/sre-book/table-of-contents/
- WebFetch https://sre.google/workbook/table-of-contents/
- WebFetch https://google.github.io/building-secure-and-reliable-systems/raw/toc.html
- WebFetch https://sre.google/sre-book/production-environment/
- WebFetch https://sre.google/sre-book/addressing-cascading-failures/
- WebFetch https://sre.google/workbook/non-abstract-design/
- Bash Download all three SRE book chapters into scratchpad for keyword scan
- Bash Count OS, hardware, architecture keyword hits per chapter
- Bash Show context of OS and low-level keyword hits
- Bash Show context for hardware and infrastructure keyword hits
- Bash List section headings of key chapters
- Bash Read schema, workflow, gitignore, prompts and scripts
- Bash Read the front matter lint script
- Bash Check book license, GitHub handle, main branch state, tools
- Bash List commits and files changed on main since this branch
- Bash Switch to main and fast-forward to latest
- Bash Read rule changes and new research skill
- Bash Read claim, quote and shared helper scripts
- Bash Read teammate's 07 note as a style example
- Bash Create topic branch and read script usage
- Bash Get issue numbers and build canonical page text from book copies
- Bash Find OS-related sentences in key chapters
- Bash Read context around internal Linux distribution passages
- Bash Read SRE ch2 hardware and system software sections
- Bash Read SRE ch2 software infrastructure and request path
- Bash Find hardware sentences in NALSD, BSRS ch9, SRE ch7 and ch13
- Bash Find firmware, BIOS and cluster turnup sentences
- Bash Find load balancing and failure domain sentences
- Bash Find failure domain and data integrity sentences
- Bash Find backup, Kubernetes, VM and DR sentences
- Bash Find datacenter toil, satellite, resource exhaustion sentences
- Bash Search books for workstation and hypervisor mentions
- Bash Read workstation context in BSRS ch7 and ch8
- Bash Check BSRS ch7 Shellshock case wording
- Bash Check teammate source title and claim phrasing
- Bash Query Wayback CDX for snapshots of each source page
- Bash Query Wayback snapshot list for each source URL
- Bash Check a few remaining sentence spans
- Write /private[REDACTED:path]
- Bash Verify all spec quotes against local page text
- Bash Fix last quote and pick Wayback snapshots containing quotes
- Bash Run add_claim for each topic in background
- Bash Check claim-adding progress logs
- Bash Find copyright and license lines in book pages
- Bash Check Workbook copyright and claim progress
- Bash Test connectivity to live and archive hosts
- Bash Check progress after retries
- Bash Stop parallel drivers and count claims written
- Bash Confirm drivers stopped and count claims per note
- Bash Kill background drivers by PID and recount claims
- Bash Restart claim adding sequentially with skip and backoff
- Bash Check sequential driver progress
- Bash Inspect a generated note and confirm .local is ignored
- Bash Check claim driver progress
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Bash Create body helper and check driver progress
- Write /private[REDACTED:path]
- Bash Patch body wording and check driver completion
- Bash Verify claim IDs and counts match the plan
- Bash Apply note bodies and refresh topic index notes lists
- Bash Check books for GPU, TPU, hypervisor, NAS, cgroup mentions
- Bash Read context of NAS appliances passage
- Bash Add NAS appliances claim to the storage note
- Edit [REDACTED:path]
- Edit [REDACTED:path]
- Read [REDACTED:path]
- Bash Add gap sections to indexes, refresh 06 index, run lint and status
- Bash Review storage note body and working tree status
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Write [REDACTED:path]
- Bash Check Thai files cover every claim ID, rerun lint, confirm nothing staged
- Bash Check whether anything is staged
- WebFetch https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/
- WebFetch https://cloud.google.com/blog/topics/developers-practitioners/how-google-got-to-rolling-linux-releases-for-desktops
- WebFetch https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
- WebFetch https://gvisor.dev/docs/
- WebFetch https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
- WebFetch https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
- WebFetch https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43438.pdf
- WebFetch https://docs.kernel.org/admin-guide/cgroup-v2.html
- WebFetch https://research.google.com/pubs/archive/43438.pdf
- WebFetch https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf
- Read [REDACTED:path]
- Bash Extract text from Borg paper PDF and search for OS terms
- Bash Search all 79 book pages for remaining gap terms
- Bash Move Thai claim files from .local to Trash
- Bash Fetch external candidate sources as plain text
- Bash Find key sentences in the gLinux blog post
- Bash Read the LISA 2013 session abstract text
- Bash Find gVisor and GKE Sandbox sentences
- Bash Find kernel-sharing and Container-Optimized OS sentences
- Bash Find kernel docs sentences on OOM group kill, livepatch, cgroups
- Bash Read context for OOM group and memory limit sentences
- Bash Fetch Google pages on containers and search for cgroups and Borg
- Bash Show page titles of fetched external sources
- Write /private[REDACTED:path]
- Bash Verify round-2 quotes against fetched page text
- Bash Find Wayback snapshots containing the round-2 org-fact quotes
- Bash Check archive search progress
- Bash Check archive search progress again
- Write /private[REDACTED:path]
- Bash Patch two body sentences and check archive progress
- Bash Check archive search process is alive
- ToolSearch select:Monitor
- Monitor round-2 Wayback archive search for topic 04 sources
- Bash Prepare round-2 claim driver
- Bash Prepare 04 index text and round-2 apply script
- Bash Look for a Wayback snapshot of the new GKE Sandbox URL
- Bash Inspect GKE Sandbox snapshot text for matching sentences
- Bash Find GKE Sandbox sentences present in both live page and snapshot
- Bash Check GKE gVisor wording in live page and snapshot
- Bash Switch GKE claims to quotes present in live page and snapshot
- Bash Add round-2 claims for topic 04 via add_claim
- Bash Check round-2 claim driver progress
- Monitor round-2 add_claim progress for topic 04
- Bash Read round-2 driver results
- Bash Verify round-2 IDs, apply bodies and index, run lint
- Bash Recheck all topic 04 quotes against live pages
- Bash Check repo state and background jobs after the pause
- Bash Fetch candidate sources for topics 05 and 06 gaps
- Bash Find CPU, machine family, TPU and GPU sentences
- Bash Look at Arm and Axion mentions in CPU platform doc
- Bash Find hardware, Titan and hypervisor sentences in Google security docs
- Bash Read isolation context and data center page sentences
- Bash Find GFE, Maglev, minikube and Debian requirement sentences
- Bash Read multiple-CPU-platform text and minikube requirements
- Bash Get exact minikube and Debian requirement text
- Write /private[REDACTED:path]
- Bash Verify round-2 quotes for 05 and 06 locally
- Bash Shorten two quotes and start Wayback snapshot search
- Monitor Wayback snapshot search for 05/06 round-2 sources
- Write /private[REDACTED:path]
- Bash Prepare round-2 apply script and driver for 05/06
- Bash Look for an archived page with the Maglev sentence
- Bash Drop Maglev claim and renumber references in prepared text
- Bash Start adding round-2 claims for 05, 06 and 04
- Monitor round-2 add_claim for 05/06 (19 claims)
- Bash Verify IDs, apply round-2 text, refresh indexes, lint
- Bash Recheck all quotes live and cited IDs for topics 04-06
