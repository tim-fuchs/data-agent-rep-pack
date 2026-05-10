# How to Ingest One Alfresco Share Page with Grounded Docs

**Date:** 2026-04-15

## Why are the instructions required?

- The [EuXFEL Alfresco server](https://docs.xfel.eu) requires authentication via user name and password.
- Scraping any Alfresco URL with a GET request that includes a simple `Authorization: USER:PW` pair in the header is not possible.

## Prerequisites

- In the steps below, replace `USER` and `PW` with your Alfresco user name and password.
- Decide, which page you want to ingest. In the following example, we use the [Alfresco FAQ](https://docs.xfel.eu/share/page/site/exfel/wiki-page?title=Alfresco_FAQ).

## Option 1: Ingestion via Alfresco API

1. Get all Alfresco containers:

   `curl -u "USER:PW" \
   "https://docs.xfel.eu/alfresco/api/-default-/public/alfresco/versions/1/sites/exfel/containers"`

2. Search the response for the "wiki" container ID:

   `1655e411-40d4-4717-aa0a-590c12f896de`

3. List wiki pages:

   `curl -u "USER:PW" \
   "https://docs.xfel.eu/alfresco/api/-default-/public/alfresco/versions/1/nodes/1655e411-40d4-4717-aa0a-590c12f896de/children"`

4. Search the response for the page ID of "Alfresco_FAQ":

   `021f62cc-f0b8-452f-a31a-d11354dc0282`

5. Create Base64 encrypted version of the USER:PW pair with `echo -n "USER:PW" | base64`:

   `VVNFUjpQVw==`

6. Ingest the page with Grounded Docs:

   `npx @arabold/docs-mcp-server@latest scrape \
   "Alfresco FAQ" \
   "https://docs.xfel.eu/alfresco/api/-default-/public/alfresco/versions/1/nodes/021f62cc-f0b8-452f-a31a-d11354dc0282/content" \
   --header "Authorization: Basic VVNFUjpQVw=="`

## Option 2: Ingestions via Cookies Authentication

1. Authenticate with Alfresco and store cookie response in a file:

   `curl -c cookies.txt -X POST \
   -d "username=USER&password=PW" \
   "https://docs.xfel.eu/share/page/dologin"`

2. Fetch web page via regular page URL:

   `curl -b cookies.txt \
   "https://docs.xfel.eu/share/page/site/exfel/wiki-page?title=Alfresco_FAQ" \
   -o alfresco.html`

3. Ingest the file with Grounded Docs (replace `PATH_TO_FILE`):

   `npx @arabold/docs-mcp-server@latest scrape "Alfresco FAQ" file:///PATH_TO_FILE/alfresco.html`

## Maintainance

1. Refresh the already ingested page:

   `npx @arabold/docs-mcp-server@latest refresh "Alfresco FAQ"`

2. Remove the ingested page:

   `npx @arabold/docs-mcp-server@latest remove "Alfresco FAQ"`

## References

- [Alfresco API](https://docs.alfresco.com/content-services/5.2/develop/rest-api-guide/install/#auth)
- ["Docs Manage" Skill of Grounded Docs](https://github.com/arabold/docs-mcp-server/blob/main/skills/docs-manage/SKILL.md)
