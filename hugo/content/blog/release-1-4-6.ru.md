+++
title = 'Вышел Kotatogram 1.4.6 beta!'
date = "2021-12-18T22:51:00+03:00"
description = 'Обновление исходников с щепоткой новых функций.'
+++

С этой версии поддерживается начинается поддержка спонсорских сообщений от Telegram. Напомню, что это необходимо, потому что без их поддержки приложение может оказаться под угрозой отключения по API ID. Также на всех более ранних версиях пропала возможность открытия каналов, которые включили у себя запрет на пересылку и сохранение контента. В этой версии такие каналы поддерживаются с сохранением этого запрета.

В этой версии есть несколько известных багов, исправлять которые попросту нет времени из-за необходимости релизнуться как можно скорее. Возможно, за время беты найдутся и другие. Но здесь не только есть новые исходники и новые баги: контрибьюторы также подкинули и новых функций, которые могут вам понравиться.

{{< subheader >}}
## Скачать бету 1.4.6
на основе Telegram Desktop 3.3
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 16.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-linux.tar.xz" class="icon solid fa-download primary" >}}
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

### macOS
Поддерживает macOS 10.15 и выше. В автоапдейтере временно задерживается, поэтому, если хотите поскорее обновиться, можете скачать отсюда.
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения
* **Возможность отключить запоминание сжатие изображений при отправке.** В Telegram Desktop после отправки изображений всегда запоминается последний режим отправки. Это удобно, но иногда это приводит к тому, что при быстрой отправке можно случайно отправить изображение без сжатия, и придётся отправлять заново. Или наоборот. Это можно настроить опцией «Сжимать изображения по умолчанию». [Добавлено контрибьютором.](https://github.com/kotatogram/kotatogram-desktop/pull/243)
* **Пользовательские автозамены теперь работают без автозамены эмодзи.** На случай, если вы не любите стандартные автозамены, но вам нужны те, что вы настроили в JSON-файле. Если вы забыли, как их настраивать, на этот счёт есть [страница, которую я так и не перенёс с вики на сайт](https://github.com/kotatogram/kotatogram-desktop/wiki/%D0%A1%D0%B2%D0%BE%D0%B8-%D0%B0%D0%B2%D1%82%D0%BE%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D1%8B-%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0). [Добавлено контрибьютором.](https://github.com/kotatogram/kotatogram-desktop/pull/242)
* **Снято ограничение на размер окна.** Это изменение позвоняет использовать приложение на более малых экранах. [Добавлено контрибьютором.](https://github.com/kotatogram/kotatogram-desktop/pull/238)

## Исправления
* Исправлена работоспособность протокола tg:// в системе. Это должно исправить проблему с ссылками в браузере.
* Исправлена опция «Внешний видеоплеер».

## Известные баги
* **Вылет при открытии анимированной аватарки в режиме «картинка-в-картинке».** Это происходит из-за привязки PiP к сообщению, которого, разумеется, нет в случае с аватарками пользователя. В TDesktop такого не происходит, потому что у анимированных аватарок нет элементов управления в принципе.
* **Неработоспособность автозагрузки медиа.** Замечено на 32-битной версии приложения под Windows, в 64-битной версии под Windows она работает. Велика вероятность, что это баг Visual Studio (который когда-то уже был), поэтому на то, чтобы искать подходящий обходной способ, нужно время. Ну или на то, чтобы баг был исправлен на уровне компилятора.
