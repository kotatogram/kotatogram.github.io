+++
title = 'Вышла бета Kotatogram 1.4.2!'
date = "2021-08-21T21:07:00+03:00"
description = 'Исправления и обновление исходников до 2.8.11.'
+++

Так как эта версия захватила часть коммитов бета-версии, в этот раз выпущена бета. Но помимо обновления исходников, в ней также появилось несколько функций и исправлений.

{{< subheader >}}
## Скачать бету 1.4.2
на основе Telegram Desktop 2.8.11
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 16.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-appimage.tar.xz" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
#### Альтернативные способы
Имейте в виду, что они могут быть обновлены не сразу.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Страница на FlatHub" link= "https://flathub.org/apps/details/io.github.kotatogram" >}}
    {{< button title="Страница на Repology" link= "https://repology.org/project/kotatogram-desktop/versions" >}}
{{< /button-group >}}

{{< subheader >}}
### macOS {#stable-macos}
Поддерживает macOS 10.15 и выше.
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения

* **Ручной выбор времени отключения уведомлений.** Стандартные опции (1 час/4 часа/18 часов/3 дня) были заменены на поле ввода, где вы можете сами указать, на сколько выключить уведомления.
* **Опция авто-входа на сайты Telegram.** В Telegram Desktop она включена всегда, но если вас она не устраивает по какой-либо причине, теперь вы можете её отключить.
* **Опция многопоточного декодирования видео.** При включении опции видео может тормозить гораздо меньше или не тормозить вообще, но будет потребляться больше ЦП и ОЗУ. А также количество потоков можно ограничить опцией `ffmpeg_thread_count` в JSON-файле настроек. Опцию добавил @Shlyupa.
* **Внешний видеоплеер.** Эта опция была скрыта под чит-кодом `videoplayer`. Теперь её можно переключить в [настройках Kotatogram](tg://settings/kotato), поэтому чит-код был убран. Если вы незнакомы с опцией из Telegram Desktop, то она позволяет воспроизводить видео в системном видеоплеере вместо встроенного. Опцию добавил @Shlyupa.
* **Отправка без метки «через @bot».** Позволяет отправить результаты инлайн-ботов без их указания. На деле работает только с ботом @gif, у остальных только показывается, что отправляется без метки. Опцию добавил @Shlyupa.
* **JSON-настройка размера шрифта.** `fonts` > `size` позволяет настроить _относительный_ размер шрифта, т.е. 0 – по умолчанию, 1 – на 1 пиксель больше, -1 – на один пиксель меньше, и т.д. Опцию добавил @Shlyupa.
* **Опция прокрутки при неактивном окне.** При включении открытый чат будет автоматически прокручиваться, когда окно неактивно. Опцию добавил @Shlyupa.
* **Портирована опция авто-удаления сообщений через месяц.** Это также должно исправить постоянные вылеты, если у вас в списке чатов был хотя бы один с автоудалением сообщений через месяц.
* Локализована кнопка автоудаления сообщения на русский.

## Исправления

* Исправлено отсутствующее «Копировать ссылку» в окне пересылки сообщения при выборе одного альбома.
* Исправлена работоспособность некоторых встроенных переводов Kotatogram.

---

А ещё я забыл подтянуть переводы с Crowdin, простите. Я их подтяну в следующем релизе.
