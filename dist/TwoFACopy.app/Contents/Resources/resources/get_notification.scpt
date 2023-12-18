tell application "System Events"
    if not (exists window "Notification Center" of application process "NotificationCenter") then
        return ""
    end if

    try
        set _groups to groups of UI element 1 of scroll area 1 of group 1 of window "Notification Center" of application process "NotificationCenter"
        set notificationsList to {}

        repeat with _group in _groups
            set titleText to value of static text 1 of _group
            set subtitleText to value of static text 2 of _group
            set messageText to ""
            if (count of static texts of _group) > 2 then
                set messageText to value of static text 3 of _group
            end if

            if titleText is not "" or subtitleText is not "" or messageText is not "" then
                set end of notificationsList to titleText & "|||" & subtitleText & "|||" & messageText
            end if
        end repeat

        return notificationsList

    on error errMsg
        return ""
    end try
end tell
