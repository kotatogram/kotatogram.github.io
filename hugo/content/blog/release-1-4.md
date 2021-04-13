+++
title = 'Kotatogram 1.4 released!'
date = "2021-04-14T00:48:00+03:00"
description = 'Time for Kotatogram to update too.'
+++

For a long time this Kotatogram was abandoned. But actually it wasn't, I just had no time to fix bugs. Some are still can be present, but since mostly it works as it should, I'm releasing to stable branch.

{{< subheader >}}
## Download stable 1.4
based on Telegram Desktop 2.7.1
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4/1.4-win32-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4/1.4-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4/1.4-win64-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4/1.4-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4/1.4-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4/1.4-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Changes

First important thing is that Telegram Desktop sources has been updated to 2.7.1, which means that now Kotatogram have all latest features from it:

* Multi-account (if you're updating from stable)
* Video calls (if you're updating from stable)
* Anonymous administrators
* Comments
* Multi-pins
* File albums
* Voice message recording without constantly holding it
* Voice chats in groups and channels
* Temporary invite links

And many other.

### Changes from last stable version

* **Local folders**
  Aside from cloud folders, Kotatogram now has local ones. Only drawback is the lack of synchronization. But in return they have limits removed as much as possible, and added new icons and filters. Also there is a separate page about them: [Local folders](/features/local-folders/).
* **Multi-forward and unquoted forward**
  Long-suffering multi-forward and unquoted forward now finally has come to stable Kotatogram version. Now you can forward messages to multiple chats at once, or send them without author. You can also use message grouping options to group them in albums, or other way around, send albums as separate messages. And yes, if you want to return old forward window behavior where chat was opened on selection, you can enable "Open chat on click" option.
* **Reworked administrator info**
  Now you can see rank and last seen status in administrator list, and who promoted them in administrator info.
* **Mention user from member list context menu**
  By the way, it also works in administrator list: calling admin to clear the group should be easier.
* **Better keyboard navigation in calendar**
  Arrow keys are now used for day selection, and Page Up/Page Down for month selection. Also you can jump to last date with End key. And no, it's not the same as jumping to last message.
* **Pinned message without sound by default**
  If you mistakenly pin message without sound, you can calmly re-pin it with sound without any additional yelling, which can't be said for pinning with sound by mistake.
* **"Retain selection after forward" option**
  This option will allow staying messages selected after sending in case you want to delete them afterwards.
* **Option to disable emoji panel on hover**
  I had no problems with it, but people complained about accidental clicks asking about this feature. So, here it is. If you need pop-up panel instead of side panel, you can right-click emoji button.
* **Expanded downloaded media clear time selection**
  Aside from default options (from 1 week to 1 year), you can now set it from 1 to 6 days.
* **Manage group/channel buttons in profile**
  For this feature [@Deelite](https://t.me/Deelite) has made a concept, and even though it wasn't fully made, it should be more convenient now: at least you don't need every time to open "Manage group" to see recent actions log. Bonus: you can see administrators of any group now even if you're not an admin.
* **Fixed bug with switching notification sound in tray**
  Or, rather, notification sound was switching, but label wasn't updated. Now it's updating.
* **Fixed links to settings sections**
  Links such as tg://settings/kotato are working again.
* **More click to copy in profile**
  You can now copy ID, username and phone number.
* **Delete own messages in private chats and basic groups for everyone by default**
  I think it's more preferable option.
* **Additional info about chats in folder**
  For users in folder there is a contact status shown, and for chats it's type and admin rights if you have any.
* **More clean notifications**
  Account name in notification now shown only if notifications has been received on other account.
* **Hotkey to go to date in chat**
  By default Ctrl+H is used, but if you want to set it to other hotkey, command is called `jump_to_date`.
* **Polls with multiple answers now have square checkboxes**
  Since square checkboxes are already associated with multiple choice, differentiate polls with single choice and polls with multiple choices should become easier. Idea taken from Telegram X.
* **Better groups and channels info in chat selection windows**
  Groups in these lists are now showing with owner icon (colored star)/admin icon (gray star) near the name, type and member/subscriber count. These windows can be seen when adding/removing chats in folder, privacy exception settings.
* **Improved search for theme colors in editor**
  Now search is checking not only in beginning of key, but also in the middle or in end.
* **Ability to colorize chat header separately from TDesktop theme**
  Utterly experimental ability to make Kotatogram themes on the top of Telegram Desktop themes. Colors related to Kotatogram are starting with `ktg` and always using existing Telegram Desktop colors by default, so you can use custom themes without pain.
* **New deleted account icon in chat list**
  This icon has been taken from official Telegram Android app.
* **Hide "All chats" folder and "Edit" folder button now can be hidden from context menu**
  It's an additional way to quickly change the option. It's possible that there will be more quick changes ways for more features in future.
* **Delete sticker from recent button when hovering it**
  Interesting fact: this button exists in Telegram Desktop too, but for some reason it's shown only for so-called "local stickers" (probably unsent or something like that). But since this feature could be useful for any stickers, I've decided to show it for everyone.

### From [ilya-fedin](https://github.com/ilya-fedin)

Aside from AppImage builds, that replaced static binaries, stable version now have macOS build. Please note that builds are very experimental, since neither I, nor [ilya-fedin](https://github.com/ilya-fedin) have any macOS device to test them properly, so tester help in this case is extremely important. Also keep in mind that macOS build works only on 10.15 version or higher.

Also [ilya-fedin](https://github.com/ilya-fedin) added some new features and fixes:

* **Ability to set your own API ID and hash**
  Initially the way to set them from environment variables was made (`KTGDESKTOP_API_ID=YOUR_ID` and `KTGDESKTOP_API_HASH=YOUR_HASH`), but I've added the ability to set them from start parameters (`-api-id YOUR_ID` and `-api-hash YOUR_HASH`). Since environment variables are used by default, you can use `-no-env-api` start parameter, to forcefully use embedded credentials or credentials from start paramters.
* **Disable tray icon counter**
  Earlier this option was Linux-only, since it was getting the value from environment variable. If you don't like tray counter for any reason, you can disable it.
* **System Telegram icon**
  This option is still Linux-only, but instead of environment variable it has been moved to Kotatogram Settings. It allows to use Telegram icon from system theme instead of Kotatogram, which could be important if your theme doesn't have Kotatogram icon.
* **Switching tray icon without restart**
  Keep in mind that changing tray icons without restart works only for embedded ones. If you're using custom icon (through `icon.png`), you still have to restart the client.
* **Advanced info about device in session**
  Now info is taken from default Qt methods which allows to show more version info. Also you can now see host name in session list.
* **GTK integration option for Linux**
  It's disabled by default for better compatibility with Qt, but it disables some features, and you can have clipboard issues.
* **File choose dialog option for Linux**
  This option changes file choose window to one better looking or more convenient for you. Keeo in mind: GTK option can be disabled by "GTK integration" option, and other options can be disabled on build time, but AppImage should have all options available.
* **Qt scaling engine option**
  This option allows to get app scale with same method as other Qt apps, through `QT_SCALE_FACTOR` environment variable, but it disables custom scaling inside the app.
* Fixed scrolling on scales other than 100%.
* Fixes for tray icon on Linux related to XEmbed and SNI.
* System font is now used by default on Linux.
* Fixed bold font when using system one.

### From [64Gram](https://t.me/tg_x64) (former TDesktop-x64)

* **Separated permission "Send stickers and GIFs"**
  This option actually contains four options in it: sending stickers, sending GIFs, sending games, using inline bots.
* **Do not share phone number by default**
  If you're adding to contacts with your number hidden from all, you'll have "Share phone number" checkbox, but official clients have it enabled, which can lead to accidental leak of your phone number.
* **GIF section in shared media**
  Along with photos, videos, shared links, etc., there is now GIF section in shared media.

Also about 64 bit support. Since Telegram Desktop already builds 64 bit Windows versions along with 32 bits, they are now available for Kotatogram too. Moreover, multi-account limit for 64 bit versions on all platforms was expanded to 100. 32 bit Windows build is still 10 because of out-of-memory limit crashes (about 1.5 GB).

### From other users

* Ability to disable expanding messages with monospaced text made in Telegram Desktop. [Added by CrisMystik](https://github.com/kotatogram/kotatogram-desktop/pull/58).
* Conversion of links like `tg://user?id=user_id` to mention when adding through "Create link" window. [Added by the-blank-x](https://github.com/kotatogram/kotatogram-desktop/pull/144).

### Made in Telegram Desktop

* **Disable taskbar icon flash**
  Now this option is in Telegram Desktop and works on all platforms, so its duplicate has been removed. Now it can be found in Settings > Notifications, under "Play sound" checkbox.
* **System window frame**
  Now it can be found in Settings > Advanced > System integration under "Show taskbar icon" checkbox.
* **Highlight of photo in album when opening a message in chat**
  Telegram Desktop made it a little different: instead of changing opacitly of all other photos, only target photo is highlighted with message highlight color. Also it was works on file albums too. Of course, duplicate of this feature has been removed.

### Changes from last beta version

* **Time chooser in scheduling window has been restored to default behavior**
  Probably 1.3.9 behavior will return later as option.
* **Ctrl+J for jump to date in chat was replaced to Ctrl+H**
  Telegram Desktop use Ctrl+J for Contacts for default now, so hotkey is moved slightly left.
* **Option "Mark all message as read" now more visible**
  In Telegram Desktop it can be found in folder context menu and archive context menu, and also in account context menu... if you're holding Shift+Alt before right-clicking. Now this option has been moved to context menu that doesn't need holding Shift+Alt. Bonus: you can now logout from current account right from account list.
* **Fixed "Recent stickers limit" option**
  Because of checking error you could set value in JSON config to incorrect value.
* **Outlined Kotatogram icon in settings**
  Since Telegram using ountlined icons everywhere, I've made icon near "Kotatogram Settings" menu item outlined so it matches with others. Also old settings icon is outlined too.
* **Fixed rounding of profile picture choose button**
  Bug could be seen in "New Group/Channel" window. Button was always shown as round regarding of rounding settings. Now everything is shown correctly.
* **Fixed showing time of service messages in chat list**
  Since chat list has time of last message already, there is no need in duplicating it.
* **Restored message about promoting group to supergroup**
  Since the attempt for merging group and supergroups in Telegram leads to confusion, promotion message has been restored.
* **Service message time shown only when needed**
  Mostly it's done because time is duplicated. For example, in recent actions "User edited message:" action time has been shown in next message.
* **Fixed emojis in section titles**
  Bug can be seen in scheduled messages header if user had emoji in name.
* **Fixed adding chats to local folder**
  Earlier after restart users in local folder added or removed explicitly were shown as empty.
* **Bot button callback data now can be seen in hover tooltip**
  It's an addition to already existing feature allowing to copy callback data.
* **Service message time now copied correctly**
  Earlier it can be selected but not copied.
* **Fixed repeating changelog notifications**
  Bug appeared if app was working for a long time after the update.
* **Fixed opening blocked user profile in group**
  Earlier profile was opened under blocked users window, and repeated opening led to crash.
* **Confirm before calling is now enabled by default**
  Since accidental click can be more annoying, it's better to enable it by default.
* **Profile ID is now shown by default**
  Since there are many questions about how to enable it, it's enabled by default in "Bot API" mode.
* **Restored crash reporter**
  Keep in mind: since I have no place for dumps, you should send them manually from `profile_folder/tdata/dumps`.
* **"Invite links" are now shown in profile**
  Along with blocked/administrator list and recent actions, this item also duplicated in profile.
* **Fixed repeated opening of Recent actions**
  Earlier repeated opening made filter broken.

## What's next?

Now, when update is released, I'd like to talk about what future awaits Kotatogram.

Even though there are many things to make, existing ones shouldn't be forgotten. So aside of new features, there could be changes in Kotatogram related to existing functionality.

### Settings menu changes

Settings menu currently has many items and it's bad because you can get lost in menu like this (and effect will grow since feature count is growing).

So I'm planning to improve menu to get rid of getting lost in settings.

### Test branches

Some time ago I've started to publish test versions in fork chat. Why I haven't announced it in channel? Because they were too unstable in my opinion, needed to be tested properly, and required relatively quick feedback.

But they had problems too: test version were initially built withot auto-updater, then with auto-updater, but since there was no proper test branch, this updater only can update to stable or beta. Also they had no separate versioning, which caused troubles guessing version that had bug.

So I'm planning to make test branches that will work separately from stable and beta. Why branches instead of branch? Because I can test there new features before releasing and basically experiment in them. In that case rolling back features will be less painful then rolling back beta features. Especially if they're big and almost ready. I don't want next release to be year long.

### Improving about info

Currently app information windows are mostly default. There is a need to rework them because of few reasons.

1. **Improved change logs**
  Currently change log is a placeholder leading to channel. In future I'd like change logs to say at least about big changes in current versions (or make change logs in separate window). Or ability to see all previous change logs.
2. **Improved author crediting**
  Aside of fact that Kotatogram Desktop based on Tewlegram Desktop, and, consequently, inherits all features made by everyone how contributed to it, many people contributed to Kotatogram Desktop, and it's natural that people want to be shown as co-authors. 
3. **Improved help**
  People frequently ask questions about specific features, so I'd like to make it easy at least partially with built-in ability to see help topic about specific feature. Or at least redirect them to chat where they can ask about them.

---

Finally, I'd like to thank anyone who suggesting features, making features, translates (there is a Crowdin page for translations now), reports bugs and helps to debug them, or just uses Kotatogram. There are many plans, and I hope they will come true eventually. But for now you can update and use new Kotatogram features.
