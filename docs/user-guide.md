# CRM for Jira: User Guide

CRM for Jira keeps your sales pipeline inside Jira. You track leads, contacts,
companies, deals, products and tasks in one place, and you can link any record
to a Jira work item.

Open it from the **Apps** menu in Jira, then choose **CRM for Jira**. There is
nothing to sign in to: you use the same account as in Jira.

## Contents

1. [Finding your way around](#finding-your-way-around)
2. [A typical sales flow](#a-typical-sales-flow)
3. [Leads](#leads)
4. [Deals](#deals)
5. [Contacts and Companies](#contacts-and-companies)
6. [Products](#products)
7. [Tasks](#tasks)
8. [Notes, Timeline and record cards](#notes-timeline-and-record-cards)
9. [Searching, filtering and saved views](#searching-filtering-and-saved-views)
10. [Working with many records at once](#working-with-many-records-at-once)
11. [Import and export](#import-and-export)
12. [Dashboard](#dashboard)
13. [Reports](#reports)
14. [Activities](#activities)
15. [Settings](#settings)
16. [Linking to Jira and sharing records](#linking-to-jira-and-sharing-records)
17. [Good to know](#good-to-know)

## Finding your way around

The menu on the left has ten sections:

| Section | What it is for |
|---|---|
| **Leads** | People or companies that might become customers |
| **Deals** | Sales opportunities moving through the pipeline |
| **Contacts** | People you deal with |
| **Companies** | Organisations, including parent and subsidiary links |
| **Products** | Your catalogue of things you sell |
| **Tasks** | To-dos, calls, emails and meetings |
| **Dashboard** | Numbers that show what needs attention |
| **Activities** | A log of who changed what |
| **Reports** | Charts and breakdowns, with a period comparison |
| **Settings** | Currency, the stale-deal threshold and data tools |

A number in brackets after a section name, such as **Tasks (3)**, means that
section has items needing attention (for example overdue tasks).

The search box at the top searches every section at once.

## A typical sales flow

1. A new prospect arrives. Add it as a **Lead**.
2. Contact them and update the lead's status. When it looks real, press
   **Convert**. The lead becomes a **Deal**.
3. Move the deal through the stages, adding notes, products and tasks.
4. When it ends, mark the deal **Won** or **Lost** and say why. Those reasons
   feed the reports.

## Leads

A lead is someone who has shown interest but is not yet a customer.

**Add a lead:** open **Leads**, press **Create Lead**, fill in the form and
press **Create Lead** again. Only the name is required. Useful fields:

- **Status**: New, Contacted, Qualified, Converted or Lost.
- **Rating**: Hot, Warm or Cold.
- **Source**: Web, Referral, Advertisement, Trade Show, Cold Call, Partner or
  Other.
- **Assignee**: who is responsible for the lead.

Two ways to look at leads: **Table** and **Kanban**. Switch with the buttons
above the list. In Kanban, each column is a status.

**Losing a lead:** when you set the status to Lost you are asked for a reason
(Unqualified, No Response, Not Interested, Duplicate, Wrong Contact or Other).

**Converting a lead:** open the lead and press **Convert to Deal**. You are
asked to confirm. The app creates a deal, carries over the lead's products,
and marks the lead Converted. The lead's card then shows the **Converted deal**
so you can jump to it.

Two leads or contacts cannot share the same email address. The app tells you
if you try.

## Deals

A deal is a sale you are working on.

**Add a deal:** open **Deals**, press **Create Deal**. Fields include name,
amount, **Close date**, **Next step** and its due date, **Type** (New Business,
Existing Business or Renewal), the contact and the company, and the owner.

### Stages

Every deal is in one of six stages. Each stage has a default chance of
winning:

| Stage | Win probability |
|---|---|
| New | 10% |
| Discovery | 25% |
| Negotiation | 50% |
| Proposal | 75% |
| Won | 100% |
| Lost | 0% |

You can set a different probability on a single deal if you know better.
**Weighted pipeline** is each open deal's amount multiplied by its probability.
It is a more realistic forecast than the raw total.

Change a stage from the deal's stage selector. There is no drag and drop.

**Won and Lost:** press **Mark as Won** or **Mark as Lost** on the deal. You
choose a reason (for example *Best Price* or *Product Fit* for a win, *Lost to
Competitor* or *No Budget* for a loss). Please always pick one, because
Reports break results down by reason.

### Kanban and Table

Deals open as a **Kanban** board with a column per stage and the total value of
each column. Press **Table view** to see them as a sortable list, and
**Kanban view** to go back.

### Products on a deal

Open a deal and add products from your catalogue as line items. The deal's
amount follows the line items.

### Stale deals

A deal is flagged **stale** when it has not changed stage for 14 days. An
administrator can change that number in [Settings](#settings). Use the **Stale**
filter to list them.

## Contacts and Companies

**Contacts** are people. Fields include name, title, email (and a secondary
email), phone, LinkedIn, tags, the company they work for, and who they
**Report to**. Tick **Do not contact** for people who must not be contacted;
there is a quick filter to show or hide them.

**Companies** are organisations. Fields include website, industry, address,
number of employees, annual revenue, tags, owner and a **Parent** company, so
you can model subsidiaries.

Opening a contact or company shows everything linked to it: deals, tasks,
notes and the people at that company.

**Deleting** a contact or company that has linked records shows a warning
first, so nothing disappears by accident.

**Merging duplicates:** open the duplicate record, choose **Merge into**, pick
the record you want to keep, and confirm with **Merge and Delete**. Everything
that pointed at the duplicate is moved to the record you keep.
Merging cannot be undone.

## Products

The **Products** section is your catalogue: name, **SKU**, **Price**, **Cost**,
category, unit (License, Service, Project, Subscription or One-time) and a
description. The list shows the margin. Open a product to see which deals use
it. The **Unused** filter lists products that no deal uses.

## Tasks

Tasks are things to do. Give a task a title, a type (To-do, Call, Email,
Meeting or Other), a priority (High, Normal or Low), a due date in
`YYYY-MM-DD` format and an assignee. A task can be tied to a lead, contact,
company or deal.

You can also add a task straight from a record's card (see below). Tick a task
to complete it. The **Overdue**, **Due Today** and **My Tasks** filters keep
your day under control, and the **Dashboard** lists tasks that are due soon.

## Notes, Timeline and record cards

Click a record's name anywhere in the app to open its **card**. Cards have
two columns: the details on one side, and three tabs on the other.

- **Tasks**: tasks tied to this record, with a box to add a new one.
- **Notes**: type in the *Add a note…* box and add it. Notes can be up to
  2000 characters. Notes are included in search.
- **Timeline**: every change made to the record, with who did it and when,
  for example *rating: Cold → Hot*.

The card also shows **Last activity**.

## Searching, filtering and saved views

**Search box in each section** searches that section. **Global search** at the
top searches all sections, including note text.

**Quick filters** sit above each list. Which ones you see depends on the
section: *My Leads/Deals/Contacts/Companies*, *Stale*, *Overdue*, *Due Today*,
*Unassigned*, *No Next Step*, *Do Not Contact*, *Unused* and filters by stage,
status, source, rating, industry and category. The numbered tiles on lists
work as filters too: click a tile and the list narrows to exactly those rows.

**Sorting:** click a column heading.

**Saved views:** once you have filters set, **Save view** appears. Give the view
a name and press **Save**. It shows up as a button above the list; click it to
bring those filters back, or **×** to delete it. Saved views are yours alone.

## Working with many records at once

Tick the boxes at the start of rows. Buttons appear for:

- **Assign owner**: choose a person and apply it to every selected row.
- **Change stage** (on deals).
- **Delete**: asks you to confirm before deleting.
- **Export selected rows to CSV**.

## Import and export

**Export:** press **Export CSV** on a list. A window shows the data as text.
Select all (Ctrl+A or Cmd+A), copy it, and paste it into a spreadsheet or a
file ending in `.csv`. Exports follow your current filters. Settings can also
export all your data.

**Import:** press **Import CSV** on Contacts, Companies, Leads, Deals,
Products or Tasks. Paste CSV text whose **first row is the column names**.
The window lists the column names it recognises. Each row is checked exactly
like the normal form, so a row with an invalid email, for example, is skipped
and listed with the reason; the other rows are still imported.
Check a few rows after importing: nothing can be undone in bulk.

## Dashboard

The **Dashboard** groups numbers by what you would do with each one, for
example open pipeline, weighted pipeline, win rate, sales cycle length,
tasks due soon and rep performance.

The tiles are clickable. Click **Stale** or **No Next Step** and you land on
the list of exactly those deals.

## Reports

**Reports** are grouped into sections:

- **Pipeline**: deals by stage, value by stage, forecast by close month,
  open pipeline by owner, average days spent per stage, deals by type.
- **Leads**: by status, source and rating; conversion rate by source and by
  rating; lost leads by reason.
- **Revenue**: by lead source, product, category and assignee.
- **Deal outcomes**: why you win and why you lose.
- **Accounts** and **Products**: companies by industry and size, products by
  category.
- **Operations**: tasks by type, priority and assignee.
- **Data quality**: **Potential Duplicates**, to find records worth merging.

**Compare periods:** pick a period (This month, Last month, This quarter, This
year, Last 30 days) to see won value, deals won, deals lost, win rate and new
deals next to the period before, with the change.

**Report snapshot:** press it to get a short text summary. Copy it into a Jira
comment, a Confluence page or a chat message, and it shows up formatted.

Several tables have their own **Export to CSV** button.

## Activities

**Activities** is the log of every change: who created, edited, reassigned,
converted, merged or deleted what, and when. Filter by record type or event
type. Only the most recent 500 entries are kept.

## Settings

- **Currency**: USD, EUR, GBP, JPY or INR. It changes how amounts are shown
  everywhere; it does not convert existing amounts.
- **Stale deal threshold**: days without a stage change before a deal is
  flagged stale, from 1 to 365 (default 14).
- **Data administration**: export all of your data.
- **Audit log**: how many entries are kept.

Press **Save** after changing a setting. Settings apply to everyone on your
Jira site.

## Linking to Jira and sharing records

**Link to a work item:** many records have a **Jira** field. Type a work item
key such as `PROJ-123` and save. The app checks the item exists and that you can
see it, then shows its summary and status next to the record. Use it to point
a deal at the ticket that delivers it.

**Share a record:** every card has its own web address. When you open a card,
the address in your browser changes. Copy it and paste it into a Jira
comment, and whoever opens it lands on the same record.

## Good to know

- **Required fields** are marked. Email, phone and website are checked for a
  sensible format, and amounts must be zero or more.
- **Dates** are typed as `YYYY-MM-DD`, for example `2026-11-30`. There is no
  date picker.
- **Saving takes a moment.** Wait for the window to close before you move on.
- **Not included on purpose:** email, calendar and file attachments on
  records, notifications (Jira already has its own), multiple pipelines and
  custom stages, and drag and drop.
- **Large data sets:** the app loads all records when it opens, so it is
  comfortable up to a few thousand per section. If it starts to feel slow,
  tell your administrator.
