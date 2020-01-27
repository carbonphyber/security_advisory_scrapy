# Security Advisories

A scraper for Security Advisories published by software manufacturers. These tend to be more descriptive vulnerability articles created by software manufacturers which are the twin entries for a CVE DB entry.

## Purpose

InfoSec professionals struggle to patch their software in a timely way. One of the contributing factors is that many of the tasks which contribute to automating this process is collection of data about each CVE so the InfoSec team can make smart decisions about which software patches to prioritize.

Software manufacturers tend to publish Security Advisories as soon as the software patch is released, but the CVE databases tend to leave CVE entries embargoed until days or weeks after the information is timely. This project aims to patch gaps in CVE DB info with the manufacturer-supplied info.

## Sources

### Current Manufacturer Support

- [Mozilla](https://www.mozilla.org/en-US/security/advisories/)
- [Apple](https://support.apple.com/en-us/HT201222)

### Future Manufacturer Support

Please create/vote a comment on the [Soliciting Manufacturer Support](https://github.com/carbonphyber/security_advisory_scrapy/issues/2) GitHub Issue to request new source adapters.

## Wall of Shame

All software providers who hide their security announcements behind a paywall or a web login actively hinder security firms from being able to automatically track and patch systems. The following manufacturers are encouraged to change their policies to allow easy software consumption of security feeds.

- Microsoft
- Cisco

Please report other software manufacturers which either do not publish their security advisories in a standard & timely way or which do so but in such a way that collection can not be done automatically (such as requiring a _user_ login or only make contingent upon proof of ownership of the software/hardware).

### How to remove a manufacturer from the Wall of Shame

Please file [a GitHub Issue](https://github.com/carbonphyber/security_advisory_scrapy/issues) with a hyperlink which describes how this project can automatically pull Security Advisory data.

All manufacturers who require scraping of HTML from brittle and likely to change HTML templates are encouraged to supply JSON/XML feeds (with correct HTTP caching and tolerance for respectful automated fetching).

## How to Assist

- File GitHub Issues for suggestions or defects
- Make Pull Requests to add Sources and/or fix known issues
- Contact software manufacturers and lobby for JSON/XML feeds
- If you work for a software manufacturer, 
- Suggest or build a standard for the optimal output format
- Post this project/repo on technical forums to gain popularity
