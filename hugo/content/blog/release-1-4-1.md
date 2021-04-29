+++
title = 'Kotatogram 1.4.1 released!'
date = "2021-04-29T13:18:00+03:00"
description = 'Fixes and source update to 2.7.4.'
+++

This release have no new features, but it has bug fixes. Also this version based on Telegram Desktop 2.7.4, which has scheduled voice chats and payments. More about the update on Telegram site: https://telegram.org/blog/payments-2-0-scheduled-voice-chats

{{< subheader >}}
## Download stable 1.4.1
based on Telegram Desktop 2.7.4
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win32-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win64-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
### macOS {#stable-macos}
Supports macOS 10.15 and higher. 
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.1/1.4.1-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Changes

* Description for settings with radio buttons (one-from-many selection) now shown in smaller font. Otherwise options are cut by window size when window height is low.
* Removed redundant separator in own profile. Since there is no notifications switch there, so it was odd.

## Fixes

* Kotatogram Desktop MPRIS was separated from Telegram Desktop MPRIS.
* Fixed crash when right clicking emoji button when emoji sidebar is opened and "Emoji panel on hover" is disabled.
* Possible fix for repeating changelog message. Bug could be caught if app wasn't closed after update for a long time.
* Top notification switch is not shown in own profile anymore.
