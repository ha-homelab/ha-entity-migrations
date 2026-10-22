# সীমাবদ্ধতা ও পর্যালোচনার সীমানা

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/limitations.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/limitations.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/limitations.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/limitations.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/limitations.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/limitations.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/limitations.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/limitations.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/limitations.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/limitations.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/limitations.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/limitations.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/limitations.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/limitations.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/limitations.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/limitations.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/limitations.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/limitations.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/limitations.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/limitations.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/limitations.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/limitations.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/limitations.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/limitations.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[স্থাপত্য](architecture.md) · [নিরাপত্তা](../../SECURITY.md)

পরিকল্পনার নির্ভুলতা শারীরিক/চ্যানেল/ভূমিকার ঘোষণা এবং দেওয়া ফাইলের ওপর নির্ভরশীল। টুল বাদ পড়া ড্যাশবোর্ড, ডিভাইস ট্রিগার, দৃশ্য, ব্লুপ্রিন্ট, অন্যত্র রাখা অটোমেশন, Matter ফিল্টার, বাইরের ক্লায়েন্ট বা গোপন ইন্টিগ্রেশন অবস্থা খুঁজে পায় না। প্রস্তুত প্রতিবেদনকে পূর্ণ Home Assistant অডিট বলবেন না। এই সংস্করণে প্রতিটি ভূমিকা অনন্য; বহু-থেকে-বহু অর্থগত ভূমিকা ও দল হাতে বিভাজন করতে হয়।

JSON কনফিগারেশন উৎস সমর্থিত। YAML, include, ছদ্মনাম, অ্যাঙ্কর, চালনাযোগ্য ট্যাগ, নিজস্ব কম্পোনেন্ট এবং রানটাইমে তৈরি টেমপ্লেট ব্যাখ্যা করা হয় না। স্বাভাবিকীকরণ এই সংস্করণের বাইরে এবং অর্থ হারাতে পারে; মূল রাখুন ও সমতুল্যতা যাচাই করুন। সমর্থিত JSON-ও HA-এর সম্পূর্ণ কনফিগারেশন স্কিমা দিয়ে যাচাই হয় না। স্পষ্ট ভোক্তা অবজেক্ট সরালে অবৈধ প্যারেন্ট থেকে যেতে পারে; সেটি দেখুন এবং স্বাভাবিক স্টেজিং পদ্ধতিতে HA কনফিগারেশন পরীক্ষা চালান।

সক্ষমতা ও অনুমোদিত ভূমিকা স্পষ্ট বাধা, অনুমিত নিরাপত্তা নয়। আগের নিরীহ সকেটে পাম্প বা গ্যারেজ চালক লাগানো হয়েছে কি না টুল জানে না। রিলের জানানো অবস্থা সংযোগ/লোডের আচরণ প্রমাণ করে না। শুধু নাম যাচাই করতে পুরো বাড়ির স্ক্রিপ্ট চালাবেন না বা চলন্ত যন্ত্রের বিদ্যুৎ বন্ধ-চালু করবেন না। শারীরিক কমিশনিং আলাদা নিয়ন্ত্রিত পদ্ধতির বিষয়।

এই সংস্করণ পরিকল্পনা প্রয়োগ, রেজিস্ট্রি সত্তার নাম বা অনন্য ID পরিবর্তন, HA পুনরায় লোড, নিয়ন্ত্রক পুনরারম্ভ, ইন্টিগ্রেশন সরানো বা পরিবর্তন ফেরত দেয় না। ফেরত আসা অপারেশন পরামর্শ, চালনাযোগ্য JSON Patch নয়। হাতে প্রয়োগ করলে নতুন স্ন্যাপশট নিন এবং প্রতিটি পর্যালোচিত পরিবর্তনের পর যাচাই করুন; সূচক ও সংস্করণ বদলাতে পারে। হ্যাশ স্বাক্ষর বা প্রবেশাধিকার নিয়ন্ত্রণ দেয় না।

প্রতিবেদনে ব্যক্তিগত নাম ও পরিচয় থাকতে পারে। সেগুলো প্রকাশ্য Git, ইস্যু ট্র্যাকার এবং CI আর্টিফ্যাক্টের বাইরে রাখুন। প্রকাশ্য উদাহরণ কৃত্রিম ডিভাইস ব্যবহার করে এবং বাস্তব ক্ষেত্র-যাচাই দাবি করে না। ডায়াগনস্টিক ইচ্ছাকৃতভাবে পরিকল্পনা আটকায়; force ফ্ল্যাগ, ignore তালিকা বা গোপন শিথিল মোড নেই।
