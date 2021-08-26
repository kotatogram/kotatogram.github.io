+++
title = 'Kotatogram 1.4.3 beta released!'
date = "2021-08-26T22:16:00+03:00"
description = 'Some minor features and fixes.'
+++

This update is pretty small in features, but it contains some internal work with versioning and updates that allows fasters rebuilds. Also this time I haven't forgot about translations, and Kotatogram even now has German translation.

{{< subheader >}}
## Download 1.4.3 beta
based on Telegram Desktop 2.8.11
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Changes

* **Reworked sending without "via @bot" tag**. Global setting was removed, and context menu item now sends inline query preview. Also added silent and scheduled sending for previews.
* **Optional hotkeys to restart application and to reload Kotatogram translation.** `restart_app` for restart и `reload_lang` for translation reload can be set as before: `tdata/shortcuts-custom.json`.
* Updated translations, including phrases from previous version.

## Fixes

* Fixed blocking user in "Recent Actions".
* Fixed errors and crashes in AppImage related to gdk-pixbuf.
