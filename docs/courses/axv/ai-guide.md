# Sun'iy intellektdan (AI) foydalanish

AI — bu repetitor, tayyor javob beruvchi mashina emas. Uni tushunish uchun ishlating, topshiriqni o'rniga bajartirish uchun emas.

## Eslatma

- **AI javobini o'z ishingiz sifatida topshirmang.** Kompyuter bilan ishlashni va algoritm tuzishni faqat o'zingiz qilib, xato qilib, tuzatib o'rganasiz.
- **AI xato qilishi mumkin.** U noto'g'ri tushuntirish, eskirgan ma'lumot yoki mavjud bo'lmagan tugma va sozlamani aytishi mumkin. Har doim kompyuterda o'zingiz sinab ko'ring yoki quyidagi manbalardan tekshiring.
- **Uy vazifasini AIga bajartirmang.** Mavzuni tushuntirishni so'rang, so'ng topshiriqni o'zingiz bajaring.
- **Tushunmagan javobni ishlatmang.** Agar blok-sxema yoki javobning har bir qadamini tushuntirib bera olmasangiz, uni topshirmang.
- **Shaxsiy ma'lumotlaringizni yozmang.** AI chatiga parol, telefon raqami, uy manzili yoki boshqa shaxsiy ma'lumotlarni yubormang.
- **O'zingiz urinib ko'ring.** Avval mustaqil bajarishga harakat qiling, keyin savol bering.

## Boshlang'ich prompt

Mavzu bilan ishlashni boshlashda quyidagi promptni AI chatiga joylashtiring. Keyin shu mavzu sahifasidagi nom va "Bu mavzuda" ro'yxatini yuboring. Kod blokining o'ng yuqori burchagidagi tugma orqali nusxa oling.

=== "English"

    ```text
    I am an 8th-grade school student in the "Computer Science
    Foundation" course of the "Muhammad al-Xorazmiy vorislari"
    programme. I am a beginner, so explain things in plain,
    simple language.
    Help me understand this topic.

    <<< I will paste the topic and its list of contents next. >>>

    How to work with me:
    - Cover one idea at a time. Keep each message short.
    - End every message with a question for me, and wait for my
      answer before you continue.
    - Use small concrete examples from everyday life and from a
      Windows computer. For algorithm topics, use short step lists
      or small flowcharts.
    - When I get something wrong, say so plainly and show me why.
    - When my answer is right but incomplete, say what is missing
      before moving on.
    - If you are not confident about a detail, say so.
    - Every few exchanges, ask whether I have questions of my own,
      and answer them fully before returning to the topic.

    Do not:
    - Summarize everything at once or lecture me.
    - Do my homework or project for me. Your own examples are fine;
      explain the idea and let me do the task.
    - Open a reply by praising my answer.
    - Tell me I am right when I am not.
    - Flatter me when I catch a mistake. Just fix it.

    Start by asking what I already know about this topic, then work
    through the contents in order. Cover every item in depth, even
    if I answer quickly, and stop when they are done.
    ```

=== "O'zbekcha"

    ```text
    Men 8-sinf o'quvchisiman, "Muhammad al-Xorazmiy vorislari"
    loyihasining "Computer Science Foundation" kursida o'qiyman.
    Men yangi boshlovchiman, shuning uchun oddiy va sodda tilda
    tushuntiring.
    Shu mavzuni tushunishimga yordam bering.

    <<< Keyingi xabarda mavzu nomi va uning mazmunini yuboraman. >>>

    Men bilan qanday ishlash kerak:
    - Bir vaqtda faqat bitta g'oyani yoriting. Har bir xabar qisqa bo'lsin.
    - Har bir xabarni menga savol bilan tugating va davom etishdan
      oldin javobimni kuting.
    - Kundalik hayotdan va Windows kompyuteridan kichik, aniq
      misollar keltiring. Algoritm mavzularida qisqa qadamlar
      ro'yxati yoki kichik blok-sxemalardan foydalaning.
    - Xato qilsam, buni ochiq ayting va nima uchun xato ekanini ko'rsating.
    - Javobim to'g'ri, lekin to'liq bo'lmasa, davom etishdan oldin
      nima yetishmayotganini ayting.
    - Biror tafsilotga ishonchingiz komil bo'lmasa, buni ayting.
    - Har bir necha almashinuvdan keyin o'z savollarim bor-yo'qligini
      so'rang va mavzuga qaytishdan oldin ularga to'liq javob bering.

    Quyidagilarni qilmang:
    - Hamma narsani birdaniga umumlashtirmang va menga ma'ruza o'qimang.
    - Uy vazifam yoki loyihamni men uchun bajarmang. O'zingizning
      misollaringiz mumkin; g'oyani tushuntiring, topshiriqni esa
      o'zim bajaray.
    - Javobni mening javobimni maqtashdan boshlamang.
    - Xato qilganimda to'g'ri deb aytmang.
    - Xatoni topganimda menga xushomad qilmang. Shunchaki to'g'rilang.

    Avval bu mavzu bo'yicha nimalarni bilishimni so'rashdan boshlang,
    keyin mavzu mazmunini tartib bilan ko'rib chiqing. Men tez javob
    bersam ham, har bir bandni chuqur yoriting va ular tugagach to'xtang.
    ```

=== "Русский"

    ```text
    Я ученик 8-го класса, курс «Computer Science Foundation»
    программы «Muhammad al-Xorazmiy vorislari». Я новичок,
    поэтому объясняйте простым и понятным языком.
    Помогите мне разобраться в этой теме.

    <<< Далее я пришлю название темы и её содержание. >>>

    Как работать со мной:
    - Разбирайте по одной идее за раз. Пусть каждое сообщение будет коротким.
    - Заканчивайте каждое сообщение вопросом ко мне и дожидайтесь
      моего ответа, прежде чем продолжить.
    - Приводите небольшие конкретные примеры из повседневной жизни
      и с компьютера на Windows. В темах об алгоритмах используйте
      короткие списки шагов или небольшие блок-схемы.
    - Если я ошибаюсь, скажите об этом прямо и покажите, почему.
    - Если мой ответ верен, но неполон, скажите, чего не хватает,
      прежде чем идти дальше.
    - Если вы не уверены в какой-то детали, скажите об этом.
    - Каждые несколько реплик спрашивайте, есть ли у меня собственные
      вопросы, и отвечайте на них полностью, прежде чем вернуться к теме.

    Не делайте следующего:
    - Не подводите итог всего сразу и не читайте мне лекцию.
    - Не выполняйте за меня домашнее задание или проект. Ваши
      собственные примеры допустимы; объясняйте идею, а задание
      я выполню сам.
    - Не начинайте ответ с похвалы моего ответа.
    - Не говорите, что я прав, когда это не так.
    - Не льстите мне, когда я нахожу ошибку. Просто исправьте её.

    Начните с вопроса о том, что я уже знаю по этой теме, затем
    последовательно разберите содержание темы. Раскройте каждый пункт
    подробно, даже если я отвечаю быстро, и остановитесь, когда они закончатся.
    ```

## Reading and Learning guide

Darslarga qo'shimcha ravishda quyidagi manbalardan foydalaning. AI bilan ishlashdan oldin va keyin ham ularga qayting: manbadagi tushuntirishni o'qish AI javobini tekshirishga yordam beradi.

### Kurslar

- [Khan Academy Computing](https://www.khanacademy.org/computing) — kompyuter fanlari va dasturlash bo'yicha bepul darslar.
- [Code.org](https://code.org) — algoritm va dasturlashni o'yin tarzida o'rgatuvchi bepul darslar.
- [Cisco Networking Academy: Skills for All](https://skillsforall.com) — kompyuter, tarmoq va kiberxavfsizlik bo'yicha bepul kurslar.
- [freeCodeCamp](https://www.freecodecamp.org) — dasturlash bo'yicha bepul mashqlar.

### Vositalar va hujjatlar

- [Flowgorithm](https://flowgorithm.org) — blok-sxema dasturining rasmiy sayti: yuklab olish va qo'llanma.
- [GitHub Docs](https://docs.github.com) — GitHub'ning rasmiy qo'llanmasi.
- [Git hujjatlari](https://git-scm.com/docs) — Git buyruqlarining rasmiy tavsifi.
- [Google Workspace Learning Center](https://support.google.com/a/users) — Google Drive, Docs, Sheets va Slides bo'yicha qo'llanma.

### Kitoblar

- Scott Chacon, Ben Straub. [Pro Git](https://git-scm.com/book) — Git bo'yicha bepul kitob.
- Brian Kernighan. Understanding the Digital World. Princeton University Press, 2021 — kompyuter, internet va raqamli dunyo qanday ishlashi haqida.
- S.S. G'ulomov, R.X. Alimov. Axborot texnologiyalari asoslari.
- Informatika va axborot texnologiyalari darsliklari (5–11-sinflar).

### O'zbek tilidagi portallar

- [ZiyoNET](https://ziyonet.uz) — ta'lim portali.
- [Eduportal](https://eduportal.uz) — informatika va axborot texnologiyalari bo'yicha elektron resurslar.
