-- AppleScript to Import vCard File into Daylite and Complete Tasks
on run argv
    if (count of argv) is 0 then
        display dialog "Please provide the vCard file name." buttons {"OK"}
        return
    end if
    
    set vcardFile to item 1 of argv
    tell application "Daylite"
        -- Import vCard file
        set importedContacts to import from vcard file vcardFile
        repeat with contact in importedContacts
            -- Link contact to project
            set linkedProject to first project whose name is "Software Crafters Unconference 2024"
            add contact to linkedProject
            
            -- Add tag to contact
            add tag "Unconference2024" to contact
            
            -- Add contact to group
            set targetGroup to first group whose name is "Attendees - Software Crafters Unconference 2024"
            add contact to targetGroup
        end repeat
    end tell
end run
