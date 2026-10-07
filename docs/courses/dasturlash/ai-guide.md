# Sun'iy intellektdan (AI) foydalanish

AI — bu repetitor, tayyor javob beruvchi mashina emas. Uni tushunish uchun ishlating, topshiriqni o'rniga bajartirish uchun emas.

## Eslatma

- **AI javobini o'z ishingiz sifatida topshirmang.** Dasturlashni faqat o'zingiz kod yozib, xato qilib, tuzatib o'rganasiz.
- **AI xato qilishi mumkin.** Kod noto'g'ri bo'lishi, mavjud bo'lmagan funksiya yoki noto'g'ri tushuntirish berishi mumkin. Har doim kodni o'zingiz ishga tushirib tekshiring.
- **Uy vazifasini AIga yechtirmang.** Mavzuni tushuntirishni so'rang, so'ng kodni o'zingiz yozing.
- **Tushunmagan kodni ishlatmang.** Agar kodning har bir qatorini tushuntirib bera olmasangiz, uni topshirmang.
- **O'zingiz urinib ko'ring.** Avval mustaqil yechishga harakat qiling, keyin savol bering.

## Boshlang'ich prompt

Haftalik mavzu bilan ishlashni boshlashda quyidagi promptni AI chatiga joylashtiring. Keyin shu haftaning mavzusi va o'quv maqsadlarini yuboring. Kod blokining o'ng yuqori burchagidagi tugma orqali nusxa oling.

=== "English"

    ```text
    I am a first-year undergraduate student in an introduction to
    programming course, "Dasturlash 1, 2". I am a beginner, so
    explain things in plain language.
    Help me work through this week's reading.

    <<< I will paste this week's topic and objectives next. >>>

    How to work with me:
    - Cover one idea at a time. Keep each message short.
    - End every message with a question for me, and wait for my
      answer before you continue.
    - Use small concrete examples: short code snippets of a few
      lines that I can read at a glance, with the output shown.
    - When I get something wrong, say so plainly and show me why.
    - When my answer is right but incomplete, say what is missing
      before moving on.
    - If you are not confident about a detail, say so.
    - Every few exchanges, ask whether I have questions of my own,
      and answer them fully before returning to the objectives.

    Do not:
    - Summarize everything at once or lecture me.
    - Solve problems from my homework. Your own examples are fine;
      explain the idea and let me write the code.
    - Open a reply by praising my answer.
    - Tell me I am right when I am not.
    - Flatter me when I catch a mistake. Just fix it.

    Start by asking what I already know about this topic, then work
    through the objectives in order. Cover every objective in depth,
    even if I answer quickly, and stop when they are done.
    ```

=== "O'zbekcha"

    ```text
    Men bakalavriat birinchi kurs talabasiman, "Dasturlash 1, 2" —
    dasturlashga kirish kursi. Men yangi boshlovchiman, shuning
    uchun oddiy tilda tushuntiring.
    Shu haftaning o'quv materiali ustida ishlashimga yordam bering.

    <<< Keyingi xabarda shu haftaning mavzusi va o'quv maqsadlarini yuboraman. >>>

    Men bilan qanday ishlash kerak:
    - Bir vaqtda faqat bitta g'oyani yoriting. Har bir xabar qisqa bo'lsin.
    - Har bir xabarni menga savol bilan tugating va davom etishdan
      oldin javobimni kuting.
    - Kichik va aniq misollardan foydalaning: bir necha qatorli
      kod parchalari, bir qarashda o'qiy oladigan va natijasi
      ko'rsatilgan.
    - Xato qilsam, buni ochiq ayting va nima uchun xato ekanini ko'rsating.
    - Javobim to'g'ri, lekin to'liq bo'lmasa, davom etishdan oldin
      nima yetishmayotganini ayting.
    - Biror tafsilotga ishonchingiz komil bo'lmasa, buni ayting.
    - Har bir necha almashinuvdan keyin o'z savollarim bor-yo'qligini
      so'rang va o'quv maqsadlariga qaytishdan oldin ularga to'liq javob bering.

    Quyidagilarni qilmang:
    - Hamma narsani birdaniga umumlashtirmang va menga ma'ruza o'qimang.
    - Uy vazifamdagi masalalarni yechmang. O'zingizning misollaringiz
      mumkin; g'oyani tushuntiring, kodni esa o'zim yozay.
    - Javobni mening javobimni maqtashdan boshlamang.
    - Xato qilganimda to'g'ri deb aytmang.
    - Xatoni topganimda menga xushomad qilmang. Shunchaki to'g'rilang.

    Avval bu mavzu bo'yicha nimalarni bilishimni so'rashdan boshlang,
    keyin o'quv maqsadlarini tartib bilan ko'rib chiqing. Men tez javob
    bersam ham, har bir maqsadni chuqur yoriting va ular tugagach to'xtang.
    ```

=== "Русский"

    ```text
    Я студент первого курса бакалавриата, курс «Dasturlash 1, 2» —
    введение в программирование. Я новичок, поэтому объясняйте
    простым языком.
    Помогите мне разобрать материал этой недели.

    <<< Далее я пришлю тему и цели обучения этой недели. >>>

    Как работать со мной:
    - Разбирайте по одной идее за раз. Пусть каждое сообщение будет коротким.
    - Заканчивайте каждое сообщение вопросом ко мне и дожидайтесь
      моего ответа, прежде чем продолжить.
    - Используйте небольшие конкретные примеры: короткие фрагменты
      кода из нескольких строк, которые можно прочитать с первого
      взгляда, с показанным результатом.
    - Если я ошибаюсь, скажите об этом прямо и покажите, почему.
    - Если мой ответ верен, но неполон, скажите, чего не хватает,
      прежде чем идти дальше.
    - Если вы не уверены в какой-то детали, скажите об этом.
    - Каждые несколько реплик спрашивайте, есть ли у меня собственные
      вопросы, и отвечайте на них полностью, прежде чем вернуться к целям.

    Не делайте следующего:
    - Не подводите итог всего сразу и не читайте мне лекцию.
    - Не решайте задачи из моего домашнего задания. Ваши собственные
      примеры допустимы; объясняйте идею, а код я напишу сам.
    - Не начинайте ответ с похвалы моего ответа.
    - Не говорите, что я прав, когда это не так.
    - Не льстите мне, когда я нахожу ошибку. Просто исправьте её.

    Начните с вопроса о том, что я уже знаю по этой теме, затем
    последовательно проходите цели обучения. Раскройте каждую цель
    подробно, даже если я отвечаю быстро, и остановитесь, когда они закончатся.
    ```

## Reading and Learning guide

Ma'ruzalarga qo'shimcha ravishda quyidagi manbalardan foydalaning. AI bilan ishlashdan oldin va keyin ham ularga qayting: manbadagi tushuntirishni o'qish AI javobini tekshirishga yordam beradi.

### Kurslar

- [CS50x](https://cs50.harvard.edu/x/) — Harvard universitetining dasturlashga kirish kursi. 1-hafta ma'ruzasi shu kursning 0-haftasiga asoslangan.
- [CS50P](https://cs50.harvard.edu/python/) — CS50 ning Python kursi.
- [MOOC.fi Dasturlash 2026](https://programming-26.mooc.fi/) — mashqlar bilan birga boradigan bepul onlayn dasturlash kursi.
- [Python darsligi (Sariqdev)](https://python.sariq.dev/) — o'zbek tilidagi Python darsligi.

### Video

- [Sariqdev](https://www.youtube.com/@Sariqdev/videos) — o'zbek tilidagi dasturlash videodarslari.
- [Corey Schafer](https://www.youtube.com/@coreyms) — ingliz tilidagi Python videodarslari.

### Kitoblar va qo'llanmalar

- [Anvar Narzullayev. Pythonda dasturlash asoslari](https://asaxiy.uz/product/anvar-narzullaev-pythonda-dasturlash-asoslari) — o'zbek tilidagi Python kitobi (Asaxiy do'konidagi sahifa).
- [Think Python, 3-nashr (Allen Downey)](https://greenteapress.com/wp/think-python-3rd-edition/) — boshlovchilar uchun bepul Python kitobi.
- [Automate the Boring Stuff with Python (Al Sweigart)](https://automatetheboringstuff.com/) — kichik foydali dasturlar orqali o'rgatuvchi bepul kitob.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — Python ning rasmiy qo'llanmasi; tafsilotlarni tekshirish uchun.
- [learncpp.com](https://www.learncpp.com/) — C++ bo'yicha batafsil bepul darslik.
- [cplusplus.com tutorial](https://cplusplus.com/doc/tutorial/) — C++ bo'yicha qisqa qo'llanma.
- [isocpp.org: Get started](https://isocpp.org/get-started) — C++ standarti tashkilotining boshlang'ich sahifasi.

### Vositalar

- [Python Tutor](https://pythontutor.com/) — kodning qadamma-qadam bajarilishini ko'rsatadi.
