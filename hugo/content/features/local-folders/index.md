+++
Title = "Local folders"
description = "Folders for chats without sync, but with additional features."
+++

**Warning:** This feature currently only in [beta](/download#beta).

* [Change log](#changelog)

---

For a long time users have been requested folders, and Telegram made them. But of course, folders have limitations:

* Folder count: no more than 10
* Folder name length: no more than 12 symbols
* Chat count: 100 explicitly added (including pinned), 100 explicitly excluded
* Icons: 23 items
* Filters: chat type, enabled notifications, unread, non-archived

Local folders have additional features and they have some limitations removed.

### Removed lmitations

_Please note: even though explicit limitations are removed, there are some implicit technical imitations. But they're so big that you can hit them only when you will test for it._

Following limitations were removed from local folders:

#### Folder name length

Only thing worth noting here: in side bar folders show only three lines:

![](/features/local-folders/long-folder-name.png)

Other than that, folder name can be really long.

#### Folder count

Since Telegram Desktop have scrolling for folder panel, this limitation also have been removed.

#### Chat count (added and excluded)

Of course, limitation has been removed here too. Also removing this limitation affected other limitation: pinned chat count in folder.

### Icons

In Telegram Desktop's cloud folders you can select any of 23 icons:

![](/features/local-folders/icons-tdesktop.png)

Kotatogram Desktop's local folders have 12 new icons added, which make 35 icons in total:

![](/features/local-folders/icons-kotatogram.png)

### Filters

Aside of chat type filters, Telegram offers additional filters in folders:

![](/features/local-folders/filters-cloud.png)

Kotatogram adds 6 new filters to them:

![](/features/local-folders/filters-local.png)

* **Not owned/administrated**
  Only chats when you're owner or/and administrator will stay.
* **Owned/administrated**
  Only chats when you're not owner or/and not administrator will stay.
* **Not opened in this session**
  Only chats opened recently will stay.
* **Из других папок**
  Only chats that weren't added to any other folder will stay.

### Drawbacks

Only drawback of local folders is pretty obvious: lack of synchronization between apps. But however, to transfer them to other client you just need to copy `kotato-settings-custom.json` file from your `tdata` to `tdata` of client to move folders to.

## Change log {#changelog}

### 1.4

Fixed missing chats explicitly added or removed from folder.

### 1.3.9 beta

First appearing of feature.
