+++
title = 'Kotatogram 1.4.6 beta released!'
date = "2021-12-18T22:51:00+03:00"
description = 'Updated sources with the grain of new features.'
+++

With this version starts the support of sponsored messages from Telegram. I'll remind that it's necessary change because without support of these messages the app is at risk of disabling via API ID. Also all previous version have lost the ability to open the channels with content forwarding and saving restriction enabled. This version supports these channels with support for this restriction.

This version has some known bugs, and there was no time to fix them since there is a need to release as soon as possible. Maybe there will be found the other bugs in beta. But there not just new sources and new bugs: contributors also have added some new features that you may like.

{{< subheader >}}
## Download 1.4.6 beta
based on Telegram Desktop 3.3
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-linux.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.6/1.4.6-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}


## Changes
* **Ability to disable remembering image compression when sending.** Telegram Desktop always remembers last sending mode after images were sent. It's handy, but sometimes it leads to sending images without compression by mistake when sending fast, after which you need to re-send them again. Or the other way around. You can select the mode you need by "Compress images by default" option. [Added by contributor.](https://github.com/kotatogram/kotatogram-desktop/pull/243)
* **Custom auto-replaces now work without emoji replacement enabled.** In case if you don't like default auto-replacements but you need those you have set in JSON file. If you forgot how to set them, there is [a page that wasn't moved to site from wiki](https://github.com/kotatogram/kotatogram-desktop/wiki/Custom-text-replaces). [Added by contributor.](https://github.com/kotatogram/kotatogram-desktop/pull/242)
* **Removed window size restriction.** This change allows to use the app on much smaller screens. [Added by contributor.](https://github.com/kotatogram/kotatogram-desktop/pull/238)

## Fixes
* Fixed tg:// link protocol in system. It must solve browser links problems.
* Fixed "External video player" option.

## Known bugs
* **Crash when opening animated profile picture in picture-in-picture mode.** It happens because PiP is tied to message, which, of course, doesn't exist in case of profile photos. It doesn't happen with TDesktop since animated profile pictures doesn't have any controls.
* **Automatic downloading of media doesn't work.** Noticed on 32-bit Windows version, 64-bit Windows version works fine. It's highly probable that it's a Visual Studio bug (which actually happened earlier), so the time is needed to find a fitting workaround. Or for bug to be fixed on the compiler level.
