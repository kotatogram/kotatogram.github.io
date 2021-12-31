+++
title = 'Вышел Kotatogram 1.4.8!'
date = "2021-12-31T20:00:00+03:00"
description = 'Пару фиксов для иконок у имён, и улучшение настроек шрифтов.'
+++

Этот релиз весьма неожиданный, но важный, из-за критичного вылета в «Избранном» (Saved Messages). Если вы на него не наткнулись, вам повезло, но всё же лучше обновиться.

{{< subheader >}}
## Скачать стабильную 1.4.8
на основе Telegram Desktop 3.3
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 18.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-linux.tar.xz" class="icon solid fa-download primary" >}}
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
Поддерживает macOS 10.15 и выше.
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения
* **Улучшенные настройки шрифтов.** Благодаря стараниям [@ilya-fedin](https://github.com/ilya-fedin), теперь в настройках шрифта есть их полный список для каждого поля, а также есть слайдер для изменения размера шрифта. Ранее размер шрифта можно было изменить только в JSON-настройках. Я лишь добавил «+» перед неотрицательными числами, чтобы намекнуть на то, что размер шрифта относительный.

## Исправления
* Исправлен критичный вылет в «Избранном» (Saved Messages).
* Исправлена некликабельная часть имени автора в сообщении, если рядом с ним есть иконка.
