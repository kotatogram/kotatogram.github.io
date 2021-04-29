+++
title = 'Вышел Kotatogram 1.4.1!'
date = "2021-04-29T13:18:00+03:00"
description = 'Исправления и обновление исходников до 2.7.4.'
+++

В этом релизе пока без новых функций, но зато есть исправления. Также эта версия основана на Telegram Desktop 2.7.4, в которой появились отложенные голосовые чаты и платежи. Подробнее об обновлении на сайте Telegram: https://telegram.org/blog/payments-2-0-scheduled-voice-chats

{{< subheader >}}
## Скачать стабильную 1.4.1
на основе Telegram Desktop 2.7.4
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win32-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win64-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 16.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения

* Описание для настроек с радио-кнопками (выбором одного варианта из нескольких) теперь отображается шрифтом меньшего размера. В ином случае при минимальной высоте окна варианты обрезаются размером окна.
* Убран лишний разделитель в собственном профиле. Учитывая, что там нет переключателя уведомлений, он там был только лишним.

## Исправления

* MPRIS Kotatogram Desktop был отделён от MPRIS Telegram Desktop.
* Исправлен вылет по правому клику на кнопку эмодзи, если была открыта боковая панель с эмодзи и отключена «Панель эмодзи по наведению».
* Возможное исправление повторяющегося сообщения со списком изменений. Баг можно поймать, если приложение не было закрыто после обновления долгое время.
* Верхний переключатель уведомлений больше не показывается в собственном профиле.
