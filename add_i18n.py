
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add script tag for lang.js
if "<script src=\"lang.js\"></script>" not in html:
    html = html.replace("</body>", "    <script src=\"lang.js\"></script>\n</body>")

# Replace nav items
html = html.replace("<a href=\"#categories\">Mahsulotlar</a>", "<a href=\"#categories\" data-i18n=\"n-prod\">Mahsulotlar</a>")
html = html.replace("<a href=\"#about\">Biz haqimizda</a>", "<a href=\"#about\" data-i18n=\"n-about\">Biz haqimizda</a>")
html = html.replace("<a href=\"#contact\">Aloqa</a>", "<a href=\"#contact\" data-i18n=\"n-cont\">Aloqa</a>")

# Replace nav actions block
old_nav_actions = """        <div class="nav-links">
            <a href="#categories">Mahsulotlar</a>
            <a href="#about">Biz haqimizda</a>
            <a href="#contact">Aloqa</a>
        </div>
        <a href="#contact" class="nav-cta">Bog'lanish</a>
        <button class="hamburger" id="hamburger">"""
new_nav_actions = """        <div class="nav-links">
            <a href="#categories" data-i18n="n-prod">Mahsulotlar</a>
            <a href="#about" data-i18n="n-about">Biz haqimizda</a>
            <a href="#contact" data-i18n="n-cont">Aloqa</a>
        </div>
        <div class="nav-actions">
            <div class="lang-switch">
                <div class="lang-current">
                    <img id="current-lang-img" src="https://flagcdn.com/w40/uz.png" alt="Lang">
                    <span id="current-lang-text">UZ</span>
                </div>
                <div class="lang-dropdown">
                    <div class="lang-option" onclick="changeLang('uz')"><img src="https://flagcdn.com/w40/uz.png" alt="UZ"> O'zbekcha</div>
                    <div class="lang-option" onclick="changeLang('ru')"><img src="https://flagcdn.com/w40/ru.png" alt="RU"> –усский</div>
                    <div class="lang-option" onclick="changeLang('en')"><img src="https://flagcdn.com/w40/us.png" alt="EN"> English</div>
                </div>
            </div>
            <a href="#contact" class="nav-cta" data-i18n="n-btn">Bog'lanish</a>
        </div>
        <button class="hamburger" id="hamburger">"""
html = html.replace(old_nav_actions, new_nav_actions)

# Re-read if needed, but doing simple replaces:
html = html.replace("<h1>Premium darajadagi Qoshiq, vilka va Oshxona anjomlari</h1>", "<h1 data-i18n=\"h-title\">Premium darajadagi Qoshiq, vilka va Oshxona anjomlari</h1>")
html = html.replace("<p>Restoran va do'kon egalari uchun qoshiq-vilka to'plamlarining yirik distribyutori. MDH miqyosida ulgurji xarid qiling va biznesingizni premium sifat bilan ta'minlang.</p>", "<p data-i18n=\"h-desc\">Restoran va do'kon egalari uchun qoshiq-vilka to'plamlarining yirik distribyutori. MDH miqyosida ulgurji xarid qiling va biznesingizni premium sifat bilan ta'minlang.</p>")
html = html.replace("<i class=\"fab fa-telegram\"></i> Katalogni Ko'rish", "<i class=\"fab fa-telegram\"></i> <span data-i18n=\"h-btn1\">Katalogni Ko'rish</span>")
html = html.replace("class=\"btn-outline\">Bog'lanish</a>", "class=\"btn-outline\" data-i18n=\"h-btn2\">Bog'lanish</a>")
html = html.replace("<span>Pastga suring</span>", "<span data-i18n=\"h-scroll\">Pastga suring</span>")

# Features
html = html.replace("<h4>B2B Hamkor</h4>", "<h4 data-i18n=\"f1-t\">B2B Hamkor</h4>")
html = html.replace("<p>Ishonchli ulgurji hamkorlik</p>", "<p data-i18n=\"f1-d\">Ishonchli ulgurji hamkorlik</p>")
html = html.replace("<h4>100.000+ Mijoz</h4>", "<h4 data-i18n=\"f2-t\">100.000+ Mijoz</h4>")
html = html.replace("<p>Butun O'zbekiston bo'ylab</p>", "<p data-i18n=\"f2-d\">Butun O'zbekiston bo'ylab</p>")
html = html.replace("<h4>100% Kafolat</h4>", "<h4 data-i18n=\"f3-t\">100% Kafolat</h4>")
html = html.replace("<p>Sifat kafolati</p>", "<p data-i18n=\"f3-d\">Sifat kafolati</p>")
html = html.replace("<h4>Abu Saxiy</h4>", "<h4 data-i18n=\"f4-t\">Abu Saxiy</h4>")
html = html.replace("<p>Chinni bozori, Toshkent</p>", "<p data-i18n=\"f4-d\">Chinni bozori, Toshkent</p>")

# Cats
html = html.replace("<h2>Mahsulot Kategoriyalari</h2>", "<h2 data-i18n=\"c-title\">Mahsulot Kategoriyalari</h2>")
html = html.replace("<p>Eng yuqori sifatli oshxona anjomlarini sizga taqdim etamiz</p>", "<p data-i18n=\"c-desc\">Eng yuqori sifatli oshxona anjomlarini sizga taqdim etamiz</p>")
html = html.replace("<h3>Qoshiq va Vilkalar</h3>", "<h3 data-i18n=\"c1-t\">Qoshiq va Vilkalar</h3>")
html = html.replace("<p>Premium to'plamlar</p>", "<p data-i18n=\"c1-d\">Premium to'plamlar</p>")
html = html.replace("<h3>Oshxona Anjomlari</h3>", "<h3 data-i18n=\"c2-t\">Oshxona Anjomlari</h3>")
html = html.replace("<p>Professional jihozlar</p>", "<p data-i18n=\"c2-d\">Professional jihozlar</p>")
html = html.replace("<h3>Maxsus To'plamlar</h3>", "<h3 data-i18n=\"c3-t\">Maxsus To'plamlar</h3>")
html = html.replace("<p>Sovg'a to'plamlari</p>", "<p data-i18n=\"c3-d\">Sovg'a to'plamlari</p>")

# About
html = html.replace("<h2>Nima uchun Ali?</h2>", "<h2 data-i18n=\"a-title\">Nima uchun Ali?</h2>")
html = html.replace("<p>Ali Ч O'zbekiston va MDH bozorida qoshiq-vilka to'plamlari bo'yicha o'z brendiga ega bo'lgan yirik importyor va asosiy yetkazib beruvchidir. Abu Saxiy majmuasidagi ko'p yillik faoliyatimiz va bevosita Xitoydan import imkoniyatlarimiz orqali eng yuqori sifatli mahsulotlarni birinchi qo'l narxlarda taqdim etamiz.</p>", "<p data-i18n=\"a-p1\">Ali Ч O'zbekiston va MDH bozorida qoshiq-vilka to'plamlari bo'yicha o'z brendiga ega bo'lgan yirik importyor va asosiy yetkazib beruvchidir. Abu Saxiy majmuasidagi ko'p yillik faoliyatimiz va bevosita Xitoydan import imkoniyatlarimiz orqali eng yuqori sifatli mahsulotlarni birinchi qo'l narxlarda taqdim etamiz.</p>")
html = html.replace("<p>Bizning asosiy maqsadimiz Ч restoran majmualari, yirik do'konlar va ulgurji savdo subyektlarini nafis dizayn hamda premium sifat bilan ta'minlashdir. Har bir mahsulot Ali brendi kafolati ostida sinchiklab tanlangan bo'lib, biznesingiz nufuzini yangi bosqichga olib chiqadi.</p>", "<p data-i18n=\"a-p2\">Bizning asosiy maqsadimiz Ч restoran majmualari, yirik do'konlar va ulgurji savdo subyektlarini nafis dizayn hamda premium sifat bilan ta'minlashdir. Har bir mahsulot Ali brendi kafolati ostida sinchiklab tanlangan bo'lib, biznesingiz nufuzini yangi bosqichga olib chiqadi.</p>")
html = html.replace("<span>Mijozlar</span>", "<span data-i18n=\"a-s1\">Mijozlar</span>")
html = html.replace("<span>Yillik tajriba</span>", "<span data-i18n=\"a-s2\">Yillik tajriba</span>")
html = html.replace("<span>Sifat kafolati</span>", "<span data-i18n=\"a-s3\">Sifat kafolati</span>")

# Contact
html = html.replace("<h2>Biz Bilan Bog'laning</h2>", "<h2 data-i18n=\"co-title\">Biz Bilan Bog'laning</h2>")
html = html.replace("<p>Buyurtma berish yoki savol yo'llash uchun qulay usulni tanlang</p>", "<p data-i18n=\"co-desc\">Buyurtma berish yoki savol yo'llash uchun qulay usulni tanlang</p>")

html = html.replace("<h4>Telegram Katalog</h4>", "<h4 data-i18n=\"co1-t\">Telegram Katalog</h4>")
html = html.replace("<p>Barcha mahsulotlar katalogi</p>", "<p data-i18n=\"co1-d\">Barcha mahsulotlar katalogi</p>")
html = html.replace("Ochish <i class=\"fas fa-arrow-right\"></i>", "<span data-i18n=\"co1-b\">Ochish</span> <i class=\"fas fa-arrow-right\"></i>")

html = html.replace("<h4>Telefon</h4>", "<h4 data-i18n=\"co2-t\">Telefon</h4>")
html = html.replace("<p>To'g'ridan-to'g'ri bog'lanish</p>", "<p data-i18n=\"co2-d\">To'g'ridan-to'g'ri bog'lanish</p>")
html = html.replace("Qo'ng'iroq <i class=\"fas fa-arrow-right\"></i>", "<span data-i18n=\"co2-b\">Qo'ng'iroq</span> <i class=\"fas fa-arrow-right\"></i>")

html = html.replace("<h4>Telegram Aloqa</h4>", "<h4 data-i18n=\"co3-t\">Telegram Aloqa</h4>")
html = html.replace("<p>To'g'ridan-to'g'ri yozing</p>", "<p data-i18n=\"co3-d\">To'g'ridan-to'g'ri yozing</p>")
html = html.replace("Yozish <i class=\"fas fa-arrow-right\"></i>", "<span data-i18n=\"co3-b\">Yozish</span> <i class=\"fas fa-arrow-right\"></i>")

html = html.replace("<h4>Instagram</h4>", "<h4 data-i18n=\"co4-t\">Instagram</h4>")
html = html.replace("<p>Yangi mahsulotlar va aksiyalar</p>", "<p data-i18n=\"co4-d\">Yangi mahsulotlar va aksiyalar</p>")
html = html.replace("Ko'rish <i class=\"fas fa-arrow-right\"></i>", "<span data-i18n=\"co4-b\">Ko'rish</span> <i class=\"fas fa-arrow-right\"></i>")

html = html.replace("<h4>Do'kon Manzili</h4>", "<h4 data-i18n=\"co5-t\">Do'kon Manzili</h4>")
html = html.replace("<p>Abu Saxiy Chinni bozori</p>", "<p data-i18n=\"co5-d\">Abu Saxiy Chinni bozori</p>")
html = html.replace("Xaritada <i class=\"fas fa-arrow-right\"></i>", "<span data-i18n=\"co5-b\">Xaritada</span> <i class=\"fas fa-arrow-right\"></i>")

# Footer
html = html.replace("<p>Premium sifatdagi oshxona anjomlari va qoshiq-vilka to'plamlari bilan biznesingizni bezating.</p>", "<p data-i18n=\"ft-desc\">Premium sifatdagi oshxona anjomlari va qoshiq-vilka to'plamlari bilan biznesingizni bezating.</p>")
html = html.replace("&copy; 2024 Ali Spoon Gallery. Barcha huquqlar himoyalangan.", "&copy; 2024 Ali Spoon Gallery. <span data-i18n=\"ft-bot\">Barcha huquqlar himoyalangan.</span>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

