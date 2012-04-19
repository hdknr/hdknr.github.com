.. list-table:: Reserved Member Definitions

    *   - Member  
        - Type    
        - Description

    *   - user_id 
        - string  
        - **REQUIRED** Identifier for the End-User at the Issuer.

    *   - name    
        - string  
        - End-User's full name in displayable form including all name parts, ordered according to End-User's locale and preferences.

    *   - given_name  
        - string  
        - Given name or first name of the End-User.

    *   - family_name 
        - string  
        - Surname or last name of the End-User.

    *   - middle_name 
        - string  
        - Middle name of the End-User.

    *   - nickname    
        - string  
        - Casual name of the End-User that may or may not be the same as the given_name. For instance, a nickname value of Mike might be returned alongside a given_name value of Michael.

    *   - profile 
        - string  
        - URL of End-User's profile page.

    *   - picture 
        - string  
        - URL of the End-User's profile picture.

    *   - website 
        - string  
        - URL of End-User's web page or blog.

    *   - email   
        - string  
        - The End-User's preferred e-mail address.

    *   - verified    
        - boolean 
        - True if the End-User's e-mail address has been verified; otherwise false.

    *   - gender  
        - string  
        - The End-User's gender: Values defined by this specification are female and male. Other values MAY be used when neither of the defined values are applicable.

    *   - birthday    
        - string  
        - The End-User's birthday, represented as a date string in MM/DD/YYYY format. The year MAY be 0000, indicating that it is omitted.

    *   - zoneinfo    
        - string  
        - String from zoneinfo [zoneinfo] time zone database. For example, Europe/Paris or America/Los_Angeles.

    *   - locale  
        - string  
        - The End-User's locale, represented as a BCP47 [RFC5646] language tag. This is typically an ISO 639-1 Alpha-2 [ISO639‑1] language code in lowercase and an ISO 3166-1 Alpha-2 [ISO3166‑1] country code in uppercase, separated by a dash. For example, en-US or fr-CA. As a compatibility note, some implementations have used an underscore as the separator rather than a dash, for example, en_US; Implementations MAY choose to accept this locale syntax as well.

    *   - phone_number    
        - string  
        - The End-User's preferred telephone number. E.164 [E.164] is RECOMMENDED as the format of this Claim. For example, +1 (425) 555-1212 or +56 (2) 687 2400.

    *   - address 
        - JSON object 
        - The End-User's preferred address. The value of the address member is a JSON [RFC4627] structure containing some or all of the members defined in Section 2.4.2.1.

    *   - updated_time    
        - string  
        - Time the End-User's information was last updated, represented as a RFC 3339 [RFC3339] datetime. For example, 2011-01-03T23:58:42+0000.

