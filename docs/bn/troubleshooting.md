# সমস্যা সমাধান

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/troubleshooting.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/troubleshooting.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/troubleshooting.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/troubleshooting.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/troubleshooting.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/troubleshooting.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/troubleshooting.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/troubleshooting.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/troubleshooting.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/troubleshooting.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/troubleshooting.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/troubleshooting.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/troubleshooting.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/troubleshooting.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/troubleshooting.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/troubleshooting.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/troubleshooting.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/troubleshooting.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/troubleshooting.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/troubleshooting.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/troubleshooting.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/troubleshooting.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/troubleshooting.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/troubleshooting.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[ইনস্টলেশন](installation.md) · [সীমাবদ্ধতা](limitations.md)

**নির্দেশ পাওয়া যায়নি:** ইনস্টলেশনের একই ভার্চুয়াল পরিবেশ সক্রিয় করুন। `python3 -m ha_entity_migrations --version` চেষ্টা করুন; শুধু ভুল পথ এড়াতে সিস্টেমের Python-এ ইনস্টল করবেন না।

**প্রস্থান 2, schema_invalid:** কী-গুলো চালনাযোগ্য উদাহরণ ও [ইনপুট মডেলের](model.md) সঙ্গে তুলনা করুন। অজানা ফিল্ড ত্রুটি। সংস্করণ পূর্ণসংখ্যা 1; চ্যানেলের পরিচয় স্ট্রিং। প্রতি অ্যাকশন নীতির সার্ভিস পয়েন্টার চাই। স্ন্যাপশটে সত্তা থাকে; ম্যানিফেস্টে বরাদ্দ ও ভোক্তা। ফাইল দুটি বিনিময়যোগ্য নয়।

**প্রস্থান 2, duplicate_source:** দুই উৎসনাম এক শারীরিক ফাইল শনাক্ত করে। `sources`-এ একটি ক্যাননিক্যাল নাম রাখুন এবং সব ভোক্তার `file` ফিল্ড হালনাগাদ করুন। দ্বৈত বিভাজক বা হার্ড-লিংক/কেস ছদ্মনাম সরান; ছদ্মনামে দ্বিতীয় নীতি দেবেন না। একই বিষয়বস্তুর পৃথক ফাইল সমর্থিত থাকে।

**stale_snapshot / stale_source:** প্রকৃত পরিবর্তন অনুমোদিত উৎসের সঙ্গে তুলনা করুন। পর্যালোচনার পরই fingerprint ব্যবহার করুন। ফাঁক বদলালে হ্যাশ বদলায়। শুধু পুরোনো হ্যাশ মেলাতে পুরোনো কপিতে নির্দেশ করবেন না।

**source_collision / destination_collision:** শারীরিক চ্যানেল, ভূমিকা বা সত্তার ID পুনরাবৃত্ত হয়েছে। ভূমিকা বদলের দুই দিক স্পষ্ট করুন এবং অপরিবর্তিত এন্ডপয়েন্ট কাঙ্ক্ষিত লক্ষ্য ID ধরে আছে কি না দেখুন।

**role_not_allowed / capability_missing:** ভোক্তা অনুপযুক্ত লোডে পৌঁছাবে বা সক্ষমতা হারাবে। সেটি ভূমিকা নাকি হার্ডওয়্যার অনুসরণ করবে নিশ্চিত করুন। allowed_roles স্বয়ংক্রিয়ভাবে বাড়াবেন না বা হার্ডওয়্যারে নেই এমন ক্ষমতা দাবি করবেন না। অন/অফ রিলে দিয়ে বদলানো আলো ম্লান করা যায় না।

**missing_policy / unmodeled_reference:** রেফারেন্সের এন্ডপয়েন্ট তালিকাভুক্ত করুন এবং উদ্দেশ্য নিশ্চিত করেই স্পষ্ট ভোক্তা ঘোষণা যোগ করুন। পুরোনো ইতিহাসের স্ট্রিং সক্রিয় পরিসরের বাইরে হতে পারে; ইচ্ছাকৃতভাবে ফাইল বাদ দিন, তা নথিভুক্ত করুন ও উৎসচুক্তি আবার তৈরি করুন।

**dynamic_reference / embedded_reference / indirect_target:** এই সংস্করণ মানচিত্র প্রমাণ করতে পারে না। Jinja বা দল/এলাকা/লেবেলের আচরণ আলাদা পর্যালোচনা করুন, অথবা স্পষ্ট স্বাভাবিকীকৃত আক্ষরিক কনফিগারেশন দিন। প্রোগ্রাম কখনো টেমপ্লেট চালায় না।

**display_domain_review / service_data_review / mixed_action_targets:** কার্ডের সুবিধা, অ্যাকশনের প্যারামিটার ও লক্ষ্যদল দেখুন। বহু-ডোমেন অ্যাকশন আলাদাভাবে পর্যালোচিত উৎস পরিবর্তনে ভাগ করুন; শুধু সার্ভিস ডোমেন বদলাবেন না।

**retire_scope_mixed / overlapping_edits:** অপ্রাসঙ্গিক রেফারেন্স ছাড়া সংগত পুরোনো ভোক্তা অবজেক্ট বেছে নিন। অ্যাকশন থেকে শুধু entity_id মুছবেন না: তাতে অতিবিস্তৃত লক্ষ্য বা অবৈধ কনফিগারেশন হতে পারে। প্রোগ্রাম স্বয়ংক্রিয় অবসান প্রয়োগ করে না।

**unsupported_source:** শুধু JSON পরিকল্পনা করা যায়। YAML, বাইনারি ও অন্য ফাইল নিঃশব্দে বাদ যায় না। স্পষ্টভাবে স্বাভাবিকীকৃত JSON কপি বিশ্লেষণে সাহায্য করতে পারে, কিন্তু বাস্তব সম্পাদনার আগে মূলের সঙ্গে তুলনা করতে হবে।

ন্যূনতম কৃত্রিম ইনপুট, টুল/Python সংস্করণ, প্রস্থান কোড ও ডায়াগনস্টিক কোডসহ বাগ জানান। বাড়ির অপরিশোধিত এক্সপোর্ট বা API পরিচয়পত্র কখনো সংযুক্ত করবেন না।
