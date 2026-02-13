---
layout: page
title: Volunteer Email Automation
parent: Volunteer Team
nav_order: 8
---

# Volunteer Email Automation

A Google Apps Script can automatically email volunteers when they sign up. The script:

- Runs daily (set up via Google Apps Script triggers)
- Reads email addresses from the signup spreadsheet
- Sends welcome emails with handbook link
- Tracks which volunteers have been emailed

## Setup Instructions

1. Open your Volunteer Signup Google Sheet
2. Go to Extensions > Apps Script
3. Paste the script below
4. Update the email subject, message, and BCC address
5. Set up a daily trigger: Triggers > Add Trigger > Choose `updateMasterListAndSendEmails` > Time-driven > Day timer

## Google Apps Script Code

```javascript
function updateMasterListAndSendEmails() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("Signup Status");

  // --- 1. Read source email columns ---
  // Update column numbers (A=1, D=4, G=7) based on your spreadsheet layout
  var lastRow = sheet.getLastRow();
  var sourceCols = [
    sheet.getRange(3, 1, lastRow - 2).getValues(), // Column A
    sheet.getRange(3, 4, lastRow - 2).getValues(), // Column D
    sheet.getRange(3, 7, lastRow - 2).getValues()  // Column G
  ];

  // --- 2. Flatten and extract valid emails ---
  var emailRegex = /([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,})/;
  var allEmails = [];
  sourceCols.forEach(function(col) {
    col.flat().forEach(function(e) {
      if (e) {
        var match = e.toString().match(emailRegex);
        if (match) allEmails.push(match[1].toLowerCase().trim());
      }
    });
  });
  var uniqueEmails = [...new Set(allEmails)]; // remove duplicates

  // --- 3. Read current master list and sent status ---
  // Column J = master email list, Column K = sent status
  var masterEmailsRange = sheet.getRange(2, 10, sheet.getLastRow(), 1);
  var masterEmails = masterEmailsRange.getValues().flat().map(e => e ? e.toLowerCase() : "");
  var masterSentRange = sheet.getRange(2, 11, sheet.getLastRow(), 1);
  var masterSent = masterSentRange.getValues();

  // --- 4. Add new emails to master list ---
  uniqueEmails.forEach(function(email) {
    if (!masterEmails.includes(email)) {
      masterEmails.push(email);
      masterSent.push([""]); // Initialize as not sent
    }
  });

  // --- 5. Send emails to unsent addresses ---
  var emailsToSend = [];
  masterEmails.forEach(function(email, i) {
    if (email && (!masterSent[i][0] || masterSent[i][0].trim() === "")) {
      emailsToSend.push({email: email, row: i + 2});
    }
  });

  if (emailsToSend.length === 0) {
    Logger.log("No new emails to send.");
  } else {
    // UPDATE THESE VALUES EACH YEAR
    var subject = "DjangoCon US: Volunteer Information";
    var message = `Hello Volunteer,

Thank you for signing up! This conference would not run without volunteers, so we really appreciate it!

Please review your roles and tasks for your volunteer sign up slot at the Volunteer Guidebook: [HANDBOOK LINK]

We will reach out again with more details. If you have any questions in the meantime, please reach out and let us know!

Best Regards,
[VOLUNTEER CHAIRS NAMES]
DjangoCon US Volunteer Chairs`;

    emailsToSend.forEach(function(entry) {
      MailApp.sendEmail({
        to: entry.email,
        bcc: "[YOUR_EMAIL_FOR_BCC]", // Update with volunteer chair email
        subject: subject,
        body: message
      });
      masterSent[entry.row - 2][0] = "Sent";
    });
  }

  // --- 6. Write updated master list and sent status back to sheet ---
  sheet.getRange(2, 10, masterEmails.length, 1).setValues(masterEmails.map(e => [e]));
  sheet.getRange(2, 11, masterSent.length, 1).setValues(masterSent);

  Logger.log("Emails sent: " + emailsToSend.map(e => e.email).join(", "));
}
```

## Customization Checklist

Before using, update:

- [ ] Sheet name (`"Signup Status"`) to match your spreadsheet
- [ ] Source column numbers (lines 8-12) based on where emails appear
- [ ] Master list columns (J and K, or columns 10 and 11)
- [ ] Email subject line
- [ ] Email message body with current handbook link
- [ ] BCC email address
- [ ] Volunteer chair names in signature

## Spreadsheet Structure

The script expects a sheet named "Signup Status" with:

| Column | Purpose |
|--------|---------|
| A, D, G | Source columns containing volunteer emails (adjust as needed) |
| J | Master list of all unique emails |
| K | Sent status ("Sent" or blank) |

Adjust the column numbers in the script to match your actual spreadsheet layout.
