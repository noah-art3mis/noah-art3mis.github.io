# Portfolio redesign proposal

This proposal was built for the personal portfolio before the owner clarified that the intended redesign target was simulacro.tech. It is saved independently for possible future use.

## Direction

An English-language research portfolio for potential collaborators and technical hiring teams. The original project descriptions, career history, routes, PDF downloads, and contact details establish the content. An open layout, Spline Sans headings, Instrument Sans body text, and a blue accent give the portfolio a clearer hierarchy. The system follows the visitor’s light/dark preference and uses native links without application JavaScript. Motion is limited to interaction feedback and optional smooth anchor scrolling.

The original Simulacro artwork anchors the introduction. The dissertation leads the featured work with a preview rendered from the actual PDF. Software projects use compact rows, writing gets its own section, and career details follow the work.

## Unslop assessment of the incumbent

The source establishes that the original was the standard Minima theme. The assessment concerns unconsidered defaults, not evidence that AI authored the site.

| Rendered-web family    | Verdict       | Evidence and response                                                                                                        |
| ---------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Visual                 | Absent        | No nested cards, glow, fake interface illustrations, or ornamental grids. Preserve the actual artwork.                         |
| Typography             | Present       | The identity was a small header label, and projects had body-size bold titles. Establish a main heading and distinct levels.  |
| Copy                   | Present       | The footer repeated the owner’s name twice without adding information. Keep one footer attribution.                           |
| Craft floor            | Present       | Missing home h1; skipped levels in the archive; empty Slopstopper link; no recovery link in the 404 content. Correct and test. |
| Motion                 | Absent        | The original was static. No motion devices needed removal.                                                                    |
| Colour and rhythm      | Present       | The uniform document rhythm gave research, tools, and career history similar emphasis. Separate the content by purpose.        |
| English SaaS patterns  | Absent        | No badges, feature-card triplets, numbered steps, stat banners, or permanent dark theme.                                       |

The highest-impact change is the hierarchy: introduce the person clearly, show the actual research artifact, then let visitors scan the software and writing. The plain voice and direct destinations are strengths to retain.

Impeccable’s detector ran on the rendered original and redesign. Its HTML-parser dependencies were unavailable, so it reported degraded operation. Regex matching found no hits; custom properties, selector matching, and computed contrast were not evaluated by that detector. This is not a complete accessibility audit.

## Verification evidence

Jekyll builds using the existing locked dependencies. The behavioral tests were first run against the original build and reproduced the heading, empty-link, and 404 defects, then passed after implementation. Browser checks exercised desktop light/dark layouts, 390px and 320px phones, the project archive, category navigation, keyboard skip navigation, and return-home navigation. They found no horizontal overflow, failed images, missing fragment targets, or page errors in the checked scenarios.

Lighthouse was attempted but its Chrome connection failed; no Lighthouse score is claimed. Remote historical project destinations have not been exhaustively checked. The original portfolio content remains a historical record and is not a fresh audit of project status.

## Captures

- [First viewport](screenshots/first-viewport.png)
- [Desktop](screenshots/desktop.png)
- [Mobile](screenshots/mobile.png)
- [Dark mode](screenshots/dark.png)
- [Project archive](screenshots/projects.png)
- [Project archive on mobile](screenshots/projects-mobile.png)

## Asset provenance

The Simulacro PNGs are pre-existing repository assets. `assets/images/ai-slop-paper.webp` is the first page of `assets/pdfs/ai_slop_paper.pdf`, rasterized with Poppler and encoded as WebP. Spline Sans comes from Google Fonts; Instrument Sans is reused from the owner’s local licensed font assets. Both are self-hosted with their SIL Open Font License files. The arrow icons come from Phosphor’s regular icon set, with the MIT license in `assets/Phosphor-LICENSE.txt`.
