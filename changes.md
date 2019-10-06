# Changes

Here is the list of all changes from official app.

## Current changes

* Mention user by its name instead of username: right click on mention suggestion.
* Option "Nobody" in profile photo privacy settings.
* Increased size of caption field to 150px (\~5 lines).
* Show and hide pinned message from chat menu.
* Show linked dicussion group/channel in profile.
* Always show edit timer.
* Show restriction date to user.
* "About" box link in drawer moved to app name to increase space for version.
* JSON-configured options. You have to restart app to see changes.
  * `fonts` - app font repacling.
    * `main` - replace main font.
    * `semibold` - replace semibold font.
    * `semibold_is_bold` - should semibold font be set to bold or not.
    * `monospaced` - replace monospaced font.
  * `sticker_height` - sticker height in chat (from 128 to 256).
  * `big_emoji_outline` - enable/disable white outline for big emoji.
  * `always_show_scheduled` - show scheduled messages button always or only when there are scheduled messages.
  * `show_chat_id` - show chat id in profile.

## Was made into official app
* Allow scales below 100 to be saved in local settings.
* Resize photo message when there are additional texts (author name or caption).

## Deprecated
* Font changing start options `-mainfont`, `semiboldfont`, `semiboldisbold`, `monospacefont`.
