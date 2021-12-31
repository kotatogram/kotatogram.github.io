+++
title = 'Kotatogram 1.4.8 released!'
date = "2021-12-31T20:00:00+03:00"
description = 'Few fixes near icon names and better font settings.'
+++

This release is unexpected, but important because of severe crash in Saved Messages. If you haven't caught it, you're in luck, but it's better to update anyway.

{{< subheader >}}
## Download 1.4.8 stable
based on Telegram Desktop 3.3
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 18.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-linux.tar.xz" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
#### Alternative options
Please note that update can be delayed.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="FlatHub page" link= "https://flathub.org/apps/details/io.github.kotatogram" >}}
    {{< button title="Repology page" link= "https://repology.org/project/kotatogram-desktop/versions" >}}
{{< /button-group >}}

{{< subheader >}}
### macOS
Supports macOS 10.15 and higher.
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.8/1.4.8-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}


## Changes

* **Better font settings.** Thanks to the [@ilya-fedin](https://github.com/ilya-fedin)'s work, there is now a full list of fonts after an each font name field, and also there is a slider to change font size. Earlier font size could be changed only through JSON settings. I've only added a "+" before non-negative numbers to give you a hint that font size is relative.

## Fixes

* Fixed severe crash in Saved Messages.
* Fixed non-clickable part of message author name if there an icon near it.
